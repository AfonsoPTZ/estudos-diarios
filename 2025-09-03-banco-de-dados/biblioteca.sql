-- Criação do banco de dados
CREATE DATABASE Biblioteca;
GO
USE Biblioteca;
GO

-- Tabela de autores
CREATE TABLE Autores (
    AutorID INT PRIMARY KEY IDENTITY,
    Nome VARCHAR(100) NOT NULL
);

-- Tabela de categorias
CREATE TABLE Categorias (
    CategoriaID INT PRIMARY KEY IDENTITY,
    Nome VARCHAR(50) NOT NULL
);

-- Tabela de livros
CREATE TABLE Livros (
    LivroID INT PRIMARY KEY IDENTITY,
    Titulo VARCHAR(150) NOT NULL,
    AutorID INT NOT NULL,
    CategoriaID INT NOT NULL,
    AnoPublicacao INT,
    ISBN VARCHAR(20),
    FOREIGN KEY (AutorID) REFERENCES Autores(AutorID),
    FOREIGN KEY (CategoriaID) REFERENCES Categorias(CategoriaID)
);

-- Tabela de usuários
CREATE TABLE Usuarios (
    UsuarioID INT PRIMARY KEY IDENTITY,
    Nome VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Telefone VARCHAR(20)
);

-- Tabela de empréstimos
CREATE TABLE Emprestimos (
    EmprestimoID INT PRIMARY KEY IDENTITY,
    LivroID INT NOT NULL,
    UsuarioID INT NOT NULL,
    DataEmprestimo DATE NOT NULL,
    DataDevolucao DATE,
    FOREIGN KEY (LivroID) REFERENCES Livros(LivroID),
    FOREIGN KEY (UsuarioID) REFERENCES Usuarios(UsuarioID)
);
