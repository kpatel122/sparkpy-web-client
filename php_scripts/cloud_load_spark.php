<?php
session_start();

require_once 'database.php';
require_once 'spark.php';

if(isset($_SESSION["user_id"]))
{
    $user_id = $_SESSION["user_id"];
    
}
else
{   
    //TMP remove me
    //exit("user not logged in"); //shouldn't happen
    
    //TMP
    $userLoggedIn = true;
    $user_id = 11;
}

if(isset($_POST["s"]))
{
    $sparkid = $_POST["s"];
}   
else
{
    exit("no spark id provided");
}

$res = "";

$spark = Spark::getSpark($sparkid);

//convert the result into a json object
if($spark !=null)
{
     
    $res = json_encode($spark);
}
else
{
    $res = "noresults";
}


echo $res;
http_response_code(200);

?>