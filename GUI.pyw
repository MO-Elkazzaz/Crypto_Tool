import os as o
while True:
    try:
        import customtkinter as ctk
        break
    except ImportError:
        o.system("pip install customtkinter")
import hashlib as hl

app = ctk.CTk()
message = ctk.CTk()
message.geometry("650x100+700+490")
app.geometry("700x400+570+300")
ctk.set_appearance_mode("dark")
message.resizable(False, False)
app.resizable(False, False)
message.title("Message")
app.title("Crypto Tool")
chars = "R=$jHU-kN6@XQGz5fI(dl|D4J&n<bcyh9K`%? {/1\Mt>m}\"7W!S*_Tu8ixg3vOVL#.:w0\n2C['A;YZ+],rBFeP)aEopqs~^"

big_inputs_frame = ctk.CTkFrame(app, fg_color="transparent")
small_inputs_frame = ctk.CTkFrame(big_inputs_frame, fg_color="transparent")
one_option_button = ctk.CTkButton(big_inputs_frame, text="Submit", width=130, height=40, font=("Arial", 22), hover_color="#e06cdb", command=lambda: files_validator(first_entry_obj, crypto_choice))
two_options_button = ctk.CTkButton(big_inputs_frame, text="Submit", width=130, height=40, font=("Arial", 22), hover_color="#e06cdb", command=lambda: files_validator(first_entry_obj, crypto_choice, second_entry_obj))

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

def reading_file_content(file_name):
    with open(file_name, "r") as file:
        user_text = file.read()
    return user_text, ((len(user_text)**2) % len(user_text))

def writing_content(file_path, ciphered_content):
    with open(f"ciphered_{o.path.basename(file_path)}", "w") as file:
        file.write(ciphered_content)

def writing_content_hash(file_path, file_hash):
    with open("hashes.txt", "a") as file:
        file.write(f"{o.path.basename(file_path)}'s hash is --> {file_hash} \n")

def generate_hash(file_name):
    hash_function = hl.new("sha256")
    with open(file_name, "rb") as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            hash_function.update(chunk)
    return hash_function.hexdigest()

def files_validator(first_entry, choice, second_entry=""):
    if not second_entry == "":
        entries = [first_entry, second_entry]
        entries_data = []
        for obj in entries:
            if not o.path.exists(obj.get()):
                rewrite_entry(obj, "File was not found")
            else:
                entries_data.append(obj.get())
        main(entries_data, choice)
    else:
        if not o.path.exists(first_entry.get()):
            rewrite_entry(first_entry, "File was not found")
        else:
            main([first_entry.get()], choice)

def main(inputs, choice):
    first_entry_data = inputs[0]
    if choice == "1.1":
        data = reading_file_content(first_entry_data)
        writing_content(first_entry_data, encryption(data[0], data[1]))
        message_text = "Encryption Process is done"
        app.destroy()
    elif choice == "1.2":
        data = reading_file_content(first_entry_data)
        writing_content(first_entry_data, decryption(data[0], data[1]))
        message_text = "Decryption Process is done"
        app.destroy()
    elif choice == "2.1":
        writing_content_hash(first_entry_data ,generate_hash(first_entry_data))
        message_text = text="Gnerating Hash Process is done"
        app.destroy()
    elif choice == "2.2":
        user_hash = entry_obj.get()
        file_hash = generate_hash(first_entry_data)
        writing_content_hash(first_entry_data, file_hash)
        if user_hash == file_hash:
            message_text = "The hash value you entered and file hash are the same!"
        else:
            message_text = "The hash value you entered and file hash are different!"
        app.destroy()
    elif choice == "2.3":
        print(len(inputs))
        second_entry_data = inputs[1]
        first_file_hash = generate_hash(first_entry_data)
        second_file_hash = generate_hash(second_entry_data)
        writing_content_hash(first_entry_data, first_file_hash)
        writing_content_hash(second_entry_data, second_file_hash)
        if first_file_hash == second_file_hash:
            message_text = "The first file hash and the second file hash are the same!"
        else:
            message_text = "The first file hash and the second file hash are different!"
        app.destroy()
    lable = ctk.CTkLabel(message, text=message_text, font=("Arial", 24))
    lable.pack(pady=30, anchor="center")
    message.mainloop()

def browse_file(widget):
    rewrite_entry(widget, ctk.filedialog.askopenfilename(filetypes=[("Text files", "*.txt")], title="File Name"))

