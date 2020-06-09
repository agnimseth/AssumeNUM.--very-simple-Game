import random
import time
    
name=input("Enter your name ")
print("Hi...lets play a game, game of assumption,",name)
print('==='*15)

print("rule:")
print("1} you have only 4 chance to assume a no after 4 times u gonna loss and ends the game between ")
print("2} you have to choose between 0 - 20 ")




c=int(random.randint(0,20))

count = 0

while (count < 4):
    print('-'*20)
    a=int(input("choose the no:- "))
        
    if a>21:
        print("enter the no within 20")
            
    else :
         
         if a == c:
             print("right answer, you won,:",name)
             break
            
         elif a > c:
             if (a - c )> 4:
                  print("*******--------*********-----********")
                  print("the no is less than your assumption but not near to your assumption,",name)
                  print("*******--------*********-----********")
                  count = count + 1
             
            
             else :
                 print("*******--------*********-----********")
                 print("the no is less than your assumption and also near to your assumption,",name)
                 print("*******--------*********-----********") 
                 count = count + 1
                 
                




         else:
              if (c-a) > 4:
                  print("*******--------*********-----********")
                  print(" the no is greater than your assumption but not near to your assumption,",name)
                  print("*******--------*********-----********")

                  count = count + 1
              else:
                  print("the no is greater than your assumption and also near to your assumption",name)
                  count = count + 1
                
                



print("the number was ",c,name)
time.sleep(10)
print("End of The Application")
a=input("Do you want to play again ")

