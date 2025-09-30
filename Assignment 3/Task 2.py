import math
try:
    number=float(input("Enter a Positive number:"))
    if number<=0:
        print("Please enter a number which is grater than zero for valid answer:")

    else:
        Squareroot_result=math.sqrt(number)
        log_result=math.log(number)
        sine_result=math.sin(number)

        print(f"\n result for the number{number}:")
        print(f"\n square Root:{ Squareroot_result}:")
        print(f"\n Natural logarathm {log_result}:")
        print(f"\n Sin(in Radians):{ sine_result}:")

except ValueError:
    print("Enter a valid input.")
