#analysis
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import matplotlib.mlab as mlab

song_note_meta_array=np.load('song_note_meta_array.npy')
song_interval_meta_array=np.load('song_interval_meta_array.npy')

note_meta_total=np.concatenate(song_note_meta_array)
interval_meta_total=np.concatenate(song_interval_meta_array)

#plotting total array

interval_meta_total=interval_meta_total[interval_meta_total<24]
interval_meta_total=interval_meta_total[interval_meta_total>-24]

fig1 = plt.figure()
ax1 = fig1.add_subplot(3,1,1)
hist, bins = np.histogram(interval_meta_total,bins=np.arange(-24,25,1),normed=1)

width = 1 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width,fc='gray',alpha=0.7)

density = scipy.stats.gaussian_kde(interval_meta_total)

density.covariance_factor = lambda : .1
density._compute_covariance()
x_range=np.linspace(-24,24,200)
plt.plot(x_range, density(x_range),color='orangered',linewidth=3.0)

plt.ylabel('Normalized Frequency of Interval')
plt.xlabel('Interval')
plt.title('Meta Interval Distribution')

ax1.set_xlim([-24, 24]) 

















#dist = getattr(scipy.stats, 'expon')
#param = dist.fit(frequency)
#
#pdf_fitted=dist.pdf(x,loc=param[0],scale=param[1])
#plot(x,pdf_fitted)


ax2 = fig1.add_subplot(2,1,2)
h = plt.hist(note_meta_total,bins=np.arange(min(note_meta_total),max(note_meta_total),1),fc='gray',alpha=0.7,normed=1)
density = scipy.stats.gaussian_kde(note_meta_total)

density.covariance_factor = lambda : .1
density._compute_covariance()
x_range=np.linspace(min(note_meta_total),max(note_meta_total),100)
plt.plot(x_range, density(x_range),color='orangered',linewidth=4.0)


ax2.set_xlim(min(note_meta_total),max(note_meta_total)) 
plt.ylabel('Normalized Frequency of Note')
plt.xlabel('Note')
plt.title('Meta Note Distribution')

plt.savefig('Total_interval_distribution', bbox_inches='tight' ,dpi=100)



fig2 = plt.figure()
ax3 = fig1.add_subplot(3,1,2)
hist, bins = np.histogram(interval_meta_total,bins=np.arange(-24,25,1),normed=0)
collected=zip(hist,bins);
collected=sorted(collected)
collected=collected[::-1]

frequency = [i[0] for i in collected]
jump = [int(i[1]) for i in collected]


labels=jump
values=frequency
    
plt.bar(np.arange(len(frequency)),frequency,fc='gray',alpha=0.7,)
           
plt.xticks(np.arange(len(frequency)) + width * 0.5, labels,fontsize=6)
plt.legend(loc='upper right',fontsize=16,frameon=False)
plt.ylabel('Interval Distribution')
plt.xlabel('Interval')
plt.title('Ranked Interval Distribution')
plt.savefig('Ranked_interval_distribution', bbox_inches='tight' ,dpi=100)

