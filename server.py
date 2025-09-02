from http.server import SimpleHTTPRequestHandler, HTTPServer
import json

PORT = 8000
MARKERS_FILE = "markers.json"

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/markers.json":
            with open(MARKERS_FILE, "r") as f:
                data = f.read()
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(data.encode())
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == "/markers.json":
            length = int(self.headers['Content-Length'])
            body = self.rfile.read(length)
            data = json.loads(body)
            with open(MARKERS_FILE, "w") as f:
                json.dump(data, f, indent=2)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")

if __name__ == "__main__":
    server = HTTPServer(("localhost", PORT), MyHandler)
    print(f"Serving at http://localhost:{PORT}")
    server.serve_forever()
