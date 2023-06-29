<?php
include("config.php");
session_start();
$sql = "SELECT * FROM MeineTabelle;";
$result = mysqli_query($db,$sql);

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // POST-Daten erfassen
    $postData = file_get_contents('php://input');

    // Daten in eine Datei oder Datenbank speichern
    //file_put_contents('datei.txt', $postData . PHP_EOL, FILE_APPEND);
    if (isset($_POST["sekunden"]) && isset($_POST["klasse"])) {
        // POST-Daten extrahieren
        $sekunden = $_POST["sekunden"];
        $klasse = $_POST["klasse"];

        // INSERT-Befehl erstellen und ausführen
        $sql = "INSERT INTO MeineTabelle (sekunden, klasse) VALUES ('$sekunden', '$klasse')";
        if (mysqli_query($db, $sql)) {
            echo "Datensatz erfolgreich eingefügt.";
        } else {
            echo "Fehler beim Einfügen des Datensatzes: " . mysqli_error($db);
        }
    } else {
        echo "Nicht alle erforderlichen POST-Daten wurden übermittelt.";
    }
}
?>
<div class="content">
    <div style="height: 100%; overflow: auto;">
        <table class="tabellendarstellung">
            <tr>
                <th class="tblue">ID</th>
                <th class="tblue">Datum und Uhrzeit</th>
                <th class="tblue">Sekunden</th>
                <th class="tblue">Klasse</th>
            </tr>

            <?php while ($row = mysqli_fetch_array($result)) { ?>
                <tr>
                    <td class="tblinhalt"><?php echo $row['id']; ?></td>
                    <td class="tblinhalt"><?php echo $row['datum_zeit']; ?></td>
                    <td class="tblinhalt"><?php echo $row['sekunden']; ?></td>
                    <td class="tblinhalt"><?php echo $row['klasse']; ?></td>
                </tr>
            <?php } ?>

        </table>
    </div>
</div>
<html>

<head>
    <title>Auswählen</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="../../index.css">
</head>

<body>
<h1>Here is our Website guys</h1>
<p>A lot of fun in programming<p>
</body>

<script>
    document.getElementById('auswehlenWeiter').addEventListener('click', function () {
        f2();
        window.location.href = 'unterschrift.html';
    })
    document.getElementById('Abbruch').addEventListener('click', function () {
        window.location.href = '../secondPage.html';
    })

    $('#result').html("<br />$('form').serialize():<br />"+ $('form').serialize()+"<br /><br />$('form').serializeArray():<br />" + JSON.stringify($('form').serializeArray()))
</script>

</html>
