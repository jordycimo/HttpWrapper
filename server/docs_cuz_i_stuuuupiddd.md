do_GET(self): is run every time the client tries to fetch info from the server.
- send_response() sends a status code ex (200 (regular function),404 (file not found), etc (whatever))
- send_header() sends HTTP headers to the client [mozilla documentation on HTTP headers.](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
- end_headers() signifies ending the headers being sent to the client, so you can start sending real data (html files, images, text, etc.)
- wfile.write() is used to actually write (send) data to the client. typically in UTF-8 bytes (ie the bytes("...","UTF-8) in most of these function calls.)

all media has to be encoded to base64 lol (FOR NOW)
literally add filetype checking dumb idiot!!!!!!!!
