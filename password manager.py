from cryptography.fernet import Fernet

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

key = load_key() 
fer = Fernet(key)
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
'''
def view():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print("User:",user,"Password:",fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("passwords.txt","a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
# write_key()
while True:
    mode = input("Would you like the add a new password or view existing one. (view/add) and press q to quit.")   
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")