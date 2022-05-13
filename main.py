from idlelib.tooltip import Hovertip
import requests
import datetime
import pypyodbc
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from autification import a
import keyboard
import hashlib


#SERVER=DESKTOP-S152C1O\SQLEXPRESS; Cервер Вова
#SERVER=DESKTOP-GLIOC6U\SQLEXPRESS; Сервер Лёша

connection = pypyodbc.connect('Driver={SQL Server};'
                                'SERVER=DESKTOP-GLIOC6U\SQLEXPRESS;' 
                                'Database=bd_smart_maic;')
cursor = connection.cursor()

def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Вы действительно хотите выйти из приложения?"):
        window.destroy()

window = Tk()
window.protocol("WM_DELETE_WINDOW", on_closing)
window.title("SmartMaic")
window.geometry('1500x800')
tab_control = ttk.Notebook(window)
window.resizable(False, False)



test = ttk.Style()
test.theme_create("my_tables",  parent="alt", settings={
        "TFrame":    {"configure": {"background": "#4a576b", "foreground": "white"}},
        "Treeview.Heading":    {"configure": {"background": "#3c4757", "foreground": "white"}},
        "Treeview":    {"configure": {"background": "#4a576b", "foreground": "white", "fieldbackground": "#5b6b82"}},
        "tab_control":    {"configure": {"background": "black"}},
        "TLabelframe":    {"configure": {"background": "#3c4757", "foreground": "white"}},
        "Label":    {"configure": {"background": "#3c4757", "foreground": "white"}},
        "TLabel":    {"configure": {"background": "#4a576b", "foreground": "white"}},
        "TNotebook": {"configure": {"background": "#4a576b"}},
        "TNotebook.Tab":    {"configure": {"padding": [80, 1], "background": "#3c4757", "foreground": "white"}}})
test.theme_use("my_tables")

style = ttk.Style()
style.map("Treeview", background=[('selected', '#5d8561')])

def spravka():
    f = open('Справка.txt', 'r', encoding="utf-8")
    rd = f.read()
    messagebox.showinfo('Добавление устройства', "" + str(rd) + "")

def teh_support():
    sup = open('support.txt', 'r', encoding="utf-8")
    rd_sup = sup.read()
    messagebox.showinfo('Техническая поддержка', "" + str(rd_sup) + "")

menu = Menu(window)

file_item = Menu(menu)
file_item.add_command(label='Добавление устройств', command=spravka)
file_item.add_command(label='Техническая поддержка', command=teh_support)

menu.add_cascade(label='Справка', menu=file_item)

window.config(menu=menu)

day_info_tab = ttk.Frame(tab_control)
tab_control.add(day_info_tab, text="Информация")
device_tab = ttk.Frame(tab_control)
tab_control.add(device_tab, text="SmartMaic")

tab_control.pack(expand=1, fill='both')

laibal_day = ttk.Frame(day_info_tab)
laibal_day.grid(column=0, row=0)

laibal_night = ttk.Frame(day_info_tab)
laibal_night.grid(column=0, row=1)


rows_device = ('info_smartmaic', 'ip_smartmaic', 'id_smartmaic', 'one_pulse_first_entrance', 'ed_izm_one', 'one_pulse_second_entranse', 'ed_izm_two')
device_table = ttk.Treeview(device_tab, show="headings")
device_table.grid(column=0, row=0, columnspan=3, padx=20, pady=20, sticky=tk.N)
device_table["columns"] = rows_device
device_table["displaycolumns"] = rows_device
for head in rows_device:
    device_table.column(head, anchor=CENTER, width=163)

device_table.heading(rows_device[0], text="Название")
device_table.heading(rows_device[1], text="IP-Устройства")
device_table.heading(rows_device[2], text="ID-Устройства")
device_table.heading(rows_device[3], text="Значение импульса(Ch1)")
device_table.heading(rows_device[4], text="Единица измерения")
device_table.heading(rows_device[5], text="Значение импульса(Ch2)")
device_table.heading(rows_device[6], text="Единица измерения")


