#later will be populated with actual gpio logic
#needs list of tracks
#NEEDS UPDATE WITH GPIO AND TRACKS
import random

def pollgpio(gpio):
    return bool(random.getrandbits(1))
    #return True

#def set_volume(vol, tracknum):
    #do something here
    #print(vol)
    #print(tracknum)

def mainloop_tester(b):
    max_volume = 1
    t1 = 0
    t2 = 0
    t3 = 0
    t4 = 0
    t5 = 0
    tracks = [t1, t2, t3, t4, t5]
    for q in range(100):
        for x in range(5):
            #y = tracks[x]
            if b:
                if tracks[x] < max_volume:
                    #y = y + .01
                    tracks[x] = tracks[x] + .01
                    if tracks[x] > 1:
                        tracks[x] = 1                      
            else:
                if tracks[x] > 0:
                   tracks[x] = tracks[x] - .01
            #set_volume(tracks[x], x)  
    return tracks
def mainloop():
    max_volume = 1
    t1 = 0
    t2 = 0
    t3 = 0
    t4 = 0
    t5 = 0
    tracks = [t1, t2, t3, t4, t5]
    while True:
        for x in range(5):
            #y = tracks[x]
            if pollgpio(x):
                if tracks[x] < max_volume:
                    #y = y + .01
                    tracks[x] = tracks[x] + .01
            else:
                if tracks[x] > 0:
                   tracks[x] = tracks[x] - .01
            set_volume(tracks[x], x)  
    return tracks
