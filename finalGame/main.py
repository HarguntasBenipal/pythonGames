y = int(input())
total = 0

for x in range (y):
  name = input()
  
  if (name == "Poblano"):
    total = total + 1500
    
  elif name == "Mirasol":
    total = total + 6000

  elif name == "Serrano":
    total = total + 15500
  
  elif name == "Cayenne": 
    total = total + 40000
  
  elif name == "Thai":
    total = total + 75000
  
  elif name == "Habanero":
    total = total + 125000

else :
  print (total)