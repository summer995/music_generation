from Nsound import *
import os
import random
curDir = os.chdir("/data/xiat/src/")


def make_pad (ins_kind,score,chord_duration):
    duration = chord_duration
    #define the numbered musical notation
    low = [0,261.63, 293.67, 329.6, 349.2, 391.99, 440, 493.88]
    mid = [0,523.2, 587.33, 659.25, 698.46, 738.99, 880, 987.76]
    hig = [0,1046.5, 1174.66, 1318.51, 1396.5, 1567.98, 1760, 1975.52]
    #define the base key of each chord
    C  = [ low[1], low[3], low[5]]
    Dm = [ low[2], low[4], low[6]]
    Em = [ low[3], low[5], low[7]]
    F  = [ low[4], low[6], mid[1]]
    G  = [ low[5], low[7], mid[2]]
    Am = [ low[6], mid[1], mid[3]]
    G7 = [ low[7], mid[2], mid[4]]
    #define frequency
    sr = 44100.0
    #define different AudioStream
    out1= AudioStream(sr, 2)
    out2= AudioStream(sr, 2)
    out3= AudioStream(sr, 2)
    out = [out1, out2, out3]
    #initial all the insruments
    organPipe = OrganPipe(sr)
    bass = GuitarBass(sr)
    slide = FluteSlide(sr)
    clarinet=Clarinet(sr)
    if ins_kind == "bass":
        #make the AudioStream from the music score
        for chord in score:
            if chord == "Am":
                for num in range(0,3): out[num]<<bass.play(duration,Am[num])
            if chord == "F":
                for num in range(0,3): out[num]<<bass.play(duration,F[num])
            if chord == "Dm":
                for num in range(0,3): out[num]<<bass.play(duration,Dm[num])
            if chord == "G":
                for num in range(0,3): out[num]<<bass.play(duration,G[num])
            if chord == "C":
                for num in range(0,3): out[num]<<bass.play(duration,C[num])
            if chord == "Em":
                for num in range(0,3): out[num]<<bass.play(duration,Em[num])
    elif ins_kind == "organPipe":
        #make the AudioStream from the music score
        for chord in score:
            if chord == "Am":
                for num in range(0,3): out[num]<<organPipe.play(duration,Am[num])
            if chord == "F":
                for num in range(0,3): out[num]<<organPipe.play(duration,F[num])
            if chord == "Dm":
                for num in range(0,3): out[num]<<organPipe.play(duration,Dm[num])
            if chord == "G":
                for num in range(0,3): out[num]<<organPipe.play(duration,G[num])
            if chord == "C":
                for num in range(0,3): out[num]<<organPipe.play(duration,C[num])
            if chord == "Em":
                for num in range(0,3): out[num]<<organPipe.play(duration,Em[num])
    elif ins_kind == "slide":
        #make the AudioStream from the music score
        for chord in score:
            if chord == "Am":
                for num in range(0,3): out[num]<<slide.play(duration,Am[num])
            if chord == "F":
                for num in range(0,3): out[num]<<slide.play(duration,F[num])
            if chord == "Dm":
                for num in range(0,3): out[num]<<slide.play(duration,Dm[num])
            if chord == "G":
                for num in range(0,3): out[num]<<slide.play(duration,G[num])
            if chord == "C":
                for num in range(0,3): out[num]<<slide.play(duration,C[num])
            if chord == "Em":
                for num in range(0,3): out[num]<<slide.play(duration,Em[num])
    elif ins_kind == "clarinet":
        #make the AudioStream from the music score
        for chord in score:
            if chord == "Am":
                for num in range(0,3): out[num]<<clarinet.play(duration,Am[num])
            if chord == "F":
                for num in range(0,3): out[num]<<clarinet.play(duration,F[num])
            if chord == "Dm":
                for num in range(0,3): out[num]<<clarinet.play(duration,Dm[num])
            if chord == "G":
                for num in range(0,3): out[num]<<clarinet.play(duration,G[num])
            if chord == "C":
                for num in range(0,3): out[num]<<clarinet.play(duration,C[num])
            if chord == "Em":
                for num in range(0,3): out[num]<<clarinet.play(duration,Em[num])

    out1.add(out2,0.0)
    out1.add(out3,0.0)

    return out1

