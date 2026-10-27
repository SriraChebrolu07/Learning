# import tkinter as tk
# from tkinter import messagebox
# import random

# class BillingSoftware:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("500x400")
#         self.root.title("Billing Software")

#         # Variables
#         self.customer_name = tk.StringVar()
#         self.customer_phone = tk.StringVar()
#         self.bill_number = tk.StringVar(value=str(random.randint(1000, 9999)))

#         self.item_vars = {
#             "Sanitizer": tk.IntVar(),
#             "Mask": tk.IntVar()
#         }

#         self.total_price = tk.StringVar()
#         self.tax = tk.StringVar()
#         self.total_amount = tk.StringVar()

#         # Customer Details Frame
#         customer_frame = tk.LabelFrame(self.root, text="Customer Details", font=("times new roman", 12, "bold"))
#         customer_frame.pack(fill=tk.X, padx=10, pady=5)

#         tk.Label(customer_frame, text="Customer Name", font=("times new roman", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
#         tk.Entry(customer_frame, textvariable=self.customer_name, font=("times new roman", 12)).grid(row=0, column=1, padx=10, pady=5)

#         tk.Label(customer_frame, text="Phone Number", font=("times new roman", 12, "bold")).grid(row=0, column=2, padx=10, pady=5)
#         tk.Entry(customer_frame, textvariable=self.customer_phone, font=("times new roman", 12)).grid(row=0, column=3, padx=10, pady=5)

#         tk.Label(customer_frame, text="Bill Number", font=("times new roman", 12, "bold")).grid(row=0, column=4, padx=10, pady=5)
#         tk.Entry(customer_frame, textvariable=self.bill_number, font=("times new roman", 12), state='readonly').grid(row=0, column=5, padx=10, pady=5)

#         # Items Frame
#         items_frame = tk.LabelFrame(self.root, text="Items", font=("times new roman", 12, "bold"))
#         items_frame.pack(fill=tk.X, padx=10, pady=5)

#         for idx, (item, var) in enumerate(self.item_vars.items()):
#             tk.Label(items_frame, text=item, font=("times new roman", 12, "bold")).grid(row=idx, column=0, padx=10, pady=5, sticky="w")
#             tk.Entry(items_frame, textvariable=var, font=("times new roman", 12)).grid(row=idx, column=1, padx=10, pady=5)

#         # Bill Area
#         bill_frame = tk.Frame(self.root, bd=10, relief=tk.GROOVE)
#         bill_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

#         tk.Label(bill_frame, text="Bill Area", font=("times new roman", 15, "bold")).pack(fill=tk.X)
#         scroll_y = tk.Scrollbar(bill_frame, orient=tk.VERTICAL)
#         self.textarea = tk.Text(bill_frame, yscrollcommand=scroll_y.set)
#         scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
#         scroll_y.config(command=self.textarea.yview)
#         self.textarea.pack(fill=tk.BOTH, expand=True)

#         # Button Frame
#         button_frame = tk.Frame(self.root, bd=10, relief=tk.GROOVE)
#         button_frame.pack(fill=tk.X, padx=10, pady=5)

#         tk.Button(button_frame, text="Total", font=("times new roman", 15, "bold"), command=self.calculate_total).grid(row=0, column=0, padx=20, pady=10)
#         tk.Button(button_frame, text="Generate Bill", font=("times new roman", 15, "bold"), command=self.generate_bill).grid(row=0, column=1, padx=20, pady=10)
#         tk.Button(button_frame, text="Clear", font=("times new roman", 15, "bold"), command=self.clear).grid(row=0, column=2, padx=20, pady=10)
#         tk.Button(button_frame, text="Exit", font=("times new roman", 15, "bold"), command=self.exit).grid(row=0, column=3, padx=20, pady=10)

#     def calculate_total(self):
#         total = sum(var.get() * price for var, price in zip(self.item_vars.values(), [50, 20]))
#         tax = round(total * 0.05, 2)
#         self.total_price.set(f"{total:.2f}")
#         self.tax.set(f"{tax:.2f}")
#         self.total_amount.set(f"{total + tax:.2f}")

#     def generate_bill(self):
#         self.calculate_total()
#         self.textarea.delete("1.0", tk.END)
#         self.textarea.insert(tk.END, "\tWelcome to Our Shop\n")
#         self.textarea.insert(tk.END, f"\nBill Number: {self.bill_number.get()}")
#         self.textarea.insert(tk.END, f"\nCustomer Name: {self.customer_name.get()}")
#         self.textarea.insert(tk.END, f"\nPhone Number: {self.customer_phone.get()}")
#         self.textarea.insert(tk.END, "\n======================================")
#         self.textarea.insert(tk.END, "\nProducts\t\tQTY\t\tPrice")
#         self.textarea.insert(tk.END, "\n======================================")

#         for item, var in self.item_vars.items():
#             if var.get() != 0:
#                 price = var.get() * [50, 20][list(self.item_vars.keys()).index(item)]
#                 self.textarea.insert(tk.END, f"\n{item}\t\t{var.get()}\t\t{price}")

