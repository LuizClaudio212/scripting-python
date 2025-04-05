Login Automático no SIGAA

Este é um pequeno projeto feito em Python que automatiza o login no sistema SIGAA do IFAL. A ideia é simples: evitar digitar ID e senha toda vez que for acessar o sistema.

A interface gráfica foi feita com Tkinter, com um visual limpo e agradável, e a automação usa Selenium para interagir com o navegador de forma rápida e eficiente.

Funcionalidades:
Interface gráfica amigável e responsiva

Salvamento local das credenciais (infos.txt)

Login automático via navegador com apenas um clique

Tecnologias usadas:

Python 3

Tkinter (GUI)

Selenium WebDriver

Chrome + ChromeDriver

Como usar:


Clone o repositório:

git clone https://github.com/LuizClaudio212/scripting-python.git

Instale as dependências:

pip install -r requirements.txt

Execute o script:

python main.py

Informe seu ID e senha SIGAA na interface e clique em “Salvar Informações”.

Após isso, clique em “Executar Login” e pronto! O navegador será aberto automaticamente e o login será feito sem você precisar digitar nada.

Observações
Suas credenciais ficam salvas localmente em um arquivo chamado infos.txt.
Elas não são criptografadas, então use este projeto apenas em máquinas pessoais e confiáveis.

O ChromeDriver precisa estar instalado e o caminho correto informado no código. No exemplo, o caminho usado foi:

C:\Windows\chromedriver.exe
Você pode ajustar conforme o local onde o chromedriver.exe estiver no seu sistema.

Requisitos:

Python 3.x

Google Chrome instalado

ChromeDriver compatível com a versão do seu navegador
