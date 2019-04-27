# File name: warmupDay9.py
list = [3,6,9,12]
print(list)

product = 1
for x in list:
    product *= x

print(product)

biggestnumber = 0
for number in list:
    if number > biggestnumber:
        biggestnumber = number
print(biggestnumber)


word = input("what's your word?")

print("you typed: " + word)

words = input("what is your string")

print("your string is: " + words)

string = input("Enter your string: ")
counter= 0
for s in string:
    counter = counter+1
print("Length of input string is:", counter)