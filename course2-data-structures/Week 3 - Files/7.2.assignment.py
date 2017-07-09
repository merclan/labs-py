# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open('../Files/'+fname)
average = 0
lines = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    init = line.find(' ')
    number = float(line[init:])
    average = average + number
    lines = lines + 1
print("Average spam confidence: " + str(average/lines))
