import os

def flame_extract(video_name,flame_interval,output_dir):
    cmd = "ffmpeg -i " + video_name + " 2>&1 | grep 'Duration' | cut -d ' ' -f 4 | sed s/,//"
    length = os.popen(cmd).read()
    length_0 = length.split(":")
    video_length = float(length_0[1])*60 + float(length_0[2])
    print "video length is: " + str(video_length) + "s"

    r = str(float(1.0/flame_interval))

    #os.system("mkdir test")

    print "ffmpeg -i " + video_name + " -f image2 -ss 0 -r " + r + " "+ output_dir +"test-%03d.jpg "

    os.system("ffmpeg -i " + video_name + " -f image2 -ss 0 -r " + r + " "+ output_dir +"test-%03d.jpg ")



    return video_length,length


if __name__ == "__main__":
    video_name = "test.mp4"
    flame_interval = 1.0
    output_dir = "/home/xiatian/music_generation/test_image/"
    video_length = flame_extract(video_name,flame_interval,output_dir)




