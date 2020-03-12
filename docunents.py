documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "passport", "number": "1"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]


directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006', '5400 028765', '5455 002299'],
        '3': []
       }


# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
# имя владельца и номер полки, на котором он будет храниться.
# Расширить домашние задание из лекции 2.1 «Функции — использование встроенных и создание собственных»
# новой функцией, выводящей имена всех владельцев документов. С помощью исключения KeyError проверяйте,
# есть ли поле "name" у документа.


def owner():
    doc_number = input('Введите номер документа ')
    owner_name = str
    real = False
    for document in documents:
        if document["number"] == doc_number:
            try:
                type(document["name"]) == str
            except KeyError:
                document["name"] = 'Владелец не указан'
            owner_name = 'Владелец документа - ' + document["name"]
            real = True
    if real is False:
        owner_name = 'Документа с таким номером нет'
    return owner_name


def documents_list():
    doc_list = []
    for docum in documents:
        try:
            type(docum["name"]) == str
        except KeyError:
            docum["name"] = 'Владелец не указан'
        doc_list.append(docum['type'] + ' "' + docum["number"] + '" ' + docum["name"])
    return doc_list

def shelf():
    doc_number = input('Введите номер документа ')
    shelf_number = str
    real = False
    shelf_key = 1
    for shelfs in directories:
        for docs in directories[shelfs]:
            if docs == doc_number:
                shelf_number = 'Документ лежит на полке ' + str(shelf_key)
                real = True
        shelf_key += 1
    if real is False:
        shelf_number = 'Документа с таким номером на полках нет'
    return shelf_number


def new_document():
    new_passport = input('укажите тип нового документа ')
    new_number = input('укажите номер нового документа ')
    new_name = input('укажите владельца нового документа ')
    new_self = input('На какую полку поставить документ? ')
    on_shelf = directories.get(new_self)
    if on_shelf is None:
        message = 'Такой полки нет, документ не может быть добавлен'
    else:
        new_doc = {"type": new_passport, "number": new_number, "name": new_name}
        documents.append(new_doc)
        on_shelf.append(new_number)
        message = 'Документ добавлен'
    return message

def owners():
    owner_list = []
    for document in documents:
        try:
            type(document["name"]) == str
        except KeyError:
            document["name"] = 'Владелец не указан'
        owner_list.append(document["name"])
    return owner_list





commands = ['p', 'l', 's', 'a', 'o']
print('Введите команду: \np - владелец, \nl - список, \ns - номер полки, \na - добавить документ \no - все владельцы')
command = input('? ').lower()
if command not in commands:
    print('неверная команда')
elif command == 'p':
    print(owner())
elif command == 'l':
    print(documents_list())
elif command == 's':
    print(shelf())
elif command == 'a':
    print(new_document())
elif command == 'o':
    print(owners())
