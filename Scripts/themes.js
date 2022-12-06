var themeData = [
    ["Chrome"         ],
    ["Clouds"         ],
    ["Crimson Editor" ],
    ["Dawn"           ],
    ["Dreamweaver"    ],
    ["Eclipse"        ],
    ["GitHub"         ],
    ["IPlastic"       ],
    ["Solarized Light"],
    ["TextMate"       ],
    ["Tomorrow"       ],
    ["Xcode"          ],
    ["Kuroir"],
    ["KatzenMilch"],
    ["SQL Server"           ,"sqlserver"               , "light"],
    ["Ambiance"             ,"ambiance"                ,  "dark"],
    ["Chaos"                ,"chaos"                   ,  "dark"],
    ["Clouds Midnight"      ,"clouds_midnight"         ,  "dark"],
    ["Dracula"              ,""                        ,  "dark"],
    ["Cobalt"               ,"cobalt"                  ,  "dark"],
    ["Gruvbox"              ,"gruvbox"                 ,  "dark"],
    ["Green on Black"       ,"gob"                     ,  "dark"],
    ["idle Fingers"         ,"idle_fingers"            ,  "dark"],
    ["krTheme"              ,"kr_theme"                ,  "dark"],
    ["Merbivore"            ,"merbivore"               ,  "dark"],
    ["Merbivore Soft"       ,"merbivore_soft"          ,  "dark"],
    ["Mono Industrial"      ,"mono_industrial"         ,  "dark"],
    ["Monokai"              ,"monokai"                 ,  "dark"],
    ["Nord Dark"            ,"nord_dark"               ,  "dark"],
    ["Pastel on dark"       ,"pastel_on_dark"          ,  "dark"],
    ["Solarized Dark"       ,"solarized_dark"          ,  "dark"],
    ["Terminal"             ,"terminal"                ,  "dark"],
    ["Tomorrow Night"       ,"tomorrow_night"          ,  "dark"],
    ["Tomorrow Night Blue"  ,"tomorrow_night_blue"     ,  "dark"],
    ["Tomorrow Night Bright","tomorrow_night_bright"   ,  "dark"],
    ["Tomorrow Night 80s"   ,"tomorrow_night_eighties" ,  "dark"],
    ["Twilight"             ,"twilight"                ,  "dark"],
    ["Vibrant Ink"          ,"vibrant_ink"             ,  "dark"]
];

function loadThemes(id, options)
{

  themesByName = {};
  
  themes = options.map(function(data) {
    
    
    var name = data[1] || data[0].replace(/ /g, "_").toLowerCase();
    var theme = {
        caption: data[0],
        theme: "ace/theme/" + name,
        isDark: data[2] == "dark",
        name: name
    };
    themesByName[name] = theme;
    return theme;
    
  });
  
  var light = document.getElementById("group-light");
  var dark = document.getElementById("group-dark");
 
  for(var i=0;i<themes.length;i++)
  {
    var opt = themes[i].caption;
    var val = themes[i].theme
     
    var el = document.createElement("option");
    el.textContent = opt;
    el.value = val;

    if(themes[i].isDark == true) 
      dark.appendChild(el);
    else
      light.appendChild(el);
  }
  
}

function setDefaultLightTheme(theme_name)
{
  
  document.getElementById('themes').value = theme_name;
  themeSelect();
}


function themeSelect()
{
  var e = document.getElementById("themes");
  var value = e.options[e.selectedIndex].value;
  var text = e.options[e.selectedIndex].text;
  var editor = ace.edit("editor");
  editor.setTheme(value);
}

function defaultSettings()
{
  var DEFAULT_THEME = "ace/theme/chrome";
  var DEFAULT_FONT_SIZE = '14';

  
  loadThemes("theme-select",themeData);
  setDefaultLightTheme(DEFAULT_THEME);

  document.getElementById('font-size').value = DEFAULT_FONT_SIZE;
  fontSizeChanged();

}

defaultSettings();
 