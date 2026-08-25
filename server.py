"""Small local server for the soundboard.

Run with: python server.py
Then open: http://localhost:8000
"""

from __future__ import annotations

import json
import mimetypes
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse


PROJECT_DIRECTORY = Path(__file__).resolve().parent
SUPPORTED_EXTENSIONS = {".mp3", ".m4a"}


class SoundboardHandler(SimpleHTTPRequestHandler):
    """Serve the app files and expose the current audio files at /sounds."""

    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        ".m4a": "audio/mp4",
        ".mp3": "audio/mpeg",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(PROJECT_DIRECTORY), **kwargs)

    def do_GET(self) -> None:
        if urlparse(self.path).path == "/sounds":
            self.send_sound_list()
            return
        super().do_GET()

    def send_sound_list(self) -> None:
        sounds = sorted(
            (
                item.name
                for item in PROJECT_DIRECTORY.iterdir()
                if item.is_file() and item.suffix.lower() in SUPPORTED_EXTENSIONS
            ),
            key=str.casefold,
        )
        body = json.dumps({"sounds": sounds}, ensure_ascii=False).encode("utf-8")

        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)


def main() -> None:
    address = ("127.0.0.1", 8000)
    with ThreadingHTTPServer(address, SoundboardHandler) as server:
        print("Soundboard is running at http://localhost:8000")
        print("Press Ctrl+C to stop the server.")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")


if __name__ == "__main__":
    main()
