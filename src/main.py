#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

argv = sys.argv
argc = len(sys.argv)

if __name__ == "__main__":
    filepath = ""  # 引数で受け取るファイルパス
    recipe = []    # 読み込みデータ

    # 引数が多すぎる時
    if argc == 2:
        filepath = argv[1]
    else:
        print "引数が不正です。"
        quit()

    # ファイル読み込み
    with open(filepath, 'rb') as fd:
        for line in fd:
            recipe.append(line)

    # 出力
    for line in recipe:
        print line
