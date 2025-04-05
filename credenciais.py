import os

ARQUIVO_CREDENCIAIS = "infos.txt"

def salvar_credenciais(usuario, senha):
    with open(ARQUIVO_CREDENCIAIS, 'w', encoding='utf-8') as arquivo:
        arquivo.write(f"{usuario},{senha}")

def carregar_credenciais():
    try:
        with open(ARQUIVO_CREDENCIAIS, 'r', encoding='utf-8') as arquivo:
            linha = arquivo.readline().strip()
            if not linha:
                raise FileNotFoundError
            return linha.split(',')
    except FileNotFoundError:
        return None