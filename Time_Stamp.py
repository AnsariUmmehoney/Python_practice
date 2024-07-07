import time

name = input("Enter your name : ")

timestamp=time.strftime('%H : %M : %S')
print("Now , The time is ", timestamp)

hour=int(time.strftime('%H'))


if(hour>0 and hour<=12):
    print("GoodMorning"  ,  name)

elif(hour>=12 and hour<=17):
    print("Good Afternoon"  ,  name)

elif(hour>=17 and hour<=21):
    print("Good Evening"  ,  name)

else:
    print("Good Night")