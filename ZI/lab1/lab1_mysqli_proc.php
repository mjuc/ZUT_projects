<?php
$db = mysqli_connect("localhost","user","","lab");
$qr = mysqli_query($db,"SELECT * FROM test WHERE type='unit'");
$exec = mysqli_fetch_assoc($qr);

echo $exec['_msq'];
?>