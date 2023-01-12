<?php
session_start();

require_once 'php_scripts/database.php';
require_once 'php_scripts/spark.php';

$userLoggedIn = false; //should be logged in to get here but assume nothing
$sparkExists = false;  //check if we have an existing spark in the database
$userIsOwner = false; //the user thats logged in is also the owner of the spark, if so we modify the spark if not we create a new spark

$res = "";

if(isset($_SESSION["user_id"]))
{
    $user_id = $_SESSION["user_id"];
    $userLoggedIn = true;
    //$res .= " userLoggedIn true \n";
}
else
{
    //$res .= " userLoggedIn false \n";
}

if(isset($_POST['sparkid']))
{
    $sparkExists = true;
    $spark_id = $_POST['sparkid'];
    //$res .= " sparkExists true value is '$spark_id' \n";
}
else
{
    //$res .= " sparkExists false \n";
}


/* TMP REMOVE THIS */
if($userLoggedIn == false)
{
    $userLoggedIn = true;
    $user_id = 11;

    //$res .= "TMP setting userLoggedIn true \n";
    //$res .= "TMP setting userid '$user_id' \n";
}
/****** REMOVE ME ********* */


$code = $_POST['code'];
$filename = $_POST['filename'];
$overwritemode = $_POST['overwrite']; //either check for overwrite or just overwrite if the filename exists
 
if($sparkExists == true)
{

    $sparkowner_id = Spark::getOwnerIdFromSparkId($spark_id); 
//    $res .= "\n\n spark owner is:'$sparkowner_id' \n\n";
}

if($userLoggedIn == false)
{
    //user has not logged in and attempting to save, shouldnt happen
    $res .=  "save_attempted_but_user_not_logged_in";
     
//    $res .=  " running 0 "; // the return value for pys.php this.responseText
}
else if($sparkExists == false) //new spark
{

    $filenameExists = Spark::checkDuplicateName($user_id,$filename);
    if($overwritemode == "check")
    {
        
        if($filenameExists == true)
        {
          $res = "confirm_overite";
        }
        else
        {
            Spark::createSpark($user_id,$filename,"",$code); //todo, "" is description
            $res .=  "created_ok";
        }
    }
    else
    {
        if($filenameExists == true)
        {
            //get id from filename
            $id = Spark::getSparkIdFromFilename($filename);
            $res .="updated_ok";
            Spark::updateSpark($id,$filename,$code); //no spark id for spark doesnt exist
        }
        else
        {
            $res .="no_action_shouldnt_happen";
        }
        
    }     
}
else if(($sparkExists == true) && ($sparkowner_id == $user_id))
{
    //todo check for filename change
    //todo make the filename read only for this
    //spark exists and the logged in user is the owner so update the current spark
    
    $res .="updated_ok";
    Spark::updateSpark($spark_id,$filename,$code);
    
}
else if(($sparkExists == true) && ($sparkowner_id != $user_id))
{
    //the spark exists but is not owned by the current logged in user (might have come from a url for example)
    //so copy it over to the user area by creating a new spark for the logged in user
    

    //$res .=  "\n\ **spark exists but the owner is different from the logged in user** \n";

    $filenameExists = Spark::checkDuplicateName($user_id,$filename);
 
    if($overwritemode == "check")
    {
        if($filenameExists == true)
        {
            $res = "confirm_overite";
            //$res .=  "\n\nfile exists for the user- confirm overwrite\n\n";
        }
        else
        {
            $res = "create_spark";
            Spark::createSpark($user_id,$filename,"",$code); //todo, "" is description
            //$res .=  "\n\nfile does not exist, create new \n\n";
        }
    }
    else
    {
        if($filenameExists == true)
        {
            $res = "update_spark";
            Spark::updateSpark($spark_id,$filename,$code);
        }
    }
}


echo $res;
http_response_code(200);

?>
