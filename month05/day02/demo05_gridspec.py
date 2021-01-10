"""
    网格布局  和  自由布局
"""
import matplotlib.gridspec as mg
import matplotlib.pyplot as mp

mp.figure('GridSpec',facecolor='lightgrey')
gs = mg.GridSpec(3,3)
mp.subplot(gs[0,:2])
mp.text(0.5,0.5,'1',size=36,ha='center',va='center')
mp.xticks([])
mp.yticks([])
mp.tight_layout()
mp.subplot(gs[:2,2])
mp.text(0.5,0.5,'2',size=36,ha='center',va='center')
mp.xticks([])
mp.yticks([])
mp.tight_layout()
mp.subplot(gs[1:3,0])
mp.text(0.5,0.5,'3',size=36,ha='center',va='center')
mp.xticks([])
mp.yticks([])
mp.tight_layout()
mp.subplot(gs[1,1])
mp.text(0.5,0.5,'4',size=36,ha='center',va='center')
mp.xticks([])
mp.yticks([])
mp.subplot(gs[2,1:3])
mp.text(0.5,0.5,'5',size=36,ha='center',va='center')
mp.xticks([])
mp.yticks([])
mp.figure('FlowLayout')
mp.axes([0.1,0.1,0.5,0.5])
mp.text(0.5,0.5,'111',va='center',ha='center')

mp.show()