def make_guitar_acompany(score,chord_duration,rhythm=4):
    #compute the duration of each string
    string_len = float(chord_duration) / rhythm
    #define the chord of guitar
    guitar_C  = [0,329.6,261.6,196.0,164.8,130.8,98.0]
    guitar_Dm = [0,349.2,293.7,220.0,146.8,110.0,82.4]
    guitar_Em = [0,329.6,246.9,196.0,164.8,123.5,82.4]
    guitar_F =  [0,349.2,261.6,220.0,174.6,130.8,87.3]
    guitar_G =  [0,392.0,246.9,196.0,146.8,123.5,98.0]
    guitar_Am = [0,329.6,261.6,220.0,164.8,110.0,82.4]
    guitar_G7 = [0,349.2,246.9,196.0,146.8,123.5,98.0]
    #define the acompanyment pattern of guitar
    pattern_1 = [6, 3, 2, 3, 1, 3, 2, 3]# G G7 Em
    pattern_2 = [5, 3, 2, 3, 1, 3, 2, 3]# C Am
    pattern_3 = [4, 3, 2, 3, 1, 3, 2, 3]# F Dm
    pattern_4 = [6, 3, 2, 3]# Em G G7
    pattern_5 = [5, 3, 2, 3]# C Am
    pattern_6 = [4, 3, 2, 3]# Dm F
    #define frequency
    sr = 44100.0
    #initial bass guitar
    bass = GuitarBass(sr)
    #initial tha acompany AudioStream
    guitar_acompany = AudioStream(sr , 2)
    if rhythm == 4:
        for chord in score:
            if chord == "Am":
                for string in pattern_5:
                    guitar_acompany<<bass.play(string_len,guitar_Am[string])
            if chord == "F":
                for string in pattern_6:
                    guitar_acompany<<bass.play(string_len,guitar_F[string])
            if chord == "Dm":
                for string in pattern_6:
                    guitar_acompany<<bass.play(string_len,guitar_Dm[string])
            if chord == "G":
                for string in pattern_4:
                    guitar_acompany<<bass.play(string_len,guitar_G[string])
            if chord == "C":
                for string in pattern_5:
                    guitar_acompany<<bass.play(string_len,guitar_C[string])
            if chord == "Em":
                for string in pattern_4:
                    guitar_acompany<<bass.play(string_len,guitar_Em[string])
    elif rhythm == 8:
        for chord in score:
            if chord == "Am":
                for string in pattern_2:
                    guitar_acompany<<bass.play(string_len,guitar_Am[string])
            if chord == "F":
                for string in pattern_3:
                    guitar_acompany<<bass.play(string_len,guitar_F[string])
            if chord == "Dm":
                for string in pattern_3:
                    guitar_acompany<<bass.play(string_len,guitar_Dm[string])
            if chord == "G":
                for string in pattern_1:
                    guitar_acompany<<bass.play(string_len,guitar_G[string])
            if chord == "C":
                for string in pattern_2:
                    guitar_acompany<<bass.play(string_len,guitar_C[string])
            if chord == "Em":
                for string in pattern_1:
                    guitar_acompany<<bass.play(string_len,guitar_Em[string])

    return guitar_acompany

def getPatternNum(total_duration,sample):
    sample_duration = sample.getDuration()
    total_num = float(total_duration) / sample_duration
    total_num = int(total_num + 0.5)
    return total_num

#formal function to make drum acompany
def make_drum_acompmay(score, chord_duration,drum_pattern):
    #define frequency
    sr = 44100.0
    #initial drum acompany AudioStream
    drum_acompany = AudioStream(sr, 2)
    #initial all the drums patterns
    rock = AudioStream("./drum_pattern/rock.wav")#2
    rock_high = AudioStream("./drum_pattern/rock_high.wav")#2
    Rumba = AudioStream("./drum_pattern/Rumba.wav")#2
    Tango = AudioStream("./drum_pattern/Tango.wav")#2
    pattern5 = AudioStream("./drum_pattern/16_5.wav")#2
    pattern6 = AudioStream("./drum_pattern/12_4.wav")#1.5
    pattern7 = AudioStream("./drum_pattern/12_3.wav")#1.5
    slow1 = AudioStream("./drum_pattern/slow1.wav")#1
    slow2 = AudioStream("./drum_pattern/slow2.wav")#1
    slow3 = AudioStream("./drum_pattern/slow3.wav")#1

    drum_duration = 2.0
    speed = chord_duration / drum_duration
    total_drum_num = speed * len(score)
    total_drum_num = int(total_drum_num + 0.5)

    if drum_pattern == "rock":
        for i in range(0,total_drum_num): drum_acompany<<rock
    elif drum_pattern == "Rumba":
        for i in range(0,total_drum_num): drum_acompany<<Rumba
    elif drum_pattern == "rock_high":
        for i in range(0,total_drum_num): drum_acompany<<rock_high
    elif drum_pattern == "Tango":
        for i in range(0,total_drum_num): drum_acompany<<Tango
    elif drum_pattern == "slow1":
        for i in range(0,total_drum_num): drum_acompany<<slow1
    elif drum_pattern == "slow2":
        for i in range(0,total_drum_num): drum_acompany<<slow2
    elif drum_pattern == "slow3":
        for i in range(0,total_drum_num): drum_acompany<<slow3

    return drum_acompany

