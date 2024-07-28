# main server

from http.server import BaseHTTPRequestHandler, HTTPServer

host = "localhost"
port = 8000

class server(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            self.send_response(200)
            filetype = self.path.split(".")[1]
            if filetype == "html":
                self.send_header("Content-type","text/html")
            elif filetype == "css":
                self.send_header("Content-type","text/css")
            elif filetype == "gif":
                self.send_header("Content-type","image/gif")
            self.end_headers()
            with open("./server/res/"+self.path,"rb") as f:
                self.wfile.write(f.read())
                f.close()

        except: # else show error
            self.send_response(404)
            self.send_header("Content-type","text/html")
            self.end_headers()
            with open("./server/res/error.html","rb") as f:
                self.wfile.write(f.read())
                f.close()

if __name__ == "__main__":
    print(str(host)+" on port "+str(port))
    webserver = HTTPServer((host, port), server)
    webserver.serve_forever()