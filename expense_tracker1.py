from tkinter import *
from tkinter import messagebox

class Expense:
    def __init__(self, name, category, amount) -> None:
        self.name = name
        self.category = category
        self.amount = amount

    def __str__(self):
        return f'<Expense: {self.name}.{self.category}.${self.amount:.2f}>'

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title('Expense Tracker')
        self.root.geometry('800x500+200+100')  # Updated size
        self.root.config(bg='#f0f0f0')

        self.label = Label(self.root, text='Expense Tracker App', font=('Arial', 25, 'bold'), bg='#4CAF50', fg='white', width=50, bd=5, relief=RAISED)
        self.label.pack(side='top', pady=10)

        self.label2 = Label(self.root, text='Add Expense', font=('Arial', 18, 'bold'), bg='#f0f0f0')
        self.label2.place(x=40, y=60)

        self.label3 = Label(self.root, text='Expenses', font=('Arial', 18, 'bold'), bg='#f0f0f0')
        self.label3.place(x=420, y=60)

        self.main_text = Listbox(self.root, height=9, width=30, bd=5, font=("Arial", 14), bg='#FAFAFA')
        self.main_text.place(x=380, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font=('Arial', 12), bg='#FAFAFA')
        self.text.place(x=20, y=100)

        # Add expense function
        def add_expense():
            name = self.name_entry.get()
            category = self.category_entry.get()
            amount = float(self.amount_entry.get())
            expense = Expense(name, category, amount)
            self.main_text.insert(END, expense)
            with open('expenses.txt', 'a') as file:
                file.write(str(expense) + '\n')
                file.seek(0)
            self.name_entry.delete(0, END)
            self.category_entry.delete(0, END)
            self.amount_entry.delete(0, END)

        # Delete selected expense function
        def delete_expense():
            selected = self.main_text.curselection()
            if selected:
                self.main_text.delete(selected)

        # Clear all expenses function
        def clear_expenses():
            self.main_text.delete(0, END)

        # Save expenses to file function
        def save_expenses():
            with open('expenses.txt', 'w') as file:
                items = self.main_text.get(0, END)
                for item in items:
                    file.write(item)
            messagebox.showinfo("Save", "Expenses saved successfully!")

        with open('expenses.txt', 'r') as file:
            read = file.readlines()
            for i in read:
                self.main_text.insert(END, i)
            file.close()

        self.name_label = Label(self.root, text="Name:", font=('Arial', 12), bg='#f0f0f0')
        self.name_label.place(x=20, y=220)
        self.name_entry = Entry(self.root, bd=3, width=25, font=('Arial', 12))
        self.name_entry.place(x=80, y=220)

        self.category_label = Label(self.root, text="Category:", font=('Arial', 12), bg='#f0f0f0')
        self.category_label.place(x=20, y=260)
        self.category_entry = Entry(self.root, bd=3, width=25, font=('Arial', 12))
        self.category_entry.place(x=100, y=260)

        self.amount_label = Label(self.root, text="Amount:", font=('Arial', 12), bg='#f0f0f0')
        self.amount_label.place(x=20, y=300)
        self.amount_entry = Entry(self.root, bd=3, width=25, font=('Arial', 12))
        self.amount_entry.place(x=100, y=300)

        self.button = Button(self.root, text="Add Expense", font=('Arial', 12, 'bold'),
                     width=15, bg='#4CAF50', fg='white', command=add_expense)
        self.button.place(x=100, y=340)

        self.button2 = Button(self.root, text="Delete", font=('Arial', 12, 'bold'),
                      width=10, bg='#F44336', fg='white', command=delete_expense)
        self.button2.place(x=250, y=340)

        self.button3 = Button(self.root, text="Clear All", font=('Arial', 12, 'bold'),
                      width=10, bg='#FFC107', fg='black', command=clear_expenses)
        self.button3.place(x=400, y=340)

        self.button4 = Button(self.root, text="Save", font=('Arial', 12, 'bold'),
                      width=10, bg='#2196F3', fg='white', command=save_expenses)
        self.button4.place(x=550, y=340)

def main():
    root = Tk()
    expense_tracker = ExpenseTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
