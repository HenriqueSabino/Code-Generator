### Descrição de projeto utilizada para gerar os sistemas

O projeto de backend para a biblioteca virtual, a ser desenvolvido em \<linguagem do
projeto\>, utilizando o framework \<framework do projeto\> e o Microsoft SQL Server
como banco de dados, realizará o registro e o gerenciamento de livros e estudantes.
Os dados dos alunos consistirão em detalhes pessoais e histórico de aluguel, enquanto
para os livros incluirão título, autor, ISBN, status etc. Apenas estudantes registrados
podem alugar um livro desde que esteja disponível. Uma vez que o livro é alugado,
seu status no sistema é atualizado para ”Alugado”.
A devolução de cada livro será manualmente confirmada por um bibliotecário ou
administrador, que pode então atualizar o status do livro para ”Disponível”, ”Reser-
vado”ou ”Em manutenção”com base na condição física do livro e nas futuras reservas.
Para gerenciar efetivamente os períodos de empréstimo, os administradores do
sistema podem definir durações de empréstimo padrão. Este período de empréstimo
padrão se aplica a todos os livros, sem exceções.
Os bibliotecários serão registrados no sistema e podem ser gerenciados (CRUD)
por administradores. Um usuário administrador tem amplos direitos de sistema, in-
cluindo gerenciamento de todas as entidades do sistema e alteração de configurações
do sistema. Os bibliotecários têm direitos mais limitados, focados principalmente na
realização de operações CRUD para os dados de livro e aluno.
Os usuários administradores serão inicialmente pré-carregados no banco de dados
com suas informações, que incluem credenciais. Essas credenciais e configurações
gerais do sistema serão preenchidos a partir de um arquivo de configuração externo,
que inclui configurações como a duração padrão do empréstimo do livro.
O sistema diferenciará entre entidades - estudantes e livros - e usuários do sis-
tema - bibliotecários e administradores. Os primeiros podem ser gerenciados mas não
têm direitos de usuário do sistema, enquanto os últimos têm os direitos respectivos
conforme definido em suas funções.
