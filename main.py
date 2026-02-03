import requests
import json


def get_randomuser_full_data():
    url = 'https://randomuser.me/api/'
    response = requests.get(url)
    return response.json()


def get_user_data():
    data = get_randomuser_full_data()
    user = data["results"][0]

    return {
        "full_name": user["name"]["first"] + " " + user["name"]["last"],
        "phone": user["phone"],
        "email": user["email"],
        "age": user["dob"]["age"],
        "nat": user["nat"],
        "gender": user["gender"],
        "country": user["location"]["country"]
    }


def main():
    result = get_user_data()

    with open("users.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)



main()
