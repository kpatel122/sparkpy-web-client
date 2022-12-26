<?php
class Database {
  // Properties

    private static $mysqli_conn = NULL;

    private static string $server;
    private static string $user;
    private static string $pw;
    private static string $dbname;

    private static bool $connected = false;
 
    

    private final function  __construct() 
    {
         
    }

    public static function closeConn()
    {
        self::$mysqli_conn->close();
        self::$connected = false;
    }

    public static function runProc($proc, int $mode = MYSQLI_ASSOC, int $result_mode = MYSQLI_STORE_RESULT)
    {
        $mysqli = self::getConn();
        try 
        {
          $result = $mysqli->query($proc,$result_mode);
        }
        catch (Exception $e)
        {
            
        
            echo "runProc error is ".$e->getMessage();
            echo "<BR>";
            self::$closeConn();
            exit();
        }

        if(gettype($result) == "boolean") //$mysqli->query returns a boolean or a dataset: https://www.php.net/manual/en/function.gettype.php
        {
          return $result;
        }
        else
        {
          $array = $result->fetch_all($mode);
          $result->close();
          $mysqli->next_result(); //multi query returned on stored proc
          self::closeConn();
  
          return $array;

        }

    }

    public static function getConn() {
        if(!isset(self::$mysqli_conn)) 
        {
            $ini_array = parse_ini_file("../../sparkpy.ini");


            self::$server=$ini_array["server"];
            self::$user=$ini_array["user"];
            self::$pw=$ini_array["password"];
            self::$dbname=$ini_array["database"];

            try{
                self::$mysqli_conn = new mysqli(self::$server,self::$user,
                                                self::$pw, self::$dbname);
                 
                }
                catch (Exception $e)
                {
            
                  //echo "conn error ".$mysqli->connect_error;
                  echo "connection error is ".$e->getMessage();
                  echo "<BR>";
                  exit();
                }

                self::$connected = true;    
        }
        
        if(self::$connected == false)
        {
            self::$mysqli_conn->connect(self::$server,self::$user,
            self::$pw, self::$dbname);
        }
        
        return self::$mysqli_conn;
    }
  
}

  ?>
