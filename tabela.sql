/* TrabalhoBDmapeamento: */

CREATE TABLE Acidente (
    dat varchar(12) NOT NULL,
    hora varchar(12) NOT NULL,
    UniqueKey varchar(20) PRIMARY KEY UNIQUE NOT NULL
);

CREATE TABLE Localidade (
    Id_local int UNIQUE,
    Bairro varchar(40),
    ZipCode varchar(8),
    Latitude DECIMAL ,
    Longitude DECIMAL ,
    PRIMARY KEY (Id_local)
);
CREATE TABLE TipoPessoa (
    TipoPessoa_ID int PRIMARY KEY NOT NULL,
    Descricao varchar(20) NOT NULL
);

CREATE TABLE TipoVeiculo (
    TipoVeiculo_ID int PRIMARY KEY UNIQUE NOT NULL,
    descricao varchar(40) NOT NULL
);

CREATE TABLE Fator (
    Fator_ID int PRIMARY KEY UNIQUE NOT NULL,
    descricao varchar(50) NOT NULL
);
CREATE TABLE Acidente_Veiculo (
    TipoVeiculo_ID int,
    Fator_ID int,
    UniqueKey varchar(20),
    PRIMARY KEY (TipoVeiculo_ID, Fator_ID, UniqueKey),
);

CREATE TABLE Acidente_Pessoa (
    UniqueKey varchar(20) NOT NULL,
    TipoPessoa_ID int NOT NULL,
    quantidadeFeridos int NOT NULL,
    quantidadeMortos int NOT NULL,
    PRIMARY KEY (UniqueKey,TipoPessoa_ID)
    
);

CREATE TABLE Acidente_Local (
    UniqueKey varchar(20) NOT NULL,
    Id_local int,
    OnStreet varchar(40),
    OffStreet varchar(40),
    CrossStreet varchar(40),
    PRIMARY KEY (UniqueKey, Id_local)
);
CREATE PROCEDURE InsertIntoAcidente AS INSERT INTO Acidente(dat,hora, UniqueKey) VALUES (?, ?,?);
CREATE PROCEDURE InsertIntoLocalidade AS INSERT INTO Localidade(Id_local ,Bairro, ZipCode, Latitude, Longitude) VALUES (? ,?, ?, ?, ?); 
CREATE PROCEDURE InsertTipoPessoa AS INSERT INTO TipoPessoa(TipoPessoa_ID,Descricao)VALUES (?,?);
CREATE PROCEDURE InsertTipoVeiculo AS INSERT INTO TipoVeiculo(TipoVeiculo_ID,Descricao) VALUES (?, ?); 
CREATE PROCEDURE InsertFator AS INSERT INTO Fator(Fator_ID,Descricao) VALUES (?, ?);
CREATE PROCEDURE InsertAcidenteVeiculo  AS INSERT INTO Acidente_Veiculo(TipoVeiculo_ID, Fator_ID, UniqueKey) VALUES (?, ?, ?);
CREATE PROCEDURE InsertAcidentePessoa AS INSERT INTO Acidente_Pessoa(TipoPessoa_ID, quantidadeFeridos, quantidadeMortos, UniqueKey) VALUES (?, ?, ?, ?);
CREATE PROCEDURE InsertAcidenteLocal AS INSERT INTO Acidente_Local(Id_local, UniqueKey, OnStreet, OffStreet, CrossStreet) VALUES (?, ?, ?, ?, ?);
CREATE PROCEDURE Select AS SELECT * FROM Acidente WHERE UniqueKey = ?;
 
