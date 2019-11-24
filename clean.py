import csv
​
csv_fname = "data.csv"
​
from string import ascii_lowercase
​
good_chars = ascii_lowercase + ' .,\n'
​
# clean string to leave only allowed chars
def clean(s):
    rtrn = []
    # c is char
    for c in s:
        if c in good_chars:
            rtrn.append(c)
    return rtrn
​
with open(csv_fname,'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        lyric = row[0].lower()
        lyric = list(lyric)
        lyric = clean(lyric)
