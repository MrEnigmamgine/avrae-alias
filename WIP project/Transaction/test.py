!test
<drac2>
args=['+25.5gp','-10sp',"12cp","A description of transaction"]
coinTypes=["cp","sp","ep","gp","pp"]
coinRates={"cp":100,"sp":10,"ep":2,"gp":1,"pp":0.1}
outstr = []
for i, arg in enumerate(args):
    if not arg.isnumeric():
        numbers = arg[:-2]
        letters = arg[(len(arg)-2):].lower()
        if (numbers.replace('.','',1).strip('-+').isnumeric()) and (letters in coinTypes):
            outstr += [float(numbers),letters]
        elif not letters in coinTypes:
            descstr = arg
        
</drac2>
{{outstr}} desc- {{descstr}}






################ 
!test
<drac2>
coinTypes=["cp","sp","ep","gp","pp"]
gp = "+25.5"
outstr = gp.isnumeric()
</drac2>
{{outstr}}

amount=int(''.join([x for x in a if x in "0123456789-"])or 0)
coinType=''.join([x for x in a[1:] if not x.isdigit()])

!test
<drac2>
txt = '25.5'
outstr = isdecimal.()
</drac2>
{{outstr}}


prevVal=((sum([float(pouch[1][x]/coinRates[x]*coinRates[defaultCoin]) for x in coinTypes]) {defaultCoin}'))