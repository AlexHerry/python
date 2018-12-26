import urllib2
file = urllib2.urlopen('https://rivennero.me/index.php')
message = file.read()
print message