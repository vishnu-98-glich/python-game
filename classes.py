import random
import colorama
from colorama import Fore, Back, Style
colorama.init()
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    red = '\033[31m'
    purple = '\033[45m'


class character:
    def __init__(self,hp,mp,attack,defend,dmagic,wmagic):
        self.hp=hp
        self.max_hp=hp
        self.mp=mp
        self.max_mp=mp
        self.attack=attack
        self.defend=defend
        self.dmagic=dmagic
        self.wmagic=wmagic
        self.action=["Attack","Magic"]

    def display(self,name):

        if self.hp<100 and self.mp<10:
            print(bcolors.OKBLUE,name,bcolors.ENDC,"-",bcolors.OKGREEN,"HP",bcolors.ENDC,":","[",bcolors.red,self.hp,bcolors.ENDC,"/",self.max_hp,"]\t\t",bcolors.FAIL,"MP",bcolors.ENDC,":","[",bcolors.red,self.mp,bcolors.ENDC,"/",self.max_mp,"]")
            return 1
        elif self.hp<100:
            print(bcolors.OKBLUE,name,bcolors.ENDC ,"-", bcolors.OKGREEN,"HP" ,bcolors.ENDC, ":" , "[",bcolors.red, self.hp,bcolors.ENDC, "/", self.max_hp, "]",bcolors.FAIL ,"MP" ,bcolors.ENDC, ":", "[", self.mp, "/", self.max_mp, "]")
            return 1
        elif self.mp<10:
            print(bcolors.OKBLUE,name, bcolors.ENDC,"-",bcolors.OKGREEN, "HP" ,bcolors.ENDC, ":" , "[",self.hp,  "/", self.max_hp, "]",bcolors.FAIL,"MP" ,bcolors.ENDC, ":", "[", bcolors.red, self.mp, bcolors.ENDC, "/", self.max_mp, "]")
            return 1
        else:
            print(bcolors.OKBLUE,name, bcolors.ENDC,"-", bcolors.OKGREEN,"HP",bcolors.ENDC, ":" ,"[", self.hp, "/", self.max_hp, "]",bcolors.FAIL,"MP", bcolors.ENDC, ":", "[", self.mp, "/", self.max_mp, "]")

    def generate_dmg(self):
         low=self.attack-10
         high=self.attack
         a=random.randrange(low,high)
         if self.hp<100:
             a=a/2
             return a
         else:
             return a
    def generate_dmge(self):
         low=self.attack-10
         high=self.attack
         a=random.randrange(low,high)
         if self.hp<100:
             a=a*2
             return a
         else:
             return a

    def implement_dmg(self,dam,name):

        self.hp=self.hp-dam
        print(bcolors.OKBLUE,name,bcolors.ENDC,"have delt",dam,"damage\n")
    def get_hp(self):
        return self.hp
    def set_hp(self):
        self.hp=0
    def displaymagic(dmagic,wmagic):
        print(bcolors.OKBLUE,"Dark magic:\n",bcolors.ENDC)
        n=0
        for i in dmagic:
            print("\t",bcolors.FAIL,n+1,bcolors.ENDC,"-",dmagic[n]["name"],":",dmagic[n]["damage"],"(",bcolors.FAIL,"MP",bcolors.ENDC,":",dmagic[n]["cost"],")")
            n=n+1
            g=n
        print(bcolors.OKBLUE,"White magic:\n",bcolors.ENDC)
        n=0
        for j in wmagic:
            print("\t",bcolors.FAIL,g+1,bcolors.ENDC,"-",wmagic[n]["name"],":",wmagic[n]["heal"],"(",bcolors.FAIL,"MP",bcolors.ENDC,":",wmagic[n]["cost"],")")
            n=n+1
            g=g+1
    def mpcheck(self,g,d,w):

        if(g==str(1)):
            b = d[0]["cost"]
            if self.mp<b:
                print(bcolors.red, "Low power to perform magic", bcolors.ENDC)
                return 1

        if(g == str(2)):
            b = d[1]["cost"]
            if self.mp < b:
                print(bcolors.red,"Low power to perform magic",bcolors.ENDC)
                return 1

        if (g == str(3)):
            b = d[2]["cost"]
            if self.mp < b:
                print(bcolors.red, "Low power to perform magic", bcolors.ENDC)
                return 1

        if (g == str(4)):
            b = d[0]["cost"]
            if self.mp < b:
                print(bcolors.red, "Low power to perform magic", bcolors.ENDC)
                return 1

        if (g == str(5)):
            b = d[1]["cost"]
            if self.mp < b:
                print(bcolors.red, "Low power to perform magic", bcolors.ENDC)
                return 1


    def magicattack(self,d,w,g,q):
        if q==6:
            if (g == str(1)):
                a = d[0]["damage"]*2
                b = d[0]["cost"]
                print(bcolors.red,"The sky is raining fire!\n",bcolors.ENDC)
                print("Your magic have delt", a, "damage")
                self.hp = self.hp - a
                if self.hp < 0:
                    self.hp = 0
                return b
            elif (g == str(2)):
                a = d[1]["damage"]*2
                b = d[1]["cost"]
                print("The lighting strikes the ground")
                print("Your magic have delt", a, "damage")
                self.hp = self.hp - a
                if self.hp < 0:
                    self.hp = 0
                return b
            elif (g == str(3)):
                a = d[2]["damage"]*2
                b = d[2]["cost"]
                print("Earthquate from knowhere")
                print("Your magic have delt", a, "damage")
                self.hp = self.hp - a
                if self.hp < 0:
                    self.hp = 0
                return b
            elif (g == str(4)):
                a = w[0]["heal"]*2
                b = w[0]["cost"]
                print(bcolors.OKGREEN, "Your health is increased by", bcolors.ENDC, a)

                return b
            elif (g == str(5)):
                a = w[1]["heal"]*2
                b = w[0]["cost"]
                print(bcolors.OKGREEN, "Your health is increased by", bcolors.ENDC, a)

                return b
            else:
                print(bcolors.red, "oops!.Try again", bcolors.ENDC)
                return 1


        else:

            if(g==str(1)):
              a=d[0]["damage"]
              b=d[0]["cost"]
              print(bcolors.red, "The sky is raining fire!", bcolors.ENDC)
              print("Your magic have delt",a,"damage")
              self.hp=self.hp-a
              if self.hp<0:
                  self.hp=0
              return b
            elif(g==str(2)):
                a = d[1]["damage"]
                b = d[1]["cost"]
                print("The lighting strikes the ground")
                print("Your magic have delt", a, "damage")
                self.hp =self.hp - a
                if self.hp < 0:
                    self.hp = 0
                return b
            elif(g==str(3)):
                a = d[2]["damage"]
                b = d[2]["cost"]
                print("Earthquate from knowhere")
                print("Your magic have delt", a, "damage")
                self.hp = self.hp - a
                if self.hp < 0:
                    self.hp = 0
                return b
            elif (g ==str( 4)):
                a = w[0]["heal"]
                b = w[0]["cost"]
                print(bcolors.OKGREEN,"Your health is increased by", bcolors.ENDC,a)

                return b
            elif (g == str(5)):
                 a = w[1]["heal"]
                 b = w[0]["cost"]
                 print(bcolors.OKGREEN,"Your health is increased by",bcolors.ENDC, a)

                 return b
            else:
                 print(bcolors.red,"oops!.Try again",bcolors.ENDC)
                 return 1

    def reducemp(self,a):
        self.mp=self.mp-a
    def updatehp(self,a):
        if self.hp<100:

            self.hp=self.hp+a*2
            if self.hp>self.max_hp:
                self.hp=self.max_hp
        else:
            self.hp = self.hp + a
            if self.hp > self.max_hp:
                self.hp = self.max_hp
