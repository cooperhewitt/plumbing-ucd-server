# plumbing-ucd-server

This doesn't work yet because codecs and Flask...

	74 ->/usr/local/bin/ucd-server.py -c ucd-server.cfg
	INFO:werkzeug: * Running on http://127.0.0.1:5000/

	curl -X POST -F 'string=hello☃' http://localhost:5000/

	ERROR:UCD_SERVER:Exception on / [POST]
	Traceback (most recent call last):
	  File "/usr/local/lib/python2.7/dist-packages/Flask-0.10.1-py2.7.egg/flask/app.py", line 1817, in wsgi_app
	    response = self.full_dispatch_request()
	  File "/usr/local/lib/python2.7/dist-packages/Flask-0.10.1-py2.7.egg/flask/app.py", line 1477, in full_dispatch_request
	    rv = self.handle_user_exception(e)
	  File "/usr/local/lib/python2.7/dist-packages/Flask-0.10.1-py2.7.egg/flask/app.py", line 1381, in handle_user_exception
	    reraise(exc_type, exc_value, tb)
	  File "/usr/local/lib/python2.7/dist-packages/Flask-0.10.1-py2.7.egg/flask/app.py", line 1475, in full_dispatch_request
	    rv = self.dispatch_request()
	  File "/usr/local/lib/python2.7/dist-packages/Flask-0.10.1-py2.7.egg/flask/app.py", line 1461, in dispatch_request
	    return self.view_functions[rule.endpoint](**req.view_args)
	  File "/usr/local/lib/python2.7/dist-packages/plumbing_ucd_server-0.11-py2.7.egg/EGG-INFO/scripts/ucd-server.py", line 40, in lookup
	  File "/usr/lib/python2.7/encodings/utf_8.py", line 16, in decode
	    return codecs.utf_8_decode(input, errors, True)
	UnicodeEncodeError: 'ascii' codec can't encode character u'\u2603' in position 5: ordinal not in range(128)
	INFO:werkzeug:127.0.0.1 - - [25/Nov/2014 16:00:20] "POST / HTTP/1.1" 500 -

## See also

* https://github.com/cooperhewitt/py-cooperhewitt-unicode