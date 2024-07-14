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

\033[1;32m             Encryption, Decryption and Hashing\033[0m
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
        choice = input("\033[1;31m(Please enter 1, 2 or 3.)\n>>> \033[0m").strip()
    return choice

def reading_file_content(file_name):
    while True:
        try:
            with open(file_name, "r") as file:
                user_text = file.read()
            return user_text, file_name
        except FileNotFoundError:
            file_name = input("\033[1;31mfile not found try again:\n>>> \033[0m").strip()

def writing_content(file_name, ciphered_content):
    with open("ciphered_" + file_name, "w") as file:
        file.write(ciphered_content)

def encryption_decryption(choice):
    print("\033[1;34mhello to the best files Encryptor & Decryptor\033[0m")
    t.sleep(2)
    file_content, file_name = reading_file_content(input("\033[1;33mPlease enter the file name\
(make sure the file is in the current directory)\n>>> \033[0m").strip())
    shift = (len(file_content)**2) % len(file_content)
    if choice == "1":
        writing_content(file_name, encryption(file_content, shift))
        print("\033[1;34mEncryption Done.\033[0m")
    else:
        writing_content(file_name, decryption(file_content, shift))
        print("\033[1;34mDecryption Done.\033[0m")

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
            file_name = input("\033[1;31mfile not found try again\n>>> \033[0m")

def writing_content_hash(file_hash, file_name):
    with open("hashes.txt", "a") as file:
        file.write(f"{file_name}'s hash is --> {file_hash} \n")

def hashing():
    print("\033[1;34mHello to the best SHA file hash generator\033[0m")
    t.sleep(2)
    choice = choice_validator(input("\033[1;33mDo you want to\n[1] \
Generate SHA hash\n[2] Compare hash value with file hash\n[3] \
Compare file hash with file hash\n>>> \033[0m"))
    if choice == "1":
        file_hash, file_name = generate_hash(input("\033[1;33mPlease enter the file name\
(make sure the file is in the current directory)\n>>> \033[0m").strip())
        t.sleep(1)
        print("\033[1;34mGenerating Hash...\033[0m")
        t.sleep(2)
        print("\033[1;34mThe SHA hash for {} is:\033[0m \033[1;36m{}\033[0m".format(file_name, file_hash))
        writing_content_hash(file_hash, file_name)
        t.sleep(1)
        print("\033[1;34myour new hash has written in hashes.txt file\033[0m")
    elif choice == "2":
        user_hash = input("\033[1;33mEnter Hash\n>>> \033[0m").strip()
        t.sleep(1)
        file_hash, file_name = generate_hash(input("\033[1;33mPlease enter the file name\
(make sure the file is in the current directory)\n>>> \033[0m").strip())
        t.sleep(2)
        print("\033[1;34mGenerating Hash...\033[0m")
        t.sleep(1)
        print("\033[1;34mThe SHA hash for {} is:\033[0m \033[1;36m{}\033[0m".format(file_name, file_hash))
        t.sleep(1)
        if user_hash == file_hash:
            print("\033[1;34mThe hash value you entered and file hash are\033[0m \033[1;32mthe same!\033[0m")
        else:
            print("\033[1;34mThe hash value you entered and file hash are\033[0m \033[1;31mdifferent!\033[0m")
        writing_content_hash(file_hash, file_name)
        t.sleep(1)
        print("\033[1;34myour new hash has written in hashes.txt file\033[0m")
    else:
        first_file_hash, first_file_name = generate_hash(input("\033[1;33mPlease enter the first file name\
(make sure the file is in the current directory)\n>>> \033[0m").strip())
        second_file_hash, second_file_name = generate_hash(input("\033[1;33mPlease enter the\
second file name\n>>> \033[0m").strip())
        while first_file_name == second_file_name:
            second_file_hash, second_file_name = generate_hash(input("\033[1;31mYou have\
entered the same file, enter another name\n>>> \033[0m").strip())
        t.sleep(1)
        print("\033[1;34mGenerating Hash...\033[0m")
        t.sleep(1)
        print("\033[1;34mThe SHA hash for {} is:\033[0m \033[1;36m{}\033[0m".format(first_file_name, first_file_hash))
        t.sleep(1)
        print("\033[1;34mThe SHA hash for {} is:\033[0m \033[1;36m{}\033[0m".format(second_file_name, second_file_hash))
        t.sleep(2)
        if first_file_hash == second_file_hash:
            print("\033[1;34mThe first file hash and the second file hash are\033[0m \033[1;32mthe same!\033[0m")
        else:
            print("\033[1;34mThe first file hash and the second file hash are\033[0m \033[1;31mdifferent!\033[0m")
        writing_content_hash(first_file_hash, first_file_name)
        writing_content_hash(second_file_hash, second_file_name)
        t.sleep(1)
        print("\033[1;34myour new hashs has written in hashes.txt file\033[0m")

def main():
    print(title)
    choice = choice_validator(input("\033[1;33mDo you want to\n[1] Encrypt\n[2] Decrypt\n[3] Hash\n>>> \033[0m").strip())
    if choice == "1" or choice == "2":
        encryption_decryption(choice)
    else:
        hashing()
    t.sleep(1)
    print("\033[1;35mThanks and see you again!\033[0m")

main()