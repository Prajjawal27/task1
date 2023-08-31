from http.server import HTTPServer, SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/url/task':
            self.path = '/task.html'
        return SimpleHTTPRequestHandler.do_GET(self)

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), MyHandler)
    print('Server started at http://localhost:8000/url/task')
    server.serve_forever()
 