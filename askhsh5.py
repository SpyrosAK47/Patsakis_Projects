file=open ('john_missas.text','w')
file.write("mpala paizei repl ada dad adaw da")
file.close()

with open ('john_missas.text','r') as file :
  data=file.read().replace('/n','').replace(',','')
  #We can raplace every !,#,@,,%,$,&,*,(),_,+,-,= but thats not the paint 
  data=data.split()
  n=len(data)
  
  for i in range(n):
    n=len(data[i])



 #very simple and clever programm ...
    if n>3:
     data[i]=data[i]+data[i][0]+'ay'
     #it takes every word ,adds the first letter and "ay" in the end of the word
     data[i]=data[i][1:10000]
     #it takes thw word and abstarct the first letter ....i put 10000 as a big number that is not posible to be a words length 
     print (data[i]) 
file.close()  
