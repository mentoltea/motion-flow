import argparse
import os
from threading import Thread

def do(indir, outdir, strlen, mi, ma):
    os.system("python start.py " + indir + " " + outdir + " " + str(strlen) 
                  + " " + str(mi) + " " + str(ma))

def main(indir:str, outdir:str, minnum:int, maxnum: int, strlen: int, threads:int):
    diff = maxnum-minnum
    avg = int(round(diff/threads))
    thrds: list[Thread] = []
    for i in range(threads):
        thrds.append( Thread(target=do, 
                             args=(indir, outdir, strlen, i*avg + minnum, (i+1)*avg),
                             daemon=True) )
    if (maxnum > threads*avg + minnum):
        thrds.append( Thread(target=do, 
                             args=(indir, outdir, strlen, threads*avg + minnum, maxnum),
                             daemon=True) )
    for t in thrds:
        t.run()
    #os.system("ffmpeg -r " + str(framerate) + " -i " + outdir + "%0" + str(strlen) + "d.png -pix_fmt yuv420p output.mp4")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Args")
    parser.add_argument("indir", type=str)
    parser.add_argument("outdir", type=str)
    parser.add_argument("strlen", type=int)
    parser.add_argument("threads", type=int)
    parser.add_argument("minnum", type=int)
    parser.add_argument("maxnum", type=int)
    
    args = parser.parse_args()
    main(args.indir, args.outdir, args.minnum, args.maxnum, args.strlen, args.threads)