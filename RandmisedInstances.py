CARDWIDTH=249.12
CARDHEIGHT=167.04
#UK call card size

newPage(CARDWIDTH,CARDHEIGHT)

path = "krspy.ttf"
fontName = installFont(path)

x, y, w, h = 0, 0, CARDWIDTH, CARDHEIGHT

fill(1)

font("fontName")
fill(0)

txtFontSize=106

txt = FormattedString(fontSize=txtFontSize)

#set text width
txt.fontVariations(wdth=266) 

#'manually' refresh startvariable value each time and append to textBox

startvariable=randint(0,1000)
txt.fontVariations(wght=startvariable)
txt.append("C", font="crispy", fontSize=txtFontSize, fill=(0, 0, 0))
startvariable=randint(0,1000)
txt.fontVariations(wght=startvariable)
txt.append("H", font="crispy", fontSize=txtFontSize, fill=(0, 0, 0))
startvariable=randint(0,1000)
txt.fontVariations(wght=startvariable)
txt.append("A", font="crispy", fontSize=txtFontSize, fill=(0, 0, 0))
startvariable=randint(0,1000)
txt.fontVariations(wght=startvariable)
txt.append("R", font="crispy", fontSize=txtFontSize, fill=(0, 0, 0))
startvariable=randint(0,1000)
txt.fontVariations(wght=startvariable)
txt.append("G", font="crispy", fontSize=txtFontSize, fill=(0, 0, 0))
startvariable=randint(0,1000)
txt.fontVariations(wght=startvariable)
txt.append("E", font="crispy", fontSize=txtFontSize, fill=(0, 0, 0))
startvariable=randint(0,1000)
txt.fontVariations(wght=startvariable)
txt.append("S", font="crispy", fontSize=txtFontSize, fill=(0, 0, 0))

text(txt, (CARDWIDTH/2, CARDHEIGHT/2-txtFontSize/3), align="center")
