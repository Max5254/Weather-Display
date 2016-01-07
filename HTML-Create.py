# write-html.py

f = open('helloworld.html','w')
temp = 55
message = """<html>
<body>

<h1>""" + str(temp) +"""F</h1>
<img src="icon.gif"  width="104" height="142">

</body>
</html>"""

f.write(message)
f.close()