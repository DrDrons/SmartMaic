
import requests
import datetime
import pypyodbc
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Frame, Notebook, Treeview
import tkinter as tk
from tkinter import messagebox

#SERVER=DESKTOP-S152C1O\SQLEXPRESS; Cервер Вова
#SERVER=DESKTOP-GLIOC6U\SQLEXPRESS; Сервер Лёша

connection = pypyodbc.connect('Driver={SQL Server};'
                                'SERVER=DESKTOP-S152C1O\SQLEXPRESS;' 
                                'Database=bd_smart_maic;')

cursor = connection.cursor()



window = Tk()
window.title("SmartMaic")
window.geometry('1000x700')
tab_control = Notebook(window)

day_info_tab = ttk.Frame(tab_control)
tab_control.add(day_info_tab, text="Информация")
device_tab = Frame(tab_control)
tab_control.add(device_tab, text="SmartMaic")

tab_control.pack(expand=1, fill='both')

laibal_day = Frame(day_info_tab)
laibal_day.grid(column=0, row=0)

laibal_night = Frame(day_info_tab)
laibal_night.grid(column=0, row=1)

rows_device = ('info_smartmaic', 'ip_smartmaic', 'id_smartmaic')
device_table = Treeview(device_tab, show="headings")
device_table.grid(column=0, row=0, columnspan=3, padx=20)
device_table["columns"] = rows_device
device_table["displaycolumns"] = rows_device
for head in rows_device:
    device_table.column(head, anchor=CENTER)

device_table.heading(rows_device[0], text="Название")
device_table.heading(rows_device[1], text="IP-Устройства")
device_table.heading(rows_device[2], text="ID-Устройства")


rows_day_info = ('ch1', 'tch1', 'ch2', 'tch2', 'time', 'ip_smartmaic')
day_info_table = Treeview(laibal_day, show="headings")
day_info_table.pack(side=BOTTOM, padx=20, pady=(10, 10))
day_info_table["columns"] = rows_day_info
day_info_table["displaycolumns"] = rows_day_info
for head in rows_day_info:
    day_info_table.column(head, anchor=CENTER, width=160)

day_info_table.heading(rows_day_info[0], text="Первый импульсный вход")
day_info_table.heading(rows_day_info[1], text="Всего импульсов(TCh1)")
day_info_table.heading(rows_day_info[2], text="Второй импульсный вход")
day_info_table.heading(rows_day_info[3], text="Всего импульсов(TCh2)")
day_info_table.heading(rows_day_info[4], text="Время")
day_info_table.heading(rows_day_info[5], text="IP-Устройства")

laibol_neigth = Label(laibal_day, text='День')
laibol_neigth.pack(side=TOP, pady=10)

rows_night_info = ('ch1', 'tch1', 'ch2', 'tch2', 'time', 'ip_smartmaic')
night_info_table = Treeview(laibal_night, show="headings")
night_info_table.pack(side=BOTTOM, pady=(10, 10))
night_info_table["columns"] = rows_night_info
night_info_table["displaycolumns"] = rows_night_info
for head in rows_night_info:
    night_info_table.column(head, anchor=CENTER, width=160)

night_info_table.heading(rows_night_info[0], text="Первый импульсный вход")
night_info_table.heading(rows_night_info[1], text="Всего импульсов(TCh1)")
night_info_table.heading(rows_night_info[2], text="Второй импульсный вход")
night_info_table.heading(rows_night_info[3], text="Всего импульсов(TCh2)")
night_info_table.heading(rows_night_info[4], text="Время")
night_info_table.heading(rows_night_info[5], text="IP-Устройства")

laibol_daay = Label(laibal_night, text='Ночь')
laibol_daay.pack(side=TOP)

http = 'http://'
p = '/?page=getdata&devid='
Pass = '&devpass=12345'

def add_smartmaic():
    if entr_name_sm.get() == '' or entr_ip_sm.get() == '' or entr_id_sm.get() == '':
        messagebox.showwarning('Ошибка!', 'Введите все данные!')
    else:
        mySQLQuery1 = f"insert into dbo.device(info_smartmaic,ip_smartmaic,id_smartmaic) values (N'" + entr_name_sm.get() + "',N'" + entr_ip_sm.get() + "',N'" + entr_id_sm.get() + "')"
        cursor.execute(mySQLQuery1)
        connection.commit()
        update_table_sm()
        entr_name_sm.delete(0, 'end')
        entr_ip_sm.delete(0, 'end')
        entr_id_sm.delete(0, 'end')


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


'''графика'''
lbf_registraciya = LabelFrame(device_tab, text='Добавление нового устройства', width=340, height=250)
lbf_registraciya.grid(column=3, row=0, pady=10, padx=40)

entr_name_sm = Entry(lbf_registraciya, width=30)
entr_name_sm.grid(column=0, row=1, padx=(30, 30))

entr_ip_sm = Entry(lbf_registraciya, width=30)
entr_ip_sm.grid(column=0, row=3)

entr_id_sm = Entry(lbf_registraciya, width=30)
entr_id_sm.grid(column=0, row=5)


lb_name_sm = Label(lbf_registraciya, text='Название устройства')
lb_name_sm.grid(column=0, row=0, pady=10)

lb_name_sm = Label(lbf_registraciya, text='IP-Адрес')
lb_name_sm.grid(column=0, row=2, pady=10)

lb_name_sm = Label(lbf_registraciya, text='ID устройства')
lb_name_sm.grid(column=0, row=4, pady=10)


btn_add_sm = Button(lbf_registraciya, text='Добавить', width=10, command=add_smartmaic)
btn_add_sm.grid(column=0, row=8, padx=40, pady=(20, 20), sticky=tk.W)

