<?php
session_start();

require_once 'database.php';
require_once 'spark.php';

$userLoggedIn = false; //should be logged in to get here but assume nothing
$sparkExists = false;  //check if we have an existing spark in the database
$userIsOwner = false; //the user thats logged in is also the owner of the spark, if so we modify the spark if not we create a new spark

$res = "";

if(isset($_SESSION["user_id"]))
{
    $user_id = $_SESSION["user_id"];
    $userLoggedIn = true;
}

/****** TMP REMOVE ME ********* */
if($userLoggedIn == false)
{
    $userLoggedIn = true;
    $user_id = 11;
}
/****** REMOVE ME ********* */

$code = $_POST['code'];
$overwritemode = $_POST['overwrite']; //either check for overwrite or just overwrite if the filename exists
$spark_id = null;
//$sparkowner_id = null;

if(isset($_POST["filename"]))
{
    $filename = $_POST['filename'];
    $spark_id = Spark::getSparkIdFromFilename($user_id,$filename);
    $sparkExists = ($spark_id != null);
}
else
{
    //cant save without filename
    $res = "nofilename";
    exit("no filename");
}

if($userLoggedIn == false)
{
    //if the user hasnt logged in, then dont allow cloud operations
    //user has not logged in and attempting to save, shouldn't happen
    $res .=  "save_attempted_but_user_not_logged_in";
    exit("user not logged in");    
}

if($sparkExists == true) 
{
    //we know $spark_id is valid
    //see if we have to prompt the user to overwrite an existing filename
    if($overwritemode == "check")
    {
        //$res = "confirm_overwrite|".$spark_id;
        $res = "confirm_overwrite";
    }
    else
    {
        //overwrite has been confirmed
        Spark::updateSpark($spark_id,$filename,$code); //no spark id for spark doesnt exist
        $res .="updated";
    }     
}
else
{
    //spark does not exist for user, create a new one 
    Spark::createSpark($user_id,$filename,"",$code); //todo, "" is description
    $res = "created";
}

echo $res;
http_response_code(200);

?>
