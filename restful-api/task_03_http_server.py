#!/usr/bin/python3
"""creates a basic http server"""
import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """handles get requests, choosing correct response"""

    def send_json(self, code, data):
        """encode response as json data type"""
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def send_text(self, code, message):
        """encode response as plain text"""
        self.send_response(code)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

    def do_GET(self):
        """determine response type based on request"""
        if self.path == "/":
            self.send_text(200, "Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_json(200, {"name": "John", "age": 30,
                                 "city": "New York"})
        elif self.path == "/status":
            self.send_text(200, "OK")
        elif self.path == "/fine":
            self.send_text(200, "This is fine")
        elif self.path == "/info":
            self.send_json(200, {"version": "1.0",
                                 "description":
                                 "A simple API built with http.server"})
        else:
            self.send_text(404, "Endpoint not found")


if __name__ == "__main__":
    server = http.server.HTTPServer(("", 8000), SimpleAPIHandler)
    print("Server active on port 8000")
    server.serve_forever()
