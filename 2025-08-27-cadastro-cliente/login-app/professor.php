<?php
require __DIR__ . '/lib/auth.php';
require_login('professor');
$u = current_user();
?>
<!doctype html>
<html lang="pt-br"><meta charset="utf-8"><body>
<h2>Painel do Professor</h2>
<p>Bem-vindo, <?=htmlspecialchars($u['name'])?> (<?=htmlspecialchars($u['email'])?>).</p>
<p><a href="logout.php">Sair</a></p>
</body></html>
