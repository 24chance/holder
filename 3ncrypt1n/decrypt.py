import os, string, random, re, sys
from hashlib import sha256

alphabet = string.ascii_letters + string.digits + ' @!#$%^&*(){}[]/?~.,-=+_:;<>|`"\''  # Include digits
MARKER = "$3nCryPt3D$\n\n"

def generate_mappings(key):
    # Create a SHA-256 hash of the key
    hash_value = sha256(key.encode()).hexdigest()
    # Seed the random number generator with the hash value
    random.seed(hash_value)
    
    char_to_num = {}
    num_to_char = {}
    
    numbers = list(range(1, 1000000))  # Reduce the range
    random.shuffle(numbers)
    
    for char in alphabet:
        random_num = numbers.pop()
        char_to_num[char] = random_num
        num_to_char[random_num] = char
    
    return num_to_char

def decrypt(encrypted_text, key):
    num_to_char = generate_mappings(key)
    decrypted_text = ''
    
    # Remove marker before decrypting
    if encrypted_text.startswith(MARKER):
        encrypted_text = encrypted_text[len(MARKER):]
    else:
        print("File is not encrypted")
        sys.exit(1)
    
    components = re.findall(r'(\d+|\n)', encrypted_text)  # Include '\n' in the regex pattern
    for component in components:
        if component.isdigit():
            decrypted_text += num_to_char.get(int(component), '')  # Use the digit as the default value
        else:
            decrypted_text += component  # Append newline characters directly
    
    return decrypted_text

def is_valid_decrypted_text(decrypted_text):
    # Check if the decrypted text contains mostly valid characters
    if not decrypted_text:
        return False
    
    valid_chars = set(alphabet + '\n')
    for char in decrypted_text:
        if char not in valid_chars:
            return False
    
    # Additional checks can be added here
    # For instance, checking for the presence of common words or patterns
    common_words = ['the', 'and', 'is', 'in', 'to', 'of', 'a', 'with', 'that', 'for']
    if not any(word in decrypted_text for word in common_words):
        return False
    
    return True

def open_file(key):
    global file_name
    if os.path.exists(file_name) and os.path.isfile(file_name):
        with open(file_name, "r") as file:
            encrypted_text = file.read()
        
        decrypted_text = decrypt(encrypted_text, key)
        if decrypted_text is not None and is_valid_decrypted_text(decrypted_text):
            with open(file_name, "w") as outfile:
                outfile.write(decrypted_text)
            return decrypted_text
        else:
            print("Decryption failed: invalid key or content.")
            return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <file_name>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    key = input("Enter decryption key: ")
    decrypted = open_file(key)
    if decrypted:
        print('File decrypted successfully')
    else:
        print("<--EX00284, $-Failed to decrypt the file due to an invalid key or content.-->")
