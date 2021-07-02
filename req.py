#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 19:13
# @Author  : zhangyq
# @File    : req.py
# @Software: PyCharm
import unittest
import requests
from unittest import mock
class mockserver(unittest.TestCase):

    def setUp(self) -> None:
        pass
    def test_loggin(self):
        url='http://wwww.biadu.com/api/payment'

        data={"real_name":"zhangyq",
              'money':200,
              'phone':'15190909090'
              }
        #response=requests.post(url=url,data=data)

        mock_res=requests.Response()
        mock_res.status_code=200
        mock_res._content={"status":1,'msg':'支付成功','orderid':{'202106301036'}}

        with mock.patch.object(requests,"post",return_value=mock_res):
            res=requests.post(url=url,data=data)
            print(res.content)
if __name__ == '__main__':
    unittest.main()






