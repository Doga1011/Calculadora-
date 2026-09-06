import tkinter as tk

def button_click(char):
    display.insert(tk.END, char)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        resultado = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(resultado))
    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(tk.END, "Erro: divisão por zero")
    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "Erro")

janela = tk.Tk()
janela.title("Calculadora")

display = tk.Entry(janela, width=20, font=("Arial", 18), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

botoes = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

linha, coluna = 1, 0
for texto in botoes:
    acao = calculate if texto == "=" else (lambda t=texto: button_click(t))
    tk.Button(janela, text=texto, width=5, height=2, command=acao).grid(row=linha, column=coluna)
    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

tk.Button(janela, text="C", width=22, height=2, command=clear).grid(row=linha, column=0, columnspan=4)

janela.mainloop()

    