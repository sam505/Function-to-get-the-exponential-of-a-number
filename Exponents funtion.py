def exponential_function(number, power):
    result = 1
    print("When calling the function enter the value of the number and the power it is supposed to be raised to. ")
    for index in range (power):
        result = result * number
    return result


print (exponential_function(4, 7))