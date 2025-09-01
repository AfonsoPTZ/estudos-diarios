<?php
session_start();
$err = $_GET['error'] ?? '';
$msg = [
  'missing' => 'Preencha e selecione um papel.',
  'invalid' => 'Credenciais inválidas ou usuário não existe.',
  'auth'    => 'Faça login para acessar.',
][$err] ?? '';
?>
<!doctype html>
<html lang="pt-br">
<head>
  <meta charset="utf-8">
  <title>Login — Demo</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>body{font-family:Arial;max-width:420px;margin:40px auto;padding:0 16px}
  .card{border:1px solid #ddd;border-radius:12px;padding:18px}
  .row{margin:10px 0}.err{color:#b00020;margin:8px 0}</style>
</head>
<body>
  <h2>Login</h2>
  <?php if($msg): ?><div class="err"><?=htmlspecialchars($msg)?></div><?php endif; ?>
  <div class="card">
    <form method="post" action="process_login.php">
      <div class="row">
        <label>Email<br>
          <input type="email" name="email" required style="width:100%">
        </label>
      </div>
      <div class="row">
        <label>Senha<br>
          <input type="password" name="password" required style="width:100%">
        </label>
      </div>
      <div class="row">
        Papel:<br>
        <label><input type="radio" name="role" value="aluno"> Aluno</label><br>
        <label><input type="radio" name="role" value="professor"> Professor</label><br>
        <label><input type="radio" name="role" value="responsavel"> Responsável</label>
      </div>
      <div class="row">
        <button type="submit">Entrar</button>
      </div>
    </form>
  </div>
  <p style="margin-top:14px">Dica: use os testes — aluno@teste.com / 123456 (aluno), prof@teste.com / 123456 (professor), resp@teste.com / 123456 (responsável).</p>
</body>
</html>
