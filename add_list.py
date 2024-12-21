username=input("Имя пользователя ")
title=input("Заголовок заметки ")
content=input("Описание заметки ")
status=input("Статус заметки ")
created_date=input('Дата создания заметки в формате "день-месяц-год" ')
issue_date=input('Дата истечения заметки в формате "день-месяц-год" ')

my_list=[]
for i in range(3):
    elem=input(f"Название заголовка {i+1} ")
    my_list.append(elem)

print(username)
print(title)
print(content)
print(status)
print(created_date[:5])
print(issue_date[:5])

