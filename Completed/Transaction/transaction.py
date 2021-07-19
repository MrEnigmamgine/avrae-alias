!alias transaction embed
<drac2>
args=&ARGS&
coinTypes=["cp","sp","ep","gp","pp"]
coinRates={"cp":100,"sp":10,"ep":2,"gp":1,"pp":0.1}
defaultCoin="gp"
coinPouchName="Coin Pouch"
bagDict={i[0]:i[1] for i in load_json(bags)} #load bags as a dictionary
pouch=bagDict[coinPouchName]
prevVal=0
for coin in coinTypes:
    prevVal += (pouch[coin]/coinRates[coin])
transactionText=''
error=False
errorText=''
descstr=''
change=False
for i, arg in enumerate(args):
    if not arg.isnumeric():
        numbers=arg[:-2]
        letters=arg[(len(arg)-2):].lower()

        if (numbers.replace('.','',1).strip('-+').isnumeric()) and (letters in coinTypes):
            change=True
            amount=int(numbers)
            coinType=letters
            pouch[coinType] += amount
            transactionText += arg.strip('+') +', '
        elif (numbers.replace('.','',1).strip('-+').isnumeric()) and (not letters in coinTypes):
            error = True
            errorText='Invalid Coin Type'
            break
        elif not letters in coinTypes:
            descstr += arg+' '
        else:
            error=True
            break
newVal = 0
for coin in coinTypes:
    newVal += (pouch[coin]/coinRates[coin])
if (not change) and (newVal-prevVal == 0):
    error=True 
    errorText="Coins are wrong."
elif descstr == '':
    error=True
    errorText="Missing description."
if not error:
    character().set_cvar("bags", dump_json(list(bagDict.items()) )) #Commit the changes to cvar
    plus = newVal-prevVal
    logText = '**T:** ('+round(prevVal,2)+defaultCoin+' -> '+round(newVal,2)+defaultCoin+')\n'+'**C:** '+transactionText.rstrip(', ')+'\n'+'**D:** \"'+descstr+"\""
    tText = name+' makes a transaction!'
else:
    tText = name+' tries to make a transaction!'
    logText = "Something went wrong.\n**Error Message:** "+errorText

</drac2>
-title '{{tText}}'
-desc '{{logText}}'
-thumb <image>
-footer '!transaction [+/-]Xgp [+/-]Xsp "Description of Transaction"'


################################################################################################
############### Here begins notes and testing stuff.  Not part of Alias ########################
################################################################################################

!tra +25gp -10sp 12cp "Description of transaction"

# Load the bags cvar
bags = load_json(get("bags", "[]"))
# Loop through each bag in the list of bags
for index, bag in enumerate(bags):
  # Separate out the name of the bag from the contents
  bag, items = bag
  # Is our current bag the coin pouch? if so end the loop
  if bag == "Coin Pouch":
    break
else:
  # Otherwise, if there was no coin pouch, add one
  index = len(bags)
  bags.append(["Coin Pouch", {}])
# Lets just worry about the coin pouch for now, we can add it back later
coinPouch = bags[index]

# Update the bag in the list of bags
bags[index] = coinPouch
# Update the cvar
character().set_cvar('bags', dump_json(bags))


##############################################

#load bags as dictonary
bagDict = {i[0]:i[1] for i in load_json(get("bags", "[]")) } 
#save dictonary to cvar
character().set_cvar("bags", dump_json(list(bagDict.items()) )) 
