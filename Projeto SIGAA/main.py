import pyautogui
import os
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox


def salvar_info():
    navegador_nome = inputNavegador_nome.get()
    sigaa_id = inputID_sigaa.get()
    sigaa_senha = inputSenha_sigaa.get()
    if navegador_nome.strip() == "" or sigaa_id.strip() == "" or sigaa_senha.strip() == "":
        messagebox.showerror(title="Error", message="Preencha todos os campos!")
        return

    with open('infos.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(f'{navegador_nome},{sigaa_id},{sigaa_senha}')

    messagebox.showinfo(title="Sucesso", message="informações armazenadas no sistema!")

    



def automacao():
    # Obtenha o caminho absoluto do diretório atual
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho absoluto para a imagem
    image_path = os.path.join(current_dir, 'SENHAIMG.png')

    #pausa de 2.0Sec a cada comando
    pyautogui.PAUSE = 2.0

    #caso arrastar o mouse ao topo esquerdo da tela encerrar o progama
    pyautogui.FAILSAFE = True


   
    #scipt principal
    try: 
        with open('infos.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo.readlines():
                info = linha.split(',')
                if len(info) == "":
                    messagebox.showerror(title="Error", message="Não existe nenhuma informação armazenada no sistema!")
                    return

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Não existe nenhuma informação armazenada no sistema!")
        return
    
    pyautogui.press('win')
    pyautogui.typewrite(info[0])
    pyautogui.press('enter')


    pyautogui.hotkey('ctrl', 'Shift', 'n')
    pyautogui.PAUSE = 1.0
    pyautogui.typewrite('https://sigaa.ifal.edu.br/sigaa/verTelaLogin.do')
    pyautogui.press('enter')

    pyautogui.PAUSE = 1.0
    pyautogui.typewrite(info[1])

    # Aguarda até que a imagem 'senha.png' seja encontrada na tela
    senha_img_localizar = pyautogui.locateOnScreen(image_path)

    if senha_img_localizar:
        # Obtém as coordenadas do centro da imagem encontrada
        x, y = pyautogui.center(senha_img_localizar)
        # Clica nas coordenadas do centro da imagem
        pyautogui.click(x+35, y)

        pyautogui.typewrite(info[2])
        pyautogui.press('enter')
    else:
        print("Imagem 'SENHAIMG.png' não encontrada na tela.")




#interface

windows = Tk()
windows.title("Progama de login no SIGAA entre outros...")
windows.geometry("600x300")

#perguntando sobre navegador
lblNevegador_nome = Label(windows, text="Qual navegador você quer acessar?")
lblNevegador_nome.pack()
inputNavegador_nome = Entry(windows,  bd=2)
inputNavegador_nome.pack()

#perguntando ID DO SIGAA
lblId_sigaa = Label(windows, text="Qual é o seu ID no SIGAA?")
lblId_sigaa.pack()
inputID_sigaa = Entry(windows, bd=2)
inputID_sigaa.pack()

#perguntando senha do sigaa junto de tratamento de imagem

vsenha = StringVar
lblSenha_sigaa = Label(windows, text="Qual é sua senha no SIGAA?")
lblSenha_sigaa.pack()
inputSenha_sigaa = Entry(windows, textvariable=vsenha, show='*')
inputSenha_sigaa.pack()

#botao para salvar as informacoes
btn_salvar_informacoes = Button(windows, text="Salvar informações no sistema", command=salvar_info)
btn_salvar_informacoes.pack()


#botao para executar o scripting automatizado
btn_executar_script = Button(windows, text="Executar scripting de login no SIGAA", command=automacao)
btn_executar_script.pack()


windows.mainloop()