import sys
import zipfile
import re


"""
extract text from a zip file
"""
def zip2ruby(fname):
    with zipfile.ZipFile(fname, 'r') as zf:
        # zipファイルの中身を取得
        lst = zf.namelist()
        print(lst)
        
        # zipファイル内のファイルを指定
        item = zf.infolist()[0]

        with zf.open(item.filename) as f:
            # テキストの文字コードのshift-jisでデコード
            return f.read().decode('shift_jis')

"""
remove ruby and other symbols
"""
def ruby2txt(ruby):
   # テキスト上部の【テキスト中に現れる記号について】箇所の除去
    txt = re.split(r'-{50,}', ruby)[2]
 
    # テキスト下部の「底本：～」の除去
    txt = re.split(r'底本：', txt)[0]
 
    # ルビ、ルビの付く文字列の始まりを特定する記号、入力者注を除去
    txt = re.sub(r'《.*?》|［＃.*?］|｜', '', txt)
 
    # 改行コードを除くいくつかのスペース（例えば全角スペース、半角スペース、タブ）をまとめて削除
    txt = re.sub(r"[\u3000 \t]", "", txt)

    # テキスト前後の空白を除去
    return txt.strip()

"""
main function
"""
def main():
    # zipファイルパスを引数として渡す
    argvs = sys.argv
    if len(argvs) != 3:
        print('Usage: python3 {} "zip file path"'.format(argvs[0]))
        exit()
 
    ruby = zip2ruby(argvs[1])
    txt = ruby2txt(ruby)
    
    # decide file name
    textFile = '../ao2txt/' + argvs[2]
    
    with open(textFile, 'w', encoding='utf-8') as f:
        f.write(txt)

    print("done!")
 
if __name__ == '__main__':
    main()
