<?php
session_start();

function is_logged_in(): bool {
    return isset($_SESSION['user']);
}

function require_login(?string $role = null): void {
    if (!is_logged_in() || ($role !== null && $_SESSION['user']['role'] !== $role)) {
        header('Location: index.php?error=auth');
        exit;
    }
}

function current_user(): ?array {
    return $_SESSION['user'] ?? null;
}
