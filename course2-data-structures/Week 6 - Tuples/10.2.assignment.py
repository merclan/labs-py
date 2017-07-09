# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each
# of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string
# a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "../Files/mbox-short.txt"
handle = open(name)

dic = dict()

for line in handle:
    words = line.split()

    if line.startswith("From") and len(words) > 2:
        hour = words[5].split(':')[0]
        dic[hour] = dic.get(hour, 0) + 1

lst = sorted([(k,v)for (k,v) in dic.items()])

for key, val in lst:
    print (key, val)