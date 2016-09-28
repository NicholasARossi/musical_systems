#single_song_analysis_driver
#extended analysis
def MA(filename):

    import numpy as np
    import midi
    import collections as cl
    import pdb
    import time
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.stats import powerlaw
    import powerlaw as pl
    import scipy 
    import matplotlib.mlab as mlab
    import re
    import itertools
    import string
    
    from scipy.cluster.vq import kmeans, vq
    
    
    most_common=[]  
    most_common=[]
    interval_totals=[]
    note_totals=[]               
    pattern = midi.read_midifile(filename)
    #track = midi.Track(pattern)
    #track[2]=[]
    
    ticks=[]
    notes=[]
    num_tracks=len(pattern)
    
    from itertools import repeat
    all_voices = [[] for i in repeat(None, num_tracks)]
    
    
    #total_list=[]
    #we evaluate each individual track
    for x,track in enumerate(pattern):
    
        ticks=[]
        notes=[]
    
        
        for event in track:
            if isinstance(event, midi.NoteOnEvent): # check that the current event is a NoteEvent, otherwise it won't have the method get_pitch() and we'll get an error
                #if event.data[1]!=0:
                if event.channel!=9:
                    temp=event.get_pitch()   
                    notes.append(temp)
                    ticks.append(event.tick)
        
        if ticks:
            novel_ticks=[]
            for tick in ticks:
                novel_ticks.append(round(tick, -2))
                
            ticks=novel_ticks
    
            progressive_ticks=[]
            progressive_ticks=np.cumsum(ticks)
            notes_clean=[]
            (ticks_sorted,notes_sorted) = zip(*sorted(zip(progressive_ticks,notes)))
            complete=zip(notes_sorted,ticks_sorted);
            clean_complete=list(cl.OrderedDict.fromkeys(complete))
            all_voices[x]=clean_complete
            #total_list[x]=clean_complete
            #total_list[x]=clean_complete
            
          
    for idx,voice in enumerate(all_voices) :
        temp_voice=voice
        if voice:
            last = voice[-1] 
            #remove simultaneous notes (no chords)
            for i in range(len(voice)-2,-1, -1):
                if last[1] == voice[i][1]:
                    del voice[i]
                else:
                    last=voice[i]
        
    
            
    
            notes = [int(i[0]) for i in voice]
            ticks = [int(i[1]) for i in voice]
            note_array = np.asarray(notes)
            tick_array = np.asarray(ticks)
            if np.ptp(note_array) >24:
                centers, _ = kmeans(note_array, 2, iter=100)
                cluster, _ = vq(note_array, centers)
                all_voices[idx]=zip(note_array[cluster==0],tick_array[cluster==0])
                all_voices.append(zip(note_array[cluster==1],tick_array[cluster==1]))
                
         
        for voice in all_voices:  
            if voice:
                last = voice[-1] 
                #remove simultaneous notes (no chords)
                for i in range(len(voice)-2,-1, -1):
                    if last[1] == voice[i][1]:
                        del voice[i]
                    else:
                        last=voice[i]
            
        
                
        
                notes = [int(i[0]) for i in voice]
                note_array = np.asarray(notes)
        
                
                
                
                b=np.roll(note_array,-1)
                intervals=b-note_array
                
                
                
                
                #min_data=  np.min(intervals)
                #max_data= np.max(intervals)
                #bins = np.arange(min_data,max_data)
                #plt.hist(intervals,bins)
                #plt.ylabel('Interval Frequency')
                

        
                interval_totals.append(intervals)
                note_totals.append(note_array)
                    
                        
             
    
            
            
           
    return interval_totals,note_totals    
if __name__ == "__main__": MA()