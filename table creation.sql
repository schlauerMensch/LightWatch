CREATE TABLE mysql.MeineTabelle (
    id INT AUTO_INCREMENT PRIMARY KEY,
    datum_zeit TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    sekunden FLOAT,
    klasse VARCHAR(50)
);