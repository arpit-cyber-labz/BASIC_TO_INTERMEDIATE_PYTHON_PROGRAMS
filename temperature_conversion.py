choice = int(input("Enter 1 for Celsius to Fahrenheit, 2 for Fahrenheit to Celsius: "))

if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    f = c * 9/5 + 32
    print("Temperature in Fahrenheit:", f)

elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print("Temperature in Celsius:", c)

else:
    print("Invalid choice")
