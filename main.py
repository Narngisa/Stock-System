import os
import json
import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# โหลดสต็อก
def load_json():
    global recipes, stock, dessert

    recipes_path = "./json/recipes.json"
    stock_path = "./json/stock.json"
    dessert_path = "./json/dessert.json"

    try:
        os.makedirs('./json', exist_ok=True)

        if os.path.exists(recipes_path):
            with open(recipes_path, "r", encoding="utf-8") as f:
                recipes = json.load(f)

        if os.path.exists(stock_path):
            with open(stock_path, "r", encoding="utf-8") as f:
                stock = json.load(f)

        if os.path.exists(dessert_path):
            with open(dessert_path, "r", encoding="utf-8") as f:
                dessert = json.load(f)

    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการโหลดข้อมูล: {e}")

    print("โหลดข้อมูลสำเร็จ 📦")

# เพิ่มจำนวนวัตถุดิบ
def add_ingredient(name, amount):
    if name in stock:
        stock[name] += amount
        print(f"เพิ่ม {name} จำนวน {amount} หน่วย")
    else:
        stock[name] = amount
        print(f"เพิ่ม {name} จำนวน {amount} หน่วย ลงในสต็อก")

# ลบวัตถุดิบ
def remove_ingredient(name):
    if name in stock:
        amount = stock[name]
        del stock[name]
        print(f"ลบ {name} ออกจากสต็อกแล้ว จำนวน {amount} หน่วย")
    else:
        print(f"ไม่มีชื่อวัตถุดิบ {name} ในสต็อก")

# ลดจำนวนวัตถุดิบ
def reduce_ingredient(name, amount):
    if name in stock:
        if stock[name] >= amount:
            stock[name] -= amount
            print(f"ลด {name} จำนวน {amount} หน่วย จาก {stock[name] + amount} เหลือ {stock[name]} หน่วย")
        else:
            print(f"ไม่สามารถลดจำนวน {name} ได้ เนื่องจากมีในสต็อกไม่เพียงพอ")
    else:
        print(f"ไม่มีชื่อวัตถุดิบ {name} ในสต็อก")

# ทำขนมหวาน
def make_item(item_name, quantity):
    if item_name not in recipes:
        print("ไม่มีสูตรสำหรับเมนูนี้")
        return

    required = recipes[item_name]
    for ing, amount in required.items():
        total_required = amount * quantity
        if stock.get(ing, 0) < total_required:
            print(f"วัตถุดิบ {ing} ไม่พอ (ต้องการ {total_required} มี {stock.get(ing, 0)})")
            return

    for ing, amount in required.items():
        stock[ing] -= amount * quantity
    send_item(f"ผลิต {item_name} จำนวน {quantity} ชุดเรียบร้อย", item_name, quantity)

# สรุปสต็อก
def summarize_stock():
    liquid_items = ["น้ำ", "วิปครีม", "นมสด", "น้ำมะนาว", "ครีมสด"]
    fruit_items = ["แอปเปิ้ลเขียว", "แอปเปิ้ลแดง", "สตรอว์เบอร์รี่", "ส้ม"]
    leaf_item = ["ผักกาดแก้ว"]
    summary = []

    print("📦 สรุปยอดวัตถุดิบในคลัง:")
    print("-" * 40)
    for item, amount in stock.items():
        if item in liquid_items:
            print(f"{item} {amount} ml")
            line = f"{item} {amount} ml"
        elif item == "ไข่ไก่":
            print(f"{item} {amount} ฟอง")
            line = f"{item} {amount} ฟอง"
        elif item in fruit_items:
            print(f"{item} {amount} ลูก")
            line = f"{item} {amount} ลูก"
        elif item == "น้ำแข็ง":
            print(f"{item} {amount} ก้อน")
            line = f"{item} {amount} ก้อน"
        elif item in leaf_item:
            print(f"{item} {amount} ใบ")
            line = f"{item} {amount} ใบ"
        else:
            print(f"{item} {amount} g")
            line = f"{item} {amount} g"
        summary.append(line)
    print("-" * 40)

    with open("./out/output.txt", "w", encoding="utf-8") as f:
        for line in summary:
            f.write(line + "\n")

