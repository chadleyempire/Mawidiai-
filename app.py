from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        with open("MawidyAPK/app/index.html", "r") as f:
            page = f.read()

        self.wfile.write(page.encode())

server = HTTPServer(('0.0.0.0', 8080), MyHandler)
print("Server running at http://localhost:8080")
server.serve_forever()
