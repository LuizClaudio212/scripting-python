# Login Automático no SIGAA

Este é um pequeno projeto feito em Python que automatiza o login no sistema SIGAA do IFAL. A ideia é simples: evitar digitar ID e senha toda vez que for acessar o sistema.

A interface gráfica foi feita com Tkinter, com um visual limpo e agradável, e a automação usa Selenium para interagir com o navegador de forma rápida e eficiente.

## Funcionalidades

- Interface gráfica amigável e responsiva  
- Salvamento local das credenciais (infos.txt)  
- Login automático via navegador com apenas um clique  

## Tecnologias usadas

- Python 3  
- Tkinter (GUI)  
- Selenium WebDriver  
- webdriver-manager (para gerenciamento automático do ChromeDriver)  
- Google Chrome  

## Como usar

1. Clone o repositório: git clone https://github.com/LuizClaudio212/scripting-python.git


2. Instale as dependências: pip install -r requirements.txt


3. Execute o script: python main.py


4. Na interface, informe seu ID e senha SIGAA e clique em “Salvar Informações”.

5. Em seguida, clique em “Executar Login”. O navegador será aberto e o login será feito automaticamente.

## Observações

- Suas credenciais são salvas localmente no arquivo `infos.txt`.
- Elas **não são criptografadas**, então use este projeto apenas em computadores pessoais e confiáveis.
- O Chrome precisa estar instalado no sistema. O ChromeDriver será gerenciado automaticamente pelo `webdriver-manager`.
