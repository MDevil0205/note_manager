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

note={
    "Имя пользователя":username,
    "Заголовок заметки":title,
    "Описание заметки":content,
    "Статус заметки":status,
    'Дата создания заметки в формате "день-месяц-год"':created_date,
    'Дата истечения заметки в формате "день-месяц-год"':issue_date,
    "Название заголовка":my_list}

print("\nВы ввели данные: ")
for key, value in note.items():
    print("{0}:{1}".format(key,value))