def rewrite_entry(widget, text):
    widget.delete(0, ctk.END)
    widget.insert(0, text)

def delete(frame):
    for widget in frame.winfo_children():
        widget.grid_forget()

def select_file(parent=big_inputs_frame, order="", row_num=2):
    file_path_frame = ctk.CTkFrame(parent, fg_color="transparent")
    lable = ctk.CTkLabel(file_path_frame, text=f"{order} File Path:  ", font=("Arial", 24))
    lable.grid(row=0, column=0, sticky="w")
    entry = ctk.CTkEntry(file_path_frame, placeholder_text="full file path".center(50), text_color="#FFCC70", width=350, height=40, corner_radius=32, font=("Arial", 20))
    entry.grid(row=0, column=1, sticky="w")
    button = ctk.CTkButton(file_path_frame, text="Browse", width=70, height=40, command=lambda: browse_file(entry), hover_color="#e06cdb", font=("Arial", 20))
    button.grid(row=0, column=3, padx=25, sticky="w")
    file_path_frame.grid(row=row_num, column=0, padx=15, pady=10, sticky="w")
    return entry

def input_frame(parent=big_inputs_frame):
    input_frame = ctk.CTkFrame(parent, fg_color="transparent")
    lable = ctk.CTkLabel(input_frame, text="   Hash Value:  ", font=("Arial", 24))
    lable.grid(row=0, column=0, sticky="w")
    entry = ctk.CTkEntry(input_frame, placeholder_text="Enter Hash".center(50), text_color="#FFCC70", width=350, height=40, corner_radius=32, font=("Arial", 20))
    entry.grid(row=0, column=1, sticky="w")
    input_frame.grid(pady=10 ,sticky="w")
    return entry

def option_one(choice):
    global first_entry_obj, crypto_choice
    big_inputs_frame.grid(row=1, sticky="w")
    delete(big_inputs_frame)
    if choice == "Encryption":
        first_entry_obj = select_file(row_num=1)
        crypto_choice = "1.1"
        one_option_button.grid(padx=275, pady=50)
    elif choice == "Decryption":
        first_entry_obj = select_file(row_num=1)
        crypto_choice = "1.2"
        one_option_button.grid(padx=275, pady=50)
    else:
        option_frame("Hash Option:  ", ["Generate SHA hash", "Compare hash value with file hash", "Compare file hash with file hash"], func=option_two, row_num=1, parent=big_inputs_frame)

def option_two(choice):
    global first_entry_obj, second_entry_obj, crypto_choice, entry_obj
    small_inputs_frame.grid(row=2, sticky="w")
    delete(small_inputs_frame)
    if choice == "Generate SHA hash":
        first_entry_obj = select_file(parent=small_inputs_frame)
        crypto_choice = "2.1"
        one_option_button.grid(padx=275, pady=50)
    elif choice == "Compare hash value with file hash":
        entry_obj = input_frame(parent=small_inputs_frame)
        first_entry_obj = select_file(parent=small_inputs_frame, row_num=3)
        crypto_choice = "2.2"
        one_option_button.grid(padx=275, pady=50)
    elif choice == "Compare file hash with file hash":
        first_entry_obj = select_file(parent=small_inputs_frame, order="First")
        second_entry_obj = select_file(parent=small_inputs_frame, order="Second", row_num=3)
        crypto_choice = "2.3"
        two_options_button.grid(padx=275, pady=50)

def on_close():
    message.destroy()
    if not app == None:
        app.destroy()

def option_frame(text,values, func, row_num=0, parent=app):
    option_frame = ctk.CTkFrame(parent, fg_color="transparent")
    lable = ctk.CTkLabel(option_frame, text=text, font=("Arial", 24))
    lable.grid(row=0, column=0, sticky="w")
    optionmenu_var = ctk.StringVar(value="Choose Option")
    option_menu = ctk.CTkOptionMenu(option_frame,values=values, dropdown_fg_color="#1f6aa5", variable=optionmenu_var, command=func, width=215, height=40, corner_radius=32, font=("Arial", 24), dropdown_hover_color="#e06cdb")
    option_menu.grid(row=0, column=1, sticky="w")
    option_frame.grid(row=row_num, column=0, padx=15, pady=20, sticky="w")

app.protocol("WM_DELETE_WINDOW", on_close)
message.protocol("WM_DELETE_WINDOW", on_close)

option_frame("Crypto Option:  ", ["Encryption", "Decryption", "Hashing"], option_one)

app.mainloop()