<?php
require __DIR__ . '/lib/db.php';

$pdo = get_pdo();

// Cria tabela de usuários (email+role únicos) e insere alguns usuários de exemplo
$pdo->exec("
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  password_hash TEXT NOT NULL,
  role TEXT NOT NULL CHECK(role IN ('aluno','professor','responsavel')),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(email, role)
);
");

function seed($pdo, $name, $email, $pass, $role) {
    $hash = password_hash($pass, PASSWORD_DEFAULT);
    $stmt = $pdo->prepare("INSERT OR IGNORE INTO users (name, email, password_hash, role) VALUES (?,?,?,?)");
    $stmt->execute([$name, $email, $hash, $role]);
}

// Usuários de teste (senha: 123456)
seed($pdo, 'Alice Aluna', 'aluno@teste.com', '123456', 'aluno');
seed($pdo, 'Pedro Professor', 'prof@teste.com', '123456', 'professor');
seed($pdo, 'Rita Responsável', 'resp@teste.com', '123456', 'responsavel');

echo "Banco inicializado! Você já pode ir para <a href='index.php'>index.php</a>.";
