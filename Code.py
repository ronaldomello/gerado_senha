import requests

#desativa a opção de inspecionar o Python interativamente
import os
os.environ['PYTHONINSPECT'] = '0'

from tkinter import *
import random
import string
import pyperclip

def gerar_senha():
    # Obtém o tamanho da senha digitado no campo
    tamanho = int(entry_tamanho.get())
    
    # Gera uma senha aleatória com o tamanho especificado
    caracteres = string.ascii_letters + string.digits + "@#$%&"
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))

    # Atualiza o texto do label com a senha gerada
    label_senha.config(text="Senha: " + senha)
    
    # Copia a senha para a área de transferência
    pyperclip.copy(senha)

def copiar_senha():
    # Obtém a senha atual do label
    senha = label_senha.cget("text").replace("Senha: ", "")
    
    # Copia a senha para a área de transferência
    pyperclip.copy(senha)

# Cria a janela
janela = Tk()
janela.title("Gerador de Senhas")

# Define as opções de estilo para os widgets
estilo = {"bg": "#ECECEC", "fg": "#333333", "font": ("Arial", 12)}

# Cria o campo para o tamanho da senha
label_tamanho = Label(janela, text="Tamanho da senha:", **estilo)
entry_tamanho = Entry(janela, width=5, **estilo)
entry_tamanho.insert(0, "8") # Valor padrão é 8 caracteres

# Cria o botão e o label
botao_gerar = Button(janela, text="Gerar Senha", command=gerar_senha, **estilo)
botao_copiar = Button(janela, text="Copiar Senha", command=copiar_senha, **estilo)
label_senha = Label(janela, text="Senha: ", **estilo)

# Define o ícone da janela
#janela.iconbitmap("lock.ico")

# Posiciona os widgets na janela
label_tamanho.pack(pady=10)
entry_tamanho.pack(pady=10)
label_senha.pack(pady=10)
botao_gerar.pack(side=LEFT, padx=5)
botao_copiar.pack(side=LEFT, padx=5)

# Inicia o loop principal do Tkinter
janela.mainloop()






