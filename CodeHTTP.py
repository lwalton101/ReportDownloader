from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, urlsplit, parse_qsl
from AuthCodeResponse import AuthCodeResponse

class CodeHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<p>You may close this tab and return to the application</p>", "utf-8"))

        dictionary = dict(parse_qsl(urlsplit(self.path).query))
        AuthCodeResponse.code = dictionary["code"]