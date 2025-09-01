# Cadastro de Cliente

Este projeto é um sistema simples de cadastro de clientes, desenvolvido em PHP, com autenticação para diferentes tipos de usuários: aluno, professor e responsável.

## Estrutura do Projeto

- **login-app/**
  - `index.php`: Página inicial de login.
  - `process_login.php`: Processa o login dos usuários.
  - `logout.php`: Realiza o logout do usuário.
  - `aluno.php`, `professor.php`, `responsavel.php`: Páginas específicas para cada tipo de usuário.
  - `init_db.php`: Inicializa o banco de dados.
  - **data/**: Contém os arquivos do banco de dados (`app.db`, `database.sqlite`).
  - **lib/**: Bibliotecas auxiliares para autenticação (`auth.php`) e acesso ao banco de dados (`db.php`).

## Como executar

1. Certifique-se de ter o PHP instalado em sua máquina.
2. Inicie um servidor local na pasta `login-app`:
   ```powershell
   cd login-app
   php -S localhost:8080
   ```
3. Acesse `http://localhost:8080` no navegador.

## Funcionalidades

- Login para diferentes tipos de usuários.
- Redirecionamento para páginas específicas conforme o tipo de usuário.
- Banco de dados SQLite para armazenamento dos dados.

## Observações

- O projeto é apenas para fins de estudo.
- Para reinicializar o banco de dados, execute `init_db.php`.

---

Desenvolvido por AfonsoPTZ.
