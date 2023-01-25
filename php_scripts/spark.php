<?php
class Spark {

private static int $id;
private static string $name;
private static $code;
private static $owner_id; 

private final function  __construct() 
{
     
}

public static function getUserAccountSparks($spark_id)
{
    $query= "CALL spark_get_on_user_id(?)"; 
    Database::prepare($query);
    Database::getPrepared()->bind_param("i", $spark_id); 
    $res = Database::runPrepared();
    
    return $res;

}

public static function getSpark($id)
{
    $query= "CALL spark_get_on_id(?)"; 
    Database::prepare($query);
    Database::getPrepared()->bind_param("i", $id); 
    $res = Database::runPrepared();

    if($res !=null)
    {
        return $res[0];
    }
    else
    {
        return null;
    }
}

public static function getCode()
{
    return self::$code;
}
public static function getName()
{
    return self::$name;
}
public static function getOwnerId()
{
    return self::$owner_id;
}

public static function checkDuplicateName($user_id,$filename)
{
    /* return if the filename already exists for the user */
    $query= "CALL spark_get_count_on_id_and_name(?,?)"; 
    Database::prepare($query);
    Database::getPrepared()->bind_param("is", $user_id,$filename); 
    $res = Database::runPrepared();

    return ($res[0]["num"] == 1);
}

//update an exisiting 
public static function updateSpark($spark_id,$name,$code)
{
    $query= "CALL spark_save_code_on_id(?,?,?)"; 
    Database::prepare($query);
    Database::getPrepared()->bind_param("iss", $spark_id,$name,$code); 
    Database::execPrepared();
}

public static function deleteSpark($spark_id)
{
    $query= "CALL spark_delete(?)"; 
    Database::prepare($query);
    Database::getPrepared()->bind_param("i", $spark_id); 
    Database::execPrepared();
}

public static function getSparkIdFromFilename($userid, $filename)
{
    //without calling the entire get spark query

    $query= "CALL spark_get_id_on_filename(?,?)"; 
    Database::prepare($query);
    Database::getPrepared()->bind_param("is", $userid, $filename); 
    $res = Database::runPrepared();

    if($res == null)
    {
        return null;
    }

    return $res[0]["spark_id"];

}


public static function getOwnerIdFromSparkId($spark_id)
{
    //without calling the entire get spark query

    $query= "CALL spark_get_owner_on_spark_id(?)"; 
    Database::prepare($query);
    Database::getPrepared()->bind_param("i", $spark_id); 
    $res = Database::runPrepared();

    if($res == null)
    {
        return null;
    }

    $row = $res[0];

    return $row["owner_id"];

}

//create a new spark
public static function createSpark($owner_id,$name,$description,$code)
{
     
    $query= "CALL spark_create(?,?,?,?)"; 
    Database::prepare($query);
    Database::getPrepared()->bind_param("isss", $owner_id,$name,$description,$code); 
    $res = Database::runPrepared();
    return $res[0]["new_id"];
}

}