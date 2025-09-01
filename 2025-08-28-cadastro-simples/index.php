<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>testephp</title>
</head>

  <style>
    body {
      background: linear-gradient(120deg, #f0f4f8 0%, #c2e9fb 100%);
      font-family: 'Segoe UI', Arial, sans-serif;
      margin: 0;
      padding: 0;
    }
    .container {
      max-width: 400px;
      margin: 40px auto;
      background: #fff;
      border-radius: 12px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.08);
      padding: 32px 24px;
    }
    h2 {
      text-align: center;
      color: #2196f3;
    }
    form {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    label {
      font-weight: 500;
      margin-bottom: 4px;
    }
    input, select {
      padding: 8px;
      border-radius: 6px;
      border: 1px solid #bdbdbd;
      font-size: 1rem;
    }
    button {
      background: #2196f3;
      color: #fff;
      border: none;
      border-radius: 6px;
      padding: 10px;
      font-size: 1rem;
      cursor: pointer;
      transition: background 0.2s;
    }
    button:hover {
      background: #1769aa;
    }
    .dados {
      background: #e3f2fd;
      border-radius: 8px;
      padding: 16px;
      margin-bottom: 24px;
      box-shadow: 0 2px 8px rgba(33,150,243,0.08);
    }
  </style>
</head>

<body>


  <div class="container">
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
      $nome = htmlspecialchars($_POST["nome"]);
      $cpf = htmlspecialchars($_POST["cpf"]);
      $numero = htmlspecialchars($_POST["numero"]);
      $email = htmlspecialchars($_POST["email"]);
      $nascimento = htmlspecialchars($_POST["nascimento"]);
      echo "<div class='dados'>";
      echo "<h2>Dados recebidos:</h2>";
      echo "<strong>Nome:</strong> $nome <br>";
      echo "<strong>CPF:</strong> $cpf <br>";
      echo "<strong>Número:</strong> $numero <br>";
      echo "<strong>E-mail:</strong> $email <br>";
      echo "<strong>Data de Nascimento:</strong> $nascimento <br>";
      echo "</div>";
    }
    ?>
    <form method="POST">
      <label for="nome">Nome:</label>
      <input type="text" id="nome" name="nome" required>
      <label for="cpf">CPF:</label>
      <input type="text" id="cpf" name="cpf" required>
      <label for="numero">Número:</label>
      <input type="text" id="numero" name="numero" required>
      <label for="email">E-mail:</label>
      <input type="email" id="email" name="email" required>
      <label for="nascimento">Data de Nascimento:</label>
      <input type="date" id="nascimento" name="nascimento" required>
      <button type="submit">Enviar</button>
    </form>
  </div>

  
</body>
</html>