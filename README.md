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
    	
## See also

* https://github.com/cooperhewitt/py-cooperhewitt-unicode
* https://github.com/cooperhewitt/py-cooperhewitt-flask