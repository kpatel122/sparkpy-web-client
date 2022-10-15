import roboarmlib as robotzio
from browser import document,aio,alert,window,bind 


#<div id='unity_events'> must exist on web page
@bind(document["unity_events"], "InputText")
def eventOccured(ev):
    #method 1 bind pattern
    print("method 1 " + ev.detail)
    
    #method 2 div value set in pyslib.jslib
    print("method 2 " + document["unity_events"].value)

     


#event method 3 binded in async def main()
def onInput(ev):
    print("method 3 " + str(ev))

async def main():
    print("start")
    
    #function inputEventHandler( event ) 
    #{

    #/* method 3
    #create custom dispatch function in pys.html
    #onInputEvent is a function created in the brython script file- see samples/eventhandler.py*/
    #if( onInputEvent != null )
    #{
    #  onInputEvent( event );
    #}
         
    #}
    window.onInputEvent= onInput
    
 
    

robotzio.run(main)
