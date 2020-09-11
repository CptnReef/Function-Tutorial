#Question 1
#Creating variables to be used in Parameter
width = "to be overwritten"
height = "example"

#Parameters are logic place holders for equation
def area(width, height):
    result = width * height
    #returning the result variable into parameter
    return result

#Question 2
#This variable is not only calling function, but reassigning parameters expression inside "result = 5 * 6"
result = area(5, 6)
print(result)

#Question 3
#Calling function again, but this time with different values
result = area(7, 6)
print(result)
#Making new line space + Calling function again-again, but this time with new different values
result = area(area(5,5), area(10,10))
print(str(result) + "\n")

#Question 4
def subtract(num1, num2):
    result = num1 - num2
    return result

#Question 5
result = subtract(100, 10)
print(result)
result = subtract(100, 1000)
print(str(result) + "\n")

#Question 7
def add(num1, num2): 
       result = num1 + num2
       return result

result = add(33, 66)
print(result)

result = add(3, 36)
print(str(result) + "\nend of calculations!")
