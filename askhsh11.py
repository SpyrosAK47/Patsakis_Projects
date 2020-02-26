file=open ('john_missas.txt','w')
#we take into account that every number is has a blank space bettwen himself and the next one ....also every 4 numbers we change lines ...
file.write("8 0 2 99\n5 69 72 33\n9 103 10 15\n43 42 98 32\n10 18 27 15\n567 922 1224 345\n47 52 24 10\n2 7 8 10")
#its not like an actual list but pyhton reads it as its like a list ..and there is no errors 
file.close()
file=open('john_missas.txt','r')
w=file.read()
file.close()
print("These are the available foursomes from the text")
print(w)
print("Please give 6 numbers ,not more ,not less:")

le=[]
lebron=""
james=w+" "

for i in james:
  if i!=" " and i!="\n":
    lebron=lebron+i
  else:
    le.append(lebron)
    lebron=""

missas=[]
for i in range(6):
  j=int(input("Please give a number:"))
  o=str(j)
  missas.append(o)

print("The 6 numbers that you gave are:")
print(missas)

k=len(le)
jordan=0
shaq=0
rings=False
  
w=0
for i in range(k//4):
  for j in range(w,w+4):
    if le[j] in missas:
      jordan=jordan+1
  if jordan==4:
    rings=True
  else :
    jordan=0
    w=w+4

if rings==True:
  print("There is an available foursome")
else:
  print("There is not an available foursome")      
