# plumbing-ucd-server

A simple Flask-based HTTP pony to lookup Unicode character names for a string.

## Example

	/usr/local/bin/ucd-server.py -c ucd-server.cfg

### GET /?string=<STRING>
	
	curl 'http://localhost:5000/?string=hello☃'

	{
	  "chars": [
	    [
	      "h", 
	      "LATIN SMALL LETTER H"
	    ], 
	    [
	      "e", 
	      "LATIN SMALL LETTER E"
	    ], 
	    [
	      "l", 
	      "LATIN SMALL LETTER L"
	    ], 
	    [
	      "l", 
	      "LATIN SMALL LETTER L"
	    ], 
	    [
	      "o", 
	      "LATIN SMALL LETTER O"
	    ], 
	    [
	      "\u2603", 
	      "SNOWMAN"
	    ]
	  ], 
	  "stat": "ok"
	}

### POST /

	curl -X POST -F 'string=⚓anchor' http://localhost:5000

	{
	  "chars": [
	    [
	      "\u2693", 
	      "ANCHOR"
	    ], 
	    [
	      "a", 
	      "LATIN SMALL LETTER A"
	    ], 
	    [
	      "n", 
	      "LATIN SMALL LETTER N"
	    ], 
	    [
	      "c", 
	      "LATIN SMALL LETTER C"
	    ], 
	    [
	      "h", 
	      "LATIN SMALL LETTER H"
	    ], 
	    [
	      "o", 
	      "LATIN SMALL LETTER O"
	    ], 
	    [
	      "r", 
	      "LATIN SMALL LETTER R"
	    ]
	  ], 
	  "stat": "ok"
	}
    	
## Config

`plumbing-ucd-server` uses utility functions exported by the
[cooperhewitt.flask.http_pony](https://github.com/cooperhewitt/py-cooperhewitt-flask/blob/master/cooperhewitt/flask/http_pony.py)
library which checks your Flask application's configuration for details about
how to handle things.

The following settings should be added to a standard [ini style configutation
file](https://en.wikipedia.org/wiki/INI_file).

### [flask]

#### port

The TCP port you want your Flask server to listen on.

### [http_pony]

We don't actually need anything exported in this section but I think you'll need this (empty) section until I get around to patching [cooperhewitt.flask.http_pony](https://github.com/cooperhewitt/py-cooperhewitt-flask/blob/master/cooperhewitt/flask/http_pony.py) to do the right thing.

## See also

* https://github.com/cooperhewitt/py-cooperhewitt-unicode
* https://github.com/cooperhewitt/py-cooperhewitt-flask
