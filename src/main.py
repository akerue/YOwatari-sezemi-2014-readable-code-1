#!/usr/bin/env python
# -*- coding:utf-8 -*-

if __name__ == "__main__":
    # 読み込みデータ
    recipe = []

    # ファイル読み込み
    with open("src/recipe.txt", 'rb') as fd:
        for line in fd:
            recipe.append(line)

    # 出力
    for line in recipe:
        print line
