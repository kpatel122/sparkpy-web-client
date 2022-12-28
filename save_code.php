<?php
session_start();

require_once 'php_scripts/database.php';
require_once 'php_scripts/spark.php';
 
$id = $_POST['id'];
$code = $_POST['code'];

Spark::saveCode($id,"test",$code);

http_response_code(200);

echo "ok" // the return value for pys.php this.responseText

?>
