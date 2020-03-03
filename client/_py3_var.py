# -*- coding: utf-8 -*-

"""
@Author: Shaoweihua.Liu
@Contact: liushaoweihua@126.com
@Site: github.com/liushaoweihua
@File: __init__.py1.py
@Time: 2020/3/2 10:54 AM
"""

# Codes come from <bert-as-service>:
#    Author: Han Xiao
#    Github: https://hanxiao.github.io
#    Email: artex.xh@gmail.com
#    Version: 1.10.0


__all__ = ['_py2', '_str', '_buffer', '_raise']

_py2 = False
_str = str
_buffer = memoryview


def _raise(t_e, _e):
    raise t_e from _e