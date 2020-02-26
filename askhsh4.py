leonis=input ("Please give a word:")
while leonis=="":
   leonis=input("Please give a word:")
 #we dont want the user  to give us a blank space as a word
 
 
def converter(leonis):
     #The main function that converts a string to ASCII CODE
          num=''.join(str(ord(c))for c in leonis)
          int_num=int(num)
          
          
          if  int_num>1 :
             for i in range(2,int_num):
               if(int_num%1)==0:
                  print(int_num,",That number is not a prime one ,im sorry ")
                  
                  
                  break
          else :
                 print(int_num,"is a prime number")
                 

converter(leonis)   

#There are many mathematical ways to prove that a number is a prime one ....not all the ways are efficient or fast .Others are fast but
#have flaws based on their lack of accuracy or limited function...Wilson's theorem is the best and most accurate way ...simnple saying that 
# In number theory, Wilson's theorem states that a natural number n > 1 is a prime number if and only if the product of all the positive integers
 #less than n is one less than a multiple of n. That is (using the notations of modular arithmetic), the factorial {\displaystyle 
 #(n-1)!=1\times 2\times 3\times \cdots \times (n-1)}(n - 1)! = 1 \times 2 \times 3 \times \cdots \times (n - 1) satisfies
#{\displaystyle (n-1)!\ \equiv \ -1{\pmod {n}}}(n-1)!\ \equiv\ -1 \pmod n   
#thats not easily achievable using Python ..so i used a more programming effective and faster way 