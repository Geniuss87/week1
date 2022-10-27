# def authorize_check(username, entered_username, password, entered_password):
#
#     if username == entered_username and password == entered_password:
#         return
#     else:
#         return
# entered_username = input('Введите логин ')
# entered_password = input(str('Введите пароль '))
# result = authorize_check("arthur001", entered_username, "12345678qwe", entered_password)
# print(result)

# def func(district: str, material: str, area: float, price):
#     if (district == 'чон-арык' or district == 'байтик' or district == 'ортосай') and \
#             (material == 'кирпич' and area <= 4 and price <= 50000) or \
#             (material == 'пескоблок' and area <= 5 and price <= 45000):
#         return True
#     else:
#         return False
#
#
# result = func('чон-арык', 'кирпич', 4, 49000)
# print(result)

# def get_extension(filename):
#     if filename[filename.find(".") + 1:] == 'png':
#     return True
#     else:
#     return False
#
#
# result = get_extension('file.png')
# print(result)

# def get_extension(filename):
#     file = str(filename)
#     if file[file.find('.') + 1:] == 'png': # находит текст после точки
#         return 'Расширение файла - {}'.format('png')
#     elif file[file.find('.') + 1:] == 'jpeg':
#         return 'Расширение файла - {}'.format('jpeg')
#     elif file[file.find('.') + 1:] == 'html':
#         return 'Расширение файла - {}'.format('html')
#     elif file[file.find('.') + 1:] == 'doc':
#         return 'Расширение файла - {}'.format('doc')
#     elif file[file.find('.') + 1:] == 'xlsx':
#         return 'Расширение файла - {}'.format('xlsx')
#     else:
#         return None
#
#
# result = get_extension('text.doc')
# print(result)


# def bank(m ,n):
#     Eff_rate = (((1 + (10 / 100)) ** n) - 1) * (100 / n)
#     Deposit = int(m + ((m * (Eff_rate / 100)) * n))
#     return Deposit
#
#
# result = bank(1000, 2)
# print(result)

# def knight_beats(x1, x2, y1, y2):
#     if (x2 == x1 + 2 or x2 == x1 - 2) and (y2 == y1 - 1 and y2 == y1 + 1):
#         return 'Yes'
#     elif (y2 == y1 - 2 or y2 == y1 + 2) and (x2 == x1 + 1 or x2 == x1 - 1):
#         return 'Yes'
#     else:
#         return 'No'
#
#
# result = knight_beats(4, 5, 4, 3)
# print(result)

# def choose_pc(ram: int, hdd: int, hdd_type: str, price: float, condition: bool):
#     # hdd_type = str(input())
#     if (ram >= 4 and ram <= 8) and ((hdd_type == 'SSD' and hdd >= 256) or (hdd_type == 'HDD' and hdd >= 1000)) and \
#     price <= 1000 and condition == 1:
#         return 'Подходит'
#     else:
#         return 'Не подходит'
#
#
# result = choose_pc(9, 300, 'SSD', 760, 1)
# print(result)


# def buy_car(model: str, year: int, usage: int, color: str, owner: int, price: float, left_wheel: bool):
#     if ((model.upper() == 'TOYOTA' or model.upper() == 'LEXUS') and (color == 'white' or color == 'grey') \
#             and year >= 2004 and left_wheel == True and owner <= 2) and ((usage <= 150000 and price <= 10000) \
#                     or (usage >= 200000 and price <= 8000)):
#         return True
#     else:
#         return False
#
#
# result = buy_car('toyota', 2005, 201000, 'grey', 2, 7000, True)
# print(result)

def determine_quarter_of_coordinate(x, y):
    if (int(x) > 0) and (int(y) > 0):
        return 1
    elif (int(x) < 0) and (int(y) > 0):
        return 2
    elif (int(x) < 0) and (int(y) < 0):
        return 3
    elif (int(x) > 0) and (int(y) < 0):
        return 4
    else:
        return None


result = determine_quarter_of_coordinate('1', '4')
print(result)

def determine_quarter_of_coordinate(x, y):
    if (x > 0) and (y > 0):
        return 1
    elif (x < 0) and (y > 0):
        return 2
    elif (x < 0) and (y < 0):
        return 3
    elif (x > 0) and (y < 0):
        return 4
    else:
        return None


result = determine_quarter_of_coordinate(-2, -2)
print(result)