#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import codecs


argv = sys.argv
argc = len(sys.argv)

# keyがlistの添字な辞書へ変換
def list2dict(val_list):
    return dict(zip(range(0,len(val_list)), val_list))

class Dish:

    def __init__(self, name, url):
        self.name = name
        self.url = url

    def get_info_str(self):
        return "%s %s" % (self.name, self.url) # 料理の情報文字列を返す

class Recipe:

    def __init__(self, filepath):
        self.dic = {}

        # ファイル読み込み
        tmp_data = []
        with codecs.open(filepath, 'r', encoding="utf-8") as fd:
            lines = fd.readlines()
            self.user = lines.pop(0).rstrip() # 最初の行はユーザ名
            for line in lines:
                # 改行を除去して名前とURLにパース
                name, url = line.rstrip().split(" ")
                tmp_data.append(Dish(name, url))
        self.dic = list2dict(tmp_data)

def print_recipe(recipe, recipe_id=None):

    print "%s: " % (recipe.user)

    if recipe_id is None:
        # ID指定なし

        for recipe_id, dish in recipe.dic.items():
            print "%d: %s" % (recipe_id, dish.get_info_str())
    else:
        # ID指定あり
        if output_id in recipe.dic:
            print "%d: %s" % (output_id, recipe.dic[output_id].get_info_str())
        else:
            print "レシピがありません。"

if __name__ == "__main__":
    # 引数を念のためチェック
    if argc == 2:
        recipe = Recipe(filepath=argv[1])

        print_recipe(recipe)

    elif argc == 3:
        recipe = Recipe(filepath=argv[1])
        output_id = int(argv[2])

        print_recipe(recipe, output_id)

    else:
        print "引数が不正です。"
        quit()
