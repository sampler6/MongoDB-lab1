from tkinter import *
from tkinter import ttk
import json
from db import *
from pymongo.command_cursor import CommandCursor

class AggregationApp:
    def __init__(self, master, f):
        self.master = master
        self.master.title("Aggregate Football Data")

        self.collection_combobox = ttk.Combobox(master, values=['games', "teams"])
        self.collection_combobox.place(relx=0.35, rely=0.05, relwidth=0.3)
        self.collection_combobox.set("teams")
        self.collection_combobox.bind("<<ComboboxSelected>>", self.change)

        self.collection_label = Label(master, text="Выбранная коллекция", font=f)
        self.collection_label.place(relx=0.35, rely=0.0, relwidth=0.3)


        self.command_label = Label(master, text="Команда для агрегации:", font=f)
        self.command_label.place(relx=0.3, rely=0.1, relwidth=0.4)

        self.command_entry = Text(master)
        self.command_entry.place(relx=0.2, rely=0.14, relheight=0.4, relwidth=0.6)

        self.aggregate_button = Button(master, text="Выполнить агрегацию", command=self.perform)
        self.aggregate_button.place(relx=0.8, rely=0.505)

        self.documents_text = Text(master, width=90, height=20, state="disabled")
        self.documents_text.place(relx=0.1, relwidth=0.8, rely=0.54)

        self.collection = teams

    def perform(self):
        result: pymongo.command_cursor.CommandCursor = perform_aggregation(self.command_entry.get("1.0", END),
                                                                           self.collection)
        if result is None:
            return
        self.show_documents(result)

    def show_documents(self, result):
        self.documents_text.config(state=NORMAL)
        self.documents_text.delete(1.0, END)

        for document in result:
            self.documents_text.insert(END, json.dumps({x: document[x] for x in document if x not in "_id"}, indent=4,
                                                       ensure_ascii=False) + '\n_______________________________________\n\n')

        self.documents_text.config(state="disabled")

    def change(self, event):
        self.collection = choose_collection(self.collection_combobox.get())
        print(self.collection)



if __name__ == "__main__":
    root = Tk()
    root.geometry("1080x720")
    root['bg'] = 'grey'
    app = AggregationApp(root, ("Courier", "16", NORMAL))
    root.mainloop()
