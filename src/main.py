#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys


argv = sys.argv
argc = len(sys.argv)

# keyがlistの添字な辞書へ変換
def list2dict(val_list):
    return dict(zip(range(0,len(val_list)), val_list))


class Recipe:

    def __init__(self, filepath):
        self.data = {}

        # ファイル読み込み
        tmp_data = []
        with open(filepath, 'rb') as fd:
            for line in fd:
                tmp_data.append(line.rstrip())  # 改行を除去して追加
        self.data = list2dict(tmp_data)


if __name__ == "__main__":
    filepath = ""  # 引数で受け取るファイルパス
    recipe = []    # 読み込みデータ

    # 引数を念のためチェック
    if argc == 2:
        recipe = Recipe(filepath=argv[1])

        # 出力
        for recipe_id, recipe_name in recipe.data.items():
            print "%d: %s" % (recipe_id, recipe_name)
    elif argc == 3:
        recipe = Recipe(filepath=argv[1])
        output_id = int(argv[2])

        # 出力
        if output_id in recipe.data:
            print "%d: %s" % (output_id, recipe.data[output_id])
        else:
            print "レシピがありません。"
    else:
        print "引数が不正です。"
        quit()
