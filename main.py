import socket

IP = '127.0.0.1'
PORT = 2000
HEADERS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'

def start_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((IP, PORT))
        server.listen(4)
        while True:
            print(f'Start... http://{IP}:{PORT}')
            client, address = server.accept()
            data = client.recv(1024).decode('utf-8')
            content = load_html(data)
            client.send(content)
            client.shutdown(socket.SHUT_WR)
    except:
        server.close()
        print('Shutdown.')

def load_html(request):
    path = request.split(' ')[1]
    if path == '/':
        path = 'home.html'
    try:
        with open('templates/'+path, 'rb') as file:
            response = file.read()
    except FileNotFoundError:
        with open('templates/404.html', 'rb') as file:
            response = file.read()
    return HEADERS.encode('utf-8') + response


if __name__ == '__main__':
    start_server()