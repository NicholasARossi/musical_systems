#Analyze Scraped Data
import final_motif_analysis
import os
import time
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
interval_meta_total=[]
note_meta_total=[]
t = time.time()
final_motifs_meta=[]
for filename in os.listdir('files'):
    if filename!='.DS_Store':
        final_motif=[]
        final_motif_int=[]
        
        try:
            final_motif_notes=final_motif_analysis.MA('files/'+filename)
            final_motifs_meta.append(final_motif_notes)



            

        except: # catch *all* exceptions
            print(filename, " has failed")
      
elapsed = time.time() - t
print elapsed


np.save('final_motif_meta',final_motifs_meta)


