# -*- coding: utf-8 -*-

"""
@Author: Shaoweihua.Liu
@Contact: liushaoweihua@126.com
@Site: github.com/liushaoweihua
@File: __init__.py.py
@Time: 2020/3/2 2:27 PM
"""

# Codes come from <bert-as-service>:
#    Author: Han Xiao
#    Github: https://hanxiao.github.io
#    Email: artex.xh@gmail.com
#    Version: 1.10.0


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def main():
    from bert_serving.server import BertServer
    from bert_serving.server.helper import get_run_args
    with BertServer(get_run_args()) as server:
        server.join()


def benchmark():
    from bert_serving.server.benchmark import run_benchmark
    from bert_serving.server.helper import get_run_args, get_benchmark_parser
    args = get_run_args(get_benchmark_parser)
    run_benchmark(args)


def terminate():
    from bert_serving.server import BertServer
    from bert_serving.server.helper import get_run_args, get_shutdown_parser
    args = get_run_args(get_shutdown_parser)
    BertServer.shutdown(args)