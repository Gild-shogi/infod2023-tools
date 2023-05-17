import sys

from colorinfo import ColorInfo


def SimilarOfDegree(f1, f2):
    info1 = ColorInfo(f1)
    info2 = ColorInfo(f2)

    if info1.width != info2.width or info1.height != info2.height:
        print("[要確認] 2つのファイルの画像サイズが異なります。")
        return 0
    else:
        sum1 = 0
        sum2 = 0
        sum12 = 0
        for i in range(len(info1.rgb)):
            sum1 = sum1 + info1.rgb[i]
            sum2 = sum2 + info2.rgb[i]
            sum12 = sum12 + min(info1.rgb[i], info2.rgb[i])
        if sum1 != sum2:
            print("[要確認] 2つのデータを比較した結果、総画素数が異なります。")
            return 0
        else:
            return sum12 / sum1


def SimilarOfDegree64(f1, f2):
    info1 = ColorInfo(f1)
    info2 = ColorInfo(f2)

    if info1.width != info2.width or info1.height != info2.height:
        print("[要確認] 2つのファイルの画像サイズが異なります。")
        return 0
    else:
        sum1 = 0
        sum2 = 0
        sum12 = 0
        for i in range(len(info1.color64)):
            sum1 = sum1 + info1.color64[i]
            sum2 = sum2 + info2.color64[i]
            sum12 = sum12 + min(info1.color64[i], info2.color64[i])
        if sum1 != sum2:
            print("[要確認] 2つのデータを比較した結果、総画素数が異なります。")
            return 0
        else:
            return sum12 / sum1


if __name__ == "__main__":
    args = sys.argv
    files = []
    if len(args) != 3:
        files.append("img2-1024/1024_2.bmp")
        files.append("img2-1024/1024_3.bmp")
    else:
        files.append(args[1])
        files.append(args[2])
    print("類似度 {:.3}".format(SimilarOfDegree(files[0], files[1])))
    print("類似度 {:.3}".format(SimilarOfDegree64(files[0], files[1])))
