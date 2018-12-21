# coding:utf-8
import socket
 
cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
 
try:
    cli_socket.connect(("39.105.219.16", 8000))
    print("[目标服务器连接成功]")
    print("-" * 98)
 
    ret_bytes = cli_socket.recv(1024)
    ret_str = str(ret_bytes, encoding="utf-8")
    print(ret_str)
 
    while True:
        input_str = input("我：")
        if "q" == input_str:
            cli_socket.sendall(bytes(input_str, encoding="utf-8"))
            break
     #   else:
        cli_socket.sendall(bytes(input_str, encoding="utf-8"))
        ret_bytes = cli_socket.recv(1024)
        ret_str = str(ret_bytes, encoding="utf-8")
        print("               服务器："+ret_str+"\n")
         #   print("*" * 98)

except IOError as out:
    print(out)
finally:
    cli_socket.close()