def add_dessert(name, amount):
    if name in dessert:
        dessert[name] += amount
        print(f"เพิ่ม {name} จำนวน {amount} หน่วย")
    else:
        dessert[name] = amount
        print(f"เพิ่ม {name} จำนวน {amount} หน่วย ลงในตู้เย็น")


def reduce_dessert(name, amount):
    if name in dessert:
        if dessert[name] >= amount:
            dessert[name] -= amount
            print(f"ลด {name} จำนวน {amount} หน่วย จาก {dessert[name] + amount} เหลือ {dessert[name]} หน่วย")
        else:
            print(f"ไม่สามารถลดจำนวน {name} ได้ เนื่องจากมีในสต็อกไม่เพียงพอ")
    else:
        print(f"ไม่มีชื่อวัตถุดิบ {name} ในสต็อก")

def send_dessert(name, amount):

    all_items = ["Cheesecake", "Brownie", "Apple Pie", "Pancake", "Ice Cream(Vanilla)", "Ice Cream(Chocolate)", "Milk", "Water", "Cocoa Milk", "Orange Juice", "Orange Smoothie", "Apple Juice", "Apple Smoothie", "Lime Juice", "Lime Smoothie", "Strawberry Juice", "Strawberry Smoothie", "Milk", "Water", "Cocoa Milk", "Orange Juice", "Orange Smoothie", "Apple Juice", "Apple Smoothie", "Lime Juice", "Lime Smoothie", "Strawberry Juice", "Strawberry Smoothie", "Chocolate Mousse", "Grass Jelly", "Bingsu(Strawberry)", "Bingsu(Orange)", "Bingsu(Apple)", "Bingsu(Chocolate)", "Shaved Ice(Strawberry)", "Shaved Ice(Orange)", "Shaved Ice(Apple)", "Shaved Ice(Chocolate)", "Panna Cotta(Strawberry)", "Panna Cotta(Orange)", "Panna Cotta(Apple)", "Soy Milk", "Oat Milk", "Green Tea", "Macaron(Chocolate)", "Macaron(Vanilla)", "Sandwich"]

    if name in dessert:
        if name in all_items:
            if name == "Cheesecake" or name == "Apple Pie":
                amount = 8 * amount
            elif name == "Brownie":
                amount = 16 * amount
            elif name == "Pancake" or name == "Milk" or name ==  "Water" or name == "Cocoa Milk" or name == "Orange Juice" or name == "Orange Smoothie" or name == "Apple Juice" or name == "Apple Smoothie" or name == "Lime Juice" or name == "Lime Smoothie" or name == "Strawberry Juice" or name == "Strawberry Smoothie" or name == "Chocolate Mousse" or name == "Green Tea":
                amount = 1 * amount
            elif name == "Ice Cream(Vanilla)" or name == "Ice Cream(Chocolate)":
                amount = 16 * amount
            elif name == "Grass Jelly" or name == "Bingsu(Strawberry)" or name == "Bingsu(Orange)" or name == "Bingsu(Apple)" or name == "Bingsu(Chocolate)" or name == "Shaved Ice(Strawberry)" or name == "Shaved Ice(Orange)" or name == "Shaved Ice(Apple)" or name == "Shaved Ice(Chocolate)" or name == "Panna Cotta(Strawberry)" or name == "Panna Cotta(Orange)" or name == "Panna Cotta(Apple)":
                amount = 4 * amount
            elif name == "Soy Milk" or name == "Oat Milk" or name == "Sandwich":
                amount = 7 * amount
            elif name == "Macaron(Chocolate)" or name == "Macaron(Vanilla)":
                amount = 20 * amount
        dessert[name] += amount

        print(f"เพิ่ม {name} จำนวน {amount} หน่วย ลงในตู้เย็น")
    else:
        dessert[name] = amount
        print(f"เพิ่ม {name} จำนวน {amount} หน่วย ลงในตู้เย็น")

