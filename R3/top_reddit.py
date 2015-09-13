import urllib, json, sys
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
for i in range(10):
    data = hot["data"]["children"][i]["data"]
    print "Post: " + data["title"] + "\nKarma: " + str(data["score"]) + "\npost url: www.reddit.com" + data["permalink"] + "\nlink: " + data["url"]+ "\n"
