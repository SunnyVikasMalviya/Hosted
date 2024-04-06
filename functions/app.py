#! python3
# app.py
# 1. 
# 2. 

import cgi
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/new_user_registration':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            form_data = cig.parse_qs(post_Data.decode('utf-8'))
            email = form_data['Email'][0]
            username = form_data['Username'][0]
            password = form_data['Password'][0]

            #TODO: Perform email validation processing

            if username == 'admin' and password == "password":
                message = 'Login Successful!'
            else:
                message = 'Invalid username or password. Please try again.'

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response_data = {'message': message}
            self.wfile.write(json.dumps(response_data).encode('utf-8'))

    def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        print(f'Starting server on port {port}...')
        httpd.serve_forever()

if __name__ == "__main__":
    run()