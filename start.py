import PIL
from PIL import Image
import algorithm
import webbrowser
import argparse


def main(indir:str, outdir:str, minnum:int, maxnum: int, strlen: int):
    for i in range(minnum, maxnum):
        if (i%10==0): print(i)
        j = i+1
        istr = str(i)
        jstr = str(j)
        filenamei = '0'*(strlen-len(istr)) + istr + ".png"
        filenamej = '0'*(strlen-len(jstr)) + jstr + ".png"
        imgi = Image.open(indir + filenamei)
        imgj = Image.open(indir + filenamej)
        img = algorithm.alg(imgi, imgj)
        img.save(outdir + filenamei)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Args")
    parser.add_argument("indir", type=str)
    parser.add_argument("outdir", type=str)
    parser.add_argument("strlen", type=int)
    parser.add_argument("minnum", type=int)
    parser.add_argument("maxnum", type=int)
    
    args = parser.parse_args()
    main(args.indir, args.outdir, args.minnum, args.maxnum, args.strlen)