#from sys import path
#path.append(r"/home/xiat/music_generation/")
from go_svm import *
from music_function import *
from image_extract import *
from compare_images import *
from video_frequence_detect import *
import os


if __name__ == "__main__":
    #extract image from the video
    #video_name = "/home/xiat/music_generation/test10.mp4"
    video_name = sys.argv[1]
    flame_interval = 1.0
    picture_dir = "/home/xiat/music_generation/test_image/"
    os.system("rm "+ picture_dir + "*")
    video_length, length = flame_extract(video_name,flame_interval,picture_dir)

    mood_duration,frame = extract_key_frame_time(picture_dir)
    mood_duration.append(video_length - sum(mood_duration))

    for i in mood_duration:
        print i
    for i in frame:
        print i

    #get the emotion of every picture in picture_dir
    output_dir = "/home/xiat/music_generation/" + video_name.split("/")[-1]
    os.mkdir(output_dir)

    #predict emotion by GoogleNet and svm classfier
    emotion_list = predict_emotion(picture_dir)
    print emotion_list
    #extract the video frame change frequence feature
    video_frequence_feature = compute_frequence_feature(mood_duration,video_name)
    print video_frequence_feature

    if len(video_frequence_feature) < len(emotion_list):
        print "error: video frequence feature length is less than emotion list!!!!!!!!!!!"

    frequence_weight = 0.3
    #add the predicted emotion and the frequence feature
    for index, emotion in enumerate(emotion_list):
        emotion_list[index] += video_frequence_feature[index] * frequence_weight
        print emotion_list[index]


    #transform the emotion into mood list
    mood_list = []
    for emotion in emotion_list:
        mood = get_mood_from_1Dcoordinate(emotion)
        mood_list.append(mood)
    print mood_list

    part_duration = 16.0
    mode1 = "all_guitar"
    mode2 = "all_piano"
    mode3 = "mix_guitar_and_piano"
    print "genreate all guitar music**********************************************"
    generate_music_from_moodList_with_time(mood_list,part_duration,mood_duration,mode1,output_dir)
    print "genreate all piano music************************************"
    generate_music_from_moodList_with_time(mood_list,part_duration,mood_duration,mode2,output_dir)
    print "genreate mix piano and guitar music************************************"
    generate_music_from_moodList_with_time(mood_list,part_duration,mood_duration,mode3,output_dir)

    print "*********************************************************************"
    print "picture dir: " + picture_dir
    print "ouput music dir: " + output_dir

    length = length.strip("\n")
    #video_name = "/home/xiat/music_generation/test.mp4"
    print "compound the video and audio................."
    os.system("ffmpeg -i "+video_name+" -vcodec copy -an temp.mp4")
    os.system("ffmpeg -i "+output_dir+"/GenerateMusic_all_guitar.wav -ss 00:00:00 -t "+length+" -f mp3 -acodec libmp3lame -y "+output_dir+"/GenerateMusic_all_guitar.mp3")
    os.system("ffmpeg -i "+output_dir+"/GenerateMusic_all_piano.wav -ss 00:00:00 -t "+length+" -f mp3 -acodec libmp3lame -y "+output_dir+"/GenerateMusic_all_piano.mp3")
    os.system("ffmpeg -i "+output_dir+"/GenerateMusic_mix_guitar_and_piano.wav -ss 00:00:00 -t "+length+" -f mp3 -acodec libmp3lame -y "+output_dir+"/GenerateMusic_mix_guitar_and_piano.mp3")
    os.system("ffmpeg -i temp.mp4 -i "+output_dir+"/GenerateMusic_all_guitar.mp3 -vcodec copy -acodec copy " + output_dir + "/output_all_guitar.avi -y")
    os.system("ffmpeg -i temp.mp4 -i "+output_dir+"/GenerateMusic_all_piano.mp3 -vcodec copy -acodec copy " + output_dir + "/output_all_piano.avi -y")
    os.system("ffmpeg -i temp.mp4 -i "+output_dir+"/GenerateMusic_mix_guitar_and_piano.mp3 -vcodec copy -acodec copy " + output_dir + "/output_mix_guitar_and_piano.avi -y")
    os.remove("temp.mp4")
    os.system("rm "+ output_dir +"/*.wav")
    print "end****************************"
    print "video is in: "+ output_dir

    #os.system("scp -r "+output_dir+" root@172.16.3.38:/var/www/File")

    #os.system("scp /home/xiat/music_generation/end root@172.16.3.38:/var/www/File/"+video_name.split("/")[-1])
