#driver script
import matplotlib.pyplot as plt
import midi
import numpy as np

import single_song_analysis_function

meta_common_motifs,meta_common_motif_counts,meta_common_motif_beats= single_song_analysis_function.MA('romance.mid')
#in case the analysis is intensive; you can cache
# pickle.dump( meta_common_motifs, open( "motifs.p", "wb" ) )
# pickle.dump( meta_common_motif_counts, open( "counts.p", "wb" ) )
#
# #
# # meta_common_motifs = pickle.load( open( "motifs.p", "rb" ) )
# #
# # meta_common_motif_counts = pickle.load( open( "counts.p", "rb" ) )
total_notes=np.array([])
for j,meta_common_motif in enumerate(meta_common_motifs):
    if len(np.unique(meta_common_motif))>2:
        if max(abs(np.diff(meta_common_motif)))<8:
            if meta_common_motif_counts[j]>3:
                plt.plot(range(len(meta_common_motif)),meta_common_motif,'o-',linewidth=3,alpha=0.5)#,alpha=meta_common_motif_counts[j]/200.0)
                total_notes=np.append(total_notes,meta_common_motif)
                #### we begin writing the sample
                pattern = midi.Pattern()
                # Instantiate a MIDI Track (contains a list of MIDI events)
                track = midi.Track()
                # Append the track to the pattern
                pattern.append(track)
                for n,note in enumerate(meta_common_motif):
                    # Instantiate a MIDI note on event, append it to the track
                    on = midi.NoteOnEvent(tick=100, velocity=100, pitch=int(note))
                    track.append(on)
                    # Instantiate a MIDI note off event, append it to the track
                    off = midi.NoteOffEvent(tick=100, pitch=int(note))
                    track.append(off)
                # Add the end of track event, append it to the track
                eot = midi.EndOfTrackEvent(tick=1)
                track.append(eot)
                # Print out the pattern
                # Save the pattern to disk
                midi.write_midifile("motifs/"+str(j)+".mid", pattern)

print(set(total_notes))
plt.title('Bad Romance Motifs')
plt.xlabel('Note Order')
plt.ylabel('Note Tone')
plt.savefig('total_motifs.png')