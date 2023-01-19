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
    //echo "<BR>..Adding user..<BR>";
    $insert_proc = "CALL add_user('$token_id','$name','$email','$iv')";
    Database::runProc($insert_proc);
}

function CheckIfUserExists(string $token_id)
{   
    $user_count = "CALL get_user_id_count('$token_id')";

    $result = Database::runProc($user_count,MYSQLI_NUM);
    $col = $result[0][0];
    
    if($col == 1) 
      return true;

    return false;
}

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
  global $userid, $username, $email,$pic;
  $id_token = $_POST["credential"];

 

  $ini_array = parse_ini_file("../../../sparkpy.ini");
  $CLIENT_ID = $ini_array["google_client"];

  $client = new Google_Client(['client_id' => $CLIENT_ID]);  // Specify the CLIENT_ID of the app that accesses the backend
  $payload = $client->verifyIdToken($id_token);
  
  if ($payload) {
    
    $userid = $payload['sub'];
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
        SetSessionVariables();
        
        $user_exists = CheckIfUserExists($userid);
        if($user_exists == false)
        {
          $iv = EncryptUserData($username,$email);
          AddUser($username,$userid,$email,$iv);
        }

        $res = $pic;
      }
      else
      {
        $res = "invalid_token";
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