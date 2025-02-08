import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import datetime

try:
    df = pd.read_csv('./records.csv')
except Exception as e:
    data = {
        "Date":[],
        "Amount":[],
        "Description":[],
        "Type":[],
    }

    df = pd.DataFrame(data)

def main():
    app = Application("Budget App")
    app.mainloop()

class Application(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)

        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        main_frame = MainFrame(self)
        main_frame.grid(row=0, column=0)
        

class MainFrame(tk.Frame):

        def __init__(self, parent):
            super().__init__(parent)
            
            # labels and entries
            self.label_date = tk.Label(self, text = "Date (YYYY-MM-DD)")
            self.label_date.grid(row = 0, column = 0)
            self.entry_date = tk.Entry(
                self, validatecommand = self.validate_date, validate = "focusout")
            self.entry_date.grid(row = 0, column = 1)
            # for displaying errors
            self.label_date_display = tk.Label(self, text = " ")
            self.label_date_display.grid(row = 0, column = 2)

            self.label_description = tk.Label(self, text = "Description")
            self.label_description.grid(row = 1, column = 0)
            self.entry_description = tk.Entry(
                self, validatecommand = self.validate_description, validate = "focusout")
            self.entry_description.grid(row = 1, column = 1)

            # for displaying errors
            self.label_description_display = tk.Label(self, text = "")
            self.label_description_display.grid(row = 1, column = 2)
            
            self.label_amount = tk.Label(self, text = "Amount")
            self.label_amount.grid(row = 2, column = 0)
            self.entry_amount = tk.Entry(
                self, validatecommand = self.validate_amount, validate = "focusout")
            self.entry_amount.grid(row = 2, column = 1)
            # for displaying errors
            self.label_amount_display = tk.Label(self, text = "")
            self.label_amount_display.grid(row = 2, column = 2)

            self.label_type = tk.Label(self, text = "Type")
            self.label_type.grid(row = 3, column = 0) 
            self.combo_type = ttk.Combobox(self, state = "readonly")
            self.combo_type.grid(row = 3, column = 1)
            self.combo_type['values'] = ('Credit',  'Debit')
            self.combo_type.current(0)

            # for displaying errors
            self.label_type_display = tk.Label(self, text = "")
            self.label_type_display.grid(row = 3, column = 2)
            
            # buttons
            self.button_add = tk.Button(self, text = 'Add Entry', command = self.add_entry)
            self.button_add.grid(row = 4, column = 0, columnspan = 2)
            self.button_view = tk.Button(self, text = 'View Entry', command = self.view_entry)
            self.button_view.grid(row = 5, column = 0, columnspan = 2)

        def validate_date(self):
            try:
                datetime.date.fromisoformat(self.entry_date.get())
                self.label_date_display.config(
                    text = "✓",
                    foreground = "green",
                )
                return(True)
            except ValueError:
                self.label_date_display.config(
                    text = "X",
                    foreground = "red",
                )
                return(False)

        def validate_amount(self):
                    
            try:
                float(self.entry_amount.get())
                self.label_amount_display.config(
                    text = "✓",
                    foreground = "green",
                )
                return(True)
            except ValueError:
                self.label_amount_display.config(
                    text = "X",
                    foreground = "red",
                )
                return(False)

        def validate_description(self):
                    
            if len(self.entry_description.get()) > 0:
                self.label_description_display.config(
                    text = "✓",
                    foreground = "green",
                )
                return(True)
            else:
                self.label_description_display.config(
                    text = "X",
                    foreground = "red",
                )
                return(False)

                
        def add_entry(self):
            global df
            
            if (self.validate_date() and self.validate_amount() and self.validate_description()):
                
                data = {
                    'Date': [self.entry_date.get()],
                    'Amount': [self.entry_amount.get()],
                    'Description': [self.entry_description.get()], 
                    'Type': [self.combo_type.get()]
                }

                row = pd.DataFrame(data)
                df = pd.concat([df, row], ignore_index = True)
                df.to_csv('./records.csv', index = False)
                messagebox.showinfo("Success", "record updated")
                self.entry_date.delete(0, tk.END)
                self.entry_amount.delete(0, tk.END)
                self.entry_description.delete(0, tk.END)
            else:
                messagebox.showinfo("Error", "invalid input")
           
        def view_entry(self):
            pass


        
main()

# todo 
#validated entry as class
# data in class