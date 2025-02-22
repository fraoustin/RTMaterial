# RedmineThemeMaterrial

RTMaterial is a theme for redmine.

![web](screenshots/2.png "Example of view web")

![web](screenshots/4.png "Example of view mobile")

The theme use two colors: *Primary* and *Accent*.

You can change the default theme: you can copy theme in stylesheet\colors in stylesheet\ and rename theme color.css.

You can change the default icon: you can copy icon in stylesheet\ico in favicon\ and rename theme favicon.ico.

Sample

```
cp stylesheet\colors\color-blue-red.css stylesheet\
mv stylesheet\colors.css stylesheet\color.css.default
mv stylesheet\color-blue-red.css stylesheet\color.css 
mv stylesheet\ico\icon-blue.ico favicon\favicon.ico 
```

the link for explication on install theme ion redmine https://www.redmine.org/projects/redmine/wiki/Themes

You can add a specific color theme by project: You must use https://github.com/fraoustin/redmine_rtmaterial plugin.

List of color:

- red
- pink
- purple
- deepPurple
- indigo
- blue
- lightBlue
- cyan
- teal
- green
- lightGreen
- lime
- yellow
- amber
- orange
- deepOrange
- brown
- grey
- blueGrey


You can load a specific theme  

You can use palette of color from https://material-ui.com/customization/color/

Icons from https://feathericons.com/

## Install with local redmine

::

    cd /usr/src/redmine/public/themes
    git clone https://github.com/fraoustin/RTMaterial.git
    #
## Use Docker

Your Dockerfile for Redmine 5.X

::

    FROM redmine:5.x

    WORKDIR /usr/src/redmine/public/themes
    RUN git clone https://github.com/fraoustin/RTMaterial.git
    WORKDIR /usr/src/redmine/public/themes/RTMaterial/stylesheets
    RUN cp colors/color-red-blue.css colors.css
    RUN cp ico/icon-red.ico ../favicon/favicon.ico

Your Dockerfile for Redmine 6.0

::

    FROM redmine:6.0

    WORKDIR /usr/src/redmine/public/themes
    RUN git clone https://github.com/fraoustin/RTMaterial.git
    WORKDIR /usr/src/redmine/public/themes/RTMaterial/stylesheets
    RUN cp colors/color-red-blue.css colors.css
    RUN cp ico/icon-red.ico ../favicon/favicon.ico
    RUN ln -s /usr/src/redmine/public/themes/RTMaterial /usr/src/redmine/themes/RTMaterial
    
You can use 

::

    docker build -t myredmine .
    docker run -d -p 3000:3000 --name myredmine myredmine

