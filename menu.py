import customtkinter as ctk
from main import *

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x300")
app.title("Лаунчер гри")

def run_game():
    name = name_input.get()
    host = adres_input.get()
    port = port_input.get()
    if name and host and port:
        app.destroy()
        start_game(name, host, port)


name_lbl = ctk.CTkLabel(app, text="Імя гравця:")
name_lbl.pack(pady=10)
name_input = ctk.CTkEntry(app)
name_input.pack()

app_adres = ctk.CTk()
app_adres.geometry("400x300")
app_adres.title("Лаунчер гри")

adres_lbl = ctk.CTkLabel(app, text="Адрес сервера:")
adres_lbl.pack(pady=10)
adres_input = ctk.CTkEntry(app)
adres_input.insert(0, "2.tcp.eu.ngrok.io")
adres_input.pack()

port_lbl = ctk.CTkLabel(app, text="Порт:")
port_lbl.pack(pady=10)
port_input = ctk.CTkEntry(app)
port_input.insert(0, "18875")
port_input.pack()

knopka = ctk.CTkButton(app, text="Запустити гру",command=run_game).pack(pady=20)

app.mainloop()