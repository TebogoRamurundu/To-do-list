...
# 1.  Add
# 2. Subract
# 3. Multipy
# 4. Divide
...

print("select an operation to perform:")
print("1 Add")
print("2 Subract")
print("3 Multiply")
print("4 Divide")

Choice = input( "Enter your choice")

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if Choice == "1":
   print(num1+num2)
elif Choice == "2":
   print(num1-num2)

elif Choice == "3":
 print(num1*num2)

elif Choice == "4":
  if num2 == 0.0:
    print("Divide by 0 Error")
else:    
  print(num1/num2)


