import time,os
import subprocess

receive_file = "raw"

receive_folder = "/data/chencj/httpServer/"

def check_receive(pre_files):
    new_files = os.listdir(receive_folder)
    #print new_files
    if len(new_files) - len(pre_files) == 1:
        return True
    else:
        return False

def generate_music(receive_folder,new_file):
    #os.system("nohup python ../generate_music_from_image.py " +receive_folder + new_file)
    cmd = "python ../generate_music_from_image.py " +receive_folder + new_file
    log = open(new_file.split(".")[0]+"_log.txt",'w')
    subprocess.Popen(["python","../generate_music_from_image.py",receive_folder + new_file],stdout=log)



    #subprocess.Popen(["nohup","python","../generate_music_from_image.py",receive_folder + new_file,">",new_file.split(".")[0]+".txt"])


def main_thread():
    while True:
        files = os.listdir(receive_folder)
        print time.time()
        time.sleep(1)
        if check_receive(files):
            new_files = os.listdir(receive_folder)
            new_file = new_files[len(new_files)-1]
            generate_music(receive_folder,new_file)
        else:
            print "waiting for files"


if __name__ == "__main__":
    main_thread()




