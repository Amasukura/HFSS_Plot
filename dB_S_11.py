import csv
import matplotlib.pyplot as plt

freq = []
S11 = []

freq_start = 125

freq_end = 211

result_path = "result/H-bend_dB.csv"

with open(result_path) as f:
    reader = csv.reader(f)
    firstLoop = True
    for row in reader:
        if firstLoop:
            firstLoop = False
        else:
            if freq_start <= float(row[1]) <= freq_end:
                freq.append(float(row[1]))
                S11.append(float(row[2]))
            else:
                continue

plt.rcParams['font.family'] = 'Arial' #全体のフォントを設定
plt.rcParams["font.size"] = 12                      #フォントの大きさ
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

fig = plt.figure()
ax = fig.add_subplot(111)


ax.axhspan(-100, -15, color = "deepskyblue", alpha = 0.5) #y方向塗りつぶし
ax.axhspan(-100, -20, color = "darkcyan", alpha = 0.3)

ax.plot(freq,S11,"k-",label="$S_{11}$")

ax.set_xlim(freq_start, freq_end)
ax.set_ylim(-55,0)

h1, l1 = ax.get_legend_handles_labels()
ax.legend(h1, l1)
#ax.legend(h1, l1)

###############################################################analysis#######################################################################

print("Max S11:"+str(max(S11))+"[dB] "+"Freqency:"+str(freq[S11.index(max(S11))])+"[GHz]")
print("min S11:"+str(min(S11))+"[dB] "+"Freqency:"+str(freq[S11.index(min(S11))])+"[GHz]")

freq_under_10 = []
for i in range(len(freq)):
    if S11[i] < -10:
        freq_under_10.append(freq[S11.index(S11[i])])

print("Percentage of -10 dB range:"+str((len(freq_under_10)/len(freq))*100)+" [%] between "+str(min(freq))+" [GHz] and "+str(max(freq))+" [GHz]")

freq_under_15 = []
for i in range(len(freq)):
    if S11[i] < -15:
        freq_under_15.append(freq[S11.index(S11[i])])

print("Percentage of -15 dB range:"+str((len(freq_under_15)/len(freq))*100)+" [%] between "+str(min(freq))+" [GHz] and "+str(max(freq))+" [GHz]")

freq_under_20 = []
for i in range(len(freq)):
    if S11[i] < -20:
        freq_under_20.append(freq[S11.index(S11[i])])

print("Percentage of -20 dB range:"+str((len(freq_under_20)/len(freq))*100)+" [%] between "+str(min(freq))+" [GHz] and "+str(max(freq))+" [GHz]")

ax.set_xlabel("Freqency [GHz]")
ax.set_ylabel("Magnitude $S_{11}$ [dB]")

plt.savefig("Figs/"+(result_path.replace(".csv","")).replace("result/","")+".png")
plt.show()
