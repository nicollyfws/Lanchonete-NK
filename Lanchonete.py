import tkinter as tk
from tkinter import messagebox

def atualizar_listas():
    lista_lanche_pendentes.delete(0, tk.END)
    lista_lanche_concluidas.delete(0, tk.END)
    for lanche in lanche_pendentes + lanche_concluidas:
        lista_lanche_pendentes.insert(tk.END, lanche) if lanche not in lanche_concluidas else lista_lanche_concluidas.insert(tk.END, lanche)

def manipular_lanche(acao):
    lanche = entrada_lanche.get().strip()
    try:
        lanche_selecionada = lista_lanche_pendentes.curselection()
        lanche = lista_lanche_pendentes.get(lanche_selecionada) if lanche == "" else lanche
    except IndexError:
        lanche_selecionada = None

    if acao == "adicionar" and lanche: lanche_pendentes.append(lanche)
    elif acao == "excluir" and lanche_selecionada: lanche_pendentes.remove(lanche)
    elif acao == "concluir" and lanche_selecionada:
        lanche_pendentes.remove(lanche)
        lanche_concluidas.append(lanche)

    entrada_lanche.delete(0, tk.END)
    atualizar_listas()

janela = tk.Tk()
janela.title("Lista de lanche Diárias")

lanche_pendentes, lanche_concluidas = [], []

entrada_lanche = tk.Entry(janela, width=40)
entrada_lanche.grid(row=0, column=0, padx=10, pady=10)

tk.Button(janela, text="Adicionar lanche", width=20, command=lambda: manipular_lanche("adicionar")).grid(row=0, column=1, padx=10, pady=10)
lista_lanche_pendentes = tk.Listbox(janela, height=10, width=50)
lista_lanche_pendentes.grid(row=1, column=0, padx=10, pady=10)
lista_lanche_concluidas = tk.Listbox(janela, height=10, width=50)
lista_lanche_concluidas.grid(row=1, column=1, padx=10, pady=10)

tk.Button(janela, text="Excluir lanche", width=20, command=lambda: manipular_lanche("excluir")).grid(row=2, column=0, padx=10, pady=10)
tk.Button(janela, text="Concluir lanche", width=20, command=lambda: manipular_lanche("concluir")).grid(row=2, column=1, padx=10, pady=10)

atualizar_listas()

janela.mainloop()
