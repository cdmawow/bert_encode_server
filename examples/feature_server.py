# -*- coding: utf-8 -*-

"""
@Author: Shaoweihua.Liu
@Contact: liushaoweihua@126.com
@Site: github.com/liushaoweihua
@File: feature_server.py
@Time: 2020/3/3 4:09 PM
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from ..server import BertServer
from ..server.helper import  get_run_args


if __name__ == "__main__":
    with BertServer(get_run_args()) as server:
        server.join()
