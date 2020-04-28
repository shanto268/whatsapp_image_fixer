import os, sys

dl = "/Users/sshanto/Downloads/"
pics = os.listdir(dl)
targets = []

def process():
    if len(sys.argv) == 1:
        print("input name required!")
        return 
    else:
        newName = sys.argv[1]
        for pic in pics:
            ext = pic.split(".")[-1]
            if ext == "jpeg" and pic[0] == "W":
                time = (pic.split(" ")[4]).split(".")
                time = 3600*float(time[0]) + 60*float(time[1]) + float(time[2])
                targets.append(pic)

        for i in range(len(targets)):
            os.rename(dl+targets[i],dl+newName+str(i+1)+".jpeg")
        return 

process()