# ฟังก์ชัน send_item ที่จะบันทึกข้อมูลลงใน JSON
def send_item(message, name, amount):

    send_dessert(name, amount)

    # บันทึกข้อมูลกลับไปยังไฟล์ JSON
    try:
        with open("./json/dessert.json", "w", encoding="utf-8") as f:
            json.dump(dessert, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการบันทึกข้อมูล: {e}")

    # สร้างข้อความสำหรับ log
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}"

    print(log_message)

def save_stock():
    try:
        with open("./json/stock.json", "w", encoding="utf-8") as f:
            json.dump(stock, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการบันทึกข้อมูล: {e}")
        messagebox.showerror("ผิดพลาด", "ไม่สามารถบันทึกข้อมูลสต็อกได้")

def save_dessert():
    try:
        with open("./json/dessert.json", "w", encoding="utf-8") as f:
            json.dump(dessert, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการบันทึกข้อมูล: {e}")
        messagebox.showerror("ผิดพลาด", "ไม่สามารถบันทึกข้อมูลตู้เย็นได้")

# โหลดข้อมูลสต็อก
load_json()

# หน้าต่างสต็อก
root = Tk()
root.title("Felix - ระบบจัดการวัตถุดิบ")

# เปลี่ยนไอคอนเป็น .png หรือ .jpg
icon = PhotoImage(file="./icon/cake.ico")
root.iconphoto(True, icon)

# ขนาดหน้าจอ
root.geometry("1000x600")

# ส่วนหัว GUI
title = Label(root, text="📦 Felix Stock System", font=("TH Sarabun New", 24, "bold"))
title.pack(pady=10)

# ใช้ Notebook สำหรับหลายหน้า
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# หน้าที่ 1 (สรุปสต็อก)
frame1 = Frame(notebook)
notebook.add(frame1, text="📦 สต็อก")

# แสดงสรุปวัตถุดิบ
def show_summary():
    summary_window.delete(1.0, END)  # ล้างข้อมูลเดิม
    liquid_items = ["น้ำ", "วิปครีม", "นมสด", "น้ำมะนาว", "ครีมสด", "มายองเนส", "ซอสมะเขือเทศ"]
    fruit_items = ["แอปเปิ้ลเขียว", "แอปเปิ้ลแดง", "สตรอว์เบอร์รี่", "ส้ม", "มะเขือเทศ", "แตงกวา", "หอมใหญ่"]
    leaf_item = ["ผักกาดแก้ว"]
    for item, amount in stock.items():
        if item in liquid_items:
            line = f"{item} {amount} ml"
        elif item == "ไข่ไก่":
            line = f"{item} {amount} ฟอง"
        elif item in fruit_items:
            line = f"{item} {amount} ลูก"
        elif item == "น้ำแข็ง":
            line = f"{item} {amount} ก้อน"
        elif item in leaf_item:
            line = f"{item} {amount} ใบ"
        else:
            line = f"{item} {amount} g"

        # กำหนดสีตามจำนวนวัตถุดิบ
        if amount < 500:
            color = "red"
        elif amount < 2000:
            color = "yellow"
        else:
            color = "green"
        summary_window.insert(END, line + "\n", color)

    # กำหนดสีข้อความใน Text widget
    summary_window.tag_config("red", foreground="red")
    summary_window.tag_config("yellow", foreground="orange")
    summary_window.tag_config("green", foreground="green")

# กรอบแสดงข้อมูล
summary_window = Text(frame1, width=60, height=15, font=("TH Sarabun New", 14))
summary_window.pack(pady=0)

# ส่วนที่ต้องการให้ปุ่มอยู่ข้างๆ กัน
frame_buttons = Frame(frame1)  # สร้าง Frame ใหม่เพื่อใส่ปุ่ม
frame_buttons.pack(pady=5)

# ปุ่มสรุป
btn_summary = Button(frame_buttons, text="📋 สรุปยอดวัตถุดิบ", command=lambda: [summarize_stock(), show_summary()])
btn_summary.pack(side=LEFT, padx=5)  # ปรับให้ปุ่มอยู่ข้างๆ กัน

# ปุ่มโหลดสต็อก
btn_load = Button(frame_buttons, text="🔄 โหลดสต็อก", command=lambda: [load_json(), show_summary()])
btn_load.pack(side=LEFT, padx=5)  # ปรับให้ปุ่มอยู่ข้างๆ กัน

# ส่วนเพิ่มวัตถุดิบ
frame_system = Frame(frame1)
frame_system.pack(pady=5)

ingredient_list = list(stock.keys())
ingredient_combobox = ttk.Combobox(frame_system, values=ingredient_list, font=("TH Sarabun New", 14), width=25)
ingredient_combobox.grid(row=0, column=0, padx=5)
entry_amount = Entry(frame_system, font=("TH Sarabun New", 14), width=10)
entry_amount.grid(row=0, column=1, padx=5)

# ฟังก์ชันเพิ่มวัตถุดิบ
def add_to_stock():
    name = ingredient_combobox.get()
    
    # ตรวจสอบชื่อวัตถุดิบในสต็อก
    if name == "":
        messagebox.showerror("ผิดพลาด", f"กรุณาใส่ {name} ในสต็อก")
        return  # ไม่ดำเนินการต่อหากชื่อวัตถุดิบไม่พบ
    
    try:
        amount = float(entry_amount.get())
        add_ingredient(name, amount)
        messagebox.showinfo("สำเร็จ", f"เพิ่ม {name} จำนวน {amount} หน่วยแล้ว")
        show_summary()
        save_dessert()
    except ValueError:
        messagebox.showerror("ผิดพลาด", "กรุณาใส่จำนวนเป็นตัวเลข")

# ลดจำนวนวัตถุดิบ
def decrease_ingredient():
    name = ingredient_combobox.get()
    try:
        amount = float(entry_amount.get())
        if amount <= 0:
            raise ValueError("จำนวนต้องเป็นค่าบวก")
        reduce_ingredient(name, amount)
        messagebox.showinfo("สำเร็จ", f"ลด {name} จำนวน {amount} หน่วยแล้ว")
        show_summary()
        save_stock()
    except ValueError:
        messagebox.showerror("ผิดพลาด", "กรุณาใส่จำนวนเป็นตัวเลขที่มากกว่า 0")

# ลบวัตถุดิบ
def delete_ingredient():
    name = ingredient_combobox.get()
    if name in stock:
        amount = stock[name]
        remove_ingredient(name)
        messagebox.showinfo("สำเร็จ", f"ลบ {name} ออกจากสต็อกแล้ว จำนวน {amount} หน่วย")
        show_summary()
        save_stock()
    else:
        messagebox.showerror("ผิดพลาด", f"ไม่มีชื่อวัตถุดิบ {name} ในสต็อก")

# ปุ่มเพิ่ม, ลบ, ลดจำนวนวัตถุดิบ
Button(frame_system, text="➕ เพิ่ม", command=add_to_stock).grid(row=0, column=2, padx=5)
Button(frame_system, text="🗑️ ลบ", command=delete_ingredient).grid(row=0, column=3, padx=5)
Button(frame_system, text="➖ ลดจำนวน", command=decrease_ingredient).grid(row=0, column=4, padx=5)

# สร้างกรอบเลือกเมนูและจำนวน
frame_make_item = Frame(frame1)
frame_make_item.pack(pady=10)

# Combobox สำหรับเลือกเมนู
menu_list = list(recipes.keys())
menu_combobox = ttk.Combobox(frame_make_item, values=menu_list, font=("TH Sarabun New", 14), width=25)
menu_combobox.grid(row=0, column=0, padx=5)

entry_quantity = Entry(frame_make_item, font=("TH Sarabun New", 14), width=10)
entry_quantity.grid(row=0, column=1, padx=5)

# ฟังก์ชันทำขนม
def make_dessert():
    item_name = menu_combobox.get()
    try:
        quantity = int(entry_quantity.get())
        
        # ตรวจสอบเมนู
        if item_name not in recipes:
            messagebox.showerror("ผิดพลาด", f"ไม่มีสูตรสำหรับเมนู {item_name}")
            return

        required = recipes[item_name]
        for ing, amount in required.items():
            total_required = amount * quantity
            if stock.get(ing, 0) < total_required:
                messagebox.showerror("ผิดพลาด", f"วัตถุดิบ {ing} ไม่พอ (ต้องการ {total_required} มี {stock.get(ing, 0)})")
                return
        
        make_item(item_name, quantity)
        messagebox.showinfo("สำเร็จ", f"ผลิต {item_name} จำนวน {quantity} ชุดแล้ว")
        show_summary()
        save_stock()
    except ValueError:
        messagebox.showerror("ผิดพลาด", "กรุณาใส่จำนวนเป็นตัวเลข")

Button(frame_make_item, text="🍰 ทำขนม", command=lambda: [make_dessert(), show_refrigerator()]).grid(row=0, column=3, padx=5)

# หน้าที่ 2 (เพิ่มวัตถุดิบหลายรายการ)
frame2 = Frame(notebook)
notebook.add(frame2, text="➕ เพิ่มวัตถุดิบ")

# กรอบช่องรายการทั้งหมด
frame_bulk_add = Frame(frame2)
frame_bulk_add.pack(pady=10)

# เก็บช่องที่สร้าง
bulk_entries = []

# ฟังก์ชันลบแถววัตถุดิบ
def remove_entry(row_frame, entry_tuple):
    row_frame.destroy()
    if entry_tuple in bulk_entries:
        bulk_entries.remove(entry_tuple)

# ฟังก์ชันเพิ่มช่องกรอกวัตถุดิบใหม่
def add_bulk_entry():
    row = Frame(frame_bulk_add)
    row.pack(pady=5)

    ing_combobox = ttk.Combobox(row, values=list(stock.keys()), font=("TH Sarabun New", 14), width=25)
    ing_combobox.pack(side=LEFT, padx=5)

    amount_entry = Entry(row, font=("TH Sarabun New", 14), width=10)
    amount_entry.pack(side=LEFT, padx=5)

    entry_tuple = (ing_combobox, amount_entry)

    btn_delete = Button(row, text="🗑️ ลบ", command=lambda: remove_entry(row, entry_tuple))
    btn_delete.pack(side=LEFT, padx=5)

    bulk_entries.append(entry_tuple)

# ปุ่มเพิ่มช่องรายการใหม่
btn_create_input = Button(frame2, text="➕ เพิ่มช่องรายการ", command=add_bulk_entry)
btn_create_input.pack(padx=10)

# ปุ่มเพิ่มวัตถุดิบทั้งหมด
def add_multiple_ingredients():
    success = []
    for combobox, entry in bulk_entries:
        name = combobox.get()
        try:
            amount = float(entry.get())
            if name:
                add_ingredient(name, amount)
                success.append(f"{name} จำนวน {amount} หน่วยแล้ว")
        except ValueError:
            continue

    if success:
        messagebox.showinfo("สำเร็จ", f"เพิ่มวัตถุดิบ:\n" + "\n".join(success))
        show_summary()
        save_stock()
    else:
        messagebox.showerror("ผิดพลาด", "กรุณาใส่ข้อมูลให้ถูกต้อง")

btn_add_multiple = Button(frame2, text="✅ เพิ่มวัตถุดิบทั้งหมด", command=add_multiple_ingredients)
btn_add_multiple.pack(padx=10)

frame3 = Frame(notebook)
notebook.add(frame3, text="➕ ตู้เย็น")

def show_refrigerator():
    refrigerator_window.delete(1.0, END)  # ล้างข้อมูลเดิม
    slice_items = ["Cheesecake", "Brownie", "Apple Pie", "Pancake", "Macaron(Chocolate)", "Macaron(Vanilla)", "Sandwich"]
    scoop_items = ["Ice Cream(Vanilla)", "Ice Cream(Chocolate)"]
    glass_items = ["Water", "Milk", "Soy Milk", "Oat Milk", "Cocoa Milk", "Green Tea", "Orange Juice", "Orange Smoothie", "Apple Juice", "Apple Smoothie", "Lime Juice", "Lime Smoothie", "Strawberry Juice", "Strawberry Smoothie"]
    cup_items = ["Chocolate Mousse", "Grass Jelly", "Bingsu(Strawberry)", "Bingsu(Orange)", "Bingsu(Apple)", "Bingsu(Chocolate)", "Shaved Ice(Strawberry)", "Shaved Ice(Orange)", "Shaved Ice(Apple)", "Shaved Ice(Chocolate)", "Panna Cotta(Strawberry)", "Panna Cotta(Orange)", "Panna Cotta(Apple)"]
    bottle_item = ["Blood"]

    for item, amount in dessert.items():
        if item in slice_items:
            line = f"{item} {amount} ชิ้น"
        elif item in scoop_items:
            line = f"{item} {amount} สกู๊ป"
        elif item in glass_items:
            line = f"{item} {amount} แก้ว"
        elif item in cup_items:
            line = f"{item} {amount} ถ้วย"
        elif item in bottle_item:
            line = f"{item} {amount} ขวด"
        else:
            line = f"{item} ไม่สามารถจัดหมวดหมู่ได้ !!"
        refrigerator_window.insert(END, line + "\n")

# กรอบแสดงข้อมูล
refrigerator_window = Text(frame3, width=60, height=15, font=("TH Sarabun New", 14))
refrigerator_window.pack(pady=0)

# ส่วนที่ต้องการให้ปุ่มอยู่ข้างๆ กัน
frame_refrigerator = Frame(frame3)  # สร้าง Frame ใหม่เพื่อใส่ปุ่ม
frame_refrigerator.pack(pady=5)

# ปุ่มโหลดสต็อก
btn_load_ref = Button(frame_refrigerator, text="🔄 โหลดสต็อก", command=lambda: [load_json(), show_refrigerator()])
btn_load_ref.pack(side=LEFT, padx=5)  # ปรับให้ปุ่มอยู่ข้างๆ กัน

# ส่วนเพิ่มวัตถุดิบ
frame_ref = Frame(frame3)
frame_ref.pack(pady=5)

ref_list = list(dessert.keys())
ref_combobox = ttk.Combobox(frame_ref, values=ref_list, font=("TH Sarabun New", 14), width=25)
ref_combobox.grid(row=0, column=0, padx=5)
ref_amount = Entry(frame_ref, font=("TH Sarabun New", 14), width=10)
ref_amount.grid(row=0, column=1, padx=5)

# ฟังก์ชันเพิ่มวัตถุดิบ
def add_to_dessert():
    name = ref_combobox.get()
    
    # ตรวจสอบชื่อวัตถุดิบในสต็อก
    if name == "":
        messagebox.showerror("ผิดพลาด", f"กรุณาใส่ {name} ในสต็อก")
        return  # ไม่ดำเนินการต่อหากชื่อวัตถุดิบไม่พบ
    
    try:
        amount = float(ref_amount.get())
        add_dessert(name, amount)
        messagebox.showinfo("สำเร็จ", f"เพิ่ม {name} จำนวน {amount} หน่วยแล้ว")
        show_refrigerator()
        save_dessert()
    except ValueError:
        messagebox.showerror("ผิดพลาด", "กรุณาใส่จำนวนเป็นตัวเลข")

# ลดจำนวนวัตถุดิบ
def serve_dessert():
    name = ref_combobox.get()
    try:
        amount = float(ref_amount.get())
        if amount <= 0:
            raise ValueError("จำนวนต้องเป็นค่าบวก")
        reduce_dessert(name, amount)
        messagebox.showinfo("สำเร็จ", f"ลด {name} จำนวน {amount} หน่วยแล้ว")
        show_refrigerator()
        save_dessert()
    except ValueError:
        messagebox.showerror("ผิดพลาด", "กรุณาใส่จำนวนเป็นตัวเลขที่มากกว่า 0")

# ปุ่มเพิ่ม, ลบ, ลดจำนวนวัตถุดิบ
Button(frame_ref, text="➕ เพิ่ม", command=add_to_dessert).grid(row=0, column=2, padx=5)
Button(frame_ref, text="➖ เสริฟ", command=serve_dessert).grid(row=0, column=3, padx=5)

# ออกจากโปรแกรม
def on_exit():
    load_json()
    save_stock()
    save_dessert()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_exit)

# เริ่มโปรแกรม
show_summary()
show_refrigerator()
root.mainloop()
