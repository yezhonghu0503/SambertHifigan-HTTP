# 导入 http.server 模块
import http.server
import socketserver

# 指定服务器的 IP 地址和端口
host = "127.0.0.1"
port = 8000

# 创建一个 HTTP 服务器，将当前目录作为根目录
handler = http.server.SimpleHTTPRequestHandler

# 启动服务器
with socketserver.TCPServer((host, port), handler) as httpd:
    print(f"Server started at {host}:{port}")
    # 保持服务器运行
    httpd.serve_forever()
