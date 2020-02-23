# function for obtaining the exponent of a number
def exponential_function(number, power):
    result = 1
    print("When calling the function enter the value of the number and the power it is supposed to be raised to. ")
    for index in range (power):
        result = result * number
    return result


print (exponential_function(4, 7))

# different code for getting the exponent of a number
num = input("Enter the number you want to get the exponent: ")
pow = input("Enter the power to raise the number to: ")
answer = 1
for index in range (int(pow)):
    answer = answer * int(num)
print( answer)
