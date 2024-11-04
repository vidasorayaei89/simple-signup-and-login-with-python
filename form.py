import json
import datetime
import random



def load():
    with open("form.json") as infile:
        return json.load(infile)
def save(form):
    with open("form.json", "w") as outfile:
        json.dump(form, outfile, indent=4)

def signup():
    form = load()
    time = datetime.datetime.now().strftime("%Y %B %d %H %M %S")
    username = input("enter your username : ".title())
    for i in form:
        while i["username"] == username:
            print("we have this username...".title())
            username = input("enter your username : ".title())
    password = input("enter your password : ".title())
    email = input("enter your email address : ".title())
    while not email.endswith("@gmail.com") and not email.endswith("@email.com"):
        email = input("enter your email address : ".title())
    idcode = random.randint(100000, 999999)
    info = {
        "time": time,
        "username": username,
        "password": password,
        "email": email,
        "idcode": idcode
    }
    print(f"your login time is --> {time} username --> {username}\npasword --> {password}\nemail --> {email}\nidcode --> {idcode}")
    form.append(info)
    save(form)
def login():
    while True:
        question = input("do you want to login as an (1) --> admin or a (2) --> client ?  ".title())
        if question == "1":
            key = "324"
            a_question = input("enter the key please : ".title())
            if a_question == key :
                ask = input("hello and welcome admin what do you want to do :\n1)edit\n2)delete\n3)exit\n".title())
                if ask == "1":
                    form =load()
                    if not form:
                        print("data base is empty".title())
                        continue
                    form = load()
                    username = input("enter your username : ".title())
                    founder = False
                    for i in form:
                        if i["username"] == username:
                            founder = True
                            n_username = input("enter your new username : ".title())
                            i["username"] = n_username
                            save(form)
                    if not founder:
                        print("dont find".title())
                elif ask == "2":
                    form = load()
                    if not form:
                        print("data base is empty".title())
                        continue
                    form = load()
                    username = input("enter your username : ".title())
                    founder = False
                    for i in form:
                        if i["username"] == username:
                            founder = True
                            form.remove(i)
                            save(form)
                    if not founder:
                        print("dont find".title())
                elif ask == "3":
                    print("by then".title())
                    break
                else:
                    print("try again".title())
        elif question == "2":
                    form = load()
                    username = input("enter your username : ".title())
                    password = input("enter your password : ".title())
                    founder = False
                    for i in form:
                        if i["username"] == username:
                            if i["password"] == password:
                                founder = True
                                print("login successfully...".title())
                    if not founder:
                        print("dont find".title())
                    else:
                        return founder

def main():
    print("hello and welcome to our website form...".title())
    print()
    print("-" * 40)
    print()
    question = input("do you want to start ? ".title())
    print()
    print("-" * 40)
    print()
    if question.lower() == "y" or question.lower() == "yes":
        while True:
            menu = input("enter your choice :\n1)signup\n2)login\n3)exit\n".title())
            if menu == "1":
                signup()
            elif menu == "2":
                if login():
                    break
                else:
                    return login()
            elif menu == "3":
                print("by then".title())
                break
            else:
                print("try again".title())
    else:
        print("try again...".title())
        main()
main()

