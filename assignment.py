# A program that checks whether a number is prime or not
num = 19
if num > 1:
    for i in range(2, (num//2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# A program that checks whether a letter is a vowel or consonant
def vowelOrConsonant(x):
    if (x == 'a' or x == 'e' or
            x == 'i' or x == 'o' or x == 'u'):
        print("Vowel")
    else:
        print("Consonant")

vowelOrConsonant('a')
vowelOrConsonant('e')

# A python program demonstrating the concept of inheritance
class A:
    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2 working")

a1 = A()
a1.feature1()
a1.feature2()

class B(A):
    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("Feature 4 working")

b1 = B()
b1.feature3()
b1.feature4()



