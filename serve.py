from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

class Handler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        ".html": "text/html",
        ".js": "application/javascript",
        ".mjs": "application/javascript",
        ".json": "application/json",
        ".wasm": "application/wasm",
        ".mp3": "audio/mpeg",
        ".wav": "audio/wav",
        ".ogg": "audio/ogg",
    }

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8000
    print(f"Serving on http://{host}:{port}/")
    ThreadingHTTPServer((host, port), Handler).serve_forever()
