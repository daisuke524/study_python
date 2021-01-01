# @IT｜[Python入門] リストの基本
# id関数(組み込み関数)
"""""""""""""""""
id「アインデンティティー」
Pythonではオブジェクト(数値、文字列、リストなど...)を定義(例えば、x = 1 のこと...)すると「それを識別する値」が
割り当てられる。割り当てられた値はメモリに保存され変化することはない。

下記の2点は同義：
・somelist = somelist + anotherlist
・somelist += anotherlist

補足：
『「somelist = somelist + anotherlist」と「somelist += anotherlist」は「リストを結合する」という意味では同一
の操作だが、実際には最終的なオブジェクトのアイデンティティーが異なるので、完全に同一ではない。』らしい。
"""""""""""""""""
somelist = [0, 1, 2]
print(somelist) # [0, 1, 2]
print(id(somelist)) # 140517508198880
# リストとリストを結合
somelist = somelist + [3, 4]
print(somelist) # [0, 1, 2, 3, 4]
print(id(somelist)) # 140447345920592 <- アイデンティティーの値が変わっている
somelist += [5, 6]
print(somelist) # [0, 1, 2, 3, 4, 5, 6]
print(id(somelist)) # 140447345920592
print('')
