'''
def product_digit(num):
    
    absolute = abs(num)

    str_num = str(absolute)

    product = 1

    for i in str_num:

        digit = int(i)
        product *= digit

    return product 


num = int(input("Enter number: "))
print(f"The product of digit is {product_digit(num)}")


def product_digit(num):

'''

