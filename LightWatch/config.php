<?php
error_reporting(E_ALL);

// Zum Aufbau der Verbindung zur Datenbank
define('MYSQL_HOST',      'localhost');
define('MYSQL_BENUTZER',  'root');
define('MYSQL_KENNWORT',  'password');
define('MYSQL_DATENBANK', 'mysql');

$db = mysqli_connect(
    "127.0.0.1",
    "root",
    "password",
    "mysql"
);

if (!$db) {
    die('keine Verbindung möglich: ' . mysqli_error());
}
