grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(type(students))
#переводим множество в список
print(students)
students = sorted(list(students))
print(students)
grades[0] = sum(grades[0])/len(grades[0])
print(grades[0])
grades[1] = sum(grades[1])/len(grades[1])
grades[2] = sum(grades[2])/len(grades[2])
grades[3] = sum(grades[3])/len(grades[3])
grades[4] = sum(grades[4])/len(grades[4])
print(grades)
nambers = dict(zip(students,grades))
print(nambers)
print(type(nambers))
quantity = int(input("Введите количество записей, которые вы хотите добавить: "))
for i in range(quantity):
    name = input("Введите имя нового студента: ")
    ball = input("Введите средний балл нового студента: ")
    nambers[name] = ball
print("Словарь после добавления пользовательского ввода:", nambers)
#хотела сделать возможность пользовательского ввода, чтобы в список можно было добавлять новых сткдентов и их оценку, но,
#кажется слишком высоко замахнулась, так как не смогла сообразить и даже найти вразумительный ответ
#как именно мне в качестве значения добавлять несколько оценок, а потом автоматически посчитать средний балл по всем.
#в итоге можно добавить только студента с уже известным средним баллом. Так, чисто для учета, но без подсчетов
#не уверена, что поняла все задания как надо, но итог появившийся в консоли вроде верный