rows_day_info = ('name', 'ch1', 'tch1', 'ed_izm_one', 'ch2', 'tch2', 'ed_izm_two', 'data', 'time', 'ip_smartmaic', 'id_smartmaic')
day_info_table = ttk.Treeview(laibal_day, show="headings")
day_info_table.pack(side=BOTTOM, padx=20, pady=(10, 10))
day_info_table["columns"] = rows_day_info
day_info_table["displaycolumns"] = rows_day_info
for head in rows_day_info:
    day_info_table.column(head, anchor=CENTER, width=130)

day_info_table.heading(rows_day_info[0], text="Название")
day_info_table.heading(rows_day_info[1], text="Импульсный вход 1")
day_info_table.heading(rows_day_info[2], text="За всё время(TCh1)")
day_info_table.heading(rows_day_info[3], text="Еденица измерения")
day_info_table.heading(rows_day_info[4], text="Импульсный вход 2")
day_info_table.heading(rows_day_info[5], text="За всё время(TCh2)")
day_info_table.heading(rows_day_info[6], text="Еденица измерения")
day_info_table.heading(rows_day_info[7], text="Дата")
day_info_table.heading(rows_day_info[8], text="Время")
day_info_table.heading(rows_day_info[9], text="IP-Устройства")
day_info_table.heading(rows_day_info[10], text="ID-Устройства")

laibol_neigth = ttk.Label(laibal_day, text='День')
laibol_neigth.pack(side=TOP, pady=10)

rows_night_info = ('name', 'ch1', 'tch1', 'ed_izm_one', 'ch2', 'tch2', 'ed_izm_two', 'data', 'time', 'ip_smartmaic', 'id_smartmaic')
night_info_table = ttk.Treeview(laibal_night, show="headings")
night_info_table.pack(side=BOTTOM, pady=(10, 10))
night_info_table["columns"] = rows_night_info
night_info_table["displaycolumns"] = rows_night_info
for head in rows_night_info:
    night_info_table.column(head, anchor=CENTER, width=130)

night_info_table.heading(rows_night_info[0], text="Название")
night_info_table.heading(rows_night_info[1], text="Импульсный вход 1")
night_info_table.heading(rows_night_info[2], text="За всё время(TCh1)")
night_info_table.heading(rows_night_info[3], text="Еденица измерения")
night_info_table.heading(rows_night_info[4], text="Импульсный вход 2")
night_info_table.heading(rows_night_info[5], text="За всё время(TCh2)")
night_info_table.heading(rows_night_info[6], text="Еденица измерения")
night_info_table.heading(rows_night_info[7], text="Дата")
night_info_table.heading(rows_night_info[8], text="Время")
night_info_table.heading(rows_night_info[9], text="IP-Устройства")
night_info_table.heading(rows_night_info[10], text="ID-Устройства")

laibol_daay = ttk.Label(laibal_night, text='Ночь')
laibol_daay.pack(side=TOP)

http = 'http://'
p = '/?page=getdata&devid='
Pass = '&devpass=12345'

def add_smartmaic():
    if entr_name_sm.get() == '' or entr_ip_sm.get() == '' or entr_id_sm.get() == '':
        messagebox.showwarning('Ошибка!', 'Введите все данные!')
    else:
        if (entr_one_pulse_first1.get() != '' and entr_ed_izm1.get() != '' and entr_one_pulse_first2.get() == '' and entr_ed_izm2.get() == '')\
                or (entr_one_pulse_first1.get() == '' and entr_ed_izm1.get() == '' and entr_one_pulse_first2.get() != '' and entr_ed_izm2.get() != '')\
                or (entr_one_pulse_first1.get() != '' and entr_ed_izm1.get() != '' and entr_one_pulse_first2.get() != '' and entr_ed_izm2.get() != ''):

            mySQLQuery1 = f"insert into dbo.device(info_smartmaic, ip_smartmaic, id_smartmaic, one_pulse_first_entrance, ed_izm_one, one_pulse_second_entranse, ed_izm_two) values (N'" + entr_name_sm.get() + "',N'" + entr_ip_sm.get() + "',N'" + entr_id_sm.get() + "',N'" + entr_one_pulse_first1.get() + "',N'" + entr_ed_izm1.get() + "',N'" + entr_one_pulse_first2.get() + "',N'" + entr_ed_izm2.get() + "')"
            cursor.execute(mySQLQuery1)
            connection.commit()
            update_table_sm()
            entr_name_sm.delete(0, 'end')
            entr_ip_sm.delete(0, 'end')
            entr_id_sm.delete(0, 'end')
            entr_one_pulse_first1.delete(0, 'end')
            entr_ed_izm1.delete(0, 'end')
            entr_one_pulse_first2.delete(0, 'end')
            entr_ed_izm2.delete(0, 'end')
        else:
            messagebox.showwarning('Ошибка!', 'Данные введены не корректно!')

