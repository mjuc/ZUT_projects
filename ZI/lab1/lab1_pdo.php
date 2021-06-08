<?php
    $dsn= "mysql:host=localhost;dbname=lab";
    $user= "user";
    $passwd= "";

    $pdo= new PDO($dsn, $user, $passwd);
    $qr= $pdo->query("SELECT * FROM test WHERE type='unit'");
    $data= $qr->fetchAll(PDO::FETCH_ASSOC);

    foreach($data as $entry)
    {
        printf("{$entry['name']}");
    }
?>