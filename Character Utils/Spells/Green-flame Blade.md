```
!snippet gfb {{"" if level<5 else ("-d 1" if level<11 else "-d 2" if level<17 else "-d 3")+"d8[fire]"}} 

-f "Green-Flame Blade | On a hit, green fire leaps from the target to a different creature of your choice that you can see within 5 feet of it. The second creature takes {{str((("1" if level<11 else "2" if level<17 else "3") +"d8 + " if level>=5 else"") + str(spell))}} fire damage." 
-title "<name> casts Green-Flame Blade with {{"[aname]" if ctx.alias[0]=="a" else "[sname]"}}!"
```