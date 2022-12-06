when importing new version of bython

problem
import brython.tests.editor as editor >>>ModuleNotFound brython
solution
put __init__.py in sub directories
https://brython.info/static_doc/en/import.html
****************************************************************

To remove brython.css
from brython.css only variables needed for console.css
--dark-3: #171A15;
--clear-3: #C6C6B7;

#console {
   width:100%;
   height:100%;
   font-size: 12px;
   font-family: Consolas,"Courier new";
   float:none;
   background-color:#171A15;
   color:#C6C6B7;
}
then brython.css can be omitted
***********************************************************************
from console.css only need:
textarea {
    -webkit-box-sizing: border-box; /* Safari/Chrome, other WebKit */
    -moz-box-sizing: border-box;    /* Firefox, other Gecko */
    box-sizing: border-box;         /* Opera/IE 8+ */
}



#editor {
   float:none;
   width:100%;
   height:100%;
}


#console {
   width:100%;
   height:100%;
   font-size: 12px;
   font-family: Consolas,"Courier new";
   float:none;
   background-color:#171A15;
   color:#C6C6B7;
}
********************************************************************************
