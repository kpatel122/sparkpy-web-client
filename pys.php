<?php
session_start();

require_once 'php_scripts/database.php';
require_once 'php_scripts/spark.php';

$user_name = NULL;
$loggedIn = "";
$userid = -1;

if (isset($_SESSION["user_id"])) {
  $pic = $_SESSION["pic"];
  $user_name = "<img src='$pic' width='25px' height='25px' referrerpolicy='no-referrer'>";
  $loggedIn = "1";
  $userid = $_SESSION["user_id"];
} else {
  //$user_name = "Login";
  $user_name = "<div   class=\"g_id_signin\" data-type=\"standard\" data-size=\"small\" data-theme=\"filled_blue\"
                  data-text=\"signin\" data-shape=\"rectangular\" data-logo_alignment=\"left\">
                  </div>";
  $loggedIn = "0";
}

$code = "";
$filename = "";
$isSparkOwner = false; //is the currently logged in user the owner of the spark
$sparkId = -1;


function userFilesTable()
{
  $html = "";
  $table = "<table id='table-useraccount'>";
  $heading = "<th colspan='2'>File</th><th>Modified</th><th colspan='3'>Actions</th>";

  $row = "<tr>
        <td class ='grid-cell-useraccount-file-icon'><img src='Images/logo-icons/favicon-32x32.png'></td>
        <td class ='grid-cell-useraccount-file-name'>spark1.py</td>
        <td class ='grid-cell-useraccount-file-mod-date'>03/02/23</td>
        <td class ='grid-cell-useraccount-actions-icon'><img src='Images/icons/edit_icon.svg'></td>
        <td class ='grid-cell-useraccount-actions-icon'><img src='Images/icons/delete_icon.svg'></td>
        <td class ='grid-cell-useraccount-actions-icon'><img src='Images/icons/share_icon.svg'></td>
        </tr>";

  $html .= $table;
  $html .= $heading;
  for ($x = 0; $x < 5; $x++) {
    $html .= $row;
  }
  $html .= "</TABLE>";

  return $html;
}


?>

<!DOCTYPE html>
<html>

<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/x-icon" href="Images/logo-icons/favicon.ico">
  <script src="https://accounts.google.com/gsi/client" async defer></script>


  <!-- sparkpy -->
  <link rel="stylesheet" href="CSS/sparkpy.css">
  <link rel="stylesheet" href="CSS/animations.css">

  <!--toggle button-->
  <title>sparkpy</title>

  <!--brython css-->

  <!-- <link rel="stylesheet" href="brython/brython.css"> !-->
  <link rel="stylesheet" href="brython/console.css">

  <!--brython js includes-->
  <script type="text/javascript" src="brython/src/brython_builtins.js"></script>
  <script type="text/javascript" src="brython/src/version_info.js"></script>
  <script type="text/javascript" src="brython/src/python_tokenizer.js"></script>
  <script type="text/javascript" src="brython/src/py_ast.js"></script>
  <script type="text/javascript" src="brython/src/py2js.js"></script>
  <script type="text/javascript" src="brython/src/loaders.js"></script>
  <script type="text/javascript" src="brython/src/py_object.js"></script>
  <script type="text/javascript" src="brython/src/py_type.js"></script>
  <script type="text/javascript" src="brython/src/py_utils.js"></script>
  <script type="text/javascript" src="brython/src/py_sort.js"></script>
  <script type="text/javascript" src="brython/src/py_builtin_functions.js"></script>
  <script type="text/javascript" src="brython/src/py_exceptions.js"></script>
  <script type="text/javascript" src="brython/src/py_range_slice.js"></script>
  <script type="text/javascript" src="brython/src/py_bytes.js"></script>
  <script type="text/javascript" src="brython/src/py_set.js"></script>
  <script type="text/javascript" src="brython/src/js_objects.js"></script>
  <script type="text/javascript" src="brython/src/stdlib_paths.js"></script>
  <script type="text/javascript" src="brython/src/py_import.js"></script>
  <script type="text/javascript" src="brython/src/unicode_data.js"></script>
  <script type="text/javascript" src="brython/src/py_string.js"></script>
  <script type="text/javascript" src="brython/src/py_int.js"></script>
  <script type="text/javascript" src="brython/src/py_long_int.js"></script>
  <script type="text/javascript" src="brython/src/py_float.js"></script>
  <script type="text/javascript" src="brython/src/py_complex.js"></script>
  <script type="text/javascript" src="brython/src/py_dict.js"></script>
  <script type="text/javascript" src="brython/src/py_list.js"></script>
  <script type="text/javascript" src="brython/src/py_generator.js"></script>
  <script type="text/javascript" src="brython/src/py_dom.js"></script>
  <script type="text/javascript" src="brython/src/py_pattern_matching.js"></script>
  <script type="text/javascript" src="brython/src/builtin_modules.js"></script>
  <script type="text/javascript" src="brython/src/async.js"></script>
  <script type="text/javascript" src="brython/src/ast_to_js.js"></script>
  <script type="text/javascript" src="brython/src/symtable.js"></script>

  <script src="brython/assets/header.brython.js"></script>


  <script src="brython/ace/ace.js" type="text/javascript" charset="utf-8"></script>
  <script src="brython/ace/ext-language_tools.js" type="text/javascript" charset="utf-8"></script>




  <script src="brython/ace/ace.js" type="text/javascript" charset="utf-8"></script>
  <script src="brython/ace/ext-language_tools.js" type="text/javascript" charset="utf-8"></script>


