<?php
class Spark {

private static int $id;
private static string $name;
private static  $code;

private final function  __construct() 
{
     
}

public static function getSpark($id)
{
    $query= "CALL spark_get_id(?)"; 
    Database::prepare($query);
    Database::getPrepared()->bind_param("i", $id); 
    $res = Database::runPrepared();
    $row = $res[0];

    self::$id = $row["id"];
    self::$name = $row["name"];
    self::$code = $row["code"];
}

public static function getCode()
{
    return self::$code;
}

public static function saveCode($id,$name,$code)
{
    $query= "CALL spark_save_code(?,?,?)"; 
    Database::prepare($query);
    Database::getPrepared()->bind_param("iss", $id,$name,$code); 
    Database::execPrepared();

}

public static function print()
{
    echo"<BR> id ".self::$id;
    echo"<BR> name ".self::$name;
    echo"<BR> code ".self::$code;
}



}