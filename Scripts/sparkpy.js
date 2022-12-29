
/* source: https://www.youtube.com/watch?v=At4B7A4GOPg */
const navbarLinks = document.getElementById('navbar-links-id');
const codeEditor = ace.edit("editor");

function navMenuClick()
{
  navbarLinks.classList.toggle('active')
}

//ace editor reference: https://ajaxorg.github.io/ace-api-docs/classes/Ace.Editor.html
function loadFile()
{
  document.getElementById('loadFileId').click(); //this element is hidden so manually click it
}


//https://developer.mozilla.org/en-US/docs/Web/API/FileReader/readAsText
function getFileFromUser() {
  //read the file contents into the webpage editor element
  const [file] = document.getElementById("loadFileId").files;
 
  const reader = new FileReader();

  reader.addEventListener("load", () => {
    var code = reader.result
    codeEditor.setValue(code);
  }, false);

  if (file) {
    reader.readAsText(file);
  }
}

function saveFile()
{
  codeToSave = codeEditor.getValue();
  download("spark.py", codeToSave);
}

function download(filename, text) {
  var pom = document.createElement('a');
  pom.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
  pom.setAttribute('download', filename);
  pom.click();
}

var isLightTheme = true;
const LIGHT_THEME = "ace/theme/chrome";
const DARK_THEME = "ace/theme/chaos";
const DEFAULT_FONT_SIZE = '14';
var editor = ace.edit("editor");

const toggle = document.getElementById("toggle-switch");
const toggleContainer = document.getElementById("settings-toggle-container");

function toggleEditorTheme()
{
  //alert("change theme");

  toggle.classList.toggle("toggle-active");
  toggleContainer.classList.toggle("toggle-container-active"); 

  
  if(isLightTheme == true)
  {
    editor.setTheme(DARK_THEME);
    isLightTheme = false;
  }
  else
  {
    editor.setTheme(LIGHT_THEME);
    isLightTheme = true;
  }
}

function fontSizeChanged() {
  size = parseInt(document.getElementById("font-size").value);
  document.getElementById('editor').style.fontSize = size + "px";
}

function setDefaultSettings()
{
 
  
  document.getElementById("font-size").value = DEFAULT_FONT_SIZE;
  editor.setTheme(LIGHT_THEME);
  fontSizeChanged();
}

setDefaultSettings();

