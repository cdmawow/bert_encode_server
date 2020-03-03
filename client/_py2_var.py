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


__all__ = ['_py2', '_str', '_buffer', '_unicode']


_py2 = True
_str = basestring
_buffer = buffer


def _unicode(x):
    return x if isinstance(x, unicode) else x.decode('utf-8')