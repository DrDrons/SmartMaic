
from tkinter import *
from tkinter import messagebox
import pypyodbc

connection = pypyodbc.connect('Driver={SQL Server};'
                                'SERVER=DESKTOP-GLIOC6U\SQLEXPRESS;' 
                                'Database=bd_smart_maic;')
cursor = connection.cursor()


# главное окно приложения
window = Tk()
window.title('Авторизация')
window.geometry('450x230')
window.resizable(False, False)

# кортежи и словари, содержащие настройки шрифтов и отступов
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
    if username_entry.get() == login[0] and password_entry.get() == password[0]:
        a += 1
        window.destroy()
    else:
        messagebox.showwarning('Ошибка!', 'Невенрый логин или пароль!')


# заголовок формы: настроены шрифт (font), отцентрирован (justify), добавлены отступы для заголовка
# для всех остальных виджетов настройки делаются также
main_label = Label(window, text='Авторизация', font=font_header, justify=CENTER, **header_padding)
# помещаем виджет в окно по принципу один виджет под другим
main_label.pack()
password = ''
# метка для поля ввода имени
username_label = Label(window, text='Имя пользователя', font=label_font, **base_padding)
username_label.pack()

# поле ввода имени ttk.Entry(mainframe, textvariable = password, show = '*')
username_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
username_entry.pack()

# метка для поля ввода пароля
password_label = Label(window, text='Пароль', font=label_font , **base_padding)
password_label.pack()

# поле ввода пароля
password_entry = Entry(window, bg='#fff', fg='#444', show='*', font=font_entry)
password_entry.pack()

# кнопка отправки формы
send_btn = Button(window, text='Войти', command=close_app)
send_btn.pack(**base_padding)

# запускаем главный цикл окна
window.mainloop()
