import urllib
from lxml import html

url = "https://material-ui.com/customization/color/"
page = html.fromstring(urllib.urlopen(url).read())

colors={}

for color in page.xpath("//*[@class='jss258']"):
    colorName = color.xpath(".//*[@class='jss255']/text()")[0]
    value = {}
    for val in color.xpath(".//*[@class='jss257']"):
        value[val.xpath("./span[1]/text()")[0]] = val.xpath("./span[2]/text()")[0]
    colors[colorName]=value

for primary in colors:
    for accent in colors:
        if primary != accent:
            filein = file('template_color.css')
            txt = filein.read()
            for val in colors[primary]:
                txt = txt.replace('Primary'+val, colors[primary][val])
            for val in colors[accent]:
                txt = txt.replace('Accent'+val, colors[accent][val])
            fileout = file('color-'+primary+'-'+accent+'.css', 'w')
            fileout.write(txt)
            fileout.close()
            filein.close()
                