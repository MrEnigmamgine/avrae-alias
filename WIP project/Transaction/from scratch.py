!test
<drac2>
args=['100gp','10sp','1cp']
args.append('2pp')
#args=&ARGS&
coinTypes=["cp","sp","ep","gp","pp"]
coinRates={"cp":100,"sp":10,"ep":2,"gp":1,"pp":0.1}
defaultCoin="gp"
coinPouchName="Coin Pouch"
bagDict = {i[0]:i[1] for i in load_json(bags)} #load bags as a dictionary
pouch= bagDict[coinPouchName]
numbers = [int(word) for word in args[0] if word.isdigit()]

outstr=numbers
</drac2>
{{outstr}}



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
