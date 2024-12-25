import random
word=input("enter the word;")
a={"stone":1,"paper":2,"sicissor":3}
computer=random.choice([1,2,3])
if(a[word]==1 and computer==1):
    print("COMPUTER CHOSED  STONE\n Draw")
elif(a[word]==2 and computer==2):
    print("COMPUTER CHOSED PAPER\n Draw")
elif(a[word]==3 and computer==3):
    print("COMPUTER CHOSED SICISSOR \n Draw")
elif(a[word]==1 and computer==2):
    print("COMPUTER CHOSED PAPER\n You Lose")
elif(a[word]==1 and computer==3):
    print("COMPUTER CHOSED SICISSOR \n You Win")
elif(a[word]==2 and computer==1):
    print("COMPUTER CHOSED  STONE\n You Win")
elif(a[word]==2 and computer==3):
    print("COMPUTER CHOSED SICISSOR \n You Lose")
elif(a[word]==3 and computer==1):
    print("COMPUTER CHOSED  STONE\n you Lose")
elif(a[word]==3 and computer==2):
    print("COMPUTER CHOSED PAPER\n You Win")
    