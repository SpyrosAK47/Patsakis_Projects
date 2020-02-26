file=open ('john_missas.text','w')
file.write("mpala paizei olympiakos patsakis hack  cryprtogrpahy python ole konstantakopoulos ")
file.close()

with open ('john_missas.text','r') as file :
  data=file.read().replace('/n','').replace(',','')
  #We can raplace every !,#,@,,%,$,&,*,(),_,+,-,= but thats not the paint 
  data=data.split()
  
  list=sorted(data, key=len , reverse=True ) 
  #sorted makes the list go to a decending order based on length of the word
  print(list)
  vowels=('a','A','o','O','u','U','e','E','i','I')
  #this list includes all the vowels so we can replace them with blank space 
 
for i in range(5):
  longest1=list[i][::-1]
  #this makes the words reversed 
  for k in longest1:
     if k in vowels:
      longest1=longest1.replace(k,'')
 #if there is a vowel in the word it is replaced by blank space 
  print(longest1)    