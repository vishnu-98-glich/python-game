from classes import character,bcolors
import re
import random
import colorama
from colorama import Fore, Back, Style
colorama.init()
result=True
res=True
z=1
p=0
darkmagic=[{"name":"Fire","damage":100,"cost":10},
      {"name":"Thunder","damage":90,"cost":7},
      {"name":"Earthquake","damage":80,"cost":5},
      ]
whitemagic=[{"name":"Healing potion","heal":100,"cost":10},
      {"name":"Recovery spell","heal":150,"cost":15},
      ]
action=["Attack","Magic"]
player=character(320,40,90,40,darkmagic,whitemagic)
enemy=character(900,40,70,40,darkmagic,whitemagic)
e="target"
print(bcolors.red+"Welcome to Wizblitzz!!\n"+bcolors.ENDC)
print("This is a short description about the game.The HP and MP represents health and magic points respectively.\n At a particular scenario you magic will deal double damage and your attack damage will be reduced to half.\nBeware! The enemy's power will also be affected in the same scenario.But this effect will not be good for you! ")
while res:
      t=input("Enter your name ")
      t=re.sub("[0-9,:.' ']","",t)

      if t=="":
            print("The name should not be blank ")
            continue
      else :
            break
character.display(player,t)
character.display(enemy,e)

while result:
      p=p+1
      n = 1
      print("======================================================")
      for i in action:
            print(bcolors.FAIL,str(n),bcolors.ENDC,":",i)
            n=n+1

      a=input("Enter your choice ")

      if a == str(1):
            print(bcolors.FAIL,"You chose to attack!!",bcolors.ENDC)
            dmg=character.generate_dmg(player)
            character.implement_dmg(enemy,dmg,t)
            x=character.get_hp(enemy)
            if  x<= 0:
                  character.set_hp(enemy)
                  print(bcolors.WARNING,"Hurray!!!!!.You won\n",bcolors.ENDC)
                  character.display(player, t)
                  character.display(enemy, e)
                  break

      elif a==str(2):
            character.displaymagic(darkmagic,whitemagic)
            while res:

                 g=input("Enter your choice ")
                 re=character.mpcheck(player,str(g),darkmagic,whitemagic)
                 if re==1:

                       z=2

                       break
                 if character.get_hp(player)<100:
                       re=6
                       r = character.magicattack(enemy, darkmagic, whitemagic, str(g),re)
                 else:
                        r=character.magicattack(enemy,darkmagic,whitemagic,str(g),re)

                 if g==str(4):
                       character.updatehp(player,whitemagic[0]["heal"])
                 elif g==str(5):
                       character.updatehp(player, whitemagic[1]["heal"])

                 if r==1:
                        continue
                 x = character.get_hp(enemy)
                 if x <= 0:
                       z=3
                       character.set_hp(enemy)
                       print(bcolors.WARNING, "Hurray!!.You won\n", bcolors.ENDC)
                       character.display(player, t)
                       character.display(enemy, e)
                       break
                 else:
                       character.reducemp(player,r)
                       break

            if z==3:
                  break
            if z==2:
                  continue
      else :
            print(bcolors.red,"***Please try again***",bcolors.ENDC)
            continue
      print(bcolors.FAIL,"Your opponent's turn!!",bcolors.ENDC)
      if p==5:
            s=random.randrange(1,3)

            character.mpcheck(enemy,str(s),darkmagic,whitemagic)
            w=character.magicattack(player, darkmagic, whitemagic,str(s), str(1))
            character.reducemp(enemy,w)
            y = character.get_hp(player)
            if y<=0:
                  character.set_hp(player)
                  character.display(player, t)
                  character.display(enemy, e)
                  print("you have lost.you died")
                  break

      else:
            dam = character.generate_dmge(enemy)
            character.implement_dmg(player, dam,e)
            y = character.get_hp(player)
            if y<=0:
                  character.set_hp(player)
                  character.display(player, t)
                  character.display(enemy, e)
                  print("you have lost.you died")
                  break
      character.display(player, t)
      character.display(enemy, e)
      if character.get_hp(player)<100:
            print("HINT:",bcolors.WARNING,"You are a wizard .Choose your action wisely",bcolors.ENDC)
