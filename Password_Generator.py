import secrets
import string

def password_generator(length):
    letters = string.ascii_letters
    digits = string.digits
    special_char = string.punctuation
    
    sequence = letters + digits + special_char
    password = ''
    pw_strong = False
    
    while not pw_strong:
        password = ''
        for i in range(length):
            password += ''.join(secrets.choice(sequence))
            
        if (any(char in special_char for char in password) and sum(digit in digits for digit in digits)>=2):
            pw_strong = True
    return password

if __name__ == '__main__':
    length = int(input('Enter the length of the password: '))
    print(password_generator(length))