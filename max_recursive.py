
def max_recursive(listElements):



def max_2_numbers(number1, number2):
    if not isinstance(number1, (int,float)) or not isinstance(number1, (int,float)):
        raise TypeError("TypeError. max_2_numbers receives 2 numbers")
    elif number1 < number2:
        return number2
    else: 
        return number1

def main():
    my_list=[1,11,19,13,17,2]
    maximo = max_recursive(my_list)
    print(maximo) # maximo debe ser 19


if __name__=="__main__":
    main()