def fast_add_smartmaic():
    if entr_name_sm.get() == '' and entr_ip_sm.get() == '' and entr_id_sm.get() == '':
        pass
    else:
        add_smartmaic()


def del_smartmaic():
    try:
        res = messagebox.askquestion('Внимание!', 'Вы действительно хотите удалить данные?')
        if res == 'yes':
            delete_sm = device_table.focus()
            order_smartmaic = device_table.item(delete_sm)['values'][1]
            mySQLQuery2 = f"DELETE FROM dbo.device WHERE ip_smartmaic='" + str(order_smartmaic) + "'"
            cursor.execute(mySQLQuery2)
            connection.commit()
            update_table_sm()
            messagebox.showinfo('Успешно!', 'Удаление прошло успешно!')
        elif res == 'no':
            messagebox.showinfo('Отмена!', 'Удаление отменено!')
    except IndexError:
        messagebox.showwarning('Ошибка', 'Выберете устройство которое нужно удалить!!!')

def insert_upgrade_data_memory():
    try:
        row_vibor_memory = device_table.focus()
        entr_name_sm.delete(0, 'end')
        entr_ip_sm.delete(0, 'end')
        entr_id_sm.delete(0, 'end')
        entr_one_pulse_first1.delete(0, 'end')
        entr_ed_izm1.delete(0, 'end')
        entr_one_pulse_first2.delete(0, 'end')
        entr_ed_izm2.delete(0, 'end')
        entr_name_sm.insert(0, str(device_table.item(row_vibor_memory)['values'][0]))
        entr_ip_sm.insert(0, str(device_table.item(row_vibor_memory)['values'][1]))
        entr_id_sm.insert(0, str(device_table.item(row_vibor_memory)['values'][2]))
        entr_one_pulse_first1.insert(0, str(device_table.item(row_vibor_memory)['values'][3]))
        entr_ed_izm1.insert(0, str(device_table.item(row_vibor_memory)['values'][4]))
        entr_one_pulse_first2.insert(0, str(device_table.item(row_vibor_memory)['values'][5]))
        entr_ed_izm2.insert(0, str(device_table.item(row_vibor_memory)['values'][6]))
        btn_add_sm['state'] = DISABLED
        btn_del_sm['state'] = DISABLED
        btn_upgrade_data['state'] = 'normal'
        query = f"SELECT id FROM dbo.device WHERE info_smartmaic='" + str(device_table.item(row_vibor_memory)['values'][0]) + "'"
        cursor.execute(query)
        id = cursor.fetchone()
        global identivity
        identivity = id[0]
    except IndexError:
        messagebox.showwarning('Ошибка!', 'Выберите строку для добавления!')
        btn_upgrade_data['state'] = 'disabled'


