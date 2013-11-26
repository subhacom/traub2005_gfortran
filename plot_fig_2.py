from pylab import *
import scipy as sp
from scipy import fftpack as fp
from scipy import signal as sg
from matplotlib import rc
import os

rc('font', size=10)

datadir = 'data'
if __name__ == '__main__':
    data = {}
    for filename in os.listdir(datadir):
        path = os.path.join(datadir, filename)
        if os.path.isfile(path):
            if filename.startswith('GROUCHO'):
                celltype = filename.rpartition('.')[-1]
                data[celltype] = loadtxt(path)
                print 'Loaded', celltype
    field1mm_col = {'suppyrRS': 11,
                    'suppyrFRB': 5,
                    'tuftIB': 5,
                    'tuftRS': 5,
                    'nontuftRS': 5,
                }
    field2mm_col = {'suppyrRS': 12,
                'suppyrFRB': 11,
                'tuftIB': 11,
                'tuftRS': 11,
                'nontuftRS': 11,                
            }
    ts = data['suppyrRS'][:, 0]
    indices = flatnonzero((ts >= 100) & (ts <= 1600))
    ts = ts[indices]
    ax = subplot(4, 2, 1)
    field_1mm = sum([data[celltype][indices, field1mm_col[celltype]] for celltype in field1mm_col], axis=0)
    dt = 1e-3 * (ts[1] - ts[0])
    plot(ts, field_1mm, 'k-', label='field at 1mm', alpha=0.7)
    field_2mm = sum([data[celltype][indices, field2mm_col[celltype]] for celltype in field2mm_col], axis=0)
    plot(ts, field_2mm, 'r-', label='field at 2 mm', alpha=0.7)
    legend(loc='best')
    subplot(4, 2, 2)
    title('Powet at 1 mm (using fft)')
    h = sg.firwin(numtaps=10, cutoff=300, nyq=0.5/dt)
    filtered_1mm = sg.lfilter(h, 1.0, field_1mm)
    fft_1mm = abs(sp.fft(filtered_1mm))
    freq_1mm = fp.fftfreq(fft_1mm.size, dt)
#    power_1mm, freq_1mm = psd(field_1mm, Fs=1/(data['suppyrRS'][1][0] - data['suppyrRS'][0][0]), noverlap=75)
    plot(freq_1mm[(freq_1mm > 10) & (freq_1mm < 100)], fft_1mm[(freq_1mm > 10) & (freq_1mm < 100)], label='power at 1 mm (fft)')
    title('Powet spectral density at 2 mm')
    filtered_2mm = sg.lfilter(h, 1.0, field_2mm)
#    power_2mm, freq_2mm = psd(filtered_2mm, Fs=100/(ts[1] - ts[0]), label='psd of field at 2mm')
    legend(loc='best')
    ax2 = subplot(4, 2, 3, sharex=ax)
    plot(ts, data['suppyrRS'][indices,1], 'k-', label='Sup. Pyr. RS')
    legend(loc='best')    
    subplot(4, 2, 4, sharex=ax, sharey=ax2)
    plot(ts, data['spinstell'][indices,1], 'k-', label='Spiny Stellate')
    legend(loc='best')
    subplot(4, 2, 5, sharex=ax, sharey=ax2)
    plot(ts, data['suppyrFRB'][indices,1], 'k-', label='Sup. Pyr. FRB')
    legend(loc='best')
    subplot(4, 2, 6, sharex=ax, sharey=ax2)
    plot(ts, data['supbask'][indices,1], 'k-', label='Sup. Basket')
    plot(ts, data['supLTS'][indices,1], 'r-', label='Sup. LTS')
    legend(loc='best')
    subplot(4, 2, 7, sharex=ax, sharey=ax2)
    plot(ts, data['tuftIB'][indices,1], 'k-', label='tufted IB')
    plot(ts, data['tuftRS'][indices,1], 'c-', label='tufted RS')
    plot(ts, data['nontuftRS'][indices,1], 'r-', label='nontufted RS')
    legend(loc='best')
    subplot(4, 2, 8, sharex=ax, sharey=ax2)
    plot(ts, data['deepbask'][indices,1], 'k-', label='Deep. Basket')
    plot(ts, data['deepLTS'][indices,1], 'r-', label='Deep. LTS')
    legend(loc='best')
    #tight_layout()
    show()
