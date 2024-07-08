
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))
fourth = int(input("Enter fourth number: "))

if first<second and first<third and first<fourth:
    print("Smallest number is ", first)
elif second<first and second<third and second<fourth:
    print("Smallest number is ", second)
elif third<first and third<second and third<fourth:
    print("Smallest number is ", third)
else:
    print("Smallest number is ", fourth)