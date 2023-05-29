Alias to help track and use the portent ability for diviner wizards.

The alias checks if the Portent CC (custom counter) is full and refuses to roll otherwise.  To refill counters use
`!g lr`

To roll and save your portent values use `!portent roll`.  You can use portent roll by using `!portent use #`, where # is 1 or 2 corresponding to the desired slot.

```
!alias portent embed 
{{a,b,c,C,M,u,P,ch="&1&",int("&2&")if"&2&".isdigit()else 0,character().cvars,"Portent",["view","roll","use","help"],0,"portentRoll",character()}}
{{v=int(ch.cc_exists(C)and ch.get_cc_max(C))}}
{{B,m,R=b-1,M.index(a)if a in M else 0,[P+str(x+1)for x in range(v)]}}
{{p,u,r=[vroll("1d20")for x in R],(m>1)*b*v*exists(P+str(b)),(m==1)*v and ch.get_cc(C)==v}}
{{n,U=(m==1)*v and ch.get_cc(C)<v,u and"Used"in c[P+str(b)]}}
{{z=c[R[B]]if u and exists(R[B])and c[R[B]].isdigit()else 0}}
{{s=[ch.set_cvar(x,str(p[R.index(x)].total))for x in R]if r else(ch.set_cvar(R[B],f"~~{z}~~ Used"),ch.mod_cc(C,-1))if u and not U else""}}
 -title "{{f"I'm sorry {name}, I'm afraid I can't do that."if n or U or(not v if 0<m<3 else 0)else f"{name} rolls for their Portent dice!"if r else f"{name} uses their {b}{'st'if b<2 else'nd'if b<3 else'rd'} Portent die to dictate a roll result!"if u else f"{name}'s Portent Rolls:"if v*exists(P+"1")*(not m>2)else"Portent"}}" {{('-desc "When you finish a long rest, use `!portent roll` to roll your Portent dice. You can replace any attack roll, saving throw, or ability check made by you or a creature that you can see with one of these foretelling rolls. Use `!portent use #` where # is the roll you want to use, not the result, before the roll. You can replace a roll in this way only once per turn.\nEach foretelling roll can be used only once."'if not(m or exists(P+"1"))or m>2 else'-desc "You have already used that roll."'if U else'-desc "You can only roll new Portent rolls after finishing a long rest."'if n else f'-desc "{name} replaces an attack roll, ability check, or saving throw roll with a {z}."'if z else'')+(''.join([f' -f "Portent Roll {x+1}|'+(str(p[x])if m==1 and not n else c[R[x]])+'"'for x in range(v)])if m<3 and exists(P+"1")else"")+(f' -f "{C}|{ch.cc_str(C)}"'if v else' -f "Custom Counter Missing!|Set up a Portent CC to use this alias!"')}} -footer "!portent help for how to use" -color <color> -thumb <image>
 ```