import random

def main():
    
    print("""\nSelect A Game :\n
1.Rock,Paper and Scissor
2.Odd Even
3.Exit""")
    
    while True:
        
        wa=input("\nYour choice (1/2/3) : ")
        wa=wa.strip()
        if wa not in ('1', '2', '3'):
           print("\nInvalid choice")
           continue

        else:
            break

    if wa =='1':
       rps()

    if wa =='2':
       oe()

    if wa =='3':
        exit

def rps():

        w=0
        l=0

        while True:

            n=(input("\nNumber of rounds you wanna play (1/3/5) : "))
            n=n.strip()

            if n not in ('1', '3', '5'):
                 print("\nInvalid choice")
                 continue

            else:
                break

        print("""\nSelect a option :\n
1.Rock
2.Paper
3.Scissor""")   

        for i in range(int(n)):
            
            oklist=['rock', 'paper', 'scissor']
            a=random.choice(oklist)

            while True:

                b=input("\nYour choice (1/2/3) : ")
                b=b.strip()

                if b not in ('1', '2', '3'):
                  print("\nInvalid choice")
                  continue

                else:
                    break

            if b=='1':
                  print("\nYour choice : rock\nComputer choice : ",a)

                  if a=='rock':
                      print("\nNo point is granted to anyside")
                      print("\n\t\t\tScore Board\n\tUser : ",w,"\t\t\tComputer : ",l)

                  elif a=='paper':
                      l=l+1
                      print("\n\t\t\tScore Board\n\tUser : ",w,"\t\t\tComputer : ",l)

                  elif a=='scissor':
                      w=w+1
                      print("\n\t\t\tScore Board\n\tUser : ",w,"\t\t\tComputer : ",l)

            elif b=='2':
                  print("\nYour choice paper :\nComputer choice : ",a)

                  if a=='paper':
                      print("\nNo point is granted to anyside")
                      print("\n\t\t\tScore Board\n\tUser : ",w,"\t\t\tComputer : ",l)

                  elif a=='scissor':
                      l=l+1
                      print("\n\t\t\tScore Board\n\tUser : ",w,"\t\t\tComputer : ",l)

                  elif a=='rock':
                      w=w+1
                      print("\n\t\t\tScore Board\n\tUser : ",w,"\t\t\tComputer : ",l)

            elif b=='3':                                  
                  print("\nYour choice scissor : \nComputer choice : ",a)

                  if a=='scissor':
                      print("\nNo point is granted to anyside")
                      print("\n\t\t\tScore Board\n\tUser : ",w,"\t\t\tComputer : ",l)

                  elif a=='rock':
                      l=l+1
                      print("\n\t\t\tScore Board\n\tUser : ",w,"\t\t\tComputer : ",l)

                  elif a=='paper':
                      w=w+1
                      print("\n\t\t\tScore Board\n\tUser : ",w,"\t\t\tComputer : ",l)  

        while True:

         if w>l:
               print("\nWinner Winner Chicken Dinner")
               break

         if l>w:
               print("\nBetter Luck Next Time")
               break

         if w==l:
               print("\n\t\t\tIt's a draw")
               print("\nBetter Luck Next Time")
               break

        while True:

             say=input("\nLet's do again (yes/no) : ")
             say=say.strip()

             if say not in ('yes', 'no'):
                 print("\nInvalid choice")
                 continue

             else:   
                 if say=='yes':
                     rps()
                     break

                 if say=='no':
                     main()
                     break

def oe():

     print("\nYou Bat First")
     u=0
     s=0
     count=0
     counts=0

     while True:

         moblist=['1', '2', '3', '4', '5', '6', '7', '8', '9']
         c=random.choice(moblist)
         d=(input("\nChoose a number (1/2/3/4/5/6/7/8/9) : "))
         d=d.strip()

         if d not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
          print("\nInvalid choice")

         if d in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
               print("\nYour call :",d,"\tComputer call :",c)

               if d!=c:
                   u=u+int(d)
                   print("\nUser : ",u,"runs")

                   if u>50:
                       if count==0:
                           print("\n\t\t\tHalf Century!!\n\t\t   Congulations Keep Going On")
                       count=count+1                             

                   if u>100:
                       if counts==0:
                           print("\n\t\t\t    Century!!\n\t\t   Congulations Keep Going On")
                       counts=counts+1    
                   continue

               elif d==c:
                   print("\n\t\t\tOut!!! \n\nNow it's your turn to ball")
                   break

     while True:

                   moblist=['1', '2', '3', '4', '5', '6', '7', '8', '9']
                   c=random.choice(moblist)         
                   d=(input("\nChoose a number (1/2/3/4/5/6/7/8/9) : "))
                   d=d.strip()

                   if d not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                    print("\nInvalid choice")

                   if d in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                    print("\nYour call :",d,"\tComputer call :",c)

                    if d!=c:
                        s=s+int(c)
                        print("\nComputer : ",s,"runs")

                        if u>s:
                             print("\nNeed",u-s,"runs to win")

                        if s>u:
                             print("\n\t\t\tScore board\n\tUser:",u,"\t\t\tComputer:",s)
                             print("\nBetter Luck Next Time")
                             break

                        else:
                            continue

                    if d==c:
                        print("\n\t\t\tOut!!!\n\n\t\t\tScore board\n\tUser:",u,"\t\t\tComputer:",s)


                        if u>s:
                         print("\nWinner Winner Chicken Dinner")
                         break

                        if s>u:
                         print("\nBetter Luck Next Time")
                         break

                        if s==u:
                         print("\n\t\t\tIt's a draw")
                         print("\nBetter Luck Next Time")
                         break

     while True:

         say=input("\nLet's do again (yes/no) : ")
         say=say.strip()

         if say not in ('yes', 'no'):
             print("\nInvalid choice")
             continue

         else:   
             if say=='yes':
                 oe()
                 break

             if say=='no':
                 main()
                 break

main()
print("\nI Love You")
    




















