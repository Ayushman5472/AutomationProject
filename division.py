Question = input("Division or Divisibility Rules?: ")
Dividend = ""
Divisor = ""
if Question == "Division":    
    Dividend = int(input("Please enter the dividend here to check if it is divisible:  "))
    Divisor = int (input("Please enter the divisor here:  "))
    if Dividend % Divisor == 0:
        print("Yes it is divisible, the answer is: ")
        print(Dividend/Divisor)
    else:
        print("No it is not fully Divisible, the answer will be: ")
        print(Dividend/Divisor)

elif Question == "Divisibility Rules":
    Number = int(input("Please enter the number (1 - 5):  ")) 
    if Number == 1:
        print("Every number is divisible by 1")
    if Number == 2:
        print("All even numbers (ending with 0,2,4,6,8) are divisible by 2")
    if Number == 3:
        print("If sum of the digits is divisible by 3, the number is divisible by 3")
    if Number == 4:
        print("If last two digits of number are divisible by 4, the number if divisible by 4")
    if Number == 5:
        print("If number ends with 0 or 5, the number is divisible by 5")
    if Number>5:
        print("Please enter a valid number")

