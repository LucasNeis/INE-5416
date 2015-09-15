import urllib, json, sys

def bubblesort(data):
    aux = 0
    for i in range(len(data), 0, -1):
        if i > 0:
            for j in range(i-1):
                if data[j][0] < data[j+1][0]:
                    aux = data[j]
                    data[j] = data[j+1]
                    data[j+1] = aux
    return data
sub = sys.argv
if len(sys.argv) == 1:
   print "\nYou must insert a subreddit name. Example: phyton top_reddit.py pcmasterrace\n"
   sys.exit(0)
hot = json.loads(urllib.urlopen("http://reddit.com/r/" + sub[1] + "/hot.json").read())
try:
    error = hot['error']
    if error:
        print "\nSub not found\n"
        sys.exit(0)
except:
    print ""
elements = []
keys = ["score","title", "permalink","url"]
for i in range(10):
    data = hot["data"]["children"][i]["data"]
    elements.append([data[j] for j in keys])
bubblesort(elements)
for info in elements:
    print "Post: " + info[1] + "\nKarma: " + str(info[0]) + "\npost url: www.reddit.com" + info[2] + "\nlink: " + info[3] + "\n"