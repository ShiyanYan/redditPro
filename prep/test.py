import bz2
import pickle
year = 2010
root_path = "/storage6/data/reddit/reddit_data/"
out_path = "/storage6/users/shiyansi/redditData/"
infile = open(root_path + str(year) + "/RC_" + str(year) + "-12.bz2","r")
data = bz2.decompress(infile.read())
outfile = open(out_path + "test" + str(year) + "-12.json","w")
for line in data:
        outfile.write(line)
outfile.close()


