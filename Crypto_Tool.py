# -------------------------------------
# ------------ Crypto Tool ------------
# -------------------------------------

# Import Statments
import time as t
import hashlib as hl

title = """
████████████████████████████████████████████████████████████
█─▄▄▄─█▄─▄▄▀█▄─█─▄█▄─▄▄─█─▄─▄─█─▄▄─███─▄─▄─█─▄▄─█─▄▄─█▄─▄███
█─███▀██─▄─▄██▄─▄███─▄▄▄███─███─██─█████─███─██─█─██─██─██▀█
▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀▄▄▄▄▀▄▄▄▄▄▀

             Encryption, Decryption and Hashing
"""

# Randomly Shuffled List of all characters
chars = "R=$jHU-kN6@XQGz5fI(dl|D4J&n<bcyh9K`%? {/1\Mt>m}\"7W!S*_Tu8ixg3vOVL#.:w0\n2C['A;YZ+],rBFeP)aEopqs~^"

def encryption(text, shift):
    enc_text = ""
    for char in text:
        enc_text = enc_text + chars[(chars.index(char) + shift) % len(chars)]
        shift += 1
    return enc_text

def decryption(text, shift): 
    dec_text = ""
    for char in text:
        dec_text = dec_text + chars[(chars.index(char) - shift) % len(chars)]
        shift += 1
    return dec_text

def choice_validator(choice):
    while choice not in ["1", "2", "3"]:
        choice = input("(Please enter 1, 2 or 3.)\n>>> ").strip()
    return choice

def reading_file_content(file_name):
    while True:
        try:
            with open(file_name, "r") as file:
                user_text = file.read()
            return user_text, file_name
        except FileNotFoundError:
            file_name = input("file not found try again:\n>>> ").strip()

def writing_content(file_name, ciphered_content):
    with open("ciphered_" + file_name, "w") as file:
        file.write(ciphered_content)

def encryption_decryption(choice):
    print("hello to the best files Encryptor & Decryptor")
    t.sleep(2)
    file_content, file_name = reading_file_content(input("Please enter the file name\
(make sure the file is in the current directory)\n>>> ").strip())
    shift = (len(file_content)**2) % len(file_content)
    if choice == "1":
        writing_content(file_name, encryption(file_content, shift))
        print("Encryption Done.")
    else:
        writing_content(file_name, decryption(file_content, shift))
        print("Decryption Done.")

def generate_hash(file_name):
    hash_function = hl.new("sha256")
    while True:
        try:
            with open(file_name, "rb") as f:
                while True:
                    chunk = f.read(4096)
                    if not chunk:
                        break
                    hash_function.update(chunk)
            return hash_function.hexdigest(), file_name
        except FileNotFoundError:
            file_name = input("file not found try again\n>>> ")

def writing_content_hash(file_hash, file_name):
    with open("hashes.txt", "a") as file:
        file.write(f"{file_name}'s hash is --> {file_hash} \n")

def hashing():
    print("Hello to the best SHA file hash generator")
    t.sleep(2)
    choice = choice_validator(input("Do you want to\n[1] \
Generate SHA hash\n[2] Compare hash value with file hash\n[3] \
Compare file hash with file hash\n>>> "))
    if choice == "1":
        file_hash, file_name = generate_hash(input("Please enter the file name\
(make sure the file is in the current directory)\n>>> ").strip())
        t.sleep(1)
        print("Generating Hash...")
        t.sleep(2)
        print("The SHA hash for {} is: {}".format(file_name, file_hash))
        writing_content_hash(file_hash, file_name)
        t.sleep(1)
        print("your new hash has written in hashes.txt file")
    elif choice == "2":
        user_hash = input("Enter Hash\n>>> ").strip()
        t.sleep(1)
        file_hash, file_name = generate_hash(input("Please enter the file name\
(make sure the file is in the current directory)\n>>> ").strip())
        t.sleep(2)
        print("Generating Hash...")
        t.sleep(1)
        print("The SHA hash for {} is: {}".format(file_name, file_hash))
        t.sleep(1)
        if user_hash == file_hash:
            print("The hash value you entered and file hash are the same!")
        else:
            print("The hash value you entered and file hash are different!")
        writing_content_hash(file_hash, file_name)
        t.sleep(1)
        print("your new hash has written in hashes.txt file")
    else:
        first_file_hash, first_file_name = generate_hash(input("Please enter the first file name\
(make sure the file is in the current directory)\n>>> ").strip())
        second_file_hash, second_file_name = generate_hash(input("Please enter the\
second file name\n>>> ").strip())
        while first_file_name == second_file_name:
            second_file_hash, second_file_name = generate_hash(input("You have\
entered the same file, enter another name\n>>> ").strip())
        t.sleep(1)
        print("Generating Hash...")
        t.sleep(1)
        print("The SHA hash for {} is: {}".format(first_file_name, first_file_hash))
        t.sleep(1)
        print("The SHA hash for {} is: {}".format(second_file_name, second_file_hash))
        t.sleep(2)
        if first_file_hash == second_file_hash:
            print("The first file hash and the second file hash are the same!")
        else:
            print("The first file hash and the second file hash are different!")
        writing_content_hash(first_file_hash, first_file_name)
        writing_content_hash(second_file_hash, second_file_name)
        t.sleep(1)
        print("your new hashs has written in hashes.txt file")

def main():
    print(title)
    choice = choice_validator(input("Do you want to\n[1] Encrypt\n[2] Decrypt\n[3] Hash\n>>> ").strip())
    if choice == "1" or choice == "2":
        encryption_decryption(choice)
    else:
        hashing()
    t.sleep(1)
    print("Thanks and see you again!")

main()
