#Equal to

value = 8
value2  = 8
# Equal to uses  == (double equals to)
print(value == value2)

#Not Equal to
# Not equal uses !=

print(value2 != value)

#Greater than >
print(value > value2)

#Lesser than <
print(value < value2)

#Lesser or Equal to <=
print(value2 <= value)

#Grater than or equal to >=
print(value2 >= value)

#Not operator

print(not True)

#is Operator
print(True is False)

is_alive = False
if is_alive is True:
    print("Hello I am alive")
elif not is_alive:
    print("I am dead")

#And Operator and Or Operator

if value == 2 or value ==4:
    print("I am either or")
elif value == 2 and value2 == 7:
    print("I have to be both")
else:
    print("I am neither those value")


alice = 'Alice'
another_alice = 'Alice'
if alice is another_alice:
    print("We are both alice")