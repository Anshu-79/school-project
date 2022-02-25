import math

input_message = "\nChoose the shape by typing the code next to it: \nSquare = s\nCircle = c\nRectangle = r\n"

shape_code = input(input_message).lower()

if shape_code == "s":
  side = float(input("\nEnter length of side: "))
  area = side ** 2
  print("The area is ", area)

elif shape_code == "c":
  radius = float(input("\nEnter length of radius: "))
  area = math.pi * (radius**2)
  print("The area is ", area)

elif shape_code == "r":
  height = float(input("\nEnter height of rectangle: "))
  width = float(input("\nEnter width of rectangle: "))
  area = height * width
  print("The area is ", area)

else:
  print("\nIncorrect input. ValueError occured.")