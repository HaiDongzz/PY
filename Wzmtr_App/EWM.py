#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/29 13:38
# @Author  : HD
# @File    : EWM.py
# @Description :

import cv2


def decode_qr_code(image_path):
    img = cv2.imread(image_path, 0)
    scanner = cv2.QRCodeDetector()
    decoded_data, _, _ = scanner.detectAndDecodeMulti(img)
    return decoded_data


qr_code_data = decode_qr_code('D:/TEST-project/温州轨道app2.0/轨道S2文件/qr_code.png')
print(qr_code_data)
