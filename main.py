from execute import *
from errors import *

import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("ATM Machine")
root.geometry("300x300")

def run_action(choice):
    if choice == 1:
        open_amount_window("Deposit", deposit)
    elif choice == 2:
        open_amount_window("Withdraw", withdraw)
    elif choice == 3:
        try:
            result = balanceenquiry(gui_mode=True)
            messagebox.showinfo("Balance", result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

def open_amount_window(action, function_ref):
    window = tk.Toplevel(root)
    window.title(action)
    tk.Label(window, text=f"Enter amount to {action.lower()}").pack(pady=5)
    amount_entry = tk.Entry(window)
    amount_entry.pack(pady=5)

    def submit():
        try:
            amt = int(amount_entry.get())
            function_ref(gui_amount=amt)
            messagebox.showinfo("Success", f"{action} ₹{amt} completed")
            window.destroy()
        except Minimumdeposit:
            messagebox.showerror("Error", "Minimum deposit is ₹100")
        except lowbalance:
            messagebox.showerror("Error", "Insufficient Funds")
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number")

    tk.Button(window, text=action, command=submit).pack(pady=10)

# GUI Buttons for ATM Menu
tk.Label(root, text="Welcome to SBI ATM", font=("Arial", 14)).pack(pady=10)
tk.Button(root, text="1. Deposit", width=20, command=lambda: run_action(1)).pack(pady=5)
tk.Button(root, text="2. Withdraw", width=20, command=lambda: run_action(2)).pack(pady=5)
tk.Button(root, text="3. Balance Enquiry", width=20, command=lambda: run_action(3)).pack(pady=5)
tk.Button(root, text="Exit", width=20, command=root.destroy).pack(pady=20)

root.mainloop()
