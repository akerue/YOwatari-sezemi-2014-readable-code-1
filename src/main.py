#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

argv = sys.argv
argc = len(sys.argv)

class Recipe:

    def __init__(self, filepath):
        self.data = []

        # ファイル読み込み
        with open(filepath, 'rb') as fd:
            for line in fd:
                self.data.append(line.rstrip())  # 改行を除去して追加


if __name__ == "__main__":
    filepath = ""  # 引数で受け取るファイルパス
    recipe = []    # 読み込みデータ

    # 引数を念のためチェック
    if argc == 2:
        filepath = argv[1]
    else:
        print "引数が不正です。"
        quit()

    recipe = Recipe(filepath)

    # 出力
    for recipe_id, recipe_name in enumerate(recipe.data):
        print "%d: %s" % (recipe_id, recipe_name)
