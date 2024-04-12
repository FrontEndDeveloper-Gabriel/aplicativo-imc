# DESENVOLVER UMA INTERFACE PARA AS PESSOAS MEDIREM SEU PESO

# IMPORTAR O TKINTER ✔
import tkinter as tk

# CRIAR UMA FUNÇÃO PARA QUE O IMC POSSA SER UTILIZADO ✔
def imc():
    idade = entry1.get()
    massa = float(entry2.get())
    altura = float(entry3.get())
    altura_calculada = altura * altura
    imc_resultado = massa // altura_calculada
    result.config(text=f"Seu IMC: {imc_resultado}")

    if imc_resultado <= 18.5:
       classificacao.config(text=f"Sua situação: Abaixo do Peso")
    elif imc_resultado >= 18.5:
       classificacao.config(text=f"Sua situação: Peso Normal")
    elif imc_resultado >= 25:
       classificacao.config(text=f"Sua situação: Sobrepeso")
    elif imc_resultado >= 30:
       classificacao.config(text=f"Sua situação: Obesidade Grau I")
    elif imc_resultado >= 35:
       classificacao.config(text=f"Sua situação: Obesidade Grau II")
    elif imc_resultado > 40:
       classificacao.config(text=f"Sua situação: Obesidade Grau III")


# CRIANDO O TÍTULO ✔
root = tk.Tk()
root.title("Seu IMC)")
root.geometry("300x300")

# ---------------------

# CRIANDO O CAMPO PARA QUE A PESSOA POSSA INSERIR A SUA IDADE ✔
label1 = tk.Label(root, text="Insira sua idade")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()


label00 = tk.Label(root, text=" ")
label00.pack()

# ---------------------

# CRIANDO O CAMPO PARA QUE A PESSOA POSSA INSERIR O SEU PESO CORPORAL ✔
peso = tk.Label(root, text="Insira seu peso: ")
peso.pack()

entry2 = tk.Entry(root)
entry2.pack()


label0 = tk.Label(root, text=" ")
label0.pack()

# ---------------------

# CRIANDO O CAMPO PARA QUE A PESSOA POSSA INSERIR A SUA ALTURA ✔
label3 = tk.Label(root, text="Insira sua altura")
label3.pack()

entry3 = tk.Entry(root)
entry3.pack()


label00 = tk.Label(root, text=" ")
label00.pack()
# ---------------------

# CRIANDO O BOTÃO PARA QUE POSSA CALCULAR ✔
btn1 = tk.Button(root, text="IMC", width= 20, fg="white", bg="#000000", command=imc)
btn1.pack()

# ---------------------

# CAMPO PARA EXIBIR O IMC ✔
result = tk.Label(root, text="Seu IMC: ")
result.pack()

# CAMPO PARA EXIBIR SUA SITUAÇÃO, DE ACORDO COM A OMS ✔
classificacao = tk.Label(root, text="Sua situação: ")
classificacao.pack()

root.mainloop()
