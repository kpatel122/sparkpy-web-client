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
<?php

require_once 'vendor/autoload.php';

$id_token = $_POST["credential"];

 
//all payload data reference: https://developers.google.com/identity/gsi/web/reference/html-reference#server-side
//https://developers.google.com/identity/gsi/web/guides/display-button



$CLIENT_ID = "866465079568-odepv40d3gf059misj6c2gropii7bca2.apps.googleusercontent.com";

$client = new Google_Client(['client_id' => $CLIENT_ID]);  // Specify the CLIENT_ID of the app that accesses the backend
$payload = $client->verifyIdToken($id_token);
if ($payload) {
  $userid = $payload['sub'];
  $username = $payload['name'];
  echo "All is well";
  // If request specified a G Suite domain:
  echo "id is " . $userid;
  echo "name is " . $username;

} else {
  // Invalid ID token
  echo "Invalid token id";
}


?>

</body>
</html> 