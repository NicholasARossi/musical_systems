#single_song_analysis_driver
#extended analysis
def MA(filename):

    import numpy as np
    import midi
    import collections as cl
    import numpy as np

    
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
            time=np.linspace(0,len(note_array),len(note_array))
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
                time=np.linspace(0,len(note_array),len(note_array))
        
                
                
                
                b=np.roll(note_array,-1)
                intervals=b-note_array
                

                
                labels, values = zip(*cl.Counter(intervals).items())
                
                a=zip(*sorted(zip(values,labels)))
        
                interval_totals.append(intervals)
                note_totals.append(note_array)
                    
                        

                
                #Rotate through the song
                def chunks(l, n):
                    if n < 1:
                        n = 1
                    return [l[i:i + n] for i in range(0, len(l), n)]
                
                
                motif_range=np.arange(4,8)
                
                common_motifs=[]
                
                for count,k in enumerate(motif_range):
                    
                    marker=k
                    iterations=np.arange(marker)
                    target=''
                    total_counts=cl.Counter()
                    

                        
                    for x in iterations :     
                        groups=chunks(intervals[x:],marker)
                        group_strings=[''.join(([np.array_str(_2) for _2 in _])) for _ in groups]
                        total_counts=cl.Counter(group_strings)+total_counts
                        target='0'+target
                        del total_counts[target] 
                    if total_counts:  
                        common_motifs.append(total_counts.most_common(1)[0])
                
                    
                        
                unique_chars=[]               
                common_motifs_lists=[]
                
                for j in common_motifs:
                    s=j[0]
                
                
                    list_s=list(s)
                    for idx,x in enumerate(list_s):
                        if x=='-':
                            list_s[idx+1]="".join([list_s[idx],list_s[idx+1]])
                            list_s.remove("-")
                
                        
                    common_motifs_lists.append(list_s)
                    a=np.asarray(list_s)
                    a=np.unique(a)
                    unique_chars.append(len(a))
                    
                
                #so here's what we have now - we've got the list of motifs, and how unique each of them is, now we'll multiply their uniqueness by the frequncy and see if we get our match
                
                occurances=[]  
                
                for i in common_motifs:
                    b = [str(k[0]) for k in most_common]
                    
                    if i:
                        if i[1] < 80:
                           
                            if i[1] >10:
                                
                                
                                if i[0] not in  b:
                                   
                                    
                                    most_common.append(i)
        

    for j in most_common:
        s=j[0]
        list_s=list(s)
        for idx,x in enumerate(list_s):
                if x=='-':
                    list_s[idx+1]="".join([list_s[idx],list_s[idx+1]])
                    list_s.remove("-")
            
                    
        common_motifs_lists.append(list_s)
        a=np.asarray(list_s)
        a=np.unique(a)
        unique_chars.append(len(a))  
    final_motif=[]                     
    occurances=[]  
 
    for i in most_common:
        
        occurances.append(i[1])
            
        impact_factor=[a*b for a,b in zip(occurances,unique_chars)]
            
            
        indices = [i for i, x in enumerate(impact_factor) if x == max(impact_factor)]
       



    if indices:        
        final_motif=most_common[indices[0]]  
        final_motif_int=common_motifs_lists[indices[0]]
    else:
        final_motif=most_common[0]
        final_motif_int=common_motifs_lists[0]
    T2 = [int(_) for _ in final_motif_int]
    final_motif_notes=[60]
    for idx,i in enumerate(T2):
        new_note=i+final_motif_notes[idx]
        final_motif_notes.append(new_note)
        

    
            
            
           
    return final_motif_notes  
if __name__ == "__main__": MA('toto-africa.mid')