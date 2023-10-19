

import cv2
import socket
import numpy as np
import io
import base64
import time
import os
import glob
def receive_all(sock, count):
    buf = b''
    while count:
        new_buf = sock.recv(count)
        if not new_buf:
            return None
        buf += new_buf
        count -= len(new_buf)
    return buf

def CycleSendPictures(img_path):
    """
    发送图片
    """
    host = "172.16.122.65"
    port = 6666
    tcpclient = socket.socket()
    tcpclient.connect((host, port))
    print("已连接服务端")
    sdata = picture2base(img_path)  #信源编码
    print(f"开始发送图片 {img_path}")
    tcpclient.send(sdata.encode())
    tcpclient.close()
    print("发送完成")

def connect_tcp():
    host = "YOUR IP "
    #host = "127.0.0.1"
    port = YOUR PORT

    global tcpclient  #全局变量便于跨函数直接访问
    tcpclient = socket.socket()
    tcpclient.connect((host, port))

    print("已连接服务端")

def SendPictures(img):  #在建立tcp链接后发送图片

    print(f"开始发送图片")
    sdata = mypicture2base(img)
    tcpclient.send(sdata.encode())

def close_tcp():
    print("发送完成")
    tcpclient.close()
    print("已断开tcp链接")
    print("Finish！！！")




# 图片转换成base64
def picture2base(path):
    """
    压缩图片数据
    """
    with open(path, 'rb') as img:
        b64encode = base64.b64encode(img.read())
        # 返回base64编码字符串
        return b64encode.decode('utf-8')

def mypicture2base(img):
    """
    压缩图片数据
    yjy
    """
    # cv2.imshow("1",img)
    # cv2.waitKey(0)
    # img_bin = img.tobytes()
    # img_bin = cv2.imencode()
    b64encode = base64.b64encode(img)
    # 返回base64编码字符串
    return b64encode.decode('utf-8')


# base64转换成图片

#该函数可以讲视频进行抽帧并发送
#
def video_pic_send():


    vidcap = cv2.VideoCapture('./video/test.mp4')

    # 读取视频的基本信息
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    video_width = int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_height = int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(fps, total_frames, video_width, video_height)

    # 每隔interval帧取一张图片
    interval = 1

    success, image = vidcap.read()
    count = 0
    while success:
        if count % interval == 0:
            #发送抽帧的图片
            # image = cv2.imread('./data/images/test.jpg')
            SendPictures(image)
            #  cv2.imshow('a',image)
            #  cv2.waitKey(1)

            # 延时
            delay_mark = time.perf_counter()
            offset = 0
            while offset < 1:
                offset = time.perf_counter() - delay_mark

        count += 1
        success, image = vidcap.read()

if __name__ == "__main__":
    # 整体逻辑依照面向过程
    # connect_tcp()
    # video_pic_send()
    # close_tcp()

    Root_PATH = './data/images/images'  # 存放图片的文件夹路径
    pic_paths = glob.glob(os.path.join(Root_PATH, '*.jpg'))
    pic_paths.sort()  #按照文件名称排序

    for i in pic_paths:
        CycleSendPictures(i)
        time.sleep(5)
        pass


