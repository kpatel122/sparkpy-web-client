
//get the settings elements
const toggleContainer = document.getElementById("settings-toggle-container");
const toggle = document.getElementById("toggle-switch");


var themesSelect = document.getElementById("themes-select");
var fontSize = document.getElementById("font-size");
var samplesSelect = document.getElementById("samples");
var loadIcon = document.getElementById("load");
var saveIcon = document.getElementById("save");  

function toggleSettings()
{
  //toggle will switch between samples select, load and save icons and themes, font size

  //toggle the icon switch from red to green or vice versa 
  toggle.classList.toggle("toggle-active");

  //check if themes is hidden, if it is then show it and font size
  if (themesSelect.style.display === "none") {

    //display themes and font size select
    themesSelect.style.display = "block";
    fontSize.style.display = "block";

    //hide samples select, load and save icons
    samplesSelect.style.display = "none";
    loadIcon.style.display = "none";
    saveIcon.style.display = "none";
    
  }
  else {

    //display samples select, load and save icons
    samplesSelect.style.display = "block";
    loadIcon.style.display = "block";
    saveIcon.style.display = "block";

    //hide themes and font select
    themesSelect.style.display = "none";
    fontSize.style.display = "none";
  }

}

function fontSizeChanged() {
  size = parseInt(document.getElementById("font-size").value);
  document.getElementById('editor').style.fontSize = size + "px";
}

function setDefaultSettings()
{
  const DEFAULT_THEME = "ace/theme/chrome";
  const DEFAULT_FONT_SIZE = '14';
  loadThemes("themes", themeData);
  setDefaultLightTheme(DEFAULT_THEME);
  document.getElementById("font-size").value = DEFAULT_FONT_SIZE;
  fontSizeChanged();
}


 


