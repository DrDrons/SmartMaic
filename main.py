from idlelib.tooltip import Hovertip
import requests
import datetime
import pypyodbc
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Frame, Notebook, Treeview
import tkinter as tk
from tkinter import messagebox
import autification


#SERVER=DESKTOP-S152C1O\SQLEXPRESS; Cервер Вова
#SERVER=DESKTOP-GLIOC6U\SQLEXPRESS; Сервер Лёша

connection = pypyodbc.connect('Driver={SQL Server};'
                                'SERVER=DESKTOP-GLIOC6U\SQLEXPRESS;' 
                                'Database=bd_smart_maic;')

cursor = connection.cursor()



window = Tk()
window.title("SmartMaic")
window.geometry('1500x1000')
tab_control = Notebook(window)

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
device_tab = Frame(tab_control)
tab_control.add(device_tab, text="SmartMaic")

tab_control.pack(expand=1, fill='both')

laibal_day = Frame(day_info_tab)
laibal_day.grid(column=0, row=0)

laibal_night = Frame(day_info_tab)
laibal_night.grid(column=0, row=1)

rows_device = ('info_smartmaic', 'ip_smartmaic', 'id_smartmaic', 'one_pulse_first_entrance', 'ed_izm_one', 'one_pulse_second_entranse', 'ed_izm_two')
device_table = Treeview(device_tab, show="headings")
device_table.grid(column=0, row=0, columnspan=3, padx=20, pady=20, sticky=tk.N)
device_table["columns"] = rows_device
device_table["displaycolumns"] = rows_device
for head in rows_device:
    device_table.column(head, anchor=CENTER, width=150)

device_table.heading(rows_device[0], text="Название")
device_table.heading(rows_device[1], text="IP-Устройства")
device_table.heading(rows_device[2], text="ID-Устройства")
device_table.heading(rows_device[3], text="Значение импульса(Ch1)")
device_table.heading(rows_device[4], text="Единица измерения")
device_table.heading(rows_device[5], text="Значение импульса(Ch2)")
device_table.heading(rows_device[6], text="Единица измерения")


rows_day_info = ('name', 'ch1', 'tch1', 'ed_izm_one', 'ch2', 'tch2', 'ed_izm_two', 'data', 'time', 'ip_smartmaic', 'id_smartmaic')
day_info_table = Treeview(laibal_day, show="headings")
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

laibol_neigth = Label(laibal_day, text='День')
laibol_neigth.pack(side=TOP, pady=10)

rows_night_info = ('name', 'ch1', 'tch1', 'ed_izm_one', 'ch2', 'tch2', 'ed_izm_two', 'data', 'time', 'ip_smartmaic', 'id_smartmaic')
night_info_table = Treeview(laibal_night, show="headings")
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

laibol_daay = Label(laibal_night, text='Ночь')
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

entr_one_pulse_first1 = Entry(lbf_registraciya, width=30)
entr_one_pulse_first1.grid(column=0, row=7)
Hovertip(entr_one_pulse_first1, "Для первого импульсного входа", hover_delay=100)

entr_ed_izm1 = Entry(lbf_registraciya, width=30)
entr_ed_izm1.grid(column=0, row=9)

entr_one_pulse_first2 = Entry(lbf_registraciya, width=30)
entr_one_pulse_first2.grid(column=0, row=11)
Hovertip(entr_one_pulse_first2, "Для второго импульсного входа", hover_delay=100)

entr_ed_izm2 = Entry(lbf_registraciya, width=30)
entr_ed_izm2.grid(column=0, row=13)

lb_name_sm = Label(lbf_registraciya, text='Название устройства')
lb_name_sm.grid(column=0, row=0, pady=10)

lb_ip = Label(lbf_registraciya, text='IP-Адрес')
lb_ip.grid(column=0, row=2, pady=10)

lb_id = Label(lbf_registraciya, text='ID устройства')
lb_id.grid(column=0, row=4, pady=10)

lb_one_pulse1 = Label(lbf_registraciya, text='Значение одного импульса')
lb_one_pulse1.grid(column=0, row=6, pady=10)

lb_ed_izm1 = Label(lbf_registraciya, text='Единица измерения')
lb_ed_izm1.grid(column=0, row=8, pady=10)

lb_one_pulse1 = Label(lbf_registraciya, text='Значение одного импульса')
lb_one_pulse1.grid(column=0, row=10, pady=10)

lb_ed_izm1 = Label(lbf_registraciya, text='Единица измерения')
lb_ed_izm1.grid(column=0, row=12, pady=10)


btn_add_sm = Button(lbf_registraciya, text='Добавить', width=10, command=add_smartmaic)
btn_add_sm.grid(column=0, row=20, padx=40, pady=(20, 20), sticky=tk.W)

btn_del_sm = Button(lbf_registraciya, text='Удалить', width=10, command=del_smartmaic)
btn_del_sm.grid(column=0, row=20, padx=40, sticky=tk.E)


def update_table_sm():
    device_table.delete(*device_table.get_children())
    mySQLQuery = ("""SELECT * FROM dbo.device""")
    cursor.execute(mySQLQuery)
    rows_device = cursor.fetchall()
    for i in rows_device:
        device_table.insert('', 'end', values=(i['info_smartmaic'], i['ip_smartmaic'], i['id_smartmaic'], i['one_pulse_first_entrance'], i['ed_izm_one'], i['one_pulse_second_entranse'], i['ed_izm_two']))

btn_add_sm = Button(device_tab, text='Добавить', width=10, command=del_smartmaic)
btn_add_sm.grid(column=0, row=10)

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
    if now_time_hour == 11 and now_time_min == 5 or now_time_hour == 20 and now_time_min == 0 or now_time_hour == 4 and now_time_min == 0:
        update_device_table(device_table)
    window.after(60000, my_mainloop)



window.after(60000, my_mainloop)
if autification.a == 1:
    window.mainloop()
#window.mainloop()
connection.close()
