# -*- coding: utf-8 -*-

"""
@Author: Shaoweihua.Liu
@Contact: liushaoweihua@126.com
@Site: github.com/liushaoweihua
@File: server.py.py
@Time: 2020/3/2 2:50 PM
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from . import BertServer
from .helper import  get_run_args


if __name__ == "__main__":
    with BertServer(get_run_args()) as server:
        server.join()