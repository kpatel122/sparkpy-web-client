<?php
session_start();

require_once 'database.php';
require_once 'spark.php';

$user_id = 0;

if (isset($_SESSION["user_id"])) {
    $user_id = $_SESSION["user_id"];
    $userLoggedIn = true;
} else {
    //TMP remove me
    //exit("user not logged in"); //shouldn't happen

    //TMP
    $userLoggedIn = true;
    $user_id = 11;
}

$action  = "";
$res = "";

if (isset($_POST["action"])) {
    $action = $_POST["action"];
}
else
{
    exit("no action provided"); //shouldn't happen

}

switch ($action)
{
    case "getusersparks": //get all sparks from the user
    {
        getUserSparks($user_id);
    }break;
    case "getspark":
    {
        if (isset($_POST["s"])) {
            getSpark($_POST["s"]);
        } else {
            exit("no spark id provided");
        }     
    }break;
}

function getUserSparks($user_id)
{
    $sparks = spark::getUserAccountSparks($user_id);

    //convert the result into a json array
    if ($sparks != null) {
        $results = array();

        foreach ($sparks as $spark) {
            array_push($results, $spark);
        }
        $res = json_encode($results);
    } else {
        $res = "noresults";
    }

    echo $res;
    http_response_code(200);
}

function getSpark($spark_id)
{
    
    $res = "";

    $spark = Spark::getSpark($spark_id);

    //convert the result into a json object
    if ($spark != null) {

        $res = json_encode($spark);
    } else {
        $res = "noresults";
    }

    echo $res;
    http_response_code(200);
}
