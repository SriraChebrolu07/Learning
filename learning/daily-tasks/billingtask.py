# import tkinter as tk
# from tkinter import messagebox

# class BillingSoftware:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Billing Software")
#         self.root.geometry("1000x700")
        
#         # Variables
#         self.customer_name = tk.StringVar()
#         self.customer_phone = tk.StringVar()
#         self.bill_number = tk.StringVar()
#         self.bill_number.set("9406")
        
#         self.sanitizer = tk.IntVar()
#         self.mask = tk.IntVar()
#         self.hand_gloves = tk.IntVar()
#         self.syrup = tk.IntVar()
#         self.cream = tk.IntVar()
#         self.thermal_gun = tk.IntVar()
        
#         self.rice = tk.IntVar()
#         self.food_oil = tk.IntVar()
#         self.wheat = tk.IntVar()
#         self.spices = tk.IntVar()
#         self.flour = tk.IntVar()
#         self.maggi = tk.IntVar()
        
#         self.sprite = tk.IntVar()
#         self.mineral_water = tk.IntVar()
#         self.juice = tk.IntVar()
#         self.coke = tk.IntVar()
#         self.lassi = tk.IntVar()
#         self.mountain_duo = tk.IntVar()
        
#         self.total_medical_price = tk.StringVar()
#         self.total_grocery_price = tk.StringVar()
#         self.total_cold_drinks_price = tk.StringVar()
        
#         self.medical_tax = tk.StringVar()
#         self.grocery_tax = tk.StringVar()
#         self.cold_drinks_tax = tk.StringVar()
        
#         # Customer Details Frame
#         customer_frame = tk.LabelFrame(self.root, text="Customer Details", font=("times new roman", 12, "bold"), bd=12, relief=tk.GROOVE)
#         customer_frame.place(x=0, y=0, relwidth=1)
        
#         tk.Label(customer_frame, text="Customer Name", font=("times new roman", 12, "bold")).grid(row=0, column=0, padx=20, pady=5)
#         tk.Entry(customer_frame, width=20, textvariable=self.customer_name, font="arial 12").grid(row=0, column=1, padx=10, pady=5)
        
#         tk.Label(customer_frame, text="Customer Phone", font=("times new roman", 12, "bold")).grid(row=0, column=2, padx=20, pady=5)
#         tk.Entry(customer_frame, width=20, textvariable=self.customer_phone, font="arial 12").grid(row=0, column=3, padx=10, pady=5)
        
#         tk.Label(customer_frame, text="Bill Number", font=("times new roman", 12, "bold")).grid(row=0, column=4, padx=20, pady=5)
#         tk.Entry(customer_frame, width=20, textvariable=self.bill_number, font="arial 12").grid(row=0, column=5, padx=10, pady=5)
        
#         # Medical Purpose Frame
#         medical_frame = tk.LabelFrame(self.root, text="Medical Purpose", font=("times new roman", 12, "bold"), bd=12, relief=tk.GROOVE)
#         medical_frame.place(x=0, y=120, width=325, height=380)
        
#         tk.Label(medical_frame, text="Sanitizer", font=("times new roman", 12, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="w")
#         tk.Entry(medical_frame, width=10, textvariable=self.sanitizer, font=("times new roman", 12, "bold")).grid(row=0, column=1, padx=10, pady=10)
        
#         tk.Label(medical_frame, text="Mask", font=("times new roman", 12, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
#         tk.Entry(medical_frame, width=10, textvariable=self.mask, font=("times new roman", 12, "bold")).grid(row=1, column=1, padx=10, pady=10)
        
#         tk.Label(medical_frame, text="Hand Gloves", font=("times new roman", 12, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky="w")
#         tk.Entry(medical_frame, width=10, textvariable=self.hand_gloves, font=("times new roman", 12, "bold")).grid(row=2, column=1, padx=10, pady=10)
        
#         tk.Label(medical_frame, text="Syrup", font=("times new roman", 12, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky="w")
#         tk.Entry(medical_frame, width=10, textvariable=self.syrup, font=("times new roman", 12, "bold")).grid(row=3, column=1, padx=10, pady=10)
        
#         tk.Label(medical_frame, text="Cream", font=("times new roman", 12, "bold")).grid(row=4, column=0, padx=10, pady=10, sticky="w")
#         tk.Entry(medical_frame, width=10, textvariable=self.cream, font=("times new roman", 12, "bold")).grid(row=4, column=1, padx=10, pady=10)
        
#         tk.Label(medical_frame, text="Thermal Gun", font=("times new roman", 12, "bold")).grid(row=5, column=0, padx=10, pady=10, sticky="w")
#         tk.Entry(medical_frame, width=10, textvariable=self.thermal_gun, font=("times new roman", 12, "bold")).grid(row=5, column=1, padx=10, pady=10)
        
