<?php
session_start();

require_once 'php_scripts/database.php';
require_once 'php_scripts/spark.php';

$user_name = NULL;

if(isset($_SESSION["user_id"]))
{
  $pic = $_SESSION["pic"];
  $user_name = "<img src='$pic' width='25px' height='25px' referrerpolicy='no-referrer'>";
}
else
{
  //$user_name = "Login";
  $user_name = "<div   class=\"g_id_signin\" data-type=\"standard\" data-size=\"small\" data-theme=\"outline\"
                  data-text=\"sign_in_with\" data-shape=\"rectangular\" data-logo_alignment=\"left\">
                  </div>";
}

$code = "NOT SET";
if(isset($_GET['s']))
{
  $id = $_GET['s'];
  Spark::getSpark($id);
  $code = Spark::getCode();
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

  

  <script type="text/python3" id="tests_editor">

  from browser import document, window, bind
  import brython.tests.editor as editor
         
  def run(ev):
    document['console'].value = ''
    editor.run(editor.editor.getValue())
    
  document['run'].bind('click', run)


  editor.reset()
  

  #samples loader
  #smp = document['samples']

  #document.forms['SamplesForm'].reset() #firefox ingnores selected attribute

  #def selectSample(ev):
  #  filename = smp.value  

  #  if(filename == ''):
  #    return

  #  fake_qs = '?foo=%s' #%time.time()
  #  code = open(filename +fake_qs).read()
  #  editor.editor.setValue(code)
  #smp.bind("change", selectSample)
    

  #editor.editor.setValue(code)

  

 
 

  </script>
  <script src="brython/ace/ace.js" type="text/javascript" charset="utf-8"></script>
  <script src="brython/ace/ext-language_tools.js" type="text/javascript" charset="utf-8"></script>

 
<body onload="brython({debug:1})">
 

<div id="g_id_onload" data-client_id="866465079568-odepv40d3gf059misj6c2gropii7bca2.apps.googleusercontent.com"
        data-login_uri="http://localhost/login_res.php" data-auto_prompt="false">
    </div>
  <!-- <button type="button" onclick="saveCode()">save</button> !-->
  <!-- NAVBAR START !-->
  <nav class="navbar">
    <div class="logo-title""><a href="/"> <img src="Images/logo.png" width="30%" height="30%"></a></div>
    <a href="#" class="navmenu-hamburger" onclick="navMenuClick();"> <!-- navMenuClick() defined in sparkpy.js-->
      <span class="bar"></span>
      <span class="bar"></span>
      <span class="bar"></span>
    </a>
    <div class="navbar-links sparkpy-fonts" id="navbar-links-id">
      <ul>
        <!-- <li><a href="pys.html">Home</a></li>!-->
        <li><a href="Docs\_build\html\index.html">Start Here</a></li>
        <li><a href="about.html">About</a></li> 
        <li><a href="login.html"><?php echo $user_name; ?></a></li>
      </ul>
    </div>
  </nav>
  <!-- NAVBAR END-->

  <!-- MAIN GRID START-->
  <div class="grid-container" id="container">

      <!-- MENU CONTAINER START-->
      <div class="grid-item grid-item-settings">

          <!--START MAIN MENU GRID !-->
          <div class="grid-parent-menu">
              <!-- play icon !-->
              <div class="grid-cell-menu-play" title="Run Code" id="run" onclick="unityRestScene()">
                  <button class="play-icon"  aria-label="run" >
                   </button><!--unityRestScene() defined in pys.html-->
                  <span style="margin-top:10px;  margin-right:0px;" class="run-text">Run</span>
              </div>
              <!-- filename input box !-->
              <div class="grid-cell-menu-filename" title="filename">
                  <input class="filename-box" value="untitled.py">
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
                  <input type="file" accept=".py" onchange="getFileFromUser()" id="loadFileId"
                      style="display: none;" /><!-- hide this field because of its default looks, linked by loadFile() !-->
              </div>

              <!--local save !-->
              <div class="grid-cell-menu-local-save" title="Save to PC">
                  <button class="save-icon" id="save" aria-label="save" onclick="saveFile()"></button>
                  <!--saveFile() defined in sparkpy.js-->
              </div>

              <!--cloud load !-->
              
              <!--cloud load !-->
			        <div class="grid-cell-menu-cloud-load" title="Load from user account" id="cloud-load"  >
				          <button class="cloud-load-icon" aria-label="save" onclick="cloudLoad()"></button> <!--saveFile() defined in sparkpy.js-->
			        </div>

              <!--cloud save !-->
              <div class="grid-cell-menu-cloud-save" title="Save to user account">
                  <button class="cloud-save-icon" id="cloud-save" aria-label="save" onclick="saveFile()"></button>
              </div>

              <!--font size !-->
              <div class="grid-cell-menu-font-size">

                  <input title="Editor font size" id="font-size" class="fontsize-box" type="number" min="10" max="20" value="14"
                      onchange="fontSizeChanged()"> <!--fontSizeChanged() defined in settingsRow.js-->
              </div>

              <div class="grid-cell-menu-status1"> <span class="status1"></span></div>
              <div class="grid-cell-menu-status2"> </div>

              <!-- login form !-->
              <div class="login_form sparkpy-fonts" id="loginButton" >
                  <h3 style="text-align:center;">Sign in to use <br>cloud features</h3>
                
                  <div   class="g_id_signin" data-type="standard" data-size="large" data-theme="outline"
                  data-text="sign_in_with" data-shape="rectangular" data-logo_alignment="left">
                  </div>

                  <button class="login_form_cancel_btn" onClick="closeLogin();" >Cancel</button>
              </div>
              <!-- login form end !-->

          </div>
          <!--END MAIN MENU GRID !-->

      </div>
      <!-- MENU CONTAINER END-->



      <!-- ACE EDITOR START-->
      <div class="grid-item grid-item-code-editor" style="border: var(--border_size_editor) var(--border_colour_editor) solid ;" >
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
   
 
    
  <script>

  const   loginForm = document.getElementById('loginButton');
  const cloudLoadIcon = document.getElementById('cloud-load');
  const   enterAnim = "anim_login_enter";
  const   exitAnim = "anim_login_exit";
  

  function cloudLoad()
  {
    openLogin();
  }

  function closeLogin()
  {
    loginForm.classList.remove(exitAnim);
    loginForm.classList.remove(enterAnim);
    
    window.setTimeout(function() {
      loginForm.classList.add(exitAnim);
    }, 50);

    window.setTimeout(function() {
      loginForm.style.display = "none";
    }, 1000);
     
  }
          
  function openLogin()
  {
             
    
    loginForm.classList.remove(exitAnim);
    loginForm.classList.remove(enterAnim);
    window.setTimeout(function() {
      loginForm.style.display = "block";
      loginForm.classList.add(enterAnim);
    }, 50);
      
    let rect = cloudLoadIcon.getBoundingClientRect();  
     
    loginForm.style.marginLeft = rect.left+ "px";
    loginForm.style.marginTop = (rect.bottom-rect.top) +3  +"px";
                  
  }
      
            
  </script>

    <!-- bridge div for linking unity application events with website e.g. collisions, input: Assets/pyslib  !-->
    <div id="unity_events"></div>

    <!--this div is a bridge unity uses this div to set return values- unity project: Assets/pyslib-->
    <div id="unity_return_values"></div>

    <div id="reset_id"></div>

 

    <script type="text/python3">
    from browser import document,window,bind,aio
    import sparkpy
    
    
    @bind(window, "message")
    def ready(ev):
      #unity instance variable (window.unint) is now valid
      sparkpy.SetUnityInstance(window.unint)
    
    </script>

    <!-- Need to merge with main grid-->
    
    <td>Brython version: <span id="version"></span></td>
    
    <!--sparkpy-->
    <script src="Scripts/sparkpy.js"></script>

    <script>
      const resetEvent = new CustomEvent('resetScene'); //only make this once
      function unityRestScene() 
      {
         
        //reset the scene. Call the reset scene method in sparkpy via binding to this event
        document.getElementById("reset_id").dispatchEvent(resetEvent); //event is binded in sparkpy.py
        //set focus on unity
        document.getElementById("unityiframe").focus();
      }

      //one of these for each type of event
      function inputEventHandler(event) 
      {
        //this function is called from pyslib.js from unity
        //input text is entered
      }

    </script>

<script>
    var editor = ace.edit("editor");
   

  
    
    <?php
    $txt = json_encode($code);
    echo "var out={$txt};";
    ?>
    
    editor.setValue(out);

    function saveCode()
    {
      //"use strict";   
 
      var xmlhttp = new XMLHttpRequest();
      xmlhttp.open("POST", "save_code.php", true);
      xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
      xmlhttp.onreadystatechange = function() {
          if (this.readyState === 4 || this.status === 200){ 
              console.log(this.responseText); // echo from php
          }       
      };

      var editor = ace.edit("editor");

      var code = editor.getValue();
      xmlhttp.send("id=1&code="+code);
       
    }

</script>


  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-W3QCQRGS7F"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-W3QCQRGS7F');
  </script>


</body>

</html>