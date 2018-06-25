from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

class Caesar(Frame):
    def __init__(self, master):
        super(Caesar, self).__init__(master)
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        self.instructionLabel = Label(self, text = "Enter the text to encrypt/decrypt:", font = ('Helvetica', 10))
        self.instructionLabel.grid(row = 0, column = 0, columnspan = 4, pady = 10)
        self.entry = ScrolledText(self, height = 5, width = 45, font = ('Helvetica', 10))
        self.entry.grid(row = 1, column = 0, columnspan = 4)
        self.keyLabel = Label(self, text = "Enter the key:", font = ('Helvetica', 10))
        self.keyLabel.grid(row = 2, column = 0, sticky = W, pady = 10)
        self.entryKey = Entry(self, width = 5, font = ('Helvetica', 10))
        self.entryKey.grid(row = 2, column = 1, sticky = W, pady = 10)
        self.encryptButton = Button(self, text = "Encrypt", width = 10, font = ('Helvetica', 10), command = self.encrypt)
        self.encryptButton.grid(row = 2, column = 3, sticky = E, pady = 10)
        self.decryptButton = Button(self, text = "Decrypt", width=10, font = ('Helvetica', 10), command = self.decrypt)
        self.decryptButton.grid(row = 2, column = 2, sticky = E, pady = 10)
        self.result = ScrolledText(self, height = 5, width = 45, font = ('Helvetica', 10))
        self.result.grid(row = 3, column = 0, columnspan = 4)
        self.result.config(state = DISABLED)
        self.clearButton = Button(self, text = "Clear", width = 10, font = ('Helvetica', 10), command = self.clear)
        self.clearButton.grid(row = 4, column = 0, columnspan = 4, pady = 10)
        self.authorLabel = Label(self, text = "Author: Michał Łukowiak", font = ('Helvetica', 7))
        self.authorLabel.grid(row = 5, column = 0, columnspan = 4, pady = 10)

    def clear(self):
        self.result.config(state = NORMAL)
        self.entry.config(state = NORMAL)
        self.entryKey.config(state = NORMAL)
        self.encryptButton.config(state = NORMAL)
        self.decryptButton.config(state = NORMAL)
        self.entry.delete(1.0, END)
        self.entryKey.delete(0, END)
        self.result.delete(1.0, END)
        self.result.config(state = DISABLED)

    def key_verification(self):
        self.flag = FALSE
        self.inputText = self.entry.get("1.0", "end-1c")
        try:
            self.key = int(self.entryKey.get())
            self.flag = TRUE
        except ValueError:
            messagebox.showerror("Error", "Wrong key value!\nNumber only!")
            self.clear()
            self.entry.insert(INSERT, self.inputText)

    def encrypt(self):
        self.key_verification()
        if self.flag == TRUE:
            self.entry.config(state = DISABLED)
            self.entryKey.config(state = DISABLED)
            self.encryptButton.config(state = DISABLED)
            self.decryptButton.config(state = DISABLED)
            self.result.config(state = NORMAL)
            toEncrypt = self.inputText.upper()
            encrypted = ""
            for letter in range(len(toEncrypt)):
                if self.key > 26:
                    self.key %= 26
                if ord(toEncrypt[letter]) < 65:
                    encrypted += chr(ord(toEncrypt[letter]))
                elif ord(toEncrypt[letter]) > 90 - self.key:
                    encrypted += chr(ord(toEncrypt[letter]) + self.key - 26)
                else:
                    encrypted += chr(ord(toEncrypt[letter]) + self.key)
            self.result.insert(INSERT, encrypted)
            self.result.config(state = DISABLED)

    def decrypt(self):
        self.key_verification()
        if self.flag == TRUE:
            self.entry.config(state = DISABLED)
            self.entryKey.config(state = DISABLED)
            self.encryptButton.config(state = DISABLED)
            self.decryptButton.config(state = DISABLED)
            self.result.config(state = NORMAL)
            toDecrypt = self.inputText.upper()
            decrypted = ""
            for letter in range(len(toDecrypt)):
                if self.key > 26:
                    self.key %= 26
                if ord(toDecrypt[letter]) < 65:
                    decrypted += chr(ord(toDecrypt[letter]))
                elif ord(toDecrypt[letter]) < 65 + self.key:
                    decrypted += chr(ord(toDecrypt[letter]) - self.key + 26)
                else:
                    decrypted += chr(ord(toDecrypt[letter]) - self.key)
            self.result.insert(INSERT, decrypted)
            self.result.config(state = DISABLED)

root = Tk()
root.title("Caesar Cipher")
root.geometry("400x350")
root.wm_maxsize(400, 350)
root.wm_minsize(400, 350)
root.iconbitmap('cc.ico')
caesar = Caesar(root).pack()
root.mainloop()