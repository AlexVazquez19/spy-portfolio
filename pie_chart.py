from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

# DATA
sector_names = ['Information Technology','Health Care','Consumer Discretionary',
'Communication Services','Financials','Industrials','Consumer Staples',
'Utilities','Materials','Real Estate','Energy']

sector_weights = []
def updateChartNumbers():
    global sector_weights
    with open('sector_weights.txt','r') as f:
        data = f.read().splitlines()
        sector_weights = []
        for elem in data:
            sector_weights.append(float(elem))

updateChartNumbers()

colors = ['#001d6c','#002d9c','#0043ce','#0f62fe','#4589ff','#78a9ff','#a56eff',
    '#8a3ffc','#6929c4','#491d8b','#31135e']

#SETUP PIE CHART
fig, ax = plt.subplots(figsize=(7,4),dpi=40)

patches, texts, pcts = ax.pie(
    sector_weights, labels=sector_names, autopct='%.1f%%',
    wedgeprops={'linewidth': 0, 'edgecolor': 'white'},
    colors=colors)

plt.setp(pcts, color='white', fontweight='bold')

# FRAMES
frm_chart = Frame()

# CONFIGURE rows and columns in frames
canvas = FigureCanvasTkAgg(fig, master=frm_chart)
canvas.draw()

# COMMANDS

def redraw():
    ax.clear()
    patches, texts, pcts = ax.pie(
    sector_weights, labels=sector_names, autopct='%.1f%%',
    wedgeprops={'linewidth': 0, 'edgecolor': 'white'},
    colors=colors)
    plt.setp(pcts, color='white', fontweight='bold')
    fig.canvas.draw_idle()

# WIDGETS

# PACKING / GRIDDING
canvas.get_tk_widget().pack(padx=30,pady=30)

# BINDS

