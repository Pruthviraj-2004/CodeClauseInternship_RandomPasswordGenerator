#Random Password Generator
import random
#create 4 lists with its characters
A_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
a_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
spl_list = ['!', '#', '$', '%', '&', '*', '+', '-', '.', '?', '@', '[', ']', '^', '_', '~']
#create an empty list to store the password
l = []

#take input from the user to define the password length
print("Random Password Generator\n")
n = int(input("Enter the Password length(Suggested above 8): "))
if(n>4):
  l.append(A_list[random.randint(0,25)])
  l.append(num_list[random.randint(0,9)])
  l.append(a_list[random.randint(0,25)])
  l.append(spl_list[random.randint(0,15)])
  for i in range(n-4):
      ran = random.randint(1,4)
      if(ran == 1):
          l.append(num_list[random.randint(0,9)])
      elif(ran == 2):
          l.append(A_list[random.randint(0,25)])
      elif(ran == 3):
          l.append(a_list[random.randint(0,25)])
      elif(ran == 4):
          l.append(spl_list[random.randint(0,15)])
  
  random.shuffle(l)
  print("The Generated Password is:", *l)
else:
  print("Password length is too small!! Try again with bigger length.")
