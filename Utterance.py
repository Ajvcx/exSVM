import json

fname = 'Pref13_tokyo2.json'
txt = []

with open(fname, "r", encoding="utf_8") as data_file:
    jsn = json.load(data_file)
    
    for a, line in enumerate(jsn, 1):
        if 4900 <= a <= 5200:
            if 'label' in line:
                print(line)
                Utterance = line["Utterance"]
                print(Utterance)
                txt.append(Utterance)
        else: 
            pass

with open("Utterance.txt", "w", encoding="utf-8") as W_file:
    W_file.write(('\n'.join(txt)))    