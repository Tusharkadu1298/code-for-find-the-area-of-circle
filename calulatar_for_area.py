#4. write a program to create area calculator
 #  """
 #  press 1 to find the area of square
 #  press 2 to find the area of rect
 #  press 3 to find the area of circle
 #  press 4 to find the area of triangle  
 #  """


n = int(input("enter the number :-- "))
print('''
press 1 to find area of square
press 2 to find area of rectangle
press 3 to find area of circle
press 4 to find area of triangle
''')

choice = int(input("enter your choice from 1 - 4: "))
if choice == 1:
    print(n*n)
elif choice == 2:
    l = int(input("enter the length :- "))
    w =int(input("enter the width :--"))
    print(l*w)
elif choice == 3:
    print(3.14*(n*n))
elif choice == 4 :
    b = int(input("enter the breadth :- "))
    h =int(input("enter the height :--"))
    print(1/2*b*h)
else:
    print("invalid statement")
    
