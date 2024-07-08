
# Increment
number = 20
while number <= 30:
    print(number)
    number += 1

# Decrement
count = 10
while count >= 1:
    print("Number is",count)
    count -= 1

# Break and continue statements
x = 100
while x <=105:
    print(x)
    if x == 103:
        break
    x += 1


y = 199
while y < 205:
    y += 1
    if y == 202:
        continue
    print(y)

# For loop

for mynum in range(5):
    print(mynum)

for mynum in range(80,90):
    print(mynum)

for z in range(1,10,3):
    print(z)

languages = ['Python','Kotlin','C++']
for lang in languages:
    print(lang)