#         # Grocery Items Frame
#         grocery_frame = tk.LabelFrame(self.root, text="Grocery Items", font=("times new roman", 12, "bold"), bd=12, relief=tk.GROOVE)
#         grocery_frame.place(x=325, y=120, width=325, height=380)
        
#         tk.Label(grocery_frame, text="Rice", font=("times new roman", 12, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="w")
#         tk.Entry(grocery_frame, width=10, textvariable=self.rice, font=("times new roman", 12, "bold")).grid(row=0, column=1, padx=10, pady=10)
        
#         tk.Label(grocery_frame, text="Food Oil", font=("times new roman", 12, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
#         tk.Entry(grocery_frame, width=10, textvariable=self.food_oil, font=("times new roman", 12, "bold")).grid(row=1, column=1, padx=10, pady=10)
        
#         tk.Label(grocery_frame, text="Wheat", font=("times new roman", 12, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky="w")
#         tk.Entry(grocery_frame, width=10, textvariable=self.wheat, font=("times new roman", 12, "bold")).grid(row=2, column=1, padx=10, pady=10)
        
#         tk.Label(grocery_frame, text="Spices", font=("times new roman", 12, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky="w")
#         tk.Entry(grocery_frame, width=10, textvariable=self.spices, font=("times new roman", 12, "bold")).grid(row=3, column=1, padx=10, pady=10)
        
#         tk.Label(grocery_frame, text="Flour", font=("times new roman", 12, "bold")).grid(row=4, column=0, padx=10, pady=10, sticky="w")
#         tk.Entry(grocery_frame, width=10, textvariable=self.flour, font=("times new roman", 12, "bold")).grid(row=4, column=1, padx=10, pady=10)
        
#         tk.Label(grocery_frame, text="Maggi", font=("times new roman", 12, "bold")).grid(row=5, column=0, padx=10, pady=10, sticky="w")
#         tk.Entry(grocery_frame, width=10, textvariable=self.maggi, font=("times new roman", 12, "bold")).grid(row=5, column=1, padx=10, pady=10)
        
#         # Cold Drinks Frame
#         drinks_frame = tk.LabelFrame(self.root, text="Cold Drinks", font=("times new roman", 12, "bold"), bd=12, relief=tk.GROOVE)
#         drinks_frame.place(x=650, y=120, width=325, height=380)
        
#         tk.Label(drinks_frame, text="Sprite", font=("times new roman", 12, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="w")
#         tk.Entry(drinks_frame, width=10, textvariable=self.sprite, font=("times new roman", 12, "bold")).grid(row=0, column=1, padx=10, pady=10)
        
#         tk.Label(drinks_frame, text="Mineral Water", font=("times new roman", 12, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
#         tk.Entry(drinks_frame, width=10, textvariable=self.mineral_water, font=("times new roman", 12, "bold")).grid(row=1, column=1, padx=10, pady=10)
        
#         tk.Label(drinks_frame, text="Juice", font=("times new roman", 12, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky="w")
#         tk.Entry(drinks_frame, width=10, textvariable=self.juice, font=("times new roman", 12, "bold")).grid(row=2, column=1, padx=10, pady=10)
        
#         tk.Label(drinks_frame, text="Coke", font=("times new roman", 12, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky="w")
#         tk.Entry(drinks_frame, width=10, textvariable=self.coke, font=("times new roman", 12, "bold")).grid(row=3, column=1, padx=10, pady=10)
        
#         tk.Label(drinks_frame, text="Lassi", font=("times new roman", 12, "bold")).grid(row=4, column=0, padx=10, pady=10, sticky="w")
#         tk.Entry(drinks_frame, width=10, textvariable=self.lassi, font=("times new roman", 12, "bold")).grid(row=4, column=1, padx=10, pady=10)
        
#         tk.Label(drinks_frame, text="Mountain Duo", font=("times new roman", 12, "bold")).grid(row=5, column=0, padx=10, pady=10, sticky="w")
#         tk.Entry(drinks_frame, width=10, textvariable=self.mountain_duo, font=("times new roman", 12, "bold")).grid(row=5, column=1, padx=10, pady=10)
        
#         # Bill Area
#         bill_frame = tk.Frame(self.root, bd=10, relief=tk.GROOVE)
#         bill_frame.place(x=0, y=500, relwidth=1, height=190)
        
#         tk.Label(bill_frame, text="Bill Area", font=("times new roman", 15, "bold")).pack(fill=tk.X)
#         scroll_y = tk.Scrollbar(bill_frame, orient=tk.VERTICAL)
#         self.textarea = tk.Text(bill_frame, yscrollcommand=scroll_y.set)
#         scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
#         scroll_y.config(command=self.textarea.yview)
#         self.textarea.pack(fill=tk.BOTH, expand=1)
        
