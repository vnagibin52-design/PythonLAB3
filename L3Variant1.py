parameters = ("«Python в инженерных задачах»", "15.10.2026", "204")

zayvki = [102, 117, 131, 145, 156, 160]

registered = {102, 117, 131, 145}

users = {
    102: "Анна Орлова",
    117: "Иван Петров", 
    131: "Иван Иванов",
    145: "Витя Березников",
    156: "Пётр Ковалёв", 
    160: "Дмитрий Смирнов",
}

print("Параметры конференции:", parameters[0], parameters[1], "аудитория", parameters[2])
print("Заявки в порядке поступления:", zayvki)
print("Зарегистрированные участники: ", sorted(registered))

print("Участники: ", end = '')

for key, value in users.items():
    print(key, "-", value, end = '')
    if key != next(reversed(users)):
            print(", ",  end = '')

print()
zayvki.append(174)
print("После добавления заявки:", zayvki)

check_id = 131
print("Участник", check_id, "зарегистрирован: ", end = '')
if check_id in registered:
    print("да")
else: print("нет")

users_id = 117
print((f"ФИО участника {users_id}:"), end = ' ')
if users_id in users:
    print(users[users_id])
else: print("не найдено")