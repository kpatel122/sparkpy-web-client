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
    $res .= " userLoggedIn true \n";
}
else
{
    $res .= " userLoggedIn false \n";
}

if(isset($_POST['sparkid']))
{
    $sparkExists = true;
    $spark_id = $_POST['sparkid'];
    $res .= " sparkExists true value is '$spark_id' \n";
}
else
{
    $res .= " sparkExists false \n";
}


/* TMP REMOVE THIS */
if($userLoggedIn == false)
{
    $userLoggedIn = true;
    $user_id = 11;

    $res .= "TMP setting userLoggedIn true \n";
    $res .= "TMP setting userid '$user_id' \n";
}
/****** REMOVE ME ********* */


$code = $_POST['code'];
$filename = $_POST['filename'];

$res .= "filename '$filename' \n";

 
if($sparkExists == true)
{

    $sparkowner_id = Spark::getOwnerIdFromSparkId($spark_id); 
    $res .= "\n\n spark owner is:'$sparkowner_id' \n\n";
}





if($userLoggedIn == false)
{
    //user has not logged in and attempting to save, shouldnt happen
     
    $res .=  " running 0 "; // the return value for pys.php this.responseText
}
else if($sparkExists == false) //new spark
{
    //todo check for the same filename
    //new spark
    
    //Spark::createSpark($user_id,$filename,"",$code); //todo, "" is description
    $res .=  " running 1"; 
     
}
else if(($sparkExists == true) && ($sparkowner_id == $user_id))
{
    //spark exists and the logged in user is the owner so update the current spark
    
    //Spark::updateSpark($spark_id,$filename,$code);
    $res .=  " running 2";
}
else if(($sparkExists == true) && ($sparkowner_id != $user_id))
{
    //the spark exists but is not owned by the current logged in user (might have come from a url for example)
    //so copy it over to the user area by creating a new spark for the logged in user
    
    //Spark::createSpark($user_id,$filename,"",$code); //todo, "" is description
    $res .=  " running 3";
}



//updateSpark($id,$name,$code)
//createSpark($owner_id,$name,$description,$code)


//Spark::saveCode($spark_id,"test",$code);

echo $res;
http_response_code(200);

//echo "ok"; // the return value for pys.php this.responseText

?>
