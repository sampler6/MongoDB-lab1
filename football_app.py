import tkinter as tk
from tkinter import ttk
import json

import db
from db import *


class FootballApp:
    def __init__(self, master: tk.Tk, main_font: tuple[str, str, str]):
        self.master = master
        self.master.title("Football Database")

        self.key_label = tk.Label(master=master, text="Ключ:", font=main_font)
        self.key_label.place(relx=0.1, rely=0.1)
        self.key_entry = tk.Entry(master=master)
        self.key_entry.place(relx=0.1, rely=0.15, relwidth=0.35)

        self.value_label = tk.Label(master=master, text="Значение:", font=main_font)
        self.value_label.place(relx=0.55, rely=0.1)
        self.value_entry = tk.Entry(master=master)
        self.value_entry.place(relx=0.55, rely=0.15, relwidth=0.35)

        self.button_add = tk.Button(text="Добавить", command=self.add)
        self.button_add.place(relx=0.2, rely=0.2, relwidth=0.20)

        self.button_add = tk.Button(text="Сохранить", command=self.save)
        self.button_add.place(relx=0.4, rely=0.2, relwidth=0.20)

        self.button_change = tk.Button(text="Изменить коллекцию", command=self.change)
        self.button_change.place(relx=0.6, rely=0.2, relwidth=0.20)

        self.documents_text = tk.Text(master, state="disabled")
        self.documents_text.place(relx=0.1, rely=0.4, relwidth=0.8)

        self.collections_combobox = ttk.Combobox(master=master, values=["games", "teams"])
        self.collections_combobox.place(relx=0.4, rely=0.3, relheight=0.05, relwidth=0.2)
        self.collections_combobox.set("teams")

        self.document = {}
        self.change()
        self.view_current_doc()

    def add(self):
        db.add(self.key_entry.get(), json.dumps(self.value_entry.get()), self.document)
        self.view_current_doc()

    def save(self):
        self.document = save(self.document, self.collection)
        self.view_current_doc()

    def change(self):
        self.collection = choose_collection(self.collections_combobox.get())
        print(self.collection)

    def view_current_doc(self):
        self.documents_text.config(state=tk.NORMAL)
        self.documents_text.delete(1.0, tk.END)
        print(self.document)
        self.documents_text.insert(tk.END, "Текущий документ: " + json.dumps(self.document))
        for doc in db.get_documents(self.collection):
            self.documents_text.insert(tk.END, json.dumps({x: doc[x] for x in doc if x not in "_id"},
                                       indent=4, ensure_ascii=False) + "\n")
        self.documents_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1080x720")
    root['bg'] = 'grey'
    app = FootballApp(root, ("Courier", "20", tk.NORMAL))
    root.mainloop()
