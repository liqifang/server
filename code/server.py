# encoding:utf-8
import socketserver
 
 
class MySever(socketserver.BaseRequestHandler):
    def handle(self):
        # 1.记录客户端socket
        conn = self.request
        # 2.向客户端发送数据
        conn.sendall(bytes("你好，我是机器人", encoding="utf-8"))
        # 3.多进程连接服务器
        while True:
            # 4.接收客户端请求信息
            ret_bytes = conn.recv(1024)
            # 5.将请求发信息转换为字符串
            ret_str = str(ret_bytes, encoding="utf-8")
            print("             客户： "+ret_str)
            tx_str=input("服务器：")
            conn.sendall(bytes(tx_str,encoding="utf-8"))
#            print("*" * 98)
            # 6.判断客户端是否请求中断连接
            if "q" == ret_str:
                break
                
 
if __name__ == "__main__":

    # 7.创建socketserver class对象
    server = socketserver.TCPServer(("", 8000), MySever)
    # 8.开启处理请求
    server.serve_forever()
             
