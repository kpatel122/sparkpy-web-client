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
  $user_name = "Login";
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
  

  <!-- sparkpy -->
  <link rel="stylesheet" href="CSS/sparkpy.css">
  <!--main styling-->
  <link rel="stylesheet" href="CSS/dropdowns.css">
  <!--settings row-->
  <link rel="stylesheet" href="CSS/settingsRow.css">
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
  smp = document['samples']

  document.forms['SamplesForm'].reset() #firefox ingnores selected attribute

  def selectSample(ev):
    filename = smp.value  

    if(filename == ''):
      return

    fake_qs = '?foo=%s' #%time.time()
    code = open(filename +fake_qs).read()
    editor.editor.setValue(code)
    
  code = 'import sparkpy\n\n #create dessert environment\nsparkpy.Environment(\"forest\")\n\n'\
          '#create robot character\nrobot = sparkpy.Character(\"ybot\")\n\n' \
          '#set animation to talk\nrobot.SetAnimation(\"talking1\")\n\n'\
          '#create a speech box\nrobot.Chat(\"Hello World\")'
  #editor.editor.setValue(code)

  smp.bind("change", selectSample)

 
 

  </script>
  <script src="brython/ace/ace.js" type="text/javascript" charset="utf-8"></script>
  <script src="brython/ace/ext-language_tools.js" type="text/javascript" charset="utf-8"></script>

<body onload="brython({debug:1})">
  <button type="button" onclick="saveCode()">save</button>
  <!-- NAVBAR START !-->
  <nav class="navbar">
    <div class="logo-title"><a href="/"> <img src="Images/logo.png" width="70%" height="70%"></a></div>
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

    <div class="grid-item grid-item-settings">

      <!-- EMBEDDED SETTINGS GRIP START -->
      <div class="settings-grid">

        <div class="settings-play-icon" title="Run">
          <button class="play-icon" id="run" aria-label="run" onclick="unityRestScene()"></button> <!--unityRestScene() defined in pys.html-->
          <!--play button-->
        </div>
        <div class="settings-settings-icon" title="Settings">

          <div class="toggle-container" id="settings-toggle-container" onclick="toggleSettings()"> <!--toggleSettings() defined in settingsRow.js-->
            <span class="toggle" id="toggle-switch"></span>
          </div>

        </div>
        <div class="settings-themes-dropdown">
          <!--themes dropdown-->
          <div id="themes-select" class="theme-select" style="display:none;" title="Editor theme">
            <select id="themes" style="max-width:min-content" onchange="themeSelect();">  <!--themeSelect() defined in themes.js-->
              <optgroup id="group-light" label="Light"></optgroup>
              <optgroup id="group-dark" label="Dark"></optgroup>
            </select>
          </div>
          <!--samples dropdown-->
          <div class="theme-select" title="Samples">
            <form name="SamplesForm" method="POST">
              <select name="samples" id="samples" style="max-width:min-content;display:block">
                <optgroup label="Basic">
                  <option disabled value="" selected>Samples</option>
                  <option value="Samples/1-CreateEnvironment.py">1-Create Environment</option>
                  <option value="Samples/2-CreateCharacter.py">2-Create Character</option>
                  <option value="Samples/3-SetAnimation.py">3-Set Animation</option>
                  <option value="Samples/4-KeyboardControl.py">4-Keyboard Control</option>
                  <option value="Samples/4-ThirdPersonControl.py">5-Third Person Control</option>
                  <option value="Samples/5-Sounds.py">6-Sounds</option>
                </optgroup>
                <optgroup label="Special Effects">
                  <option value="Samples/7-SimpleEffects.py">1-Simple Effect</option>
                  <option value="Samples/8-AdvancedEffects.py">2-Advanced Effect</option>
                </optgroup>
                <optgroup label="LOGO- Trails">
                  <option value="Samples/10-TrailsBasicLine.py">1-Line</option>
                  <option value="Samples/11-TrailsSquare.py">1-Square</option>
                  <option value="Samples/12-TrailsMuSquare.py">2-Multi Colour Square</option>
                  <option value="Samples/13-TrailsHex.py">3 Hexagon</option>
                </optgroup>
                <optgroup label="Mini Games">
                  <option value="Samples/14-Numbers.py">Number Guessing</option>
                  <option value="Samples/15-Quiz.py">Quiz</option>
                </optgroup>

              </select>
            </form>
          </div>
        </div>
        <!--Load icon/Font size when load is shown fonts select is hidden and vice versa-->
        <div class="settings-load-icon" title="Load">
          
          
          <button class="load-icon" id="load" aria-label="load" onclick="loadFile()"></button> <!--loadFile() defined in sparkpy.js-->
          <input type="file" accept=".py" onchange="getFileFromUser()" id="loadFileId" style="display: none;" /><!-- hide this field because of its default looks, linked by loadFile() !-->
          
          <input title="Font size" id="font-size" class="theme-select" style="width: 40px; padding-top: 2px; display:none;" type="number" min="10" max="20"
            value="14" onchange="fontSizeChanged();"> <!--fontSizeChanged() defined in settingsRow.js-->
            
        </div>
        <!--Save icon-->
        <!-- <div class="settings-save-icon"> !-->
        <div class="settings-save-icon" title="Save"> 
            <button class="save-icon" id="save" aria-label="save" onclick="saveFile()"></button> <!--saveFile() defined in sparkpy.js-->
        </div>
      </div>
      <!-- EMBEDDED SETTINGS GRIP END -->
    </div>

    <!-- ACE editor-->
    <div class="grid-item grid-item-code-editor" style="border: var(--border_size) var(--border_colour) solid ;" >
      <div id="editor"></div> </div>
      <div class=" grid-item grid-item-shell"><textarea id="console" autocomplete="off"></textarea></div>
      <div class="grid-item grid-item-unity" >
        <iframe id="unityiframe" src="index.html" style="width: 100%;height: 100%; border: none; margin-top: 50px; ">Browser not
          compatible.</iframe>
      </div>
    </div>
    <!-- MAIN GRID END -->


    <!-- bridge div for linking unity application events with website e.g. collisions, input: Assets/pyslib  !-->
    <div id="unity_events"></div>

    <!--this div is a bridge unity uses this div to set return values- unity project: Assets/pyslib-->
    <div id="unity_return_values"></div>

    <div id="reset_id"></div>

    <script>

    </script>
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
    <script src="Scripts/settingsRow.js"></script>
    <script src="Scripts/themes.js"></script>
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