#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

class ProxyHTTPRequestHandler(BaseHTTPRequestHandler):

    protocol_version = 'HTTP/1.1'

    def do_GET(self):
        self.handle_all()

    def do_POST(self):
        self.handle_all()

    def do_PUT(self):
        self.handle_all()

    def do_DELETE(self):
        self.handle_all()

    def handle_all(self):
        if 'Host' not in self.headers:
            self.send_error(400, None, 'Missing "Host" header')
            return

        self.send_response(302, 'Found')
        self.send_header('Location', f'https://{self.headers["Host"]}')
        self.send_header('Content-Length', '0')
        self.end_headers()


if __name__ == '__main__':

    server_address = ('0.0.0.0', 80)
    httpd = ThreadingHTTPServer(server_address, ProxyHTTPRequestHandler)

    print(f"https_redirector running on port {server_address[1]}")    
    httpd.serve_forever()

