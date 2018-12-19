import fync

def operation_eng():
    result = None
    try:
        while result is None:
            oper = (input('Enter operation ' + str((list(fync.calculator.keys()) + (list(fync.calc_func.keys())))) +
                         " or 'exit': ")).strip()
            if oper == "exit":
                print("GOODBYE")
                break

            elif oper in list(fync.calculator.keys()):
                num1 = (float(input('Enter first number: '))).strip()
                num2 = (float(input('Enter second number: '))).strip()
                result = fync.calculator[oper](num1, num2)
                print('''
                {} {} {} = {} 
                '''.format(num1, oper, num2, result))


            elif oper in list(fync.calc_func.keys()):
                num1 = (float(input('Enter number: '))).strip()
                result = fync.calc_func[oper](num1)
                print('''
                {} {} = {}
                '''.format(oper, num1, result))


            else:
                print(oper, "Incorrect operation. Try again")

    except ZeroDivisionError:
        print("Division by zero!!!!!")
    except ValueError as e:
        print("Invalid input!")
        print("Error: ", e)
    return result