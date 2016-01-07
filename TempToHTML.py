import urllib2
import urllib
import json
import webbrowser

State = 'NY'
Town = 'Trumansburg'
f = urllib2.urlopen('http://api.wunderground.com/api/132e68feddbba074/geolookup/conditions/q/' + State + '/' + Town + '.json')
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
icon_url = parsed_json['current_observation']['icon_url']

s = list(icon_url)
s[26] = 'j'
icon_url ="".join(s)

urllib.urlretrieve(icon_url,'icon.gif')
print "Current temperature in %s is: %s" % (location, temp_f)
print icon_url

# write-html.py

f = open('helloworld.html','w')
temp = temp_f
message = """<html>
<body>
<h1>The temperature for """ + location + """ is</h2>
<h2>""" + str(temp) +"""F</h2>
<img src="icon.gif"  width="104" height="142">

</body>
</html>"""

f.write(message)
filename = 'helloworld.html'
webbrowser.open_new_tab(filename)
f.close()



