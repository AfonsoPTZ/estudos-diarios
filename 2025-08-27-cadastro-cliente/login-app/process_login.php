<?php
session_start();
require __DIR__ . '/lib/db.php';

$email = trim($_POST['email'] ?? '');
$password = $_POST['password'] ?? '';
$role = $_POST['role'] ?? '';

if ($email === '' || $password === '' || $role === '') {
    header('Location: index.php?error=missing');
    exit;
}

$pdo = get_pdo();
$stmt = $pdo->prepare("SELECT id, name, email, password_hash, role FROM users WHERE email = ? AND role = ? LIMIT 1");
$stmt->execute([$email, $role]);
$user = $stmt->fetch();

if (!$user || !password_verify($password, $user['password_hash'])) {
    header('Location: index.php?error=invalid');
    exit;
}

$_SESSION['user'] = [
  'id'   => $user['id'],
  'name' => $user['name'],
  'email'=> $user['email'],
  'role' => $user['role'],
];

// Redireciona conforme o papel
switch ($user['role']) {
  case 'aluno':
    header('Location: aluno.php'); break;
  case 'professor':
    header('Location: professor.php'); break;
  case 'responsavel':
    header('Location: responsavel.php'); break;
}
exit;
