import operation_eng, operation_ru


language = None
print("<<< C-A-L-C-U-L-A-T-O-R >>>")
while  language is None:
    language = (input("Choise language 'eng'/ Выберите язык 'ru': ")).strip()
    if language == 'eng':
        operation_eng.operation_eng()
    elif language == 'ru':
        operation_ru.operation_ru()
    else:
        print("Incorrect input / Неверный ввод")
        language = None

