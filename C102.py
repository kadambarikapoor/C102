from os import name
import cv2
import dropbox
import time 
import random

start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"    
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    acces_token="sl.AxNAzKIwzmaKxtFI9G-c1G6JCKTpDG2HMVRQG6GqyPwXQU34nKtYlpe_TtAXmBNIq6wnWCgnO9w81XA2a6GOPzSVFTA-H5jR69ji38_MtLdR2gyav5INVm3WXRxOQZoTpNb731M"
    file=img_name
    file_from=file
    file_to="/testfolder1/"+(img_name)
    dbx=dropbox.Dropbox(acces_token)
    with open(file_from, 'rb')as f:
        dbx.files_upload(f.read(),file_to, mode=dropbox.files.WriteMode.overwrite)
        print("fileuploaded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)

main()