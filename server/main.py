# main server

from http.server import BaseHTTPRequestHandler, HTTPServer
from colorama import Fore, Back, Style

host = "localhost"
port = 8000

class server(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            self.send_response(200)
            filetype = self.path.split(".")[1]
            if filetype == "html":
                self.send_header("Content-type","text/html")
                self.log_message("sent text/html header")
            elif filetype == "css":
                self.send_header("Content-type","text/css")
                self.log_message("sent text/css header")
            self.end_headers()
            self.wfile.write(bytes(open("./server/res/"+self.path,"r").read(),"UTF-8"))

        except: # else show error
            self.send_response(404)
            self.send_header("Content-type","text/html")
            self.end_headers()
            self.wfile.write(bytes(open("./server/res/error.html","r").read(),"UTF-8"))

if __name__ == "__main__":
    print(Back.RED+str(host)+" on port "+str(port))
    print(Style.RESET_ALL)
    webserver = HTTPServer((host, port), server)
    webserver.serve_forever()