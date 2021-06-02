#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator")
total_bill = float(input("What is the value of the total bill? "))
tip_percentage = int(input("What percentage of tip would you like to give - 10, 12 or 15? "))
people_count = int(input("How many folks in your party? "))

per_person_cost = total_bill/people_count

person_tip_amount = per_person_cost + (per_person_cost * tip_percentage/100)

print(f"Each person should pay {round(person_tip_amount,2)}")
