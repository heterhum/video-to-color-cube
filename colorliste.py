from PIL import Image
import numpy as np
import glob
from tqdm.auto import tqdm


def colorliste(extention,longueur,hauteur,path):
    """ceci est une,
    explication
    """
    b=[]
    path = r'video-to-color-cube/imgfolder/*'+extention
    files = sorted(glob.glob(path))
    files = sorted(files, key=lambda x: int(x.split("\\")[-1].split(".")[0])) 
    for i in tqdm(range(1,500)): 
        t=[]

        imgp = Image.open(files[i-1]).convert('L')
        imgp = imgp.resize((longueur, hauteur))
        impixp = list(imgp.getdata())

        img = Image.open(files[i]).convert('L')
        img = img.resize((longueur, hauteur))
        impix = list(img.getdata())
        
        impixp=np.reshape(impixp,-1)
        impix=np.reshape(impix,-1)
        
        test = list(zip(impixp,impix))
        

        for i in range(len(test)):
            if test[i][0]!=test[i][1]:
                x=i//longueur
                y=i%longueur
                t.append((x,y))
        b.append(t)
    return b