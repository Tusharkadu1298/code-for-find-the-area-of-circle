# 1. write a program to check if number is divisible by both 6 and 9. Take an input from to user for the number.

num =int(input("enter the numbers :-- "))
if num%6==0 and num%9==0:
	print(num," :- " ,"these number get divided by 6 and 9")
else:
	print(num," :- ","these number can't get divided by 6 and 9")
