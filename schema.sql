DROP TABLE IF EXISTS donne;

CREATE TABLE donne (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age int,
    sex VARCHAR(30),
    tdt VARCHAR(20),
    par int,
    cholesterol int,
    gai int,
    ecg VARCHAR(30),
    fmax int,
    angine VARCHAR(30),
    depres int,
    pente VARCHAR(30)

);