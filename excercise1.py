num1 = 20
num2 = 30
# expected output is 700

def productCheck(num1, num2):
    if num1 * num2 <= 1000: # a check to see if the product of the 2 numbers is over 100
        return num1 * num2
    else: # the contrary 
        return num1 + num2
