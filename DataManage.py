import json

with open("base.json", "r", encoding="utf-8") as file:
    data = json.load(file)

def authenticate(login,password):
    users = data["users"]


    for user in users:
        if login == user["name"] and password == user["password"]:
            return True
    return False


def register_user(username, password, birthday, email):
    users = data["users"]

    for user in users:
        if user["name"] == username:
            return False, "Username already exists"

        if user.get("email") == email:
            return False, "Email already exists"

    new_user = {
        "name": username,
        "password": password,
        "birthday": birthday,
        "email": email
    }

    users.append(new_user)

    with open("base.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    return True, "Registration successful"