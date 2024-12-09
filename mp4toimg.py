import cv2
import os
from tqdm.auto import tqdm

def video_to_frames(video:str, path_output_dir:str, num_FPS:int, extention: str):

    vidcap = cv2.VideoCapture(video)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    frames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT) 
    count = 0
    count_saved=0
    mod=int(fps/num_FPS)

    for filename in os.listdir(path_output_dir):
        os.remove(path_output_dir + "/" + filename)
    print("Dossier vidéo vidé")

    p_bar=tqdm(total=int(frames/mod),desc="loading")

    while vidcap.isOpened():
        success, image = vidcap.read()
        if not success:
            break
        if count%mod==0:
            cv2.imwrite(os.path.join(path_output_dir, '%d'+extention) % count_saved, image)
            count_saved+=1
            p_bar.update(1)
        count+=1
    p_bar.close()

    cv2.destroyAllWindows()
    vidcap.release()
    print("Finie")