btn_del_sm = Button(lbf_registraciya, text='Удалить', width=10, command=del_smartmaic)
btn_del_sm.grid(column=0, row=8, padx=40, sticky=tk.E)


def update_table_sm():
    device_table.delete(*device_table.get_children())
    mySQLQuery = ("""SELECT * FROM dbo.device""")
    cursor.execute(mySQLQuery)
    rows_device = cursor.fetchall()
    for i in rows_device:
        device_table.insert('', 'end', values=(i['info_smartmaic'], i['ip_smartmaic'], i['id_smartmaic']))

def update_table_day_info():
    day_info_table.delete(*day_info_table.get_children())
    mySQLQuery2 = ("""SELECT * FROM dbo.day_info ORDER BY time DESC""")
    cursor.execute(mySQLQuery2)
    rows_day_info = cursor.fetchall()
    for i in rows_day_info:
        day_info_table.insert('', 'end', values=(i['ch1'], i['tch1'], i['ch2'], i['tch2'], i['time'], i['ip_smartmaic']))

def update_table_night_info():
    night_info_table.delete(*night_info_table.get_children())
    mySQLQuery4 = ("""SELECT * FROM dbo.night_info ORDER BY time DESC""")
    cursor.execute(mySQLQuery4)
    rows_night_info = cursor.fetchall()
    for i in rows_night_info:
        night_info_table.insert('', 'end', values=(i['ch1'], i['tch1'], i['ch2'], i['tch2'], i['time'], i['ip_smartmaic']))

update_table_sm()
update_table_day_info()
update_table_night_info()


def update_device_table(device_table):
    device_table.delete(*device_table.get_children())
    mySQLQuery = ("""SELECT * FROM dbo.device""")
    cursor.execute(mySQLQuery)
    rows_device = cursor.fetchall()
    for i in rows_device:
        device_table.insert('', 'end', values=(i['info_smartmaic'], i['ip_smartmaic'], i['id_smartmaic']))
        ip = str(i['ip_smartmaic'])
        id = str(i['id_smartmaic'])


        respons = requests.get(http + ip + p + id + Pass)
        respons_json = respons.json()

        data_states = datetime.datetime.now()
        final_data = data_states.strftime("%Y.%m.%d %H:%M:%S")
        now_time = data_states.hour
        print(final_data, '\n', "")

        id_info = 1


        CH1 = respons_json["data"]["Ch1"]["value"]
        TCH1 = respons_json["data"]["TCh1"]["value"]
        CH2 = respons_json["data"]["Ch2"]["value"]
        TCH2 = respons_json["data"]["TCh2"]["value"]
        ttime = final_data
        ip_smartmaic = ip

        if now_time == 12 or now_time == 20:

            mySQLQuery1 = "INSERT INTO dbo.day_info(id_info, ch1, tch1, ch2, tch2, time, ip_smartmaic) values('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(f'{id_info}', f'{CH1}', f'{TCH1}', f'{CH2}', f'{TCH2}', f'{ttime}', f'{ip_smartmaic}')
            cursor.execute(mySQLQuery1)
            connection.commit()

            print("Первый импульсный вход: ", respons_json["data"]["Ch1"]["value"])
            print("Всего на первом импульсном входе: ", respons_json["data"]["TCh1"]["value"])
            print("Второй импульсный вход: ", respons_json["data"]["Ch2"]["value"])
            print("Всего на втором импульсном входе: ", respons_json["data"]["TCh2"]["value"])
            print("")

            day_info_table.delete(*day_info_table.get_children())
            mySQLQuery2 = ("""SELECT * FROM dbo.day_info ORDER BY time DESC""")
            cursor.execute(mySQLQuery2)
            rows_day_info = cursor.fetchall()
            for i in rows_day_info:
                day_info_table.insert('', 'end', values=(i['ch1'], i['tch1'], i['ch2'], i['tch2'], i['time'], i['ip_smartmaic']))
        if now_time == 4:
            mySQLQuery3 = "INSERT INTO dbo.night_info(id_info, ch1, tch1, ch2, tch2, time, ip_smartmaic) values('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(f'{id_info}', f'{CH1}', f'{TCH1}', f'{CH2}', f'{TCH2}', f'{ttime}', f'{ip_smartmaic}')
            cursor.execute(mySQLQuery3)
            connection.commit()

            print("Первый импульсный вход: ", respons_json["data"]["Ch1"]["value"])
            print("Всего на первом импульсном входе: ", respons_json["data"]["TCh1"]["value"])
            print("Второй импульсный вход: ", respons_json["data"]["Ch2"]["value"])
            print("Всего на втором импульсном входе: ", respons_json["data"]["TCh2"]["value"])
            print("")

            night_info_table.delete(*night_info_table.get_children())
            mySQLQuery4 = ("""SELECT * FROM dbo.night_info ORDER BY time DESC""")
            cursor.execute(mySQLQuery4)
            rows_night_info = cursor.fetchall()
            for i in rows_night_info:
                night_info_table.insert('', 'end', values=(i['ch1'], i['tch1'], i['ch2'], i['tch2'], i['time'], i['ip_smartmaic']))



def my_mainloop():
    data_states = datetime.datetime.now()
    now_time_hour = data_states.hour
    now_time_min = data_states.minute
    if now_time_hour == 12 and now_time_min == 0 or now_time_hour == 20 and now_time_min == 0 or now_time_hour == 4 and now_time_min == 0:
        update_device_table(device_table)
    window.after(60000, my_mainloop)


window.after(60000, my_mainloop)
window.mainloop()
connection.close()
