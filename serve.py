
import cv2
import socket
import numpy as np
import base64
import io
import time

def ReceivePicturesCircularly():
    """
    循环接收图片
    """
   
    host = 'YOUR IP'
    port = YOUR PORT
    tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpserver.bind((host, port))
    tcpserver.listen(5)
    print("等待客户端连接...")

    while True:
        tcpclient, addr = tcpserver.accept()
        print("-" * 5 + "开始接收" + "-" * 5)
        base64_data = ""
        while True:
            rdata = tcpclient.recv(1024)
            base64_data += str(rdata, 'utf-8')
            if base64_data:
                base2picture(base64_data)
            if not rdata:
                break

        #base2picture(base64_data)
        tcpclient.close()
        print("-" * 5 + "接收完成" + "-" * 5)

    tcpserver.close()



# 图片转换成base64
def picture2base(path):
    """
    压缩图片数据
    """
    with open(path, 'rb') as img:
        b64encode = base64.b64encode(img.read())
        # 返回base64编码字符串
        return b64encode.decode('utf-8')

# base64转换成图片
def base2picture(base64_img):
    """
    使用base64进行解码图片数据
    """
    now_time = time.strftime("%Y%m%d-%H%M%S")
    print(f"保存路径为：./data/rec_img")
    print(f"保存为：./{now_time}.jpg")
    b64decode = base64.b64decode(base64_img)
    file = open(r"./data/rec_img/" + now_time + r".jpg", 'wb')
    file.write(b64decode)
    file.close()
    file_name = now_time + r".jpg"
    return file_name




if __name__ == "__main__":
    # cv2.namedWindow(str(1), cv2.WINDOW_AUTOSIZE)
    ReceivePicturesCircularly()
    pass