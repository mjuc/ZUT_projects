<?php
    $dsn= "mysql:host=localhost;dbname=lab";
    $user= "user";
    $passwd= "";

    $pdo= new PDO($dsn, $user, $passwd);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $arr = array("a","b","c","d","e","f","g","h","i","j");
    for($i=0; $i < $arr.sizeof(); $i++)
    {
        $num = rand(0,250);
        try
        {
            $qr= $pdo->exec("INSERT INTO l2 (name,number) ($arr[$i],$num)");
        }
        catch(PDOException $e)
        {
            $pdo->rollBack();
        }
    }

?>