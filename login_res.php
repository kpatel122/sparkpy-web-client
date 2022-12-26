<?php
session_start();

require_once 'vendor/autoload.php';
require_once 'php_scripts/crypto.php';
require_once 'php_scripts/database.php';

//all payload data reference: https://developers.google.com/identity/gsi/web/reference/html-reference#server-side
//https://developers.google.com/identity/gsi/web/guides/display-button


function EncryptUserData(string &$name, string &$email)
{
  $ini_array = parse_ini_file("../../sparkpy.ini");
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

function AddUser(string $name, string $token_id, string $email,string $iv)
{
    echo "<BR>..Adding user..<BR>";
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

  $ini_array = parse_ini_file("../../sparkpy.ini");
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
  
  $redirect = "/";
  header('Location: '.$redirect); //go home
  exit();
}

else
{
  $error_msg = "Received invalid login token";
}

?>



<!DOCTYPE html>
<html>
<head>
        <!-- sparkpy -->
        <link rel="stylesheet" href="CSS/sparkpy.css">
        <title>sparkpy</title>
        <link rel="icon" type="image/x-icon" href="Images/logo-icons/favicon.ico">
    </head>

    <body>
        <!-- NAVBAR START !-->
        <nav class="navbar">
            <div class="logo-title"><img src="Images/logo.png" width="70%" height="70%"></div>
            <a href="#" class="toggle-button">
            <span class="bar"></span>
            <span class="bar"></span>
            <span class="bar"></span>
            </a>
            <div class="navbar-links sparkpy-fonts">
            <ul>
                <li><a href="pys.html">Home</a></li>
                <li><a href="Docs\_build\html\index.html">Help</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="login.html">Login</a></li>
            </ul>
            </div>
        </nav>
        <!-- NAVBAR ENDS -->

        <h3><?php echo $error_msg?><h3>

</body>
</html> 