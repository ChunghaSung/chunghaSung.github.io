#!/usr/bin/env python3
"""
Simple HTTP server for testing the static website locally.
Usage: python3 serve.py [port]
Default port: 8000
"""

import http.server
import socketserver
import sys
import os

# Change to the directory containing this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Get port from command line argument or use default
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_GET(self):
        # Handle directory requests by serving index.html
        if self.path.endswith('/') or '.' not in os.path.basename(self.path):
            if self.path.endswith('/'):
                index_path = self.path + 'index.html'
            else:
                index_path = self.path + '/index.html'
            
            # Check if index.html exists
            file_path = '.' + index_path
            if os.path.exists(file_path):
                self.path = index_path
        
        super().do_GET()

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print("Press Ctrl+C to stop the server")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
