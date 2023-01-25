<?php
session_start();

require_once 'database.php';
require_once 'spark.php';

$user_id = 0;

if (isset($_SESSION["user_id"])) {
    $user_id = $_SESSION["user_id"];
    $userLoggedIn = true;
}
else
{
    echo "CL_not_legged_in";
    http_response_code(200);
    exit("Cloud load: Not logged in");

}
/*
else {
    //TMP remove me
    //exit("user not logged in"); //shouldn't happen

    //TMP
    $userLoggedIn = true;
    $user_id = 11;
}
//TMP
$user_id = 11;
*/

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
            exit("get spark: no spark id provided");
        }     
    }break;
    case "deletespark":
    {
        if (isset($_POST["s"])) {
            deleteSpark($_POST["s"]);
        } else {
            exit("spark delete: no spark id provided");
        }
        
    }break;
}

function getUserSparks($user_id)
{
    $sparks = spark::getUserAccountSparks($user_id);
    $dateformat = 'd/m/y';

    //convert the result into a json array
    if ($sparks != null) {
        $results = array();

        foreach ($sparks as $spark) {
            $mysqldate = date( $dateformat, strtotime( $spark['modified'] ) );
            $spark['modified'] =  $mysqldate;
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

function deleteSpark($spark_id)
{
    global $user_id;
    $res = "";
    //verify the logged in user is the owner of the spark
    $owner = Spark::getOwnerIdFromSparkId($spark_id);
    
    if($user_id == $owner)
    {
        Spark::deleteSpark($spark_id);
        $res = "ok";
    }
    else
    {
        $res = "user is not owner of spark";
    }
    
    echo $res;
    http_response_code(200);

}
