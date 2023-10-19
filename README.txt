English:
Function："Using TCP to transmit images from the client to the server and performing YOLO inference on the server.
This project is based on YOLOv5-5.0. Before using it, please modify "YOUR IP" and "YOUR PORT" in the "client.py" and "serve.py" files. Finally, place these three files in the YOLOv5-5.0 folder and run "tcp_detect.py" and "client.py" on both the server and the client.
"tcp_detect.py" is modified from the official YOLOv5 "detect.py" script, and you can refer to the official documentation for instructions on replacing weight files.
Please refer to the requirements in the "requirements.txt" file for the environmental prerequisites.

中文：
功能： 利用tcp传输图片从客户端到服务器，在服务器端实现YOLO对图像的推理
本项目基于YOLOv5-5.0
使用前，将clinet.py 和 serve.py 中的 YOUR IP 和YOUR PORT 修改
最后，将三个文件放置在YOLOv5-5.0的文件夹中， 分别在服务器和客户端运行tcp_detect.py 和 client.py 即可。
tcp_detect.py在YOLOv5官方detect.py修改而来，替换权重文件可参考官方。
环境要求见：requirements.txt
