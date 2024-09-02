from Hashing1 import generate_salt, hashing, mixture

def load_users(file_path):
    users = {}
    with open(file_path, 'r') as file:
        for line in file:
            user_id, password, salt_stored = line.strip().split(',')
            users[user_id] = (password, salt_stored)
    return users

def authenticate_user(users):
    user_id = input("Enter your user ID: ")
    if user_id in users:
        password1 = input("Enter your password: ")
        with open("pass hashed.txt", 'r') as file:
            for line in file:
                user_id, password, salt_stored = line.strip().split(',')
                users[user_id] = salt_stored
                pass_process = salt_stored + password1
                check_pass = hashing(salt_stored,pass_process)
                if check_pass==password:
                    print("Authentication successful")
                else:
                    print("Invalid password.")


    else:
        print("User ID not found.")


def create_new_user():
    newuser = input("Enter the username you want: ")
    newpass = input("Enter the password you want: ")
    # print('The user name is: ' + newuser + " and the password is : " + newpass)
    newinput = input('Are you sure you want to continue? (yes/no)').lower()
    salt_generated = generate_salt()
    if newinput == 'yes':
        pass_process=mixture(salt_generated, newpass)
        pass_output=hashing(salt_generated,pass_process)
        with open('pass hashed.txt', 'a') as file:
            file.write("\n" + newuser + "," + pass_output + "," + salt_generated)
            print("Account created successfully!")
    else:
        print("BYE")


def main():
    file_path = 'pass hashed.txt'
    input1 = input("Do you want to 'login' or 'create acc'?\n").lower()
    users = load_users(file_path)
    if input1 == 'login':
        authenticate_user(users)
    elif input1 == 'create acc':
        create_new_user()
    else:
        print("ERROR!")


main()
