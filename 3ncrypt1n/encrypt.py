import random, string, os, sys
from hashlib import sha256

alphabet = string.ascii_letters + string.digits + ' @!#$%^&*(){}[]/?~.,-=+_:;<>|`"\''  # Include digits
MARKER = "$3nCryPt3D$\n\n"

def generate_mappings(key):
    hash_value = sha256(key.encode()).hexdigest()
    random.seed(hash_value)
    
    char_to_num = {}
    num_to_char = {}
    
    numbers = list(range(1, 1000000))  # Reduce the range
    
    random.shuffle(numbers)
    
    for char in alphabet:
        random_num = numbers.pop()
        char_to_num[char] = random_num

    return char_to_num

def generate_char():
    random_num = random.randint(0, 50)
    return alphabet[random_num]

def randoming(encrypted_text):
    random_num = random.randint(1, 10)
    if random_num % 2 == 0:
        encrypted_text = encrypted_text[:-1]
    return encrypted_text

def encrypt(text, key):
    char_to_num = generate_mappings(key)
    encrypted_text = MARKER
    
    for char in text:
        if char == '\n':
            encrypted_text += char
        else:
            if char in char_to_num:
                encrypted_text += str(char_to_num[char]) + generate_char()
            else:
                encrypted_text += char + generate_char()
    
    encrypted_text = randoming(encrypted_text)
    return encrypted_text

def open_file(key):
    if os.path.exists(file_name) and os.path.isfile(file_name):
        with open(file_name, "r") as file:
            content = file.read()
            if content.startswith(MARKER):
                print("File is already encrypted.")
                return content

            encrypted_text = encrypt(content, key)
            with open(file.name, "w") as outfile:
                outfile.write(encrypted_text)
                print('File was encrypted sucessfully')
            return encrypted_text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python encrypt.py <file_name>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    key = input("Enter encryption key: ")
    encrypted = open_file(key)
        