def upgrade_data_frame():
    try:
        device_table.delete(*device_table.get_children())
        SQLQuery0 = f"UPDATE dbo.device SET info_smartmaic='" + entr_name_sm.get() + "', ip_smartmaic='" + entr_ip_sm.get() + "', id_smartmaic='" + entr_id_sm.get() + "', one_pulse_first_entrance='" + entr_one_pulse_first1.get() + "', ed_izm_one='" + entr_ed_izm1.get() + "', one_pulse_second_entranse='" + entr_one_pulse_first2.get() + "', ed_izm_two='" + entr_ed_izm2.get() + "' WHERE id='" + str(identivity) + "'"
        cursor.execute(SQLQuery0)
        connection.commit()
        update_table_sm()
        entr_name_sm.delete(0, 'end')
        entr_ip_sm.delete(0, 'end')
        entr_id_sm.delete(0, 'end')
        entr_one_pulse_first1.delete(0, 'end')
        entr_ed_izm1.delete(0, 'end')
        entr_one_pulse_first2.delete(0, 'end')
        entr_ed_izm2.delete(0, 'end')
    except pypyodbc.IntegrityError:
        messagebox.showwarning('Ошибка!', 'Эти данные не возможно изменить, так как они используются в другой таблице!')
    btn_add_sm['state'] = NORMAL
    btn_del_sm['state'] = NORMAL
    btn_upgrade_data['state'] = 'disabled'



def window_auntif_add():
    def sequre_pass():
        Query_p = f"SELECT adm_pas FROM dbo.adm_lp"
        cursor.execute(Query_p)
        password = cursor.fetchone()

        p = password_entry.get()
        hash_p_obj = hashlib.md5(p.encode())

        if hash_p_obj.hexdigest() == password[0]:
            add_smartmaic()
            new_window.destroy()
        else:
            messagebox.showwarning('Ошибка!', 'Неверный пароль!')

    new_window = Toplevel(window)
    new_window.geometry('450x230')
    new_window.title("Подтверждение действий")
    font_header = ('Arial', 15)
    font_entry = ('Arial', 12)
    label_font = ('Arial', 11)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}

    main_label = Label(new_window, text='Подтверждение', font=font_header, justify=CENTER, **header_padding)
    main_label.pack()
    password = ''

    password_label = Label(new_window, text='Пароль', font=label_font, **base_padding)
    password_label.pack()

    password_entry = Entry(new_window, bg='#fff', fg='#444', show='*', font=font_entry)
    password_entry.pack()

    send_btn = ttk.Button(new_window, text='Войти', command=sequre_pass)
    send_btn.pack(**base_padding)


def window_auntif_del():
    def sequre_pass():
        Query_p = f"SELECT adm_pas FROM dbo.adm_lp"
        cursor.execute(Query_p)
        password = cursor.fetchone()

        p = password_entry.get()
        hash_p_obj = hashlib.md5(p.encode())

        if hash_p_obj.hexdigest() == password[0]:
            del_smartmaic()
            new_window.destroy()
        else:
            messagebox.showwarning('Ошибка!', 'Неверный пароль!')

    new_window = Toplevel(window)
    new_window.geometry('450x230')
    new_window.title("Подтверждение действий")
    font_header = ('Arial', 15)
    font_entry = ('Arial', 12)
    label_font = ('Arial', 11)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}

    main_label = Label(new_window, text='Подтверждение', font=font_header, justify=CENTER, **header_padding)
    main_label.pack()
    password = ''

    password_label = Label(new_window, text='Пароль', font=label_font, **base_padding)
    password_label.pack()

    password_entry = Entry(new_window, bg='#fff', fg='#444', show='*', font=font_entry)
    password_entry.pack()

    send_btn = ttk.Button(new_window, text='Войти', command=sequre_pass)
    send_btn.pack(**base_padding)


def window_auntif_upgrade():
    def sequre_pass():
        Query_p = f"SELECT adm_pas FROM dbo.adm_lp"
        cursor.execute(Query_p)
        password = cursor.fetchone()

        p = password_entry.get()
        hash_p_obj = hashlib.md5(p.encode())

        if hash_p_obj.hexdigest() == password[0]:
            upgrade_data_frame()
            new_window.destroy()
        else:
            messagebox.showwarning('Ошибка!', 'Неверный пароль!')

    new_window = Toplevel(window)
    new_window.geometry('450x230')
    new_window.title("Подтверждение действий")
    font_header = ('Arial', 15)
    font_entry = ('Arial', 12)
    label_font = ('Arial', 11)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}

    main_label = Label(new_window, text='Подтверждение', font=font_header, justify=CENTER, **header_padding)
    main_label.pack()
    password = ''

    password_label = Label(new_window, text='Пароль', font=label_font, **base_padding)
    password_label.pack()

    password_entry = Entry(new_window, bg='#fff', fg='#444', show='*', font=font_entry)
    password_entry.pack()

    send_btn = ttk.Button(new_window, text='Войти', command=sequre_pass)
    send_btn.pack(**base_padding)


