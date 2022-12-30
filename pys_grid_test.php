<!--dynamic coloumns  https://codepen.io/lukerazor/pen/GVBMZK !-->
<!DOCTYPE html>
<html>

	<head>
	<script src="https://accounts.google.com/gsi/client" async defer></script>
	<link rel="stylesheet" href="CSS/sparkpy.css">
 
	<style>

	 
	
</style>

	</head>
	<body>
	<div id="g_id_onload" data-client_id="866465079568-odepv40d3gf059misj6c2gropii7bca2.apps.googleusercontent.com"
        data-login_uri="http://localhost/login_res.php" data-auto_prompt="false">
    </div>
		<!--START MAIN MENU GRID !-->
		<div class="grid-parent-menu">
			<!-- play icon !-->
			<div class="grid-cell-menu-play" title="Run Code">
				<button class="play-icon" id="run" aria-label="run"></button><!--unityRestScene() defined in pys.html--> 
				<div style="margin-top:10px;  margin-right:0px;" class="sparkpy-fonts">Run</div>   
			</div>
			<!-- filename input box !-->
			<div class="grid-cell-menu-filename" title="filename"> 
				<input class="filename-box" value="untitled.py">
			</div>

			<!-- theme toggle !-->
			<div class="grid-cell-menu-theme" title="Editor light/dark">
				<div class="toggle-container" id="settings-toggle-container" onclick="toggleSettings()"> <!--toggleSettings() defined in settingsRow.js-->
					<span class="toggle" id="toggle-switch"></span>
				</div>
			</div>

			<!-- local load icon !-->
			<div class="grid-cell-menu-local-load" title="Load from PC"> 
				<button class="load-icon" id="load" aria-label="load" onclick="loadFile()"></button> <!--loadFile() defined in sparkpy.js-->
          		<input type="file" accept=".py" onchange="getFileFromUser()" id="loadFileId" style="display: none;" /><!-- hide this field because of its default looks, linked by loadFile() !-->
			</div>
			
			<!--local save !-->
			<div class="grid-cell-menu-local-save" title="Save to PC">
				<button class="save-icon" id="save" aria-label="save" onclick="saveFile()"></button> <!--saveFile() defined in sparkpy.js-->
				 
			</div>

			

			<!--cloud load !-->
			<div class="grid-cell-menu-cloud-load" title="Load from user account">
				<button class="cloud-load-icon" id="cloud-load" aria-label="save" onclick="cloudLoad()"></button> <!--saveFile() defined in sparkpy.js-->
			</div>

			<!--cloud save !-->
			<div class="grid-cell-menu-cloud-save" title="Save to user account">
				<button class="cloud-save-icon" id="cloud-save" aria-label="save" onclick="cloudSave()"></button> <!--saveFile() defined in sparkpy.js-->
			</div>
			
			
			<!--font size !-->
			<div class="grid-cell-menu-font-size">
				
				<input title="Editor font size" id="font-size"  class="fontsize-box" type="number" min="10" max="20"
            	value="14" onchange="fontSizeChanged();"> <!--fontSizeChanged() defined in settingsRow.js-->
			</div>

			<div class="grid-cell-menu-status1"> <span class="status1"></span></div>
			<div class="grid-cell-menu-status2"> </div>

			<div class="login_form sparkpy-fonts" id="loginButton">

				<h3 style="text-align:center;">Sign in to use <br>cloud features</h3>
				<div  class="g_id_signin" data-type="standard" data-size="large" data-theme="outline"
					  data-text="sign_in_with" data-shape="rectangular" data-logo_alignment="left">
				</div>
				<button class="login_form_cancel_btn" onClick="closeLogin();" >Cancel</button>
			</div>

		</div>
		<!--END MAIN MENU GRID !-->	
		 
		
				
		
	</body>

	<script>

			function closeLogin()
			{
				var loginForm = document.getElementById('loginButton');
				loginForm.style.display = "none";
			}
            
			function cloudLoad()
			{
			 
				var loginForm = document.getElementById('loginButton');
				var cloudLoad = document.getElementById('cloud-load');
				loginForm.style.display = "block";

				var rect = cloudLoad.getBoundingClientRect();
				console.log(rect.top, rect.right, rect.bottom, rect.left);
				 

				loginForm.style.marginLeft = rect.left+ "px";
				loginForm.style.marginTop = rect.bottom+"px";
				 

				//div1.style.marginTop = div2.offsetTop; //set the margin top of the first div = the margin top of the second div
			}

			/*
			
			*/
		</script>
 
</html>