def make_drum_pattern(total_duration,drum_pattern):
    #define frequency
    sr = 44100.0
    #initial drum acompany AudioStream
    acompany = AudioStream(sr, 2)
    pattern_name = []
    dir = "/data/xiat/src/drum/"
    os.chdir(dir)
    for filename in os.listdir(dir):
        pattern_name.append(filename.split(".")[0])
    if drum_pattern in pattern_name:
        pattern = AudioStream(drum_pattern + ".wav")
        total_num = getPatternNum(total_duration,pattern)
        for i in range(0,total_num): acompany<<pattern
    return acompany




def make_bass_pattern(total_duration,bass_pattern):
    #define frequency
    sr = 44100.0
    #initial drum acompany AudioStream
    acompany = AudioStream(sr, 2)
    pattern_name = []
    dir = "/data/xiat/src/bass/"
    os.chdir(dir)
    for filename in os.listdir(dir):
        pattern_name.append(filename.split(".")[0])
    if bass_pattern in pattern_name:
        pattern = AudioStream(bass_pattern + ".wav")
        total_num = getPatternNum(total_duration,pattern)
        for i in range(0,total_num): acompany<<pattern
    return acompany

def make_high_loop_pattern(total_duration,loop_pattern):
    #define frequency
    sr = 44100.0
    #initial drum acompany AudioStream
    acompany = AudioStream(sr, 2)
    pattern_name = []
    dir = "/data/xiat/src/high_loop/"
    os.chdir(dir)
    for filename in os.listdir(dir):
        pattern_name.append(filename.split(".")[0])
    if loop_pattern in pattern_name:
        pattern = AudioStream(loop_pattern + ".wav")
        total_num = getPatternNum(total_duration,pattern)
        for i in range(0,total_num): acompany<<pattern
    return acompany




def make_acoustic_loop_pattern(total_duration,loop_pattern,mode):
    #define frequency
    sr = 44100.0
    #initial drum acompany AudioStream
    acompany = AudioStream(sr, 2)
    pattern_name = []
    src_Dir = "/data/xiat/src/"
    acoustic_loop_Dir = src_Dir + "acoustic_loop_mix_guitar_and_piano"
    if mode == "all_guitar":
        acoustic_loop_Dir = src_Dir + "acoustic_loop_guitar"
    elif mode == "all_piano":
        acoustic_loop_Dir = src_Dir + "acoustic_loop_piano"
    elif mode == "mix_guitar_and_piano":
        acoustic_loop_Dir = src_Dir + "acoustic_loop_mix_guitar_and_piano"


    dir = acoustic_loop_Dir
    os.chdir(dir)
    for filename in os.listdir(dir):
        pattern_name.append(filename.split(".")[0])
    if loop_pattern in pattern_name:
        pattern = AudioStream(loop_pattern + ".wav")
        total_num = getPatternNum(total_duration,pattern)
        for i in range(0,total_num): acompany<<pattern
    return acompany


