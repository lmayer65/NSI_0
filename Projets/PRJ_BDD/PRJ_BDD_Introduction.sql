CREATE TABLE IF NOT EXISTS Agences (
	id_agence INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	dirigeant VARCHAR(30) COLLATE UTF8mb4_UNICODE_CI,
	flotte INT
)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS Voitures(
	id_enseignant INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	id_agence INT NOT NULL,
	constructeur VARCHAR(30) COLLATE UTF8mb4_UNICODE_CI,
	annee INT,
	FOREIGN KEY(id_agence) REFERENCES Agences(id_agence)
)
ENGINE = InnoDB;