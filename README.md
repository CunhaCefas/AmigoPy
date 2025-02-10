AmigoPy
Automação de testes para o aplicativo.

Descrição
Este projeto contém a automação de testes do aplicativo utilizando Selenium com Python e o modelo Page Object Model (POM). Foram criadas diversas páginas de código dentro da pasta tests, organizadas para cobrir diferentes cenários de testes.

Estrutura do Projeto
A pasta tests contém os seguintes arquivos:

Add_carrinho.py – Responsável por adicionar um item ao carrinho. Está integrada com Cadastro.py, ou seja, cada vez que o teste roda, um novo usuário é cadastrado antes de adicionar um produto ao carrinho, finalizar a compra e reordenar.
Add_remove.py – Adiciona um produto ao carrinho e depois o remove. Chama Logvalido.py para continuar o fluxo após o login.
Cadastro.py – Realiza o cadastro de um novo usuário e pode ser chamada por outros testes.
CadastroU.py – Versão do cadastro usada antes da adaptação para POM. Pode ser executada unitariamente.
Logvalido.py – Realiza login válido e é utilizado em testes que necessitam de autenticação.
LogvalidoU.py – Versão do login válido antes da adaptação para POM, também pode ser executada unitariamente.
Lo_invalido.py – Testa um login inválido, garantindo que o sistema lida corretamente com credenciais incorretas.
Ambiente Virtual


O projeto está configurado para rodar dentro de um ambiente virtual chamado Virtual1.



Para criar o ambiente virtual:
python -m venv Virtual1


Ativar o ambiente virtual:
Virtual1\Scripts\activate