def generate_music_part(part_duration,mode,
                   drum_pattern,drum_acompany_volume,
                   bass_pattern,bass_acompany_volume,
                   high_loop_pattern,high_loop_acompany_volume,
                   acoustic_pattern,acoustic_sound_volume,
                   reverberation=True):
    sr = 44100.0
    out = AudioStream(sr,2)
    total_duration = part_duration
    if drum_pattern != "silence":
        drum_acompany = make_drum_pattern(total_duration,drum_pattern)
        drum_acompany.normalize()
        drum_acompany *= drum_acompany_volume
        out.add(drum_acompany, 0.0)
    else: pass
    if bass_pattern != "silence":
        bass_acompany = make_bass_pattern(total_duration,bass_pattern)
        bass_acompany.normalize()
        bass_acompany *= bass_acompany_volume
        out.add(bass_acompany, 0.0)
    else: pass
    if high_loop_pattern != "silence":
        high_loop_acompany = make_high_loop_pattern(total_duration,high_loop_pattern)
        high_loop_acompany.normalize()
        high_loop_acompany *= high_loop_acompany_volume
        out.add(high_loop_acompany, 0.0)
    else: pass
    if acoustic_pattern != "silence":
        acoustic_sound = make_acoustic_loop_pattern(total_duration,acoustic_pattern,mode)
        acoustic_sound.normalize()
        acoustic_sound *= acoustic_sound_volume
        out.add(acoustic_sound, 0.0)
    else: pass

    if reverberation == True:
        room = ReverberationRoom(sr, 0.60, 0.5, 1.0, 100.0)
        out = 0.5 * room.filter(out)
    else:pass

    return out

def smooth(input):
    duration = input.getDuration()

    # Create a low pass filter with a kernel of 256 terms.
    lpf = FilterLowPassFIR(input.getSampleRate(), 256, 100)

    # Create a buffer that will hold cut off frequencies.
    frequencies = Buffer()

    # Fill it with two lines
    sin = Sine(input.getSampleRate())

    frequencies << sin.drawLine(0.5 * duration, 8000, 200) \
                << sin.drawLine(0.5 * duration, 200, 8000)

    # Filter it.
    output = lpf.filter(input, frequencies)

    return output

def smooth_connect_music(music_set):
    sr = 44100
    #temp = AudioStream(sr, 2)
    out = AudioStream(sr, 2)
    #part_duration = 16
    smooth_duration = 3.0
    for index,music_part in enumerate(music_set):
        part_duration = music_part.getDuration()
        if index == 0:
            temp = AudioStream(sr, 2)
            temp<<music_set[index].substream(part_duration-smooth_duration,smooth_duration)
            temp<<music_set[index+1].substream(0,smooth_duration)
            temp = smooth(temp)
            out<<music_set[index].substream(0,float(part_duration-smooth_duration))
            out<<temp
        if index > 0 and index < len(music_set)-1:
            temp = AudioStream(sr, 2)
            temp<<music_set[index].substream(part_duration-smooth_duration,smooth_duration)
            temp<<music_set[index+1].substream(0,smooth_duration)
            temp = smooth(temp)
            out<<music_set[index].substream(smooth_duration,float(part_duration-2*smooth_duration))
            out<<temp
        if index == len(music_set) -1:
            out<<music_set[index].substream(smooth_duration,float(part_duration-smooth_duration))
    return out

#to make the size of the music smaller
def downSampleRate2(out,sr):
    raw_sr = out.getSampleRate()
    out.setSampleRate(sr)
    out.speedUp(raw_sr/sr)
    return out




######################################################################################

def get_mood_from_2Dcoordinate(valence,arousal):
    mood = "neutral"
    if valence > 0.5 and arousal >0.5:
        mood = "excited"
    elif valence < -0.5 and arousal > 0.5:
        mood = "angry"
    elif valence > 0.5 and arousal < -0.5:
        mood = "serene"
    elif valence < -0.5 and arousal < -0.5:
        mood = "sad"
    else:
        pass
    return mood

def get_mood_from_1Dcoordinate(valence):
    mood = "neutral"
    if valence > 0.55 :
        mood = "happy"
    elif valence < 0.35:
        mood = "sad"

    return mood

def get_random(list):
    part = random.randint(0,len(list)-1)
    return list[part]

def get_mood_part(mood,dir):
    os.chdir(dir)
    mood_part = []
    for filename in os.listdir(dir):
        if filename.startswith(mood):
            mood_part.append(filename.split(".")[0])
    return mood_part


###############################################################

