#Driver for extracting note interval data
import interval_note_analysis
import os
import time
import numpy as np

interval_meta_total=[]
note_meta_total=[]
t = time.time()
for filename in os.listdir('files'):
    if filename!='.DS_Store':
        final_motif=[]
        final_motif_int=[]
        
        try:
            [interval_totals,note_totals ]=interval_note_analysis.MA('files/'+filename)
            note_totals=np.concatenate(note_totals)
            interval_totals=np.concatenate(interval_totals)
            interval_meta_total.append(interval_totals)
            note_meta_total.append(note_totals)


        except: # catch *all* exceptions
            print(filename, " has failed")
      
elapsed = time.time() - t
print elapsed

song_note_meta_array=note_meta_total
song_interval_meta_array=interval_meta_total
note_meta_total=np.concatenate(note_meta_total)
interval_meta_total=np.concatenate(interval_meta_total)


vect=interval_meta_total
np.save('interval_meta_total',vect)
vect=note_meta_total
np.save('note_meta_total', vect)



