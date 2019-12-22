function setThemeColor(){
    $("body")[0].classList.forEach(cls => {
        if (cls.startsWith('project-')) {
            $.getJSON( "/projects/"+ cls.substring(8) +".json", function( data ) {
                if (data.project["custom_fields"]) {
                    data.project.custom_fields.forEach(field => {
                        if (field.name == "RTMaterial") {
                            console.log(field.value);
                            $("head").append('<link rel="stylesheet" href="/themes/RTMaterial/stylesheets/colors/color-'+ field.value +'.css" type="text/css" />');
                            $("li:contains(' "+field.value+"')").remove();
                        }
                    })
                }
            });
        }
    })
}
$(document).ready(setThemeColor)