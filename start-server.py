#!/usr/bin/env python3
"""
eightfold Development Server
A simple HTTP server for local development.

Usage:
    python start-server.py
    python start-server.py 3000  # custom port

Then open http://localhost:8000 in your browser.
"""

import http.server
import socketserver
import sys
import os

# Configuration
DEFAULT_PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__)) or "."


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP handler with cleaner logging."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        # Color coding for different status codes
        status = args[1] if len(args) > 1 else ""
        if status.startswith("2"):
            color = "\033[32m"  # green
        elif status.startswith("3"):
            color = "\033[33m"  # yellow
        elif status.startswith("4") or status.startswith("5"):
            color = "\033[31m"  # red
        else:
            color = "\033[0m"   # reset

        reset = "\033[0m"
        print(f"{color}[{args[1]}]{reset} {args[0]}")

    def end_headers(self):
        # Disable caching for development
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PORT

    # Allow port reuse to avoid "Address already in use" errors
    socketserver.TCPServer.allow_reuse_address = True

    with socketserver.TCPServer(("", port), QuietHandler) as httpd:
        print()
        print("\033[1m\033[33m  eightfold \033[0m\033[90mDevelopment Server\033[0m")
        print()
        print(f"  \033[32m➜\033[0m  Local:   \033[36mhttp://localhost:{port}\033[0m")
        print(f"  \033[90m➜\033[0m  Root:    {DIRECTORY}")
        print()
        print("  \033[90mReload browser to see changes. Press Ctrl+C to stop.\033[0m")
        print()

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n  \033[33mServer stopped.\033[0m Good work today!\n")
            sys.exit(0)


if __name__ == "__main__":
    main()
