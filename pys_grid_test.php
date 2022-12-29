<!--dynamic coloumns  https://codepen.io/lukerazor/pen/GVBMZK !-->
<!DOCTYPE html>
<html>

	<head>
	<link rel="stylesheet" href="CSS/sparkpy.css">
 
	<style>
	
</style>

	</head>
	<body>
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
				<button class="cloud-load-icon" id="cloud-load" aria-label="save" onclick="saveFile()"></button> <!--saveFile() defined in sparkpy.js-->
			</div>

			<!--cloud save !-->
			<div class="grid-cell-menu-cloud-save" title="Save to user account">
				<button class="cloud-save-icon" id="cloud-save" aria-label="save" onclick="saveFile()"></button> <!--saveFile() defined in sparkpy.js-->
			</div>
			
			<!--font size !-->
			<div class="grid-cell-menu-font-size">
				
				<input title="Editor font size" id="font-size"  class="fontsize-box" type="number" min="10" max="20"
            	value="14" onchange="fontSizeChanged();"> <!--fontSizeChanged() defined in settingsRow.js-->
			</div>

			<div class="grid-cell-menu-status1"> <span class="status1"></span></div>
			<div class="grid-cell-menu-status2"> </div>

		</div>
		<!--END MAIN MENU GRID !-->	

	</body>
 
</html>


