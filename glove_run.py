#once we have the tokenized file, we can call the glove model
import subprocess, os, sys

#make sure you have the glove model in a folder sibling to the git folder
if(not os.path.exists(sys.path[0] + "/../GloVe")):
    print("Path to GloVe model not found" + sys.path[0] + "/../GloVe")
    raise Exception("GloVe folder not found : path to download : https://github.com/stanfordnlp/GloVe")

#make sure required file demo_custom.sh is in the glove folder
if(not os.path.exists(sys.path[0] + "/../GloVe/demo_custom.sh")):
    print("Path to GloVe custom runnable not found" + sys.path[0] + "/../GloVe/demo_custom.sh")
    subprocess.run("cp " + sys.path[0] + "/demo_custom.sh " + sys.path[0] + "/../GloVe/demo_custom.sh", shell=True)

first_move = "cp " + sys.path[0] + '/samples/alice_tokenised.txt' + " " + sys.path[0] + '/../GloVe/' + "alice_tokenised.txt";
call_glove = "cd " + sys.path[0] + '/../GloVe/' + " && ./demo_custom.sh";
second_move = "cp " + sys.path[0] + '/../GloVe/' + "vectors.txt " + sys.path[0] + '/models/alice_glove.txt';

join_commands = first_move + " && " + call_glove + " && " + second_move;

process  = subprocess.Popen(join_commands, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = process.communicate()

for line in out.splitlines():
    print(line)
    
for line in err.splitlines():
    print(line)
    
if len(out.splitlines()) == 0:
    raise Exception("GloVe call failed, possibly because not run from a batch file")