'''графика'''
lbf_registraciya = tk.LabelFrame(device_tab, width=340, height=250, background="#3c4757", foreground="white")
lbf_registraciya.grid(column=3, row=0, pady=20, padx=40)


entr_name_sm = tk.Entry(lbf_registraciya, width=30, background="#4a576b", foreground="white")
entr_name_sm.grid(column=0, row=1, padx=(30, 30))

entr_ip_sm = tk.Entry(lbf_registraciya, width=30, background="#4a576b", foreground="white")
entr_ip_sm.grid(column=0, row=3)

entr_id_sm = tk.Entry(lbf_registraciya, width=30, background="#4a576b", foreground="white")
entr_id_sm.grid(column=0, row=5)

entr_one_pulse_first1 = tk.Entry(lbf_registraciya, width=30, background="#4a576b", foreground="white")
entr_one_pulse_first1.grid(column=0, row=7)
Hovertip(entr_one_pulse_first1, "Для первого импульсного входа", hover_delay=100)

entr_ed_izm1 = tk.Entry(lbf_registraciya, width=30, background="#4a576b", foreground="white")
entr_ed_izm1.grid(column=0, row=9)

entr_one_pulse_first2 = tk.Entry(lbf_registraciya, width=30, background="#4a576b", foreground="white")
entr_one_pulse_first2.grid(column=0, row=11)
Hovertip(entr_one_pulse_first2, "Для второго импульсного входа", hover_delay=100)

entr_ed_izm2 = tk.Entry(lbf_registraciya, width=30, background="#4a576b", foreground="white")
entr_ed_izm2.grid(column=0, row=13)


#"background": "#3c4757", "foreground": "white"

lb_name_sm = tk.Label(lbf_registraciya, text='Название устройства', background="#3c4757", foreground="white")
lb_name_sm.grid(column=0, row=0, pady=10)

lb_ip = tk.Label(lbf_registraciya, text='IP-Адрес', background="#3c4757", foreground="white")
lb_ip.grid(column=0, row=2, pady=10)

lb_id = tk.Label(lbf_registraciya, text='ID устройства', background="#3c4757", foreground="white")
lb_id.grid(column=0, row=4, pady=10)

lb_one_pulse1 = tk.Label(lbf_registraciya, text='Значение одного импульса', background="#3c4757", foreground="white")
lb_one_pulse1.grid(column=0, row=6, pady=10)

lb_ed_izm1 = tk.Label(lbf_registraciya, text='Единица измерения', background="#3c4757", foreground="white")
lb_ed_izm1.grid(column=0, row=8, pady=10)

lb_one_pulse1 = tk.Label(lbf_registraciya, text='Значение одного импульса', background="#3c4757", foreground="white")
lb_one_pulse1.grid(column=0, row=10, pady=10)

lb_ed_izm1 = tk.Label(lbf_registraciya, text='Единица измерения', background="#3c4757", foreground="white")
lb_ed_izm1.grid(column=0, row=12, pady=10)


btn_add_sm = tk.Button(lbf_registraciya, text='Добавить', background='#546278', fg='white', relief='ridge', width=10, command=window_auntif_add)
btn_add_sm.grid(column=0, row=20, padx=40, pady=(20, 20), sticky=tk.W)
keyboard.add_hotkey('enter', fast_add_smartmaic)

btn_del_sm = tk.Button(lbf_registraciya, text='Удалить', background='#546278', fg='white', relief='ridge', width=10, command=window_auntif_del)
btn_del_sm.grid(column=0, row=20, padx=40, sticky=tk.E)
keyboard.add_hotkey('delete', del_smartmaic)

lb_upgrade = tk.Label(lbf_registraciya, text='Изменение данных', background="#3c4757", foreground="white")
lb_upgrade.grid(column=0, row=21, pady=10)

