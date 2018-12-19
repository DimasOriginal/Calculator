import fync

def operation_ru():
    result = None
    try:
        while result is None:
            oper = (input('Введите операцию ' + str((list(fync.calculator.keys()) + (list(fync.calc_func.keys())))) +
                         " или 'exit' для выхода: ")).strip()
            if oper == "exit":
                print("Досвидание")
                break

            elif oper in list(fync.calculator.keys()):
                num1 = (float(input('Введите первое число: '))).strip()
                num2 = (float(input('Введите второе число: '))).strip()
                result = fync.calculator[oper](num1, num2)
                print('''
                {} {} {} = {} 
                '''.format(num1, oper, num2, result))


            elif oper in list(fync.calc_func.keys()):
                num1 = (float(input('Введите число: '))).strip()
                result = fync.calc_func[oper](num1)
                print('''
                {} {} = {}
                '''.format(oper, num1, result))


            else:
                print(oper, "Не правильная операция. Попробуйте ещё")

    except ZeroDivisionError:
            print("Деление на ноль !!!!!")
    except ValueError as e:
            print("Некоректный ввод")
            print("ОШИБКА: ", e)

    return result