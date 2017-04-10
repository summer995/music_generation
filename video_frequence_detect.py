import subprocess
import os

"""
Computer the time segmentation of a video.
Based on the HSI change frequence (a threshold is set) and the content change frequence
Return a list of all the time sec of the a video
"""
def get_time_sec(file_name, save_image=False):
    cmd = "scenedetect --input "+ file_name +" --detector content --threshold 10 -fs 2 -df 2"
    if save_image == True:
        cmd += " -si"
    output = subprocess.check_output(cmd, shell=True)
    time_sec = output.split("[PySceneDetect]")[-1].split(",")
    time_sec[0] = time_sec[0].split("\n")[-1]
    time_sec[-1] = time_sec[-1].split("\n")[0]

    output_time_sec =  []

    for time in time_sec:
        temp = time.split(":")
        time = float(temp[-1]) + float(temp[-2])*60
        #time = int(time+0.5)
        output_time_sec.append(time)

    output_time_sec = list(set(output_time_sec))

    output_time_sec.sort()

    return output_time_sec

"""
Compute the number of time sec between every key frame,
which is the frequence feature of the video.
Return the frame-changed frequence of an interval.
"""
def compute_interval_frequence(start_time,end_time,output_time_sec):
    if end_time < start_time:
        print "end time is less than start time"
    frame_num = 0
    for time_sec in output_time_sec:
        if time_sec <= float(end_time) and time_sec > float(start_time):
            frame_num += 1
    return float(frame_num) / (end_time - start_time)

"""
Compute the video frequence emotion feature.
"""
def compute_frequence_feature(mood_duration, file_name):
    print "*****************************************************"
    print "extract video frequence feature"
    output_time_sec = get_time_sec(file_name)

    start_time = 0
    end_time = 0

    #define the frequence emotion bound
    happy_bound = 0.5
    sad_bound = 0.1

    video_frequence_feature = []

    for duration in mood_duration:
        start_time = end_time
        end_time = start_time + duration
        interval_frequence = compute_interval_frequence(start_time,end_time,output_time_sec)
        video_frequence_feature.append(interval_frequence)
    return video_frequence_feature


if __name__ == "__main__":


    file_name = "test3.mp4"

    mood_duration = []
    for i in range(35):
        mood_duration.append(10)

    video_frequence_feature = compute_frequence_feature(mood_duration,file_name)

    print "************************************"

    for x in video_frequence_feature:
        print x