btn_select_data = tk.Button(lbf_registraciya, text='Выбрать', background='#546278', fg='white', relief='ridge', width=10, command=insert_upgrade_data_memory)
btn_select_data.grid(column=0, row=22, pady=(20, 20), sticky=tk.W, padx=40)

btn_upgrade_data = tk.Button(lbf_registraciya, text='Изменить', background='#546278', fg='white', relief='ridge', width=10, command=window_auntif_upgrade)
btn_upgrade_data.grid(column=0, row=22, sticky=tk.E, padx=40)
btn_upgrade_data['state'] = 'disabled'

def update_table_sm():
    device_table.delete(*device_table.get_children())
    mySQLQuery = ("""SELECT * FROM dbo.device""")
    cursor.execute(mySQLQuery)
    rows_device = cursor.fetchall()
    for i in rows_device:
        device_table.insert('', 'end', values=(i['info_smartmaic'], i['ip_smartmaic'], i['id_smartmaic'], i['one_pulse_first_entrance'], i['ed_izm_one'], i['one_pulse_second_entranse'], i['ed_izm_two']))

def update_table_day_info():
    day_info_table.delete(*day_info_table.get_children())
    mySQLQuery2 = ("""SELECT name,ch1,tch1,ed_izm_one,ch2,tch2,ed_izm_two,data,time,ip_smartmaic,id_smartmaic FROM dbo.day_info ORDER BY data DESC, time DESC""")
    cursor.execute(mySQLQuery2)
    rows_day_info = cursor.fetchall()
    for i in rows_day_info:
        day_info_table.insert('', 'end', values=(i['name'], i['ch1'], i['tch1'], i['ed_izm_one'], i['ch2'], i['tch2'], i['ed_izm_two'], i['data'], i['time'], i['ip_smartmaic'], i['id_smartmaic']))

def update_table_night_info():
    night_info_table.delete(*night_info_table.get_children())
    mySQLQuery4 = ("""SELECT * FROM dbo.night_info ORDER BY data DESC, time DESC""")
    cursor.execute(mySQLQuery4)
    rows_night_info = cursor.fetchall()
    for i in rows_night_info:
        night_info_table.insert('', 'end', values=(i['name'], i['ch1'], i['tch1'], i['ed_izm_one'], i['ch2'], i['tch2'], i['ed_izm_two'], i['data'], i['time'], i['ip_smartmaic'], i['id_smartmaic']))

update_table_sm()
update_table_day_info()
update_table_night_info()


