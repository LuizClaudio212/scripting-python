""" 
Versão 1.0

Código criado utilizando a biblioteca tkinter e pyautogui para automatizar o login e senha no site do SIGAA-IFAL.

Nesta primeira versão, foi implementada a interface que pergunta ao usuário o nome do navegador que o mesmo utiliza, ID e senha que utiliza no SIGAA. Tudo é salvo em um arquivo.txt.

Ao apertar no botão "Executar script de login no SIGAA", o script é executado!
"""









import pyautogui
import os
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox


#limpar as caixas do formulário após salvar as info no sistema.
def limpar_formulario():
    inputNavegador_nome.delete(0,END)
    inputID_sigaa.delete(0,END)
    inputSenha_sigaa.delete(0,END)


#salvar as info no sistema e tratar erros.
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
    limpar_formulario()
    


#script de login no SIGAA
def automacao():
    # Obtenha o caminho absoluto do diretório atual
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho absoluto para a imagem
    usuario_path = os.path.join(current_dir, 'procurarcaixadeid.png')

    
    #pausa de 2.0Sec a cada comando
    pyautogui.PAUSE = 2.0

    #caso arrastar o mouse ao topo esquerdo da tela encerrar o progama
    pyautogui.FAILSAFE = True


   
    #scipt principal
    try: 
        #ler as informações armazenadas no sistema e tratar o erro de tentar executar o script sem ter nada armazenado no sistema
        with open('infos.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo.readlines():
                info = linha.split(',')
                if len(info) == 1:
                    messagebox.showerror(title="Error", message="Não existe nenhuma informação armazenada no sistema!")
                    return

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Não existe nenhuma informação armazenada no sistema!")
        return
    
    #Fazer com que o computador tecle "Win" para pesquisar o nome do navegador e pressionar a tecla "Enter"
    pyautogui.press('win')
    pyautogui.typewrite(info[0])
    pyautogui.press('enter')

    #Entrar no navegador em modo anônimo colocar a URL do SIGAA modo classico e pressionar a tecla "Enter"
    pyautogui.hotkey('ctrl', 'Shift', 'n')
    pyautogui.PAUSE = 1.0
    pyautogui.typewrite('https://sigaa.ifal.edu.br/sigaa/verTelaLogin.do')
    pyautogui.press('enter')

    #aumentei um segundo porque alguns computadores sao mais lentos.
    pyautogui.PAUSE = 2.0
    

    # Aguarda até que a imagem 'procurarcaixadeid.png' seja encontrada na tela
    usuario_img_localizar = pyautogui.locateOnScreen(usuario_path)

    if usuario_img_localizar:
        # Obtém as coordenadas do centro da imagem encontrada
        x, y = pyautogui.center(usuario_img_localizar)

        # Clica nas coordenadas do centro da imagem, fiz alterações pois procurei o botao de "Entrar" da pagina e com base nela achei a caixa de ID.
        pyautogui.click(x+50, y-70)

        #escrever o ID
        pyautogui.typewrite(info[1])

        #pressionar "Tab" para acessar a caixa de senha da pagina do SIGAA.
        pyautogui.press('tab')

        #escrever a senha
        pyautogui.typewrite(info[2])

        #pressionar enter
        pyautogui.press('enter')

        messagebox.showinfo(title="Sucesso", message="Scripting foi realizado com êxito!")
    else:
        messagebox.showerror(title="Error", message="Imagem da caixa de ID não localizada")
        return



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

vsenha = StringVar()
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
