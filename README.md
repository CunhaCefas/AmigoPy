# AmigoPy
Pages para automação do app.


 Foram criadas 6 paginas de codigo dentro da pasta tests, Add_carrinho, Add_remove, cadastro, CadastroU, Logvalido e LogvalidoU.
 O "Add_carrinho" está integrada com "Cadastro" ou seja ela chama essa pagina dentro do codigo, cada vez que é rodada ela cria um novo cadastro e segue o fluxo de acidionar ao carrinho, finalizar a compra e reordenar.
 O mesmo acontece para add_ remov_prod, ele chama o log_valido para continuar o fluxo de adicionar o produto ao carrinho e remover.
 os LogvalidoU e CadastroU são codigos antes da adaptação de POM para ser chamado nos outros, então da pra rodar eles unitariamente, bem como o lo_inválido.

Tudo está dentro de um ambiente virtual "Virtual1" onde foi instalado o selelium.
 
 
