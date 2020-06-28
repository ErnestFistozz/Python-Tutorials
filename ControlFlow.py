#if, elif and else statements

age = 13;
if age < 16:
    print("You are not eligible to vote")
elif age >=16 and age <= 18:
    print("You are not eligible to vote\nbut can register for the up coming elections")
else:
    print("You are eligible to vote" )

# for loop statement

for value in range(10):
    print('Hello {}'.format(value))

#while loop statement
value = 0
while value  != 5:
    print("Hello Ernest, i am greeing for the {}th time".format(value))
    value += 1