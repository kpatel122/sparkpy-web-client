import sparkpy
from browser import document, bind, window

#<div id='unity_events'> must exist on web page
@bind(document["unity_events"], "InputText")
def eventOccured(ev):
    #method 1 bind pattern
    print("method 1 " + ev.detail)

    #method 2 div value set in pyslib.jslib
    print("method 2 " + document["unity_events"].value)

sparkpy.CreateEnvironment("forest")
sparkpy.ShowInputBox()

def onInput(ev):
    print("method 3 " + str(ev))

window.onInputEvent= onInput


#####pys.html#################
'''
<div id="unity_events"></div>

//one of these for each type of event
      function inputEventHandler(event)
      {

        /* method 3
        create custom dispatch here
        onInputEvent is a function created in the brython script file- see samples/eventhandler.py*/

        //check if the event handler has been created in the script
        if (onInputEvent != null)
        {
          onInputEvent(event);
        }
      }

####Unity: pyslib.jslib#############
  EventTextEntered: function (msg) {

    //method 1 JS custom events
    const event = new CustomEvent('InputText', { detail: UTF8ToString(msg) });
    parent.document.getElementById("unity_events").value = UTF8ToString(msg);

    //method 2 set the value of a <div> in py.html
    parent.document.getElementById("unity_events").dispatchEvent(event);

    //method 3: create a handler function 'inputEventHandler' in pys.html and bind it to a function in brython script
	  parent.inputEventHandler( UTF8ToString(msg) );
  },

'''

