from http.server import SimpleHTTPRequestHandler, HTTPServer

host = '0.0.0.0'
port = 8080

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, Docker!")

if __name__ == "__main__":
    with HTTPServer((host, port), MyHandler) as server:
        print(f"Serving on port {port}")
        server.serve_forever()
