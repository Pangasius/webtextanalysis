#once we have the tokenized file, we can call the glove model
import subprocess, os, sys

#make sure you have the glove model in a folder sibling to the git folder
if(not os.path.exists(sys.path[0] + "/../GloVe")):
    print("Path to GloVe model not found" + sys.path[0] + "/../GloVe")
    raise Exception("GloVe folder not found : path to download : https://github.com/stanfordnlp/GloVe")

for file in ["source", "target"]:
    first_move = "cp -f " + sys.path[0] + '/samples/' + file + '.txt' + " " + sys.path[0] + '/../GloVe/' + "tokenised.txt";
    move_sh = "cp -f " + sys.path[0] + '/demo_custom.sh' + " " + sys.path[0] + '/../GloVe/' + "demo_custom.sh";
    call_glove = "cd " + sys.path[0] + '/../GloVe/' + " && ./demo_custom.sh";
    second_move = "cp -f " + sys.path[0] + '/../GloVe/' + "vectors.txt " + sys.path[0] + '/models/' + file + '_glove.txt';

    join_commands = first_move + " && " + call_glove + " && " + second_move;
    
    print("Running command : " + join_commands)

    process  = subprocess.Popen(join_commands, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()

    for line in out.splitlines():
        print(line)
        
    for line in err.splitlines():
        print(line)
        
    if len(out.splitlines()) == 0:
        raise Exception("GloVe call failed. Usually permissions on demo_custom.sh is an issue")