
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