def generate_music_from_moodList(mood_list,part_duration,mode,output_dir):
    music_set = []

    src_Dir = "/data/xiat/src/"
    acoustic_loop_Dir = src_Dir +"acoustic_loop_mix_guitar_and_piano"
    if mode == "all_guitar":
        acoustic_loop_Dir = src_Dir + "acoustic_loop_guitar"
    elif mode == "all_piano":
        acoustic_loop_Dir = src_Dir + "acoustic_loop_piano"
    elif mode == "mix_guitar_and_piano":
        acoustic_loop_Dir = src_Dir + "acoustic_loop_mix_guitar_and_piano"
    else:
        print "No such mode: "+ mode
        print "mode choice: all_guitar,all_piano,mix_guitar_and_piano"

    high_loop_Dir = src_Dir + "high_loop"
    bass_Dir = src_Dir + "bass"
    drum_Dir = src_Dir + "drum"

    happy_acoustic_part = get_mood_part("happy",acoustic_loop_Dir)
    neutral_acoustic_part = get_mood_part("neutral",acoustic_loop_Dir)
    sad_acoustic_part = get_mood_part("sad",acoustic_loop_Dir)

    happy_drum_part = get_mood_part("happy",drum_Dir)
    neutral_drum_part = get_mood_part("neutral",drum_Dir)
    sad_drum_part = get_mood_part("sad",drum_Dir)

    for mood in mood_list:
        acoustic_part = []
        drum_part = []
        if mood == "happy":
            acoustic_part = happy_acoustic_part
            drum_part = happy_drum_part
        elif mood == "neutral":
            acoustic_part = neutral_acoustic_part
            drum_part = neutral_drum_part
        elif mood == "sad":
            acoustic_part = sad_acoustic_part
            drum_part = sad_drum_part

        drum_pattern = get_random(drum_part)
        acoustic_pattern = get_random(acoustic_part)
        print "drum pattern: " + drum_pattern
        print "acoustic pattern: " + acoustic_pattern
        part = generate_music_part(part_duration,mode,drum_pattern,0.8,
                                   "silence",0.5,"silence",0.5,
                                   acoustic_pattern,1.0)
        music_set.append(part)

    out = smooth_connect_music(music_set)
    os.chdir(output_dir)
    name = ""
    #for mood in mood_list:
    #    name += "_"+ mood
    name += "_" + mode
    out >> "GenerateMusic"+name+".wav"
####################################################################

def generate_music_from_moodList_with_time(mood_list,part_duration,mood_duration,mode,output_dir):
    music_set = []

    src_Dir = "/data/xiat/src/"
    acoustic_loop_Dir = src_Dir +"acoustic_loop_mix_guitar_and_piano"
    if mode == "all_guitar":
        acoustic_loop_Dir = src_Dir + "acoustic_loop_guitar"
    elif mode == "all_piano":
        acoustic_loop_Dir = src_Dir + "acoustic_loop_piano"
    elif mode == "mix_guitar_and_piano":
        acoustic_loop_Dir = src_Dir + "acoustic_loop_mix_guitar_and_piano"
    else:
        print "No such mode: "+ mode
        print "mode choice: all_guitar,all_piano,mix_guitar_and_piano"

    high_loop_Dir = src_Dir + "high_loop"
    bass_Dir = src_Dir + "bass"
    drum_Dir = src_Dir + "drum"

    happy_acoustic_part = get_mood_part("happy",acoustic_loop_Dir)
    neutral_acoustic_part = get_mood_part("neutral",acoustic_loop_Dir)
    sad_acoustic_part = get_mood_part("sad",acoustic_loop_Dir)

    happy_drum_part = get_mood_part("happy",drum_Dir)
    neutral_drum_part = get_mood_part("neutral",drum_Dir)
    sad_drum_part = get_mood_part("sad",drum_Dir)


    drum_volume = 0.8

    used_pattern = []



    for index,mood in enumerate(mood_list):
        acoustic_part = []
        drum_part = []
        if mood == "happy":
            acoustic_part = happy_acoustic_part
            drum_part = happy_drum_part
            drum_volume = 0.8
        elif mood == "neutral":
            acoustic_part = neutral_acoustic_part
            drum_part = neutral_drum_part
            drum_volume = 0.3
        elif mood == "sad":
            acoustic_part = sad_acoustic_part
            drum_part = sad_drum_part
            drum_volume = 0.1

        drum_pattern = get_random(drum_part)
        acoustic_pattern = get_random(acoustic_part)



        '''
        while drum_pattern in used_pattern:
            drum_pattern = get_random(drum_part)
        while acoustic_pattern in used_pattern:
            acoustic_pattern = get_random(acoustic_part)

        used_pattern.append(drum_pattern)
        used_pattern.append(acoustic_pattern)
        '''

        print "drum pattern: " + drum_pattern
        print "acoustic pattern: " + acoustic_pattern
        part = generate_music_part(part_duration,mode,drum_pattern,drum_volume,
                                   "silence",0.5,"silence",0.5,
                                   acoustic_pattern,1.0).substream(0.0,float(mood_duration[index]))
        while part.getDuration() < mood_duration[index]:
            #drum_pattern = get_random(drum_part)
            #acoustic_pattern = get_random(acoustic_part)
            print "drum pattern: " + drum_pattern
            print "acoustic pattern: " + acoustic_pattern
            part << generate_music_part(part_duration,mode,drum_pattern,drum_volume,
                                   "silence",0.5,"silence",0.5,
                                   acoustic_pattern,1.0)
        part = part.substream(0.0,float(mood_duration[index]))
        music_set.append(part)

    out = smooth_connect_music(music_set)
    os.chdir(output_dir)
    name = ""
    #for mood in mood_list:
    #    name += "_"+ mood
    name += "_" + mode
    out >> "GenerateMusic"+name+".wav"
