<?php
session_start();

require_once '../vendor/autoload.php';
require_once 'crypto.php';
require_once 'database.php';


function EncryptUserData(string &$name, string &$email)
{ 
  $ini_array = parse_ini_file("../../../sparkpy.ini");
  $key= $ini_array["key"];
  $cypher = $ini_array["cypher"];
  $iv = openssl_random_pseudo_bytes(openssl_cipher_iv_length($cypher));

  Crypto::setParams($key, $cypher);

  $e_name = Crypto::encrypt($name,$iv);
  $e_email = Crypto::encrypt($email,$iv);

  $name = $e_name;
  $email = $e_email;
  
  return $iv;

}

//all payload data reference: https://developers.google.com/identity/gsi/web/reference/html-reference#server-side
//https://developers.google.com/identity/gsi/web/guides/display-button

function AddUser(string $name, string $token_id, string $email,string $iv)
{
    $insert_proc = "CALL add_user('$token_id','$name','$email','$iv')";
    Database::runProc($insert_proc);
}

function GetUserIdFromTokenId(string $token_id)
{   
    $user_count = "CALL user_get_id_on_token('$token_id')";

    $result = Database::runProc($user_count,MYSQLI_NUM);
    
    if($result != null)
    {
      return $result[0][0];
    }
    
    return null;
}



function CheckIfUserExists(string $token_id)
{   
    $user_count = "CALL login_user('$token_id')";//"CALL get_user_id_count('$token_id')";

    $result = Database::runProc($user_count,MYSQLI_NUM);

    $col = $result[0][0];
    
    if($col == 1) 
      return true;

    return false;
}

$tokenid=""; //sub from google payload
$userid ="";
$username ="";
$email = "";
$pic="";

$error_msg = "";

function logout()
{
  UnsetSessionVariables();
}

function UnsetSessionVariables()
{
  unset($_SESSION["pic"]);
  unset($_SESSION["user_id"]);

}


function SetSessionVariables()
{
  global $userid, $pic;
  $_SESSION["user_id"] = $userid;
  $_SESSION["pic"] = $pic;
}

function ValidateGoogleToken()
{
  global $tokenid, $username, $email,$pic;
  $credential = $_POST["credential"];

 

  $ini_array = parse_ini_file("../../../sparkpy.ini");
  $CLIENT_ID = $ini_array["google_client"];

  $client = new Google_Client(['client_id' => $CLIENT_ID]);  // Specify the CLIENT_ID of the app that accesses the backend
  $payload = $client->verifyIdToken($credential);
  
  if ($payload) {
    
    $tokenid = $payload['sub'];
    $username = $payload['name'];
    $email = $payload['email'];
    $pic = $payload['picture'];
  }
  else
  {
    return false;
  }

  return true;
}

$res="";

$action = $_POST["action"];

switch ($action)
{
  
  case "login":
    {
      
      $tokencheck = ValidateGoogleToken();

      if($tokencheck == true)
      {
        
        $user_exists = CheckIfUserExists($tokenid);
        if($user_exists == false)
        {
          $iv = EncryptUserData($username,$email);
          AddUser($username,$tokenid,$email,$iv);
        }

        $userid = GetUserIdFromTokenId($tokenid);
        if($userid == null)
        {
          $res = "invalid_token_b1";
        }
        else
        {
          SetSessionVariables();
          $res = $pic;
        }
      }
      else
      {
        $res = "invalid_token_b2";
      }

      echo $res;
      http_response_code(200);
      

    }break;
  case "logout":
    {

      if(isset($_SESSION["user_id"]))
      {
        logout();
        echo "logged_out";
        http_response_code(200);
      }
      else
      {
        $res = "err logging out";
        http_response_code(200); 
        exit("trying to logout without being logged in");  
          
      }
    }break;
  default:
  {
    $res = "unknown action";
    echo $res;
    http_response_code(200);
  }break;
}