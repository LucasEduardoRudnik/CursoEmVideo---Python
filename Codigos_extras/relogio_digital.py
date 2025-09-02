import tkinter as tk
import time

def atualizar_hora():
    hora_atual = time.strftime('%H:%M:%S')  # Pega hora atual
    texto.config(text=hora_atual)           # Atualiza o Label
    janela.after(1000, atualizar_hora)      # Chama de novo a cada 1s

janela = tk.Tk()
janela.title("Relógio Digital")
janela.geometry('300x120')
janela.configure(bg='black')

texto = tk.Label(janela, font=('Courier', 40), bg='black', fg='lime')
texto.pack(expand=True)

atualizar_hora()  # <<< ESSA LINHA É FUNDAMENTAL

janela.mainloop()