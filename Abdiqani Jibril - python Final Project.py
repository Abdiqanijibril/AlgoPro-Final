import random
import tkinter as tk
from tkinter import messagebox

'''The code below makes a class for all the 

'''

class Bills:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600+300+150")
        self.root.title("Bill Management System")
        bg_color = "#ff7f50"

        #============Title label===============
        title = tk.Label(self.root, text="Bill Management System", font=('times new roman', 20, 'bold'), pady=2, bd=10, bg=bg_color, fg="white", relief=tk.GROOVE)
        title.pack(fill=tk.X)

        # ================ Groceries =======================
        self.noodles = tk.IntVar()
        self.rice = tk.IntVar()
        self.vegetables = tk.IntVar()
        self.fruits = tk.IntVar()
        self.foodoil = tk.IntVar()

        # ============== Cold Drinks =======================
        self.sprite = tk.IntVar()
        self.monster = tk.IntVar()
        self.sevenup = tk.IntVar()
        self.coke = tk.IntVar()
        self.fanta = tk.IntVar()

        # ============== Dairy =======================
        self.milk = tk.IntVar()
        self.cheese = tk.IntVar()
        self.yogurt = tk.IntVar()
        self.eggs = tk.IntVar()
        self.butter = tk.IntVar()

        # ============== Customer Details =======================
        self.customer_name = tk.StringVar()
        self.customer_phone = tk.StringVar()

        # ============== Total Price =======================
        self.drink_price = tk.StringVar()
        self.grocery_price = tk.StringVar()
        self.dairy_price = tk.StringVar()

        #===============Customer Inputs Frame===============
        F1 = tk.LabelFrame(self.root, text="Customer Inputs", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#ff7f50")
        F1.place(x=0, y=50, relwidth=1.0)

        customername_lbl = tk.Label(F1, text="Customer Name:", bg="#ff7f50", font=('times new roman', 15, 'bold'))
        customername_lbl.grid(row=0, column=0, padx=50, pady=5)
        customername_txt = tk.Entry(F1, width=30, textvariable=self.customer_name, font='arial 15', bd=7, relief=tk.GROOVE)
        customername_txt.grid(row=0, column=1, pady=5, padx=10)

        customerphone_lbl = tk.Label(F1, text="Customer Phone:", bg="#ff7f50", font=('times new roman', 15, 'bold'))
        customerphone_lbl.grid(row=0, column=2, padx=50, pady=5)
        customerphone_txt = tk.Entry(F1, width=30, textvariable=self.customer_phone, font='arial 15', bd=7, relief=tk.GROOVE)
        customerphone_txt.grid(row=0, column=3, pady=5, padx=10)
        # =============grociery Items=======================
        F2 = tk.LabelFrame(self.root, text="Groceries", bd=10, fg="White", bg="#ff7f50",)
        F2.place(x=0, y=130, width=325, height=320)
        noodles_lbl = tk.Label(F2, text="Noodles", font=('times new roman', 16, 'bold'), bg="#ff7f50", fg="black")
        noodles_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        noodles_txt = tk.Entry(F2, width=10, textvariable=self.noodles, font=('times new roman', 16, 'bold'), bd=5, relief=tk.GROOVE)
        noodles_txt.grid(row=0, column=1, padx=10, pady=10)

        rice_lbl = tk.Label(F2, text="Rice", font=('times new roman', 16, 'bold'), bg="#ff7f50", fg="black")
        rice_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        rice_txt = tk.Entry(F2, width=10, textvariable=self.rice, font=('times new roman', 16, 'bold'), bd=5, relief=tk.GROOVE)
        rice_txt.grid(row=2, column=1, padx=10, pady=10)

        vegatables_lbl = tk.Label(F2, text="Vegatables", font=('times new roman', 16, 'bold'), bg="#ff7f50", fg="black")
        vegatables_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        vegatables_txt = tk.Entry(F2, width=10, textvariable=self.vegetables, font=('times new roman', 16, 'bold'), bd=5, relief=tk.GROOVE)
        vegatables_txt.grid(row=3, column=1, padx=10, pady=10)

        fruits_lbl = tk.Label(F2, text="Fruits", font=('times new roman', 16, 'bold'), bg="#ff7f50", fg="black")
        fruits_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        fruits_txt = tk.Entry(F2, width=10, textvariable=self.fruits, font=('times new roman', 16, 'bold'), bd=5, relief=tk.GROOVE)
        fruits_txt.grid(row=4, column=1, padx=10, pady=10)

        foodoil_lbl = tk.Label(F2, text="Foodoil", font=('times new roman', 16, 'bold'), bg="#ff7f50", fg="black")
        foodoil_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        foodoil_txt = tk.Entry(F2, width=10, textvariable=self.foodoil, font=('times new roman', 16, 'bold'), bd=5, relief=tk.GROOVE)
        foodoil_txt.grid(row=5, column=1, padx=10, pady=10)

        #=============cold drink Items=======================
        F3 = tk.LabelFrame(self.root, text="Cold Drinks", bd=10, fg="white", bg="#ff7f50")
        F3.place(x=315, y=130, width=325, height=320)
        sprite_lbl = tk.Label(F3, text="Sprite", font=('times new roman', 16, 'bold'), bg="#ff7f50", fg="black")
        sprite_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        sprite_txt = tk.Entry(F3, width=10, textvariable=self.sprite, font=('times new roman', 16, 'bold'), bd=5, relief=tk.GROOVE)
        sprite_txt.grid(row=1, column=1, padx=10, pady=10)

        monster_lbl = tk.Label(F3, text="Monster", font=('times new roman', 16, 'bold'), bg="#ff7f50", fg="black")
        monster_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        monster_txt = tk.Entry(F3, width=10, textvariable=self.monster, font=('times new roman', 16, 'bold'), bd=5, relief=tk.GROOVE)
        monster_txt.grid(row=2, column=1, padx=10, pady=10)

        sevenup_lbl = tk.Label(F3, text="7up", font=('times new roman', 16, 'bold'), bg="#ff7f50", fg="black")
        sevenup_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        sevenup_txt = tk.Entry(F3, width=10, textvariable=self.sevenup, font=('times new roman', 16, 'bold'), bd=5, relief=tk.GROOVE)
        sevenup_txt.grid(row=3, column=1, padx=10, pady=10)

        coke_lbl = tk.Label(F3, text="Coke", font=('times new roman', 16, 'bold'), bg="#ff7f50", fg="black")
        coke_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        coke_txt = tk.Entry(F3, width=10, textvariable=self.coke, font=('times new roman', 16, 'bold'), bd=5, relief=tk.GROOVE)
        coke_txt.grid(row=4, column=1, padx=10, pady=10)

        fanta_lbl = tk.Label(F3, text="Fanta", font=('times new roman', 16, 'bold'), bg="#ff7f50", fg="black")
        fanta_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        fanta_txt = tk.Entry(F3, width=10, textvariable=self.fanta, font=('times new roman', 16, 'bold'), bd=5, relief=tk.GROOVE)
        fanta_txt.grid(row=5, column=1, padx=10, pady=10)

        #=================Dairy Items========================
        F4 = tk.LabelFrame(self.root, text="Dairy", bd=10, fg="white", bg="#ff7f50")
        F4.place(x=640, y=130, width=350, height=320)
        milk_lbl = tk.Label(F4, text="Milk", font=('times new roman', 16, 'bold'), bg="#ff7f50", fg="black")
        milk_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        milk_text = tk.Entry(F4, width=10, textvariable=self.milk, font=('times new roman', 16, 'bold'), bd=5, relief=tk.GROOVE)
        milk_text.grid(row=1, column=1, padx=10, pady=10)

        cheese_lbl = tk.Label(F4, text="Cheese", font=('times new roman', 16, 'bold'), bg="#ff7f50", fg="black")
        cheese_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        cheese_text = tk.Entry(F4, width=10, textvariable=self.cheese, font=('times new roman', 16, 'bold'), bd=5, relief=tk.GROOVE)
        cheese_text.grid(row=2, column=1, padx=10, pady=10)

        yogurt_lbl = tk.Label(F4, text="Yogurt", font=('times new roman', 16, 'bold'), bg="#ff7f50", fg="black")
        yogurt_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        yogurt_text = tk.Entry(F4, width=10, textvariable=self.yogurt, font=('times new roman', 16, 'bold'), bd=5, relief=tk.GROOVE)
        yogurt_text.grid(row=3, column=1, padx=10, pady=10)

        eggs_lbl = tk.Label(F4, text="Eggs", font=('times new roman', 16, 'bold'), bg="#ff7f50", fg="black")
        eggs_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        eggs_text = tk.Entry(F4, width=10, textvariable=self.eggs, font=('times new roman', 16, 'bold'), bd=5, relief=tk.GROOVE)
        eggs_text.grid(row=4, column=1, padx=10, pady=10)

        butter_lbl = tk.Label(F4, text="Butter", font=('times new roman', 16, 'bold'), bg="#ff7f50", fg="black")
        butter_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        butter_text = tk.Entry(F4, width=10, textvariable=self.butter, font=('times new roman', 16, 'bold'), bd=5, relief=tk.GROOVE)
        butter_text.grid(row=5, column=1, padx=10, pady=1)
#==============prices display============

        F5 = tk.LabelFrame(self.root, text="Prices of items", bd=10, fg="white", bg="#ff7f50")
        F5.place(x=0, y=440, width=1280, height=150)
        prices = """groceries price: noodles = 18,000, rice = 70,000, vegetables = 10,0000 + fruits = 50,000, foodoil = 150,000
        cold drinks price: sprite = 10,000, monster = 70,000, sevenup = 120,000, coke = 10,000, fanta = 10,000
        dairy price: milk = 60,000, cheese = 150,000, yogurt = 50,000, eggs = 70,000, butter = 100,000"""
        label = tk.Label (F5, text=prices, font = ('Times new roman', 15, 'bold'), fg="white", bg="#ff7f50", justify=tk.CENTER)
        label.pack(fill=tk.BOTH, expand=True)
        



#==============Add more fields for groceries, cold drinks, and dairy here as needed=======

        #========Billing Area Frame (for displaying the bill)=======
        self.billing_area = tk.LabelFrame(self.root, text="Billing Area", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#ff7f50")
        self.billing_area.place(x=955, y=130, relwidth=1.0, width=320, height=320)

        self.bill_display = tk.Label(self.billing_area, text="", font=("arial", 12), bd=5, relief=tk.GROOVE, justify="left", anchor="nw")
        self.bill_display.pack(fill=tk.BOTH, padx=10, pady=10)

        #=========Generate Bill Button=========
        generate_bill_button = tk.Button(self.root, text="Generate Bill", font=('times new roman', 15, 'bold'), fg="white", bg="#ff7f50", bd=7, command=self.generate_bill)
        generate_bill_button.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=10)

    def generate_bill(self):
        #========Random Bill Number======
        bill_number = random.randint(1000, 9999)
        bill_text = f"Bill Number: {bill_number}\n"
        bill_text += f"Customer Name: {self.customer_name.get()}\n"
        bill_text += f"Customer Phone: {self.customer_phone.get()}\n"
        bill_text += "-"*40 + "\n"

        #========= items (Groceries, Cold Drinks, Dairy) and their prices=========
        groceries_price = self.noodles.get() * 18000 + self.rice.get() * 70000 + self.vegetables.get() * 100000 + self.fruits.get() * 50000 + self.foodoil.get() * 150000
        cold_drinks_price = self.sprite.get() * 10000 + self.monster.get() * 70000 + self.sevenup.get() * 120000 + self.coke.get() * 10000 + self.fanta.get() * 10000
        dairy_price = self.milk.get() * 60000 + self.cheese.get() * 150000 + self.yogurt.get() * 50000 + self.eggs.get() * 70000 + self.butter.get() * 100000

        total_price = groceries_price + cold_drinks_price + dairy_price

        #==========Adding details to the bill=========
        bill_text += f"Groceries Total: IDR{groceries_price}\n"
        bill_text += f"Cold Drinks Total: IDR{cold_drinks_price}\n"
        bill_text += f"Dairy Total: IDR{dairy_price}\n"
        bill_text += f"Total Price: IDR{total_price}\n"

        #=======Displaying the bill in the Billing area======
        self.bill_display.config(text=bill_text)

# Create the root window
root = tk.Tk()
app = Bills(root)
root.mainloop()
