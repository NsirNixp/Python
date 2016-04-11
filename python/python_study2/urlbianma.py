import urllib
from urllib import urlencode
code = {
	'type':1,
	'key':2,
	'platform':3
}
code = urlencode(code)
print code