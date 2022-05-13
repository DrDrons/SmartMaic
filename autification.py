import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pypyodbc
import hashlib

connection = pypyodbc.connect('Driver={SQL Server};'
                                'SERVER=DESKTOP-S152C1O\SQLEXPRESS;' 
                                'Database=bd_smart_maic_two;')
cursor = connection.cursor()

window = Tk()
window.title('Авторизация')
window.geometry('450x230')
window['bg'] = "#3c4757"
window.resizable(False, False)

window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}


a = 0
def close_app():
    global a
    Query_l = f"SELECT adm_log FROM dbo.adm_lp"
    cursor.execute(Query_l)
    login = cursor.fetchone()
    Query_p = f"SELECT adm_pas FROM dbo.adm_lp"
    cursor.execute(Query_p)
    password = cursor.fetchone()

    l = username_entry.get()
    hash_l_obj = hashlib.md5(l.encode())
    p = password_entry.get()
    hash_p_obj = hashlib.md5(p.encode())

    if hash_l_obj.hexdigest() == login[0] and hash_p_obj.hexdigest() == password[0]:
        a += 1
        window.destroy()
    else:
        messagebox.showwarning('Ошибка!', 'Неверный логин или пароль!')


main_label = tk.Label(window, text='Авторизация', font=font_header, justify=CENTER, **header_padding, background="#3c4757", foreground="white")

main_label.pack()
password = ''

username_label = tk.Label(window, text='Имя пользователя', font=label_font, **base_padding, background="#3c4757", foreground="white")
username_label.pack()

username_entry = tk.Entry(window, bg='#fff', fg='#444', font=font_entry, background="#4a576b", foreground="white")
username_entry.pack()

password_label = tk.Label(window, text='Пароль', font=label_font , **base_padding, background="#3c4757", foreground="white")
password_label.pack()

password_entry = tk.Entry(window, bg='#fff', fg='#444', show='*', font=font_entry, background="#4a576b", foreground="white")
password_entry.pack()

send_btn = tk.Button(window, text='Войти', command=close_app, background='#546278', fg='white', relief='ridge')
send_btn.pack(**base_padding)

window.mainloop()
