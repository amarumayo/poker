import tkinter as tk
from tkinter import messagebox
import pandas as pd

try:
    df = pd.read_csv('./records.csv')
except Exception as e:
    data = {
        "Date":[],
        "Description":[],
        "Amount":[],
        "Type":[],
    }

    df = pd.DataFrame(data)

class BudgetTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Tracker")


        # labels and entries
        self.label_date = tk.Label(root, text = "Date (YYYY-MM-DD)")
        self.label_date.grid(row = 0, column = 0)
        self.entry_date = tk.Entry(root)
        self.entry_date.grid(row = 0, column = 1)

        self.label_description = tk.Label(root, text = "Description")
        self.label_description.grid(row = 1, column = 0)
        self.entry_description = tk.Entry(root)
        self.entry_description.grid(row = 1, column = 1)

        self.label_amount = tk.Label(root, text = "Amount")
        self.label_amount.grid(row = 2, column = 0)
        self.entry_amount = tk.Entry(root)
        self.entry_amount.grid(row = 2, column = 1)

        self.label_type = tk.Label(root, text = "Type")
        self.label_type.grid(row = 3, column = 0)
        self.entry_type = tk.Entry(root)
        self.entry_type.grid(row = 3, column = 1)

        # Buttons
        self.button_add = tk.Button(root, text = 'Add Entry', command = self.add_entry)
        self.button_add.grid(row = 4, column = 0, columnspan = 2)
        self.button_view = tk.Button(root, text = 'View Entry', command = self.view_entry)
        self.button_view.grid(row = 5, column = 0, columnspan = 2)
    
    def add_entry(self):
        # retrieve data
        date = self.entry_date.get()
        amount = self.entry_amount.get()
        description = self.entry_description.get()
        type_ = self.entry_type.get()
        if date and amount and description and type:
            new_row = pd.DataFrame({
                "Date":date,
                "Description":[description],
                "Amount":[amount],
                "Type":[type_],
            })
            global df
            df = pd.concat([df, new_row], ignore_index = True)
            df.to_csv('./records.csv', index = False)
            messagebox.showinfo("Sucess", "New entry saved.")
            self.entry_amount.delete(0, tk.END)
            self.entry_date.delete(0, tk.END)
            self.entry_description.delete(0, tk.END)
            self.entry_type.delete(0, tk.END)


        else:
            messagebox.showerror("Error", "All fields must be populated.")

    def view_entry(self):
        global df

        self.top = tk.Toplevel(self.root)
        self.top.title("View Entries")
        text = tk.Text(self.top)
        text.pack()

        for index, row in df.iterrows():
            text.insert(
                tk.END, 
                "Date: " + row['Date'] + " | Description: " + row['Description'] + 
                " | Amount: " + str(row['Amount']) + " | Type: " + row['Type'] + '\n')

            edit_button = tk.Button(
                self.top, text = "edit", command = lambda i = index: self.edit_entry(i))

            delete_button = tk.Button(
                self.top, text = "delete", command = lambda i = index: self.delete_entry(i))
            text.window_create(tk.END, window = edit_button)
            text.window_create(tk.END, window = delete_button)
            text.insert(tk.END, "\n\n")

    def edit_entry(self, index):
        
        global df
        self.edit_top = tk.Toplevel(self.root)
        self.edit_top.title("Edit Entries")

        # edit date
        self.edit_date = tk.Entry(self.edit_top)
        self.edit_date.insert(0, df.at[index,'Date'])
        self.edit_date.pack()

        # edit description
        self.edit_description = tk.Entry(self.edit_top)
        self.edit_description.insert(0, df.at[index,'Description'])
        self.edit_description.pack()

        # edit amount
        self.edit_amount = tk.Entry(self.edit_top)
        self.edit_amount.insert(0, df.at[index,'Amount'])
        self.edit_amount.pack()

        # edit type 
        self.edit_type = tk.Entry(self.edit_top)
        self.edit_type.insert(0, df.at[index,'Type'])
        self.edit_type.pack()

        save_button = tk.Button(
            self.edit_top, text = "save", command = lambda i = index: self.save_edit(i))
        save_button.pack()

    def save_edit(self, index):
        global df
        df.at[index, 'Date'] = self.edit_date.get()
        df.at[index, 'Description'] = self.edit_description.get()
        df.at[index, 'Amount'] = self.edit_amount.get()
        df.at[index, 'Type'] = self.edit_type.get()
        df.to_csv('./records.csv', index = False)
        messagebox.showinfo("Sucess", "Record updated.")
        self.edit_top.destroy()
        self.top.destroy()
        self.view_entry()




    def delete_entry(self, index):
        global df

root = tk.Tk()
app = BudgetTrackerApp(root)
root.mainloop()