<?php
$db = new mysqli("localhost","user","","lab");
if ($db->connect_errno)
{
    echo "Failed to connect" . $db->connect_error;
}
$qr = $db->query("SELECT * FROM test WHERE type='unit'");
if(!$qr)
{
    echo "Fail to run query: (" . $mysqli->errno .") " . $mysqli->error;
}
if($row = $qr->fetch_assoc())
{
    echo $row['name'];
}
?>