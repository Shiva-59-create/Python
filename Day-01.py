 #adding elements
# #appending elements to a lists
# student = []
# student.append(20)
# print(student)


# #tuple
# student = (10,20,30)
# print(student)

# #dictonary
# student = ({"name": "John", "age": 20})
# print(student)

# #type conversion
# age = input("Enter your age")
# print("Your age is: " + str(age))
# print(type(age))

# #converting string to integer 
# x ="200"
# y = int(x)
# print(type(y))

# #int to float
# x = 10
# y = float(x)
# print(type(y))
# print(y)
# print(type(x))

# #append
# student = [19,12,23]
# student.append("12")
# print(student)

# # dictonary
# student = {"name": "John", "age": 20}
# print(student)  

# #set
# student = {19,12,23,1,2,3,4,5,6,7,8,9}
# print(student)

# #set
# student = {19}
# print(type(student))

# type conversion 
# x =("200")
# y = int (x)
# print(type(y))
 
# #operators
# x = 10
# y = 5
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x // y)
# print(x % y)
# print(x ** y)
 

# addition assignment operator
# x = 10
# x += 5 
# print(x)

# #boolean``
# a = 5
# b = 10
# print(a>b)

# #is refers to check whether names are belongs to 
# #same objects 
# a = 5
# b = 5
# print(a is b)

#membership operator
# #in, not in
# numbers = [10, 20, 30, 40, 50]
# print(20 in numbers)
# print(60 not in numbers)

# #bitwise xor operator
# print(10 ^ 5) # 1010 ^ 0101 = 1111 = 15

#precedence of operators

#  result = (10 + 5) * 2
# print(result)

# #shopping
# price = 1000
# quantity = 3
# total = price - quantity
# if total >=3000:
#     discount = total * 0.10
#     else:
#         discount = 0
#     final_amount = total - discount
#     print(final_price)

#Built-in function 

#1 Length - len() -return no.ofelements

# a=[10,20,30,40,50]
# print(max(a))
# print(len(a))
# print(min( a))

# #4,sum()-Adding elements in list 
# a = [10,20,40,30,50]
# print(sorted(a))

#list method

#1.append - Adding element to the end 
# a = [10,20,30]
# #list_name.append(value
# a.append(90)
# print(a)

#extend - Adding multiple elenments 

# nums = [10,20,30,40]
# nums.append([50,60])
# print(nums)

# #insert() - Adding a element 
# a = ([1,20,30,40])
# a.insert(2,10)
# print(a)

# #remove() - removes the first matching element 
# a = [10,20,30,20]
# a.remove(20)
# print(a)

# #indexing() - returns the index of first value
# a = (10,20,30,40,30)
# print(a.index(30))

#sort()
# nums = [20,40,30,60,50]
# nums.sort()
# print(nums)


#if,ifelse  #conditional statements
# age = int(input("Enter your age: "))  
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

#elif statement
# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     print("Grade: A")   
# elif marks >= 80:
#         print("Grade: B")
# elif marks >= 70:
#         print("Grade: C")

#NESTED IF ELSE
# age = 25
# has_id = True 
# if age >= 18:
#     print("You are eligible to vote.")
#     if has_id:
#         print("You have a valid ID.")
#     else:
#         print("You need a valid ID to vote.")

# #1 atm
# card_valid = True
# pin_correct = True
# if card_valid and pin_correct:
#     print("Access granted. You can proceed with your transactions.")
# else:  
#     print("Access denied. Please check your card and PIN.")

# #online shopping
# item_in_stock = True
# login_with_account = False
# if item_in_stock and login_with_account:
#     print("payment is done.")
# else:
#     print("Payment failed. Please check item availability and login status.")


# #atm
# card_valid = True
# pin_correct = True
# card = int(input("Enter your card number: "))
# pin = int(input("Enter your PIN: "))
# if card == 7207095628:
#     print("Access granted. You can proceed with your transactions.")
# else:  
#     print("Access denied. Please check your card and PIN.") 

# if pin == 1234:
#    print("Access granted. You can proceed with your transactions.")
# else:  
#     print("Access denied. Please check your card and PIN.")
# if card == 7207095628 and pin == 1234:
#     print("Access granted. You can proceed with your transactions.")
# else:
#     print("Access denied. Please check your card and PIN.")

# if card == 7207095628 and pin == 1234:
#        print("available balance is 10000")
#        print("Enter the amount to withdraw: ")
#        amount = int(input())
# if amount <= 10000:
#            print("Transaction successful. Please collect your cash.")
# else:
#            print("Insufficient balance. Transaction failed.")

#identify A number either positive, negative or zero
# number = int(input("Enter a number: "))
# if number > 0:
#     print("The number is positive.")
# elif number < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")   
#


# even or odd number
# number = int(input("Enter a number: ")) 
# if number % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

#largest of two numbers
# number = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
# if number > number2:
#     print("The largest number is:", number)
# elif number2 > number:
#     print("The largest number is:", number2)
# else:
#     print("Both numbers are equal.")/

# #college addmission
# marks = int(input("Enter your marks: "))
# entrance = int(input("did you pass entrance exam? (yes,no): "))

# if marks >= 75 and entrance.lower() == "yes":
#     print("Congratulations! You are eligible for admission.")   

#login system
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if username == "admin" and password == "password123":
#     print("Login successful. Welcome, admin!")
# else:
#     print("Login failed. Please check your username and password.")  



# #driving eligibility
# age = int(input("Enter your age: "))
# driving_license = input("Do you have a valid driving license? (yes/no): ")
# if age >= 18 and driving_license.lower() == "yes":
#     print("You are eligible to drive.")
# else:
#     print("You are not eligible to drive.")

#movie ticket pricing
#below 5 - free
#5-12 - 100 
#13-59 - 200
#60 and above - 120

# age = int(input("Enter your age: "))
# if age < 5:
#     print("Ticket price: Free") 
# elif age >= 5 and age <= 12:
#     print("Ticket price: 100")
# elif age >= 13 and age <= 59:
#     print("Ticket price: 200")
# elif age >= 60:
#     print("Ticket price: 120")

# #leap year
# year = int(input("Enter a year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(year, "is a leap year.")
#         else:
#             print(year, "is not a leap year.")
#     else:
#         print(year, "is a leap year.")
# else:
#     print(year, "is not a leap year.")
 

# # employee management system
# #performance >90 and experience >5 = 20% hike
# #performance >90 and experience <5 = 10% hike
# #performance >80 = 10% hike
# #performance >70 = 5% hike

# performance = int(input("Enter employee performance score: "))
# experience = int(input("Enter employee years of experience: "))
# salary = float(input("Enter employee current salary: "))
# hike_salary1= salary + (salary * 0.20)  # 20% hike
# hike_salary2= salary + (salary * 0.10)  # 10% hike
# hike_salary3= salary + (salary * 0.05)  # 5% hike
# if performance > 90 and experience > 5:
#     print("Employee is eligible for a 20% salary hike.",hike_salary1)
# elif performance > 90 and experience < 5:
#     print("Employee is eligible for a 10% salary hike.",hike_salary2)
# elif performance > 80:
#     print("Employee is eligible for a 10% salary hike.",hike_salary2)
# elif performance > 70:
#     print("Employee is eligible for a 5% salary hike.",hike_salary3)


#