#         # Button Frame
#         button_frame = tk.Frame(self.root, bd=10, relief=tk.GROOVE)
#         button_frame.place(x=0, y=700, relwidth=1, height=100)
        
#         tk.Button(button_frame, text="Total", font=("times new roman", 15, "bold"), command=self.total).grid(row=0, column=0, padx=20, pady=10)
#         tk.Button(button_frame, text="Generate Bill", font=("times new roman", 15, "bold"), command=self.generate_bill).grid(row=0, column=1, padx=20, pady=10)
#         tk.Button(button_frame, text="Clear", font=("times new roman", 15, "bold"), command=self.clear).grid(row=0, column=2, padx=20, pady=10)
#         tk.Button(button_frame, text="Exit", font=("times new roman", 15, "bold"), command=self.exit).grid(row=0, column=3, padx=20, pady=10)
        
#     def total(self):
#         self.total_medical_price.set(str((self.sanitizer.get()*50) + (self.mask.get()*20) + (self.hand_gloves.get()*150) +
#                                          (self.syrup.get()*80) + (self.cream.get()*120) + (self.thermal_gun.get()*750)))
        
#         self.total_grocery_price.set(str((self.rice.get()*40) + (self.food_oil.get()*110) + (self.wheat.get()*50) +
#                                          (self.spices.get()*30) + (self.flour.get()*25) + (self.maggi.get()*10)))
        
#         self.total_cold_drinks_price.set(str((self.sprite.get()*20) + (self.mineral_water.get()*15) + (self.juice.get()*25) +
#                                              (self.coke.get()*20) + (self.lassi.get()*25) + (self.mountain_duo.get()*20)))
        
#         self.medical_tax.set(str(round((float(self.total_medical_price.get()) * 0.05), 2)))
#         self.grocery_tax.set(str(round((float(self.total_grocery_price.get()) * 0.1), 2)))
#         self.cold_drinks_tax.set(str(round((float(self.total_cold_drinks_price.get()) * 0.05), 2)))
        
#     def generate_bill(self):
#         self.textarea.delete("1.0", tk.END)
#         self.textarea.insert(tk.END, "\tWelcome to Our Shop\n")
#         self.textarea.insert(tk.END, f"\nBill Number: {self.bill_number.get()}")
#         self.textarea.insert(tk.END, f"\nCustomer Name: {self.customer_name.get()}")
#         self.textarea.insert(tk.END, f"\nPhone Number: {self.customer_phone.get()}")
#         self.textarea.insert(tk.END, "\n======================================")
#         self.textarea.insert(tk.END, "\nProducts\t\tQTY\t\tPrice")
#         self.textarea.insert(tk.END, "\n======================================")
        
#         if self.sanitizer.get() != 0:
#             self.textarea.insert(tk.END, f"\nSanitizer\t\t{self.sanitizer.get()}\t\t{self.sanitizer.get()*50}")
#         if self.mask.get() != 0:
#             self.textarea.insert(tk.END, f"\nMask\t\t{self.mask.get()}\t\t{self.mask.get()*20}")
#         if self.hand_gloves.get() != 0:
#             self.textarea.insert(tk.END, f"\nHand Gloves\t\t{self.hand_gloves.get()}\t\t{self.hand_gloves.get()*150}")
#         if self.syrup.get() != 0:
#             self.textarea.insert(tk.END, f"\nSyrup\t\t{self.syrup.get()}\t\t{self.syrup.get()*80}")
#         if self.cream.get() != 0:
#             self.textarea.insert(tk.END, f"\nCream\t\t{self.cream.get()}\t\t{self.cream.get()*120}")
#         if self.thermal_gun.get() != 0:
#             self.textarea.insert(tk.END, f"\nThermal Gun\t\t{self.thermal_gun.get()}\t\t{self.thermal_gun.get()*750}")
            
#         if self.rice.get() != 0:
#             self.textarea.insert(tk.END, f"\nRice\t\t{self.rice.get()}\t\t{self.rice.get()*40}")
#         if self.food_oil.get() != 0:
#             self.textarea.insert(tk.END, f"\nFood Oil\t\t{self.food_oil.get()}\t\t{self.food_oil.get()*110}")
#         if self.wheat.get() != 0:
#             self.textarea.insert(tk.END, f"\nWheat\t\t{self.wheat.get()}\t\t{self.wheat.get()*50}")
#         if self.spices.get() != 0:
#             self.textarea.insert(tk.END, f"\nSpices\t\t{self.spices.get()}\t\t{self.spices.get()*30}")
#         if self.flour.get() != 0:
#             self.textarea.insert(tk.END, f"\nFlour\t\t{self.flour.get()}\t\t{self.flour.get()*25}")
#         if self.maggi.get() != 0:
#             self.textarea.insert(tk.END, f"\nMaggi\t\t{self.maggi.get()}\t\t{self.maggi.get()*10}")
            
