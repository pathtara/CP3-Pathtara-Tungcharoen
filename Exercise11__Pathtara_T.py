###Pyramid Generator###
input = int(input("Pyramid's row : '"))
space = input
for i in range(1, input + 1):
      space -= 1
      i = (i * 2) - 1                       
      print(str(" " * space) + str("*" * i)) 