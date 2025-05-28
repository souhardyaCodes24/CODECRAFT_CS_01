import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode):
    result = ""
    if mode == "decrypt":
        shift = -shift
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result



def encrypt_text():
    try:
        message = entry_message.get()
        shift = int(entry_shift.get())
        if not message:
            raise ValueError("Empty message")
        encrypted = caesar_cipher(message, shift, "encrypt")
        output.delete(0, tk.END)
        output.insert(0, encrypted)
    except:
        messagebox.showinfo("Error", "Please enter message and a valid shift key.")

def decrypt_text():
    try:
        message = entry_message.get()
        shift = int(entry_shift.get())
        if not message:
            raise ValueError("Empty message")
        decrypted = caesar_cipher(message, shift, "decrypt")
        output.delete(0, tk.END)
        output.insert(0, decrypted)
    except:
        messagebox.showinfo("Error", "Please enter message and a valid shift key.")


# GUI setup
window = tk.Tk()
window.title("Caesar Cipher")
window.geometry("500x200")


tk.Label(window, text="Enter Message:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_message = tk.Entry(window, width=40)
entry_message.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Shift Key:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_shift = tk.Entry(window, width=10)
entry_shift.grid(row=1, column=1, padx=10, pady=10, sticky="w")



tk.Button(window, text="Encrypt", command=encrypt_text).grid(row=2, column=0, padx=10, pady=10)
tk.Button(window, text="Decrypt", command=decrypt_text).grid(row=2, column=1, padx=10, pady=10, sticky="w")
 
tk.Label(window, text="Result:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
output = tk.Entry(window, width=40)
output.grid(row=3, column=1, padx=10, pady=10)

tk.Label(window, text="By: Souhardya Saha").grid(row=5, column=2, padx=10, pady=10, sticky="e")

window.mainloop()
