# if, elif and else statements

age = 13;
if age < 16:
    print("You are not eligible to vote")
elif age >= 16 and age <= 18:
    print("You are not eligible to vote\nbut can register for the up coming elections")
else:
    print("You are eligible to vote")

# for loop statement

for value in range(10):
    print('Hello {}'.format(value))

# while loop statement
value = 0
while value != 5:
    print("Hello Ernest, i am greeting for the {}th time".format(value))
    value += 1

name = 'Ernest'

while True:
    current_name = input('Please Enter your name: ')
    print(current_name)
    if current_name == name:
        break

while True:
    your_name = input('Please enter your name: ')
    if your_name != 'Ernest':
        continue
    print('Hello Joe, what is your password: ')
    password = input('Please put in your password: ')
    if password == 'swordfish':
        break
print('Done with while loop')

required_name = 'Ernest'
while True:
    new_name = input('Enter your name: ')
    if new_name == required_name:
        required_password = 'P@55w0rd'
        while True:
            new_password = input('Enter your password: ')
            if new_password != required_password:
                continue
            else:
                print("Login successful")
                break
        break
    else:
        continue