<body onload="brython({debug:1})">


  <div id="g_id_onload" data-client_id="866465079568-odepv40d3gf059misj6c2gropii7bca2.apps.googleusercontent.com" data-login_uri="http://localhost/login_res.php" data-auto_prompt="false">
  </div>
  <!-- <button type="button" onclick="saveCode()">save</button> !-->
  <!-- NAVBAR START !-->
  <nav class="navbar">
    <div class="logo-title""><a href=" /"> <img src="Images/logo.png" width="30%" height="30%"></a></div>
    <a href="#" class="navmenu-hamburger" onclick="navMenuClick();"> <!-- navMenuClick() defined in sparkpy.js-->
      <span class="bar"></span>
      <span class="bar"></span>
      <span class="bar"></span>
    </a>
    <div class="navbar-links sparkpy-fonts" id="navbar-links-id">
      <ul>
        <!-- <li><a href="pys.html">Home</a></li>!-->
        <li><a href="#" onclick="samplesClicked();">Samples</a></li>
        <li><a href="Docs\_build\html\index.html">Start Here</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="login.html"><?php echo $user_name; ?></a></li>
      </ul>
    </div>
  </nav>
  <!-- NAVBAR END-->

  <!-- MAIN GRID START-->
  <div class="main-grid-container" id="container">

    <!-- MENU CONTAINER START-->
    <div class="grid-item grid-item-settings">

      <!--START MAIN MENU GRID !-->
      <div class="grid-parent-menu">
        <!-- play icon !-->
        <div class="grid-cell-menu-play" title="Run Code" id="run" onclick="unityRestScene()">
          <button class="play-icon" aria-label="run" id="play-icon-id">
          </button><!--unityRestScene() defined in pys.html-->
          <span style="margin-top:10px;  margin-right:0px;" id="play-text-id" class="run-text">Run</span>
        </div>
        <!-- filename input box !-->
        <div class="grid-cell-menu-filename" title="filename">
          <input class="filename-box" value="untitled.py" id="filename-id">
        </div>

        <!-- theme light/dark toggle !-->
        <div class="grid-cell-menu-theme" title="Editor light/dark">
          <div class="toggle-container" id="settings-toggle-container" onclick="toggleEditorTheme()">
            <!--toggleSettings() defined in settingsRow.js-->
            <span class="toggle" id="toggle-switch"></span>
          </div>
        </div>

        <!-- local load icon !-->
        <div class="grid-cell-menu-local-load" title="Load from PC">
          <button class="load-icon" id="load" aria-label="load" onclick="loadFile()"></button>
          <!--loadFile() defined in sparkpy.js-->
          <input type="file" accept=".py" onchange="getFileFromUser()" id="loadFileId" style="display: none;" /><!-- hide this field because of its default looks, linked by loadFile() !-->
        </div>

        <!--local save !-->
        <div class="grid-cell-menu-local-save" title="Save to PC">
          <button class="save-icon" id="save" aria-label="save" onclick="saveFile()"></button>
          <!--saveFile() defined in sparkpy.js-->
        </div>

        <!--cloud load !-->

        <!--cloud load !-->
        <div class="grid-cell-menu-cloud-load" title="Load from user account" id="cloud-load">
          <button class="cloud-load-icon" aria-label="save" onclick="cloudLoad()"></button> <!--saveFile() defined in sparkpy.js-->
        </div>

        <!--cloud save !-->
        <div class="grid-cell-menu-cloud-save" title="Save to user account">
          <button class="cloud-save-icon" id="cloud-save" aria-label="save" onclick="cloudSave()"></button>
        </div>

        <!--font size !-->
        <div class="grid-cell-menu-font-size">

          <input title="Editor font size" id="font-size" class="fontsize-box" type="number" min="10" max="20" value="14" onchange="fontSizeChanged()"> <!--fontSizeChanged() defined in settingsRow.js-->
        </div>

        <div class="grid-cell-menu-status1"> <span class="status1"></span></div>
        <div class="grid-cell-menu-status2"> </div>

        <!-- login form !-->
        <div class="login_form sparkpy-fonts" id="loginButton">
          <h3 style="text-align:center;">Sign in to use <br>cloud features</h3>

          <div class="g_id_signin" data-type="standard" data-size="large" data-theme="filled_black" data-text="sign_in_with" data-shape="rectangular" data-logo_alignment="left">
          </div>

          <button class="login_form_cancel_btn" onClick="closeLogin();">Cancel</button>
        </div>
        <!-- login form end !-->

      </div>
      <!-- MENU CONTAINER END-->

    </div>
    <!-- MENU CONTAINER END-->



    <!-- ACE EDITOR START-->
    <div class="grid-item grid-item-code-editor" style="border: var(--border_size_editor) var(--border_colour_editor) solid ;">
      <div id="editor"></div>
    </div>
    <!-- ACE EDITOR END-->

    <!-- CONSOLE START-->
    <div class=" grid-item grid-item-shell">
      <textarea id="console" autocomplete="off"></textarea>
    </div>
    <!-- CONSOLE END-->

    <!-- GRAPHICS START-->
    <div class="grid-item-unity">
      <iframe id="unityiframe" src="index.html" style="width: 100%; height: 100%; border: none; margin-top:10px; ">Browser not
        compatible.</iframe>
    </div>
    <!-- GRAPHICS END-->
  </div>
  <!-- MAIN GRID END -->

  <!-- SAMPLES START !-->
  <div class="samples_container center_element sparkpy-fonts" id="samples_container">
    <h3 style="text-align:center;">Samples</h3>
    <div class="grid-samples-parent">

      <div class="grid-samples-div1 samples_category_basic" onclick="openSample('CreateEnvironment.py')">
        <video muted="muted" onmouseover="this.play()" onmouseout="this.pause();" loop class="samples_video">
          <source src="Vids/environment.mp4" type="video/mp4">
          </source>
        </video>
        <div class="samples_description">
          1.Create Environment
        </div>
      </div>

      <div class="grid-samples-div2 samples_category_basic" onclick="openSample('CreateCharacter.py')">
        <video muted="muted" onmouseover="this.play()" onmouseout="this.pause();" loop class="samples_video">
          <source src="Vids/character.mp4" type="video/mp4">
          </source>
        </video>
        <div class="samples_description ">
          2.Create Character
        </div>
      </div>
      <div class="grid-samples-div3 samples_category_basic" onclick="openSample('SetAnimation.py')">
        <video muted="muted" onmouseover="this.play()" onmouseout="this.pause();" loop class="samples_video">
          <source src="Vids/set_animation.mp4" type="video/mp4">
          </source>
        </video>
        <div class="samples_description">
          3.Set Animation
        </div>
      </div>
      <div class="grid-samples-div4 samples_category_basic" onclick="openSample('KeyboardControl.py')">
        <video muted="muted" onmouseover="this.play()" onmouseout="this.pause();" loop class="samples_video">
          <source src="Vids/keyboard_control.mp4" type="video/mp4">
          </source>
        </video>
        <div class="samples_description">
          4.Keyboard Control
        </div>
      </div>
      <div class="grid-samples-div5 samples_category_basic" onclick="openSample('ThirdPersonControl.py')">
        <video muted="muted" onmouseover="this.play()" onmouseout="this.pause();" loop class="samples_video">
          <source src="Vids/third_person.mp4" type="video/mp4">
          </source>
        </video>
        <div class="samples_description">
          5.Third Person Control
        </div>
      </div>
      <div class="grid-samples-div6 samples_category_basic" onclick="openSample('Sounds.py')">
        <video muted="muted" onmouseover="this.play()" onmouseout="this.pause();" loop class="samples_video">
          <source src="Vids/sounds.mp4" type="video/mp4">
          </source>
        </video>
        <div class="samples_description">
          6.Sounds
        </div>
      </div>
      <div class="grid-samples-div7 samples_category_basic" onclick="openSample('Effects.py')">
        <video muted="muted" onmouseover="this.play()" onmouseout="this.pause();" loop class="samples_video">
          <source src="Vids/effects.mp4" type="video/mp4">
          </source>
        </video>
        <div class="samples_description">
          7.Effects
        </div>
      </div>
      <div class="grid-samples-div8 samples_category_basic" onclick="openSample('Primitives.py')">
        <video muted="muted" onmouseover="this.play()" onmouseout="this.pause();" loop class="samples_video">
          <source src="Vids/primitives.mp4" type="video/mp4">
          </source>
        </video>
        <div class="samples_description">
          8.Primitives
        </div>
      </div>
      <div class="grid-samples-div9 samples_category_basic" onclick="openSample('Quiz.py')">
        <video muted="muted" onmouseover="this.play()" onmouseout="this.pause();" loop class="samples_video">
          <source src="Vids/quiz.mp4" type="video/mp4">
          </source>
        </video>
        <div class="samples_description">
          9.Quiz Game
        </div>
      </div>
      <div class="grid-samples-div10 samples_category_basic" onclick="openSample('Numbers.py')">
        <video muted="muted" onmouseover="this.play()" onmouseout="this.pause();" loop class="samples_video">
          <source src="Vids/number_guessing.mp4" type="video/mp4">
          </source>
        </video>
        <div class="samples_description">
          10.Number Guessing Game
        </div>
      </div>
      <div class="grid-samples-div11 samples_category_basic" onclick="openSample('TrailsBasicLine.py')">
        <video muted="muted" onmouseover="this.play()" onmouseout="this.pause();" loop class="samples_video">
          <source src="Vids/trails_line.mp4" type="video/mp4">
          </source>
        </video>
        <div class="samples_description">
          11.Trails-Line
        </div>
      </div>
      <div class="grid-samples-div12 samples_category_basic" onclick="openSample('TrailsSquare.py')">
        <video muted="muted" onmouseover="this.play()" onmouseout="this.pause();" loop class="samples_video">
          <source src="Vids/trails_square.mp4" type="video/mp4">
          </source>
        </video>
        <div class="samples_description">
          12.Trails-Square
        </div>
      </div>
      <div class="grid-samples-div13 samples_category_basic" onclick="openSample('TrailsMuSquare.py')">
        <video muted="muted" onmouseover="this.play()" onmouseout="this.pause();" loop class="samples_video">
          <source src="Vids/multi_coloured_square.mp4" type="video/mp4">
          </source>
        </video>
        <div class="samples_description">
          13.Trails-Multi Colour Square
        </div>
      </div>
      <div class="grid-samples-div14 samples_category_basic" onclick="openSample('TrailsMuSquare.py')">
        <video muted="muted" onmouseover="this.play()" onmouseout="this.pause();" loop class="samples_video">
          <source src="Vids/multi_coloured_square.mp4" type="video/mp4">
          </source>
        </video>
        <div class="samples_description">
          14.Trails-Triangle
        </div>
      </div>
      <div class="grid-samples-div15 samples_category_basic" onclick="openSample('TrailsMuSquare.py')">
        <video muted="muted" onmouseover="this.play()" onmouseout="this.pause();" loop class="samples_video">
          <source src="Vids/multi_coloured_square.mp4" type="video/mp4">
          </source>
        </video>
        <div class="samples_description">
          15.Trails-Triangle
        </div>
      </div>
    </div>

    <button class="login_form_cancel_btn" onClick="samplesClicked();">Close</button>
  </div>
  <!-- SAMPLES END !-->

  <!--USER ACCOUNT START !-->
  <div class="account_container center_element sparkpy-fonts" id="account_container">
    <div class="grid-useraccount-parent">
      <div class="grid-cell-useraccount-heading">My Account</div>
      <div class="grid-cell-useraccount-settings">Settings</div>
      <div class="grid-cell-useraccount-files">
        <?php //echo userFilesTable(); ?>
        
        <table id='table-useraccount'>
          <thead>
            <th colspan='2'>File</th><th>Modified</th><th colspan='3'>Actions</th>
          </thead>
          <tbody id="tbody"> 
          </tbody>
        </table>
          
      </div>
      <div class="grid-cell-useraccount-footer"> <button class="login_form_cancel_btn" onClick="closeAccount();">Close</button> </div>

    </div>
  </div>
  <!--USER ACCOUNT END !-->

  <!-- ALERT BOX START !-->
  <div class="alertbox_container warning center_element sparkpy-fonts" id="alertbox_container_id">
    <div class="grid-alertbox-parent">
      <div class="grid-cell-alertbox-header">
        <span style="width: 100%; margin-left: 0px; padding: 10px;"> <img src="Images/icons/warning_icon.svg"> File Exists </span>
      </div>
      <div id="alert_message_id" class="grid-cell-alertbox-body" style="padding-top: 10px;padding-bottom: 10px;">Overwrite ?</div>
      <div class="grid-cell-alertbox-footer">
        <span>
          <button class="alert_btn" onClick="overwriteSave()">Yes</button>
          <button class="alert_btn" onClick="overwriteClose()">No</button>
        </span>
        <div style="padding-top: 10px;">
          <input type="checkbox" id="overwrite_checkbox" name="overwrite">
          <label for="overwrite">remember my choice</label>
        </div>
      </div>
    </div>
  </div>


  <!-- ALERT BOX END !-->

  <!-- global script variables start !-->

  <?php
  //has a spark been set
  if (isset($_GET['s'])) {
  $sparkId = $_GET['s'];
  Spark::getSpark($sparkId);
  $code = Spark::getCode();
  $filename = Spark::getName();
  //echo "<script>sessionStorage.setItem(\"sparkid\", $sparkId); </script>";
  echo "<script> document.getElementById(\"filename-id\").value = '$filename'; </script>";
  
  }
  ?>

  <script>
    const mainGridContainer = document.getElementById('container');

    var accountOpened = false;

    var loggedIn = (<?php echo $loggedIn ?> == "1");

    const editor = ace.edit("editor");

    //called when the spark id is given in the url
    function setFilename(filename)
    {
      alert("filename is " + filename);
      document.getElementById("filename-id").value = filename; 
    }

    function cloudSave() {

      loggedIn = true; //TMP ONLY
      if (loggedIn == false) {
        openLogin();
      } else {
        let filename = document.getElementById("filename-id").value;
        let code = editor.getValue();
        let promptForOverwrite = true;

        let noPromptFilename = sessionStorage.getItem("overwrite_no_prompt_name");

        if (noPromptFilename == filename) {
          promptForOverwrite = false
        }
        saveCode(promptForOverwrite);

      }
    }

    const alertBoxContainer = document.getElementById("alertbox_container_id");
    const alertMessage = document.getElementById("alert_message_id");

    function confirmOverwrite() {
      //an existing filename exists, display the confirm to overwrite alert box
      let filename = document.getElementById("filename-id").value;

      alertBoxContainer.style.display = "block";
      alertMessage.innerHTML = "Overwrite " + filename + "?"

    }

    function overwriteSave() {
      //when the user confirms they want to overwrite

      //get checkbox value
      let remember_my_choice = document.getElementById("overwrite_checkbox").checked;
      let filename = document.getElementById("filename-id").value;
      let hasSparkid = false;

      //user has selected to remember overwrite choice, store the spark id for the coice in session storage
      if (remember_my_choice == true) {
        sessionStorage.setItem("overwrite_no_prompt_name", filename); //this filename will not prompt an alert box
      }

      //the user has confirmed they want to overwrite so no need for an alertbox
      let alertForOverwrite = false;

      saveCode(alertForOverwrite);
      overwriteClose();

    }

    function overwriteClose() {
      //the user cancels the confirm to overwrite alert box
      alertBoxContainer.style.display = "none";
    }

    function saveCode(checkForOverwrite) 
    {
      //"use strict"; 
      var xmlhttp = new XMLHttpRequest();
      xmlhttp.open("POST", "php_scripts/cloud_save.php", true);
      xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
      xmlhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) 
        {
          console.log("response is ");
          console.log(this.responseText); // echo from php
          let action = this.responseText;
          if (action == "confirm_overwrite") {
            //sessionStorage.setItem("sparkid",sparkid);
            confirmOverwrite();
          }
        }
      };

      //var editor = ace.edit("editor");

      var code = editor.getValue();
      let filename = document.getElementById("filename-id").value;
      let querystring = "code=" + code + "&filename=" + filename;

      if (checkForOverwrite == true) {
        querystring += "&overwrite=check";
        console.log("&overwrite=check");//check with the user for overwrite
      } else {
        querystring += "&overwrite=yes";//overwrite the file without prompting the user
        console.log("&overwrite=yes");
      }

      //console.log("sending query string " + querystring);
      xmlhttp.send(querystring);

    }


    function cloudLoad() {

      //todo check if use is logged in 	
      //openLogin();	
      //if code is not loaded from db by user, load default
      //if(codeLoaded != "1")

      //TMP
      loggedIn = true;

      if (loggedIn == false) {
        openLogin();
      } else if (loggedIn == true && this.accountOpened == false) {
        openAccount();
        this.accountOpened = true;
      }
    }
    const accountContainer = document.getElementById("account_container");
    const accountEnterAnim = "anim_samples_enter";
    const accountExitAnim = "anim_samples_exit";

    function  fillUserSparkTable(sparks)
    {


      let row = "";

      for (var s of sparks) 
      {
        row+=`<tr> \
            <td class ='grid-cell-useraccount-file-icon'><img src='Images/logo-icons/favicon-32x32.png'></td> \
            <td class ='grid-cell-useraccount-file-name' onClick='loadSpark(${s.spark_id})'>${s.name}</td> \
            <td class ='grid-cell-useraccount-file-mod-date'>${s.modified}</td> \
            <td class ='grid-cell-useraccount-actions-icon'><img src='Images/icons/edit_icon.svg'></td> \
            <td class ='grid-cell-useraccount-actions-icon'><img src='Images/icons/delete_icon.svg'></td> \
            <td class ='grid-cell-useraccount-actions-icon'><img src='Images/icons/share_icon.svg'></td> \
            </tr>`;
      }

      var tbody = document.getElementById("tbody");
      tbody.innerHTML = row;
    }

    async function loadSpark(sparkid)
    {
      const myInit = {
      method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded' 
        },
        body: `s=${sparkid}`
      };
      
      const myRequest = new Request('php_scripts/cloud_load_spark.php', myInit);
      
      let response = await fetch(myRequest);
      let data = await response.text();
      console.log("load spark data is " + data);

      if(data!="noresults")
      {
        let spark = JSON.parse(data);
        editor.setValue(spark.code);
        document.getElementById("filename-id").value = spark.name;
      }

      closeAccount();
    }
 
    async function getAccountDetails()
    {
      const myInit = {
      method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded' 
        },
      
      };

      const myRequest = new Request('php_scripts/cloud_load.php', myInit);

      let response = await fetch(myRequest);
      let data = await response.text();
      let sparks = JSON.parse(data);
  
      fillUserSparkTable(sparks);
    }

    async function openAccount() {

      getAccountDetails();

      mainGridContainer.classList.toggle("blur_element");

      accountContainer.classList.remove(accountEnterAnim);
      accountContainer.classList.remove(accountExitAnim);
      window.setTimeout(function() {
        accountContainer.style.display = "block";
        accountContainer.classList.add(accountEnterAnim);

      }, 50);
    }

    function closeAccount() {
      accountContainer.classList.remove(accountEnterAnim);
      accountContainer.classList.remove(accountExitAnim);
      accountContainer.classList.remove(accountEnterAnim);
      accountContainer.classList.remove(accountExitAnim);

      window.setTimeout(function() {
        accountContainer.classList.add(accountExitAnim);
      }, 50);
      window.setTimeout(function() {
        mainGridContainer.classList.toggle("blur_element");
      }, 500);

      window.setTimeout(function() {
        accountContainer.style.display = "none";
      }, 1000);
      this.accountOpened = false;
    }
  </script>

  <!-- Sample JS !-->
  <script>
    //const editor = ace.edit("editor");
    const samplesContainer = document.getElementById('samples_container');
    const samplesEnterAnim = "anim_samples_enter";
    const samplesExitAnim = "anim_samples_exit";


    //const mainGridContainer = document.getElementById('container');
    const blueAmount = "10px";
    let samplesOpened = false;

    async function openSample(name) {

      //open the file
      const response = await fetch('Samples/' + name);
      const data = await response.text();

      //load the code
      //const editor = ace.edit("editor");
      editor.setValue(data);

      //close the samples box
      samplesClicked()
    }

    function openSamples() {

      samplesContainer.classList.remove(samplesEnterAnim);
      samplesContainer.classList.remove(samplesExitAnim);
      window.setTimeout(function() {
        samplesContainer.style.display = "block";
        samplesContainer.classList.add(samplesEnterAnim);
      }, 50);

    }

    function closeSamples() {

      samplesContainer.classList.remove(samplesEnterAnim);
      samplesContainer.classList.remove(samplesExitAnim);

      samplesContainer.classList.remove(samplesEnterAnim);
      samplesContainer.classList.remove(samplesExitAnim);

      window.setTimeout(function() {
        samplesContainer.classList.add(samplesExitAnim);
      }, 50);


      window.setTimeout(function() {
        mainGridContainer.classList.toggle("blur_element");

      }, 500);


      window.setTimeout(function() {
        samplesContainer.style.display = "none";

      }, 1000);

    }


    function samplesClicked() {

      if (samplesOpened == false) {
        mainGridContainer.classList.toggle("blur_element");
        samplesOpened = true;
        openSamples();

      } else {

        samplesOpened = false;
        closeSamples()

      }
    }
  </script>
  <!-- End Samples JS !-->


  <!-- Login JS !-->
  <script>
    const loginForm = document.getElementById('loginButton');
    const cloudLoadIcon = document.getElementById('cloud-load');
    const enterAnim = "anim_login_enter";
    const exitAnim = "anim_login_exit";

    function closeLogin() {
      loginForm.classList.remove(exitAnim);
      loginForm.classList.remove(enterAnim);

      window.setTimeout(function() {
        loginForm.classList.add(exitAnim);
      }, 50);

      window.setTimeout(function() {
        loginForm.style.display = "none";
      }, 1000);

    }

    function openLogin() {

      loginForm.classList.remove(exitAnim);
      loginForm.classList.remove(enterAnim);
      window.setTimeout(function() {
        loginForm.style.display = "block";
        loginForm.classList.add(enterAnim);
      }, 50);

      let rect = cloudLoadIcon.getBoundingClientRect();

      loginForm.style.marginLeft = rect.left + "px";
      loginForm.style.marginTop = (rect.bottom - rect.top) + 3 + "px";

    }
  </script>

  <!-- END login js !-->

  <!-- bridge div for linking unity application events with website e.g. collisions, input: Assets/pyslib  !-->
  <div id="unity_events"></div>

  <!--this div is a bridge unity uses this div to set return values- unity project: Assets/pyslib-->
  <div id="unity_return_values"></div>

  <div id="reset_id"></div>



  <script type="text/python3">
    from browser import document,window,bind
    import brython.tests.editor as editor
    import sparkpy

    def run(ev):
      document['console'].value = ''
      editor.run(editor.editor.getValue())
         
    editor.reset()

    @bind(window, "message")
    def ready(ev):
      #unity instance variable (window.unint) is now valid
      sparkpy.SetUnityInstance(window.unint)
      window.engineLoaded() #if you need to call JS after the engine is loaded.
      document['run'].bind('click', run)

    </script>

  <script>
    //page loaded function
    window.addEventListener("load", pageLoaded, true);
    async function pageLoaded() {
      c = document.getElementById("run");
      c.disabled = true;

      var codeLoaded = "<?php echo isset($_GET['s']); ?>";

      //if code is not loaded from db by user, load default
      if (codeLoaded != "1") {
        const response = await fetch('Samples/Default.py');
        const data = await response.text();

        //load the code
        editor.setValue(data);
      }
    }

    //engine loaded function
    function engineLoaded() {

    }
  </script>

  <!-- Need to merge with main grid-->

  <span style="display: none;" id="version"></span><!--Brython version: need this id for brython to load properly  !-->

  <!--sparkpy-->
  <script src="Scripts/sparkpy.js"></script>

  <script>
    const resetEvent = new CustomEvent('resetScene'); //only make this once
    function unityRestScene() {

      //reset the scene. Call the reset scene method in sparkpy via binding to this event
      document.getElementById("reset_id").dispatchEvent(resetEvent); //event is binded in sparkpy.py
      //set focus on unity
      document.getElementById("unityiframe").focus();
    }

    //one of these for each type of event
    function inputEventHandler(event) {
      //this function is called from pyslib.js from unity
      //input text is entered
    }
  </script>

  <!--Save cloud  code !-->
  <script>
    //var editor = ace.edit("editor");

    <?php
    $txt = json_encode($code);
    echo "var out={$txt};";
    ?>

    editor.setValue(out);
  </script>


  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-W3QCQRGS7F"></script>
  <script>
    window.dataLayer = window.dataLayer || [];

    function gtag() {
      dataLayer.push(arguments);
    }
    gtag('js', new Date());

    gtag('config', 'G-W3QCQRGS7F');
  </script>


</body>

</html>