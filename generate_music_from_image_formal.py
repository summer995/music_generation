#from sys import path
#path.append(r"/home/xiatian/music_generation/")
from go_svm import *
from music_function import *
from image_extract import *
#from compare_images import *
import os


if __name__ == "__main__":

    #extract image from the video
    video_name = "/home/xiatian/music_generation/test.mp4"
    flame_interval = 16.0
    picture_dir = "/home/xiatian/music_generation/test_image/"
    flame_extract(video_name,flame_interval,picture_dir)

    #get the emotion of every picture in picture_dir
    output_dir = "/home/xiatian/music_generation/"
    emotion_list = predict_emotion(picture_dir)
    print emotion_list

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
    generate_music_from_moodList(mood_list,part_duration,mode1,output_dir)
    print "genreate all piano music************************************"
    generate_music_from_moodList(mood_list,part_duration,mode2,output_dir)
    print "genreate mix piano and guitar music************************************"
    generate_music_from_moodList(mood_list,part_duration,mode3,output_dir)

    print "*********************************************************************"
    print "picture dir: " + picture_dir
    print "ouput music dir: " + output_dir

    video_name = "/home/xiatian/music_generation/test.mp4"
    print "compound the video and audio................."
    os.system("ffmpeg -i "+video_name+" -vcodec copy -an temp.mp4")
    os.system("ffmpeg -i temp.mp4 -i "+output_dir+"GenerateMusic_all_guitar.wav -vcodec copy -acodec copy output_all_guitar.avi")
    os.system("ffmpeg -i temp.mp4 -i "+output_dir+"GenerateMusic_all_piano.wav -vcodec copy -acodec copy output_all_piano.avi")
    os.system("ffmpeg -i temp.mp4 -i "+output_dir+"GenerateMusic_mix_guitar_and_piano.wav -vcodec copy -acodec copy output_mix_guitar_and_piano.avi")
    os.remove("temp.mp4")
    print "end****************************"
    print "video is in: "+ output_dir

