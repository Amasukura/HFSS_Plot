import csv
import matplotlib.pyplot as plt

freq = []
S22 = []
S21 = []

freq_start = 125

freq_end = 211

result_path = "result/Probe_2port_2221.csv"

with open(result_path) as f:
    reader = csv.reader(f)
    firstLoop = True
    for row in reader:
        if firstLoop:
            firstLoop = False
        else:
            if freq_start <= float(row[0]) <= freq_end:
                freq.append(float(row[0]))
                S22.append(float(row[1]))
                S21.append(float(row[2]))
            else:
                continue

#print(dB)
plt.rcParams['font.family'] = 'Arial' #全体のフォントを設定
plt.rcParams["font.size"] = 24                      #フォントの大きさ
plt.rcParams["xtick.direction"] = "in"              #x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams["ytick.direction"] = "in"              #y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams["xtick.minor.visible"] = True          #x軸補助目盛りの追加
plt.rcParams["ytick.minor.visible"] = True          #y軸補助目盛りの追加
plt.rcParams["xtick.major.width"] = 1.0             #x軸主目盛り線の線幅
plt.rcParams["ytick.major.width"] = 1.0             #y軸主目盛り線の線幅
plt.rcParams["xtick.minor.width"] = 1.0             #x軸補助目盛り線の線幅
plt.rcParams["ytick.minor.width"] = 1.0             #y軸補助目盛り線の線幅
plt.rcParams["xtick.major.size"] = 10               #x軸主目盛り線の長さ
plt.rcParams["ytick.major.size"] = 7               #y軸主目盛り線の長さ
plt.rcParams["xtick.minor.size"] = 5                #x軸補助目盛り線の長さ
plt.rcParams["ytick.minor.size"] = 3                #y軸補助目盛り線の長さ
plt.rcParams['xtick.top'] = False                   #x軸の上部目盛り
plt.rcParams['ytick.right'] = False                 #y軸の右部目盛り
plt.rcParams["axes.linewidth"] = 1.0                #囲みの太さ

fig = plt.figure(figsize=(11, 8))
ax = fig.add_subplot(111)

ax.plot(freq,S21,"-",color = "black",linewidth = 2,label="$S_{21}$")

#ax.axhspan(-40, -15, color = "deepskyblue", alpha = 0.5) #y方向塗りつぶし
#ax.axhspan(-85, -20, color = "darkcyan", alpha = 0.3)

ax.set_xlim(freq_start, freq_end)
ax.set_ylim(-3,0)

#挿入係数入れるとき
#ax2 = ax.twinx()
#ax2.set_ylim(-50,0)
#ax2.plot(freq,S12,"-.",color = "gray",label="S(2,1)") gray
#ax2.plot(freq,S22,"-.",color = "grey",linewidth = 2,label="$S_{11}$")
#ax2.axvspan(125, 163, color = "navy", alpha = 0.1)


h1, l1 = ax.get_legend_handles_labels()
#h2, l2 = ax2.get_legend_handles_labels()
#ax.legend(h1 + h2, l1 + l2,fontsize = 22)
#ax.legend(h1, l1)

################################################################plot#####################################################################################

ax.set_xlabel("Freqency [GHz]")
ax.set_ylabel("Magnitude $S_{21}$[dB]")
#ax2.set_ylabel("Magnitude $S_{11}$ [dB]")

plt.tight_layout()
#plt.savefig("Figs/H-bend_OLD.png")
plt.savefig("Figs_for_presentation/"+(result_path.replace(".csv","")).replace("result/","")+".png")
plt.show()

freq_under_20 = []
for i in range(len(freq)):
    if S22[i] < -20:
        freq_under_20.append(freq[S22.index(S22[i])])
print("Percentage of -20 dB range:"+str((len(freq_under_20)/len(freq))*100)+" [%] between "+str(min(freq))+" [GHz] and "+str(max(freq))+" [GHz]")

