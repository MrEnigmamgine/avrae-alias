### Snippet to enable sneak attacks with a rogue.


```
!snippet sneak {{dice=ceil(int(get('RogueLevel',0))/2)}} {{f'-d1 "{dice}d6" -f "Sneak Attack|Once per turn, you can deal an extra {dice}d6 damage to one creature you hit with an attack if you have advantage on the attack roll."' if dice else '-f "Liar|You are not a rogue. You do not get sneak attack."'}}
```