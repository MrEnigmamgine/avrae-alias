!alias transaction embed
<drac2>
#declare args
arg1="&1&"
arg2="&2&"
coinTypes=["cp","sp","ep","gp","pp"]
coinRates={"cp":100,"sp":10,"ep":2,"gp":1,"pp":0.1}
defaultCoin="gp"
coinPouchName="Coin Pouch"
bagsLoaded=load_json(bags) #loads the cvar "bags" as a JSON object
pouch=([x for x in bagsLoaded if x[0]==coinPouchName]+[[]])[0] #get only the coin pouch
amount=int(''.join([x for x in arg1 if x in "0123456789-"])or 0) #isolate the number (*30*gp) not sure how
coinType=''.join([x for x in arg1[1:] if not x.isdigit()]) #isolate the coin string (30*gp*) not sure how
error=not coinType in coinTypes #this line does nothing useful because the next line destroys the value
error=pouch==[] #ensures that pouch is an array
amountInDefaultCoin=sum([float((amount if coinType==x else 0)/coinRates[x]*coinRates[defaultCoin]) for x in coinTypes])
prevVal=((f'{sum([float(pouch[1][x]/coinRates[x]*coinRates[defaultCoin]) for x in coinTypes])} {defaultCoin}'))
error or pouch[1].update({coinType:pouch[1][coinType]+amount})
error or [(set("y",coinTypes[coinTypes.index(x)+1]),set("R",int(coinRates[x]/coinRates[y])),set("p",pouch[1][x]//R),(pouch[1].update({y:pouch[1][y]+p}),pouch[1].update({x:pouch[1][x]-p*R}))if pouch[1][x]<0 else'')for x in coinTypes[:-1]]
error=[x for x in pouch[1]if pouch[1][x]<0]
error or set_cvar("bags",dump_json(bagsLoaded))
curVal=((f'{sum([float(pouch[1][x]/coinRates[x]*coinRates[defaultCoin]) for x in coinTypes])} {defaultCoin}'))
transaction="&2&"
transaction.replace(' "',' “').replace('" ','” ').replace('"','“'if transaction.startswith('"')else'”',1).replace('"','”').replace("'", r"\'")
failMsg=(f"{name} does not have enough funds: \nTransaction: {transaction} \nRequired Funds: {str(-amountInDefaultCoin)} {defaultCoin} \nCurrent Funds: {prevVal}")
successMsg=(f"C: {name} \nA: %1% ({prevVal} -> {curVal}) \nT: {transaction}")
</drac2>
-desc "{{failMsg if error else successMsg}}"
-thumb <image>
-footer "!transaction +Xgp \"Description of Transaction\""
