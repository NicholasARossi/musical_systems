#printing the data
#This makes the final motif plot
import numpy as np
import matplotlib.pyplot as plt

final_motifs_meta=np.load('final_motif_meta.npy')
tableau20= [(46, 9, 39), (217, 0, 0),(255,45,0),(255,140,0),(4,117,111),(47,52,59),(52,152,219),(46, 9, 39), (217, 0, 0),(255,45,0),(255,140,0),(4,117,111),(47,52,59),(52,152,219)]
tableau20=tableau20[::-1]             
for i in range(len(tableau20)):  
    r, g, b = tableau20[i]  
    tableau20[i] = (r / 255., g / 255., b / 255.)
    
plt.rc('axes', color_cycle=tableau20)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.set_ylabel('Value of Note')
ax1.set_xlabel('Order of Note')
ax1.set_title('Meta Motifs')
for motif in final_motifs_meta:
    ax1.plot( motif,'o-',alpha=.2,linewidth=3.0)
    
plt.savefig('meta_motif_range.png', bbox_inches='tight' ,dpi=100)