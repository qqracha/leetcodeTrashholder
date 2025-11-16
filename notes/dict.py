# Значения
d = {"user1": "+79481267421",
     "user2": "+79474217492",
     "user3": "+79341849284"}

print(f"Count telephone users: {len(d)}\n--------------") # count keys + value

# Новости
d["user1"] = "number is busy" # обновляем значение словаря
print(f"Current news: \nNumber 'user1' was changed - {d['user1']}\n--------------")

# Телефонная книжка
user_responce = input("Which user are you interested in?\nUse 'list' for more info.\nEnter user key: ")
if user_responce == "list":
    print("--------------\nUser list:\n" + "\n".join(d.keys()))
    number = input("--------------\nEnter user key: ")
    try:
        print(f"{number} number: {d[number]}")
    except KeyError:
        print("Wrong user key. Try again")
else:
    try:
        print(f"{user_responce} number: {d[user_responce]}")
    except KeyError:
        print("Current user not found. Try again")