<?php
class Spark {

private static int $id;
private static string $name;
private static $code;
private static $owner_id; 

private final function  __construct() 
{
     
}

public static function getSpark($id)
{
    $query= "CALL spark_get_on_id(?)"; 
    Database::prepare($query);
    Database::getPrepared()->bind_param("i", $id); 
    $res = Database::runPrepared();
    $row = $res[0];

    self::$id = $row["spark_id"];
    self::$name = $row["name"];
    self::$code = $row["code"];
    self::$owner_id = $row["owner_id"];
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

//update an exisiting 
public static function updateSpark($spark_id,$name,$code)
{
    $query= "CALL spark_save_code(?,?,?)"; 
    Database::prepare($query);
    Database::getPrepared()->bind_param("iss", $spark_id,$name,$code); 
    Database::execPrepared();
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
    Database::execPrepared();

}

public static function print()
{
    echo"<BR> id ".self::$id;
    echo"<BR> name ".self::$name;
    echo"<BR> code ".self::$code;
}



}