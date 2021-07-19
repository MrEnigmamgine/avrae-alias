!alias lifestyle embed
<drac2>
args,n = &ARGS&,"\n"

if cc_exists("Experience"):
    None
else:
    Msg = f""" -desc 
    "
    Experience counter not setup.\nPlease type `!xp`
    "
    """
    return Msg
    
if exists("bags"):
    None
else:
    Msg = f""" -desc 
    "
    Coins not setup.\nPlease type `!coins`
    "
    """
    return Msg

one = get_cc("NNB RP") if cc_exists("NNB RP") else 0
two = "In <#810313622374187038>: `!xp " +one+" RPXP`" if (not one == 0) else ''

create_cc("NNB RP",0,proficiencyBonus*280,"none") 
create_cc("DT",0,14,"none","bubble")

set_cc("DT",14)
set_cc("NNB RP",0)

a = load_json(bags)
[a[x][1].update({"gp":a[x][1].gp-7}) for x in range(len(a)) if a[x][0] == 'Coin Pouch'][0]
set_cvar("bags",dump_json(a))
money = [a[x][1].get("gp") for x in range(len(a)) if a[x][0] == 'Coin Pouch'][0]

Msg=f""" -desc 
"
**Gold**
Modest lifestyle: **-7gp**
Total: **{money}gp** 
{two}
"
"""

return Msg
</drac2>
-title "**<name>'s summary for the week!**"
-footer "Neverwinter: New Beginnings | Weekly Living Expenses"
-thumb <image>
-color <color>