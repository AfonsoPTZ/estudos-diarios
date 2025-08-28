<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>testephp</title>
</head>
<body>

<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $nome = $_POST["nome"];
  $cpf = $_POST["cpf"];
  $numero = $_POST["numero"];
  $email = $_POST["email"];
  $nascimento = $_POST["nascimento"];

  echo "<h2>Dados recebidos:</h2>";
  echo "Nome: $nome <br>";
  echo "CPF: $cpf <br>";
  echo "Número: $numero <br>";
  echo "E-mail: $email <br>";
  echo "Data de Nascimento: $nascimento <br>";
  echo "<br><a href='cadastro.php'>Voltar</a>";
}


?>

<form method="POST">
  Nome: <input type="text" name="nome"><br>
  CPF: <input type="text" name="cpf"><br>
  Número: <input type="text" name="numero"><br>
  E-mail: <input type="email" name="email"><br>
  Data de Nascimento: <input type="date" name="nascimento"><br>
  <button type="submit">Enviar</button>
</form>


</body>
</html>