#         self.textarea.insert(tk.END, "\n--------------------------------------")
#         self.textarea.insert(tk.END, f"\nTotal Price: \t\t\t{self.total_price.get()}")
#         self.textarea.insert(tk.END, f"\nTax: \t\t\t{self.tax.get()}")
#         self.textarea.insert(tk.END, f"\nTotal Amount: \t\t\t{self.total_amount.get()}")
#         self.textarea.insert(tk.END, "\n--------------------------------------")

#     def clear(self):
#         self.customer_name.set("")
#         self.customer_phone.set("")
#         self.bill_number.set(str(random.randint(1000, 9999)))

#         for var in self.item_vars.values():
#             var.set(0)

#         self.total_price.set("")
#         self.tax.set("")
#         self.total_amount.set("")
#         self.textarea.delete("1.0", tk.END)

#     def exit(self):
#         self.root.destroy()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = BillingSoftware(root)
#     root.mainloop()



import tkinter as tk
from tkinter import messagebox
import random

class BillingSoftware:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x400")
        self.root.title("Billing Software")

        # Variables
        self.customer_name = tk.StringVar()
        self.customer_phone = tk.StringVar()
        self.bill_number = tk.StringVar(value=str(random.randint(1000, 9999)))

        self.sanitizer = tk.IntVar()
        self.mask = tk.IntVar()

        self.total_price = tk.StringVar()
        self.tax = tk.StringVar()
        self.total_amount = tk.StringVar()

        # Customer Details Frame
        customer_frame = tk.LabelFrame(self.root, text="Customer Details", font=("times new roman", 12, "bold"))
        customer_frame.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(customer_frame, text="Customer Name", font=("times new roman", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(customer_frame, textvariable=self.customer_name, font=("times new roman", 12)).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(customer_frame, text="Phone Number", font=("times new roman", 12, "bold")).grid(row=0, column=2, padx=10, pady=5)
        tk.Entry(customer_frame, textvariable=self.customer_phone, font=("times new roman", 12)).grid(row=0, column=3, padx=10, pady=5)

        tk.Label(customer_frame, text="Bill Number", font=("times new roman", 12, "bold")).grid(row=0, column=4, padx=10, pady=5)
        tk.Entry(customer_frame, textvariable=self.bill_number, font=("times new roman", 12), state='readonly').grid(row=0, column=5, padx=10, pady=5)

        # Items Frame
        items_frame = tk.LabelFrame(self.root, text="Items", font=("times new roman", 12, "bold"))
        items_frame.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(items_frame, text="Sanitizer", font=("times new roman", 12, "bold")).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(items_frame, textvariable=self.sanitizer, font=("times new roman", 12)).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(items_frame, text="Mask", font=("times new roman", 12, "bold")).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(items_frame, textvariable=self.mask, font=("times new roman", 12)).grid(row=1, column=1, padx=10, pady=5)

        # Bill Area
        bill_frame = tk.Frame(self.root, bd=10, relief=tk.GROOVE)
        bill_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        tk.Label(bill_frame, text="Bill Area", font=("times new roman", 15, "bold")).pack(fill=tk.X)
        scroll_y = tk.Scrollbar(bill_frame, orient=tk.VERTICAL)
        self.textarea = tk.Text(bill_frame, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=tk.BOTH, expand=True)

        # Button Frame
        button_frame = tk.Frame(self.root, bd=10, relief=tk.GROOVE)
        button_frame.pack(fill=tk.X, padx=10, pady=5)

        tk.Button(button_frame, text="Generate Bill", command=self.generate_bill, bg="cadetblue", fg="white", pady=15, font=("times new roman", 15, "bold")).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(button_frame, text="Clear", command=self.clear, bg="cadetblue", fg="white", pady=15, font=("times new roman", 15, "bold")).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(button_frame, text="Exit", command=self.root.quit, bg="cadetblue", fg="white", pady=15, font=("times new roman", 15, "bold")).pack(side=tk.LEFT, padx=5, pady=5)

    def generate_bill(self):
        self.textarea.delete('1.0', tk.END)
        bill_content = (
            f"Bill Number: {self.bill_number.get()}\n"
            f"Customer Name: {self.customer_name.get()}\n"
            f"Phone Number: {self.customer_phone.get()}\n\n"
            f"Products\t\tQty\t\tPrice\n"
            f"Sanitizer\t\t{self.sanitizer.get()}\t\t{self.sanitizer.get() * 50}\n"
            f"Mask\t\t{self.mask.get()}\t\t{self.mask.get() * 10}\n"
        )

        total_price = self.sanitizer.get() * 50 + self.mask.get() * 10
        tax = round(total_price * 0.05, 2)
        total_amount = total_price + tax

        bill_content += (
            f"\nTotal Price: Rs. {total_price}\n"
            f"Tax: Rs. {tax}\n"
            f"Total Amount: Rs. {total_amount}\n"
        )

        self.textarea.insert(tk.END, bill_content)

    def clear(self):
        self.customer_name.set("")
        self.customer_phone.set("")
        self.bill_number.set(str(random.randint(1000, 9999)))
        self.sanitizer.set(0)
        self.mask.set(0)
        self.textarea.delete('1.0', tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = BillingSoftware(root)
    root.mainloop()

