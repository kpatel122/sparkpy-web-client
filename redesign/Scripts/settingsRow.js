
const btn1_ctn = document.getElementsByClassName("toggle1-container")[0];
const toggle = document.getElementsByClassName("toggle")[0];
var themesSelect = document.getElementById("themes-select");
var fontSize = document.getElementById("font-size");
var samplesSelect = document.getElementById("samples");

btn1_ctn.addEventListener("click", () => {
  toggle.classList.toggle("inactive1");

  if (themesSelect.style.display === "none") {
    themesSelect.style.display = "block";
    fontSize.style.display = "block";
    samplesSelect.style.display = "none"
  }
  else {
    themesSelect.style.display = "none";
    fontSize.style.display = "none";
    samplesSelect.style.display = "block"
  }

});

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


 


