import string
import random

CHARACTERS = list(string.ascii_letters + string.digits + string.punctuation)
FILE_NAME = 'generated_passwords.txt'

def main():
    while True:
        length = input('Type the length of your password or "stop" \
to finish.\n')

        try:
            length = int(length)
            subject = input('Type a subject that will remember that password \
is for what.\n')
            password = generate_password(length)
            save_data(subject, password)
        except:
            if length == 'stop':
                print(f'You can access your passwords in the file {FILE_NAME}.')
                break
            else: print('Invalid input.')

 def generate_password(length):
    password = ''

    for i in range(length):
        password = password + random.choice(CHARACTERS)

    return password
                
def save_data(subject, password):
    password_file = open(FILE_NAME, 'a')
    password_file.write(subject + ': ' + password + '\n')
    password_file.close()

if __name__ == '__main__':
    main()
