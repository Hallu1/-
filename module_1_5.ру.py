from importlib import import_module

immutable_var = (1, 2, 3, True, 'str', 'я', "ты", "и море", 1.05) #скобки можно не использовать
print(immutable_var)
#immutable_var[0] = 2 #невозможно поменять, потому что картеж не поддерживает вообще изменение элементов.
#однако можно изменить элемент внутри элемента
print(type(immutable_var))
immutable_var = ([0,2,3],4,5,'str')
print(immutable_var)
immutable_var[0][0] = 1
print(immutable_var)
#теперь список
mutable_list = [1, 2, 3, True, 'str', 'я', "ты", "и море", 1.05]
print(mutable_list)
mutable_list[3] = False
print(mutable_list)
mutable_list = [[1, 2], 3, True, 'str', 'я', "ты", "и море", 1.05]
print(mutable_list)
mutable_list[0][1] = 'str'
print(mutable_list)
#хотела изменить элементы элементов в списке, посмотреть работает как в кортеже или нет. работает!:D

