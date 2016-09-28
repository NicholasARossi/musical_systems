#extended analysis
def MA(filename):
    #### This function accepts one midi file and isolates each voice to find the melodies - isolates the notes and motifs within
    import midi
    import collections as cl
    import numpy as np

    
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
    meta_common_motifs = []
    meta_common_motif_beats = []
    meta_common_motif_counts = []
    #we evaluate each individual track
    for x,track in enumerate(pattern):
    
        ticks=[]
        ticksoff=[]
        notes=[]
    
        
        for event in track:
            if isinstance(event, midi.NoteOnEvent): # check that the current event is a NoteEvent, otherwise it won't have the method get_pitch() and we'll get an error
                if event.data[1]!=0:
                    if event.channel!=9:
    
    
                        notes.append(event.get_pitch())
                        ticks.append(event.tick)
        if ticks:
            complete=zip(ticks,notes)
            for item in complete:
                if item[0]==0:
                    complete.remove(item)



            all_voices[x]=complete


    for voice in all_voices :
        if voice:

    
            notes = [int(i[1]) for i in voice]
            beats = [int(i[0]) for i in voice]
            note_array = np.asarray(notes)
            time=np.linspace(0,len(note_array),len(note_array))




            b=np.roll(note_array,-1)
            intervals=b-note_array

            
            labels, values = zip(*cl.Counter(intervals).items())
            
            a=zip(*sorted(zip(values,labels)))
    
            interval_totals.append(intervals)
            note_totals.append(note_array)

            
            def chunks(l, n):
                if n < 1:
                    n = 1
                return [l[i:i + n] for i in range(0, len(l), n)]
            
            
            motif_range=np.arange(4,12)
            
            common_motifs=[]
            common_motif_beats=[]
            common_motif_counts=[]
            for count,k in enumerate(motif_range):
                
                marker=k
                iterations=np.arange(marker)
                target=''
                total_counts=cl.Counter()

                    
                for x in iterations :     
                    groups=chunks(notes[x:],marker)
                    beat_groups = chunks(beats[x:], marker)
                    beat_group_strings=[str(group) for group in beat_groups]
                    group_strings=[str(group) for group in groups]
                    total_counts=cl.Counter(zip(group_strings,beat_group_strings))+total_counts
                    target='0'+target
                    del total_counts[target]
                breaker=0
                n=0
                while breaker==0:
                    if n==len(total_counts.most_common()):
                        breaker=1
                    elif np.count_nonzero(np.asarray(total_counts.most_common()[n][0][0][1:-1].split(',')).astype(np.float))==0:
                        n=n+1
                    else:
                        common_motifs.append(np.asarray(total_counts.most_common()[n][0][0][1:-1].split(',')).astype(np.float))
                        common_motif_beats.append(np.asarray(total_counts.most_common()[n][0][1][1:-1].split(',')).astype(np.float))
                        common_motif_counts.append(total_counts.most_common()[n][1])
                        breaker=1
            meta_common_motif_beats=meta_common_motif_beats+common_motif_beats
            meta_common_motifs=meta_common_motifs+common_motifs
            meta_common_motif_counts=meta_common_motif_counts+common_motif_counts

    return meta_common_motifs,meta_common_motif_counts,meta_common_motif_beats
if __name__ == "__main__": main()