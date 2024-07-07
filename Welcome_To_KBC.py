print("Welcome to KBC!")

questions = [
[ "who is the current railway minister of India" , "Mamta banargee"
     ,"Ram Vilash" , "Ashwini Vaishnaw" , "Piyush Goyal" ,"None" ,3 ],

[ "Which city is known as pink city of India" , "Banglore"
    ,"Maysore" , "Jaipur" , "Kochi" ,"None" ,3],

[ "who wrote india's National Anthem" , "Rabindranath Tagore"
     ,"Lal Bahadur Shastri" , "Chetan Bhagat" , "RK Narayan" ,"None" ,1 ],

[ "How many major religions are there in India?" , 6
    ,7 , 8 , 9 ,"None" ,1],
    
["Who wrote Vande Mataram?" ,"Sarat Chandra Chattopadhyay",
"Rabindranath Tagore" , "Bankim Chandra Chatterjee",
"Ishwar Chandra Vidyasagar" ,"None" , 3 ]   
    
    ] 


levels = [1000 , 2000 , 3000 , 5000 , 10000 , 20000, 40000, 80000 , 160000 , 320000 ]

Money = 0

for i in range(0 , len(questions)):
    question = questions[i]
    print(f"\nQuestion for Rs. {levels[i]}")
    print(f"a.{question[1]}  b.{question[2]}")
    print(f"c.{question[3]}  d.{question[4]}")

    reply = int(input("Enter your answer (1 - 4): "))
    if (reply == question[-1]):
        print(f"Correct answer , You won Rs.{levels[i]}")
        if (i==4):
            Money = 10000
        elif (i == 9):
            Money = 320000
        elif (i == 14):
            Money = 10000000
    else :
        print(f"wrong answer!")
        break
    

print(f"Your take home money is {Money}")