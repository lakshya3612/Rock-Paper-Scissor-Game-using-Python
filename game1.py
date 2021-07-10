import random
myscore=0
cscore=0
tie=0
round=1
print("""enter 1=scissor
      2=paper
      3=rock""")
while round<=10:
    print()
    print("round:",round)
    mychoice=int(input("enter your choice"))
    cchoice=random.randint(1,3)
    print("computer's choice=",cchoice)
    if mychoice==cchoice:
        print("tie")
        tie+=1
    elif mychoice==1 and cchoice==2:
        print("you score")
        myscore+=1
    elif mychoice==2 and cchoice==3:
        print("you score")
        myscore+=1
    elif mychoice==3 and cchoice==1:
        print("you score")
        myscore+=1
    elif mychoice==1 and cchoice==3:
        print("computer score")
        cscore+=1
    elif mychoice==2 and cchoice==1:
        print("computer score")
        cscore+=1
    elif mychoice==3 and cchoice==2:
        print("computer score")
        cscore+=1
    print("computer's score=",cscore)
    print("your score=",myscore)
    print("tie=",tie)
    round+=1
if myscore>cscore:
    print("YAY!You Won")
elif cscore>myscore:
    print("Better luck next time")
else:
    print("tie")
        
        
        
        

