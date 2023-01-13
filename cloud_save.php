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
}


if(isset($_POST['sparkid']))
{
    $sparkExists = true;
    $spark_id = $_POST['sparkid'];
}


/* TMP REMOVE THIS */
if($userLoggedIn == false)
{
    $userLoggedIn = true;
    $user_id = 11;
}
/****** REMOVE ME ********* */


$code = $_POST['code'];
$filename = $_POST['filename'];
$overwritemode = $_POST['overwrite']; //either check for overwrite or just overwrite if the filename exists


if($userLoggedIn == false)
{
    //if the user hasnt logged in, then dont allow cloud operations

    //user has not logged in and attempting to save, shouldn't happen
    $res .=  "save_attempted_but_user_not_logged_in";
    exit("user not logged in");    
 
}

if($sparkExists == true)
{
    //get the spark owner id
    $sparkowner_id = Spark::getOwnerIdFromSparkId($spark_id); 
}

if($sparkExists == false) 
{

    //new spark

    

    //check if the user already has the same filename in their account
    $filenameExists = Spark::checkDuplicateName($user_id,$filename);
    
    //see if we have to prompt the user to overwrite an existing filename
    if($overwritemode == "check")
    {
        //the filenmae already exists in the user account and we have to check if the user wants to overwrite    
        if($filenameExists == true)
        {
          //return a confirm overwrite message, this will prompt the 'overwrite existing file?' message on the client
          $res = "confirm_overite";
        }
        else
        {
            //the filename does not exist and the spark does not exist, so we create a new spark
            $id = Spark::createSpark($user_id,$filename,"",$code); //todo, "" is description
            $res .=  "created|".$id;
        }
    }
    else
    {
        //overwrite was confirmed and there was no check to overwrite an existing filename
        if($filenameExists == true)
        {
            //nosparkid->newspark existing filename->confirmed overwrite by user->update spark->sparkid=db sparkid for the filename

            //the file exists, so we overwrite it(update)
            //get id from filename
            $id = Spark::getSparkIdFromFilename($user_id,$filename);
            $res .="updated|".$id;
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
    //the spark exists and owner is the currently logged in user, update the spark
    //TODO check for overwrite ? 

    //todo check for filename change
    //todo make the filename read only for this
    //spark exists and the logged in user is the owner so update the current spark
    
    
    Spark::updateSpark($spark_id,$filename,$code);
    $res .="updated|".$spark_id;
}
else if(($sparkExists == true) && ($sparkowner_id != $user_id))
{
    //the spark exists but is not owned by the current logged in user (might have come from a url for example)
    //so copy it over to the user area by creating a new spark for the logged in user
    
    $filenameExists = Spark::checkDuplicateName($user_id,$filename);
    
    //do we need to check if the filename exists, we need an alert box
    if($overwritemode == "check")
    {   
        //the filename exists
        if($filenameExists == true)
        {
            //send confirm overwrite alert box
            $res = "confirm_overite";
        }
        else
        {
            //the filename does not exist, create a new spark. Essentially copy the spark over to the  
            //logged in user area
            
            $id = Spark::createSpark($user_id,$filename,"",$code); //todo, "" is description
            $res = "created|".$id;
            //$res .=  "\n\nfile does not exist, create new \n\n";
        }
    }
    else
    {
        //overwrite confirmed, so update the spark
        if($filenameExists == true)
        {
            
            Spark::updateSpark($spark_id,$filename,$code);
            $res = "updated|".$spark_id;
        }
    }
}


echo $res;
http_response_code(200);

?>
