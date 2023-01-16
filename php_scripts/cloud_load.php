<?php
session_start();

require_once 'database.php';
require_once 'spark.php';

if(isset($_SESSION["user_id"]))
{
    $user_id = $_SESSION["user_id"];
    $userLoggedIn = true;
}
else
{   
    //TMP remove me
    //exit("user not logged in"); //shouldn't happen
    
    //TMP
    $userLoggedIn = true;
    $user_id = 11;
}

$res = "";

$sparks = spark::getUserAccountSparks($user_id);

//convert the result into a json array
if($sparks !=null)
{
    $results=array();

    foreach ($sparks as $spark)
    {
        array_push($results,$spark);
    }
    $res = json_encode($results);
}
else
{
    $res = "noresults";
}

echo $res;
http_response_code(200);