import tkinter as tk
from tkinter import ttk
import json

import db
from db import *


class FootballApp:
    def __init__(self, master: tk.Tk, main_font: tuple[str, str, str]):
        self.master = master
        self.master.title("Search App")

        self.key_label = tk.Label(master=master, text="Ключ:", font=main_font)
        self.key_label.place(relx=0.15, rely=0.1)
        self.key_entry = tk.Entry(master=master)
        self.key_entry.place(relx=0.15, rely=0.15, relwidth=0.20)

        self.operator = ttk.Combobox(master=master, values=['>', '>=', '=', '<=', '<', '!='])
        self.operator.place(relx=0.40, rely=0.15, relwidth=0.2)

        self.value_label = tk.Label(master=master, text="Значение:", font=main_font)
        self.value_label.place(relx=0.65, rely=0.1)
        self.value_entry = tk.Entry(master=master)
        self.value_entry.place(relx=0.65, rely=0.15, relwidth=0.20)

        self.button_search = tk.Button(text="Искать", command=self.search)
        self.button_search.place(relx=0.4, rely=0.2, relwidth=0.20)

        self.collections_combobox = ttk.Combobox(master=master, values=["games", "teams"])
        self.collections_combobox.place(relx=0.4, rely=0.3, relheight=0.05, relwidth=0.2)
        self.collections_combobox.set("teams")

        self.documents_text = tk.Text(master, state="disabled")
        self.documents_text.place(relx=0.1, rely=0.4, relwidth=0.8)

        self.collection = ""
        self.change()

    def search(self):

        self.documents_text.config(state=tk.NORMAL)
        self.documents_text.delete(1.0, tk.END)

        for doc in search_document(self.collection, self.key_entry.get(), self.operator.get(), self.value_entry.get()):
            self.documents_text.insert(tk.END, json.dumps({x: doc[x] for x in doc if x not in "_id"},
                                                          indent=4, ensure_ascii=False) + "\n")
        self.documents_text.config(state=tk.DISABLED)

    def change(self):
        self.collection = choose_collection(self.collections_combobox.get())
        print(self.collection)



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1080x720")
    root['bg'] = 'grey'
    app = FootballApp(root, ("Courier", "20", tk.NORMAL))
    root.mainloop()
