import sqlite3

con = sqlite3.connect('ITracker.db')
cur = con.cursor()
cur.execute('''PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS Modelo_Aparelho (
    idModelo INTEGER PRIMARY KEY AUTOINCREMENT,
    Marca TEXT,
    Modelo TEXT
);

CREATE TABLE IF NOT EXISTS StatusAparelho (
    idStatus INTEGER PRIMARY KEY,
    Descricao TEXT
);

CREATE TABLE IF NOT EXISTS Cargo (
    ID_Cargo INTEGER PRIMARY KEY AUTOINCREMENT,
    Cargos TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Sala (
    idSala INTEGER PRIMARY KEY,
    NomeSala TEXT,
    EnderecoSala TEXT
);

CREATE TABLE IF NOT EXISTS Usuario (
    idUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome_Usuario TEXT NOT NULL,
    ID_Cargo INTEGER NOT NULL,
    
    FOREIGN KEY (ID_Cargo)
    REFERENCES Cargo(ID_Cargo)
);

CREATE TABLE IF NOT EXISTS Aparelho (
    id_Aparelho INTEGER PRIMARY KEY,
    patrimonio TEXT NOT NULL,
    IDStatus INTEGER NOT NULL,
    idModelo INTEGER NOT NULL,

    FOREIGN KEY (IDStatus)
    REFERENCES StatusAparelho(idStatus),

    FOREIGN KEY (idModelo)
    REFERENCES Modelo_Aparelho(idModelo)
);

CREATE TABLE IF NOT EXISTS Alocacao (
    idAlocacao INTEGER PRIMARY KEY AUTOINCREMENT,
    idUsuario INTEGER,
    id_Aparelho INTEGER,
    idSala INTEGER,
    DataAlocacao DATE,
    DataDevolucao DATE,

    FOREIGN KEY (idUsuario)
    REFERENCES Usuario(idUsuario),

    FOREIGN KEY (id_Aparelho)
    REFERENCES Aparelho(id_Aparelho),

    FOREIGN KEY (idSala)
    REFERENCES Sala(idSala)
);''')
con.commit()
