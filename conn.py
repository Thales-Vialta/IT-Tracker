import sqlite3

con = sqlite3.connect('ITracker.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS `mydb`.`Cargo` (
  `ID_Cargo` INT NOT NULL AUTO_INCREMENT,
  `Cargos` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`ID_Cargo`))
ENGINE = InnoDB

CREATE TABLE IF NOT EXISTS `mydb`.`Modelo_Aparelho` (
  `idModelo` INT NOT NULL AUTO_INCREMENT,
  `Marca` VARCHAR(45) NULL,
  `Modelo` VARCHAR(45) NULL,
  PRIMARY KEY (`idModelo`))
ENGINE = InnoDB

CREATE TABLE IF NOT EXISTS `mydb`.`Endereco` (
  `ID_End` INT NOT NULL AUTO_INCREMENT,
  `Nome_Instituição` VARCHAR(45) NOT NULL,
  `CEP` VARCHAR(11) NULL,
  `NUM` SMALLINT(4) NOT NULL,
  `Rua` VARCHAR(90) NOT NULL,
  `Bairro` VARCHAR(45) NULL,
  `Cidade` VARCHAR(45) NULL,
  `Estado` CHAR(2) NOT NULL,
  PRIMARY KEY (`ID_End`),
  UNIQUE INDEX `CEP_UNIQUE` (`CEP` ASC) VISIBLE)
ENGINE = InnoDB

CREATE TABLE IF NOT EXISTS `mydb`.`Usuario` (
  `idUsuario` INT NOT NULL AUTO_INCREMENT,
  `Nome_Usuario` VARCHAR(100) NOT NULL,
  `Idade` TINYINT(3) NOT NULL,
  `ID_Cargo` INT NOT NULL,
  `ID_End` INT NULL,
  PRIMARY KEY (`idUsuario`),
  INDEX `ID_Cargo_idx` (`ID_Cargo` ASC) VISIBLE,
  INDEX `ID_End_idx` (`ID_End` ASC) VISIBLE,
  CONSTRAINT `ID_Cargo`
    FOREIGN KEY (`ID_Cargo`)
    REFERENCES `mydb`.`Cargo` (`ID_Cargo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `ID_End`
    FOREIGN KEY (`ID_End`)
    REFERENCES `mydb`.`Endereco` (`ID_End`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB

CREATE TABLE IF NOT EXISTS `mydb`.`Aparelho` (
  `id_Aparelho` INT NOT NULL,
  `patrimonio` VARCHAR(45) NOT NULL,
  `StatusAparelho` TINYINT NOT NULL,
  `idModelo` INT NOT NULL,
  `ID_End` INT NOT NULL,
  PRIMARY KEY (`id_Aparelho`, `StatusAparelho`, `idModelo`),
  INDEX `ID_End_idx` (`ID_End` ASC) VISIBLE,
  INDEX `idModelo_idx` (`idModelo` ASC) VISIBLE,
  CONSTRAINT `ID_End`
    FOREIGN KEY (`ID_End`)
    REFERENCES `mydb`.`Endereco` (`ID_End`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idModelo`
    FOREIGN KEY (`idModelo`)
    REFERENCES `mydb`.`Modelo_Aparelho` (`idModelo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB

CREATE TABLE IF NOT EXISTS `mydb`.`Alocacao` (
  `idAlocacao` INT NOT NULL,
  `idUsuario` INT NULL,
  `id_Aparelho` INT NULL,
  `Status_Alocacao` TINYINT NULL,
  PRIMARY KEY (`idAlocacao`),
  INDEX `IDUsuario_idx` (`idUsuario` ASC) VISIBLE,
  INDEX `id_Aparelho_idx` (`id_Aparelho` ASC) VISIBLE,
  CONSTRAINT `IDUsuario`
    FOREIGN KEY (`idUsuario`)
    REFERENCES `mydb`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `id_Aparelho`
    FOREIGN KEY (`id_Aparelho`)
    REFERENCES `mydb`.`Aparelho` (`id_Aparelho`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB''')
con.commit()
