number1 = 1
number2 = 1
control= 0
counter = 0
counter_stop = int(input("How many digits of the Fibonacci Series would you like to find?:"))
print("--Fibonacci Series--")

while True:
    print(number1,end = "-")
    number2 = control + number1
    control = number1
    number1 = number2
    counter = counter + 1
    if counter == counter_stop : break