#         if self.sprite.get() != 0:
#             self.textarea.insert(tk.END, f"\nSprite\t\t{self.sprite.get()}\t\t{self.sprite.get()*20}")
#         if self.mineral_water.get() != 0:
#             self.textarea.insert(tk.END, f"\nMineral Water\t\t{self.mineral_water.get()}\t\t{self.mineral_water.get()*15}")
#         if self.juice.get() != 0:
#             self.textarea.insert(tk.END, f"\nJuice\t\t{self.juice.get()}\t\t{self.juice.get()*25}")
#         if self.coke.get() != 0:
#             self.textarea.insert(tk.END, f"\nCoke\t\t{self.coke.get()}\t\t{self.coke.get()*20}")
#         if self.lassi.get() != 0:
#             self.textarea.insert(tk.END, f"\nLassi\t\t{self.lassi.get()}\t\t{self.lassi.get()*25}")
#         if self.mountain_duo.get() != 0:
#             self.textarea.insert(tk.END, f"\nMountain Duo\t\t{self.mountain_duo.get()}\t\t{self.mountain_duo.get()*20}")
        
#         self.textarea.insert(tk.END, "\n--------------------------------------")
#         self.textarea.insert(tk.END, f"\nTotal Medical Price: \t\t\t{self.total_medical_price.get()}")
#         self.textarea.insert(tk.END, f"\nTotal Grocery Price: \t\t\t{self.total_grocery_price.get()}")
#         self.textarea.insert(tk.END, f"\nTotal Cold Drinks Price: \t\t\t{self.total_cold_drinks_price.get()}")
#         self.textarea.insert(tk.END, "\n--------------------------------------")
#         self.textarea.insert(tk.END, f"\nMedical Tax: \t\t\t{self.medical_tax.get()}")
#         self.textarea.insert(tk.END, f"\nGrocery Tax: \t\t\t{self.grocery_tax.get()}")
#         self.textarea.insert(tk.END, f"\nCold Drinks Tax: \t\t\t{self.cold_drinks_tax.get()}")
#         self.textarea.insert(tk.END, "\n--------------------------------------")
#         self.textarea.insert(tk.END, f"\nTotal Amount: \t\t\t{float(self.total_medical_price.get()) + float(self.total_grocery_price.get()) + float(self.total_cold_drinks_price.get()) + float(self.medical_tax.get()) + float(self.grocery_tax.get()) + float(self.cold_drinks_tax.get())}")
#         self.textarea.insert(tk.END, "\n--------------------------------------")
        
#     def clear(self):
#         self.customer_name.set("")
#         self.customer_phone.set("")
#         self.bill_number.set("")
#         self.sanitizer.set(0)
#         self.mask.set(0)
#         self.hand_gloves.set(0)
#         self.syrup.set(0)
#         self.cream.set(0)
#         self.thermal_gun.set(0)
#         self.rice.set(0)
#         self.food_oil.set(0)
#         self.wheat.set(0)
#         self.spices.set(0)
#         self.flour.set(0)
#         self.maggi.set(0)
#         self.sprite.set(0)
#         self.mineral_water.set(0)
#         self.juice.set(0)
#         self.coke.set(0)
#         self.lassi.set(0)
#         self.mountain_duo.set(0)
#         self.total_medical_price.set("")
#         self.total_grocery_price.set("")
#         self.total_cold_drinks_price.set("")
#         self.medical_tax.set("")
#         self.grocery_tax.set("")
#         self.cold_drinks_tax.set("")
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

        self.lays = tk.IntVar()
        self.pepsi = tk.IntVar()
        self.sandwich = tk.IntVar()

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

        tk.Label(items_frame, text="Lays", font=("times new roman", 12, "bold")).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(items_frame, textvariable=self.lays, font=("times new roman", 12)).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(items_frame, text="Pepsi", font=("times new roman", 12, "bold")).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(items_frame, textvariable=self.pepsi, font=("times new roman", 12)).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(items_frame, text="Sandwich", font=("times new roman", 12, "bold")).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(items_frame, textvariable=self.sandwich, font=("times new roman", 12)).grid(row=2, column=1, padx=10, pady=5)

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
            f"Lays\t\t{self.lays.get()}\t\t{self.lays.get() * 20}\n"
            f"Pepsi\t\t{self.pepsi.get()}\t\t{self.pepsi.get() * 30}\n"
            f"Sandwich\t\t{self.sandwich.get()}\t\t{self.sandwich.get() * 50}\n"
        )

        total_price = self.lays.get() * 20 + self.pepsi.get() * 30 + self.sandwich.get() * 50
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
        self.lays.set(0)
        self.pepsi.set(0)
        self.sandwich.set(0)
        self.textarea.delete('1.0', tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = BillingSoftware(root)
    root.mainloop()
