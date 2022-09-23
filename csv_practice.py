import csv

with open('My_file.csv','w') as mf:
    with open('Social_Network_Ads.csv','r') as sna:
        lines = sna.readlines()
        mf.write(lines[0])
        for line in lines:
            words = line.split(',')
            if words[1] == 'Male' and int(words[2]) < 40 and int(words[4]) > 0:
                mf.write(line)
