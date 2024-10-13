my_dict = {'kat': 3, 'dog': 5, 'bird': 7}
print(my_dict)
print(my_dict['kat'])
my_dict['fish']= 4
print(my_dict)
my_dict.update({'horse': 2, 'pig': 6})
print(my_dict)
a = my_dict.pop('dog')
print(a)
print(my_dict)
#множества
my_set = {1,2,5,7,2,3,True,'str', False}
print(my_set) #помню что вывод в консоль элементов в другом порядке - не ошибка, но почему не выводится True?
# В уроке у Дениса так же было, но почему, он не объяснил. Посмотрела сама.
#Оказывается True обозначается в системе как 1, а так как 1 у нас уже есть, то он не повторяется во множестве, так как там только уникальные элементы
my_set.update([10,11])
print(my_set)
my_set.remove(0) #False - как мы выяснили = 0
print(my_set)
my_set.discard('str')
print(my_set)
print(my_dict.get('fox'))