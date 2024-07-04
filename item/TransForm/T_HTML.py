#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/23 10:47
# @Author  : HD
# @File    : T_HTML.py
# @Description :
import html

text = '''
主题
温州轨道交通 S2线钢轨纪念品
内容
以温州轨道交通S2线钢轨经过特殊加工制作的纪念品。
材质
50KG/M钢轨+竹盒
尺寸
钢轨 底宽13.2CM，上宽7CM，高15.2CM， 重975G竹盒 长20cm，宽22cm，高5CM（手工测量，存在误差）
须知
以上产品自S2线开通之日起根据订单顺序发货。该文创产品由钢轨加工而成，底部保留加工打孔，表面存在凹痕、毛点等，非瑕疵品。已支付商品不退不换，遗失不补。
统一采用“温州轨道”手机应用软件线上平台售卖模式。如需发票请在收货地址末尾备注。（江浙沪包邮，其余地区参照邮政实际运费到付）
'''

html_text = html.escape(text)
html_paragraph = f"<p>{html_text}</p>"

print(html_paragraph)
