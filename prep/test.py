import bz2
import pickle
infile = open("/storage6/data/reddit/reddit_data/2005/RC_2005-12.bz2","r")
data = bz2.decompress(infile.read())
outfile = open("/storage6/users/shiyansi/redditData/test.json","w")
for line in data:
	outfile.write(line)
outfile.close()

#Count Subreddit user number
