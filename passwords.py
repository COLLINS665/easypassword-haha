import string
import secrets

# I am a lazy man, I used chatgpt to get generate_password function then I modified it.
# I wrote the rest of the code myself (the easy part haha).

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

pass_length = int(input("Enter the length of password you want to generate: "))
# password = generate_password(pass_length)

print(generate_password(pass_length))

