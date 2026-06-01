"""
 * Simple local web server to serve the Electronics Emoji symbol viewer.
 * Serving over HTTP is required because index.htm loads the icons as ES
 * modules, which browsers block under the file:// scheme (CORS).
"""

import http.server
import webbrowser
import os
import subprocess

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    # Treat index.htm as a directory index (the default is only index.html).
    index_pages = ("index.htm", "index.html")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def kill_port(port):
    try:
        # Try to kill process using the port (Linux/macOS)
        subprocess.run(["fuser", "-k", f"{port}/tcp"], capture_output=True)
    except Exception:
        pass

def run():
    kill_port(PORT)
    # Attempt to open the browser automatically
    webbrowser.open(f"http://localhost:{PORT}/index.htm")

    # ThreadingHTTPServer serves the ES module files concurrently instead of
    # one-at-a-time, which speeds up initial load over HTTP/1.1.
    http.server.ThreadingHTTPServer.allow_reuse_address = True
    with http.server.ThreadingHTTPServer(("", PORT), Handler) as httpd:
        print(f"Server started at http://localhost:{PORT}/index.htm")
        print("Press Ctrl+C to stop the server.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            httpd.server_close()

if __name__ == "__main__":
    run()