def update_device_table(device_table):
    device_table.delete(*device_table.get_children())
    mySQLQuery = ("""SELECT * FROM dbo.device""")
    cursor.execute(mySQLQuery)
    rows_device = cursor.fetchall()
    kolvo_device = len(rows_device)
    for i in rows_device:
        device_table.insert('', 'end', values=(i['info_smartmaic'], i['ip_smartmaic'], i['id_smartmaic'], i['one_pulse_first_entrance'], i['ed_izm_one'], i['one_pulse_second_entranse'], i['ed_izm_two']))
        info = str(i['info_smartmaic'])
        ip_smartmaic = str(i['ip_smartmaic'])
        id_smartmaic = str(i['id_smartmaic'])
        ed_izm_one = str(i['ed_izm_one'])
        ed_izm_two = str(i['ed_izm_two'])
        one_pulse_first_entrance = float(i['one_pulse_first_entrance'])
        one_pulse_second_entranse = float(i['one_pulse_second_entranse'])


        respons = requests.get(http + ip_smartmaic + p + id_smartmaic + Pass)
        respons_json = respons.json()

        data_states = datetime.datetime.now()
        final_data = data_states.strftime("%Y.%m.%d %H:%M:%S")
        data_and_time = str(final_data).split()
        now_time = data_states.hour
        print(final_data, '\n', "")

        CH1 = respons_json["data"]["Ch1"]["value"]
        TCH1 = respons_json["data"]["TCh1"]["value"]
        CH2 = respons_json["data"]["Ch2"]["value"]
        TCH2 = respons_json["data"]["TCh2"]["value"]
        tdate = data_and_time[0]
        ttime = data_and_time[1]
        name = info

        '''конвертация импульсов'''
        final_pokazaniya_ch1 = float(CH1) / one_pulse_first_entrance
        final_pokazaniya_tch1 = float(TCH1) / one_pulse_first_entrance
        final_pokazaniya_ch2 = float(CH2) / one_pulse_first_entrance
        final_pokazaniya_tch2 = float(TCH2) / one_pulse_first_entrance


        if now_time == 11 or now_time == 20:

            mySQLQuery1 = "INSERT INTO dbo.day_info(name, ch1, tch1, ed_izm_one, ch2, tch2, ed_izm_two, data, time, ip_smartmaic, id_smartmaic) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(f'{name}', f'{final_pokazaniya_ch1}', f'{final_pokazaniya_tch1}', f'{ed_izm_one}', f'{final_pokazaniya_ch2}', f'{final_pokazaniya_tch2}', f'{ed_izm_two}', f'{tdate}', f'{ttime}', f'{ip_smartmaic}', f'{id_smartmaic}')
            cursor.execute(mySQLQuery1)
            connection.commit()

            print("Первый импульсный вход: ", respons_json["data"]["Ch1"]["value"])
            print("Всего на первом импульсном входе: ", respons_json["data"]["TCh1"]["value"])
            print("Второй импульсный вход: ", respons_json["data"]["Ch2"]["value"])
            print("Всего на втором импульсном входе: ", respons_json["data"]["TCh2"]["value"])
            print("")

            querySelect = "SELECT id FROM day_info"
            cursor.execute(querySelect)
            id_info = cursor.fetchall()
            id_kolvo = len(id_info)

            delete_lishnie_data = kolvo_device * 2 * 365
            print(delete_lishnie_data)

            if id_kolvo > delete_lishnie_data:
                res_del = id_kolvo - delete_lishnie_data
                queryDelete = f"DELETE FROM dbo.day_info WHERE id <='"+ str(res_del) +"'"
                cursor.execute(queryDelete)

            update_table_day_info()

        if now_time == 15:
            mySQLQuery3 = "INSERT INTO dbo.night_info(name, ch1, tch1, ed_izm_one, ch2, tch2, ed_izm_two, data, time, ip_smartmaic, id_smartmaic) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(f'{name}', f'{final_pokazaniya_ch1}', f'{final_pokazaniya_tch1}', f'{ed_izm_one}', f'{final_pokazaniya_ch2}', f'{final_pokazaniya_tch2}', f'{ed_izm_two}', f'{tdate}',f'{ttime}', f'{ip_smartmaic}', f'{id_smartmaic}')
            cursor.execute(mySQLQuery3)
            connection.commit()

            print("Первый импульсный вход: ", respons_json["data"]["Ch1"]["value"])
            print("Всего на первом импульсном входе: ", respons_json["data"]["TCh1"]["value"])
            print("Второй импульсный вход: ", respons_json["data"]["Ch2"]["value"])
            print("Всего на втором импульсном входе: ", respons_json["data"]["TCh2"]["value"])
            print("")

            querySelect1 = "SELECT id FROM night_info"
            cursor.execute(querySelect1)
            id_info1 = cursor.fetchall()
            id_kolvo1 = len(id_info1)

            delete_lishnie_data1 = kolvo_device * 2 * 365
            print(delete_lishnie_data1)

            if id_kolvo1 > delete_lishnie_data1:
                res_del1 = id_kolvo1 - delete_lishnie_data1
                queryDelete1 = f"DELETE FROM dbo.day_info WHERE id <='" + str(res_del1) + "'"
                cursor.execute(queryDelete1)

            update_table_night_info()




def my_mainloop():
    data_states = datetime.datetime.now()
    now_time_hour = data_states.hour
    now_time_min = data_states.minute
    if now_time_hour == 11 and now_time_min == 40 or now_time_hour == 20 and now_time_min == 0 or now_time_hour == 4 and now_time_min == 0:
        update_device_table(device_table)
    window.after(60000, my_mainloop)




window.after(60000, my_mainloop)
if a == 1:
    window.mainloop()
#window.mainloop()
connection.close()
