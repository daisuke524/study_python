# 『 lesson３-８ 知らないとエラーになってしまいます　空白、インデント、改行の役割 』

# 【空白や改行は見やすくするために使ってよい】
# 空白は,記号などを見やすくする為に適当な場所に入れてもエラーは起きない。
# 実行結果は全て同じになる。
print("abc"+"cde")
print( "abc" + "cde" )
print(     "abc"     +     "cde"     )
# ただし、「””」で括った中に空白があれば、空白もそのまま表示られる。
print("abc          def")
# 改行も空白と同様。
print("こんにちは。今日の晩ご飯は何でしたか？")
print("おいしかったですか？")
print("何カロリーでしたか？")
# 下記は上記と同じ結果が表示される。
print("こんにちは。今日の晩ご飯は何でしたか？")

print("おいしかったですか？")

print("何カロリーでしたか？")
# 改行だけの行を「空行」と呼ぶ。

# 【行頭の空白だけは例外】
# 「インデント」= 行頭の空白のこと。1文字だけではなく、4文字や8文字の空白で構成されている事がほとんど。あと「制御構造」を示している。
# 下記のように、行頭にインデントを入れるとエラーが表示される。
"""

# coding:utf-8
    print("こんにちは")

"""    