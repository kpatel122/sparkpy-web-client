
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
  document.getElementById('loadFileId').click();
}

function getFileFromUser() {

  //const [file] = document.querySelector('input[type=file]').files;
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
/*
  if (document.createEvent) {
      var event = document.createEvent('MouseEvents');
      event.initEvent('click', true, true);
      pom.dispatchEvent(event);
  }
  else {
      pom.click();
  }
  */
}