####################################################################

if __name__ == "__main__":
    #show all the resource of music
    src_Dir = "/data/xiat/src/"
    #acoustic_loop_Dir = src_Dir + "acoustic_loop"
    high_loop_Dir = src_Dir + "high_loop"
    bass_Dir = src_Dir + "bass"
    drum_Dir = src_Dir + "drum"

    part_duration = 16.0
    mood_list = ["happy","neutral","happy","sad","neutral"]
    output_dir = "/home/xiat/music_generation/"
    mode1 = "all_guitar"
    mode2 = "all_piano"
    mode3 = "mix_guitar_and_piano"
    generate_music_from_moodList(mood_list,part_duration,mode1,output_dir)
    generate_music_from_moodList(mood_list,part_duration,mode2,output_dir)
    generate_music_from_moodList(mood_list,part_duration,mode3,output_dir)


    '''
    print "**************************************************************"
    print "acoustic choice:"
    print sorted(os.listdir(acoustic_loop_Dir))
    print "**************************************************************"
    print "high loop choice:"
    print sorted(os.listdir(high_loop_Dir))
    print "**************************************************************"
    print "bass choice:"
    print sorted(os.listdir(bass_Dir))
    print "**************************************************************"
    print "drum choice:"
    print sorted(os.listdir(drum_Dir))
    print "**************************************************************"
    '''
    '''
    #define the music score
    score = ["C", "G", "Am", "Em", "F", "Em", "F", "G" ]
    #the number of the chord
    chord_num = len(score)
    #define duration for each chord
    chord_duration = 2
    '''

    '''
    out1 = generate_music_part(part_duration=part_duration,
                         drum_pattern="fast2",drum_acompany_volume=0.4,
                         bass_pattern="silence",bass_acompany_volume=0.9,
                         high_loop_pattern="silence",high_loop_acompany_volume=0.5,
                         acoustic_pattern="happy_guitar4",acoustic_sound_volume=0.5,
                         reverberation=False)

    out2 = generate_music_part(part_duration=part_duration,
                         drum_pattern="fast1",drum_acompany_volume=0.4,
                         bass_pattern="silence",bass_acompany_volume=0.9,
                         high_loop_pattern="silence",high_loop_acompany_volume=0.5,
                         acoustic_pattern="happy_guitar5",acoustic_sound_volume=0.5,
                         reverberation=False)

    out3 = generate_music_part(part_duration=part_duration,
                         drum_pattern="fast4",drum_acompany_volume=0.4,
                         bass_pattern="silence",bass_acompany_volume=0.9,
                         high_loop_pattern="silence",high_loop_acompany_volume=0.5,
                         acoustic_pattern="happy_guitar6",acoustic_sound_volume=0.5,
                         reverberation=False)

    out4 = generate_music_part(part_duration=part_duration,
                         drum_pattern="fast5",drum_acompany_volume=0.4,
                         bass_pattern="silence",bass_acompany_volume=0.9,
                         high_loop_pattern="silence",high_loop_acompany_volume=0.5,
                         acoustic_pattern="happy_guitar7",acoustic_sound_volume=0.5,
                         reverberation=False)

    music_set = [out1,out2,out3,out4]
    out = smooth_connect_music(music_set)
    os.chdir("/home/xiat/nsound/")
    out >> "GenerateMusic.wav"
    '''


