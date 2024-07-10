import random
print ("\nWelcome to the amazing game of Snake Water and Gun !")

def check(User , Comp):
    if(User==Comp):
     return 0

    elif(User == 0 and Comp==1):
        return -1
    
    elif(User == 1 and Comp==2):
        return -1
    
    elif(User == 2 and Comp==0):
        return -1
    
    else:
        return 1
    
Comp = random.randint(0,2)   
User = int(input("0 for Snake , 1 for water , and 2 for Gun : "))

    
Score = check(User , Comp)

print(f"You choose {User}")
print(f"Computer choose {Comp}")

if Score == 0 :
    print("Its draw")

elif Score == -1:
    print("You Loose")

else :
    print("You Win")