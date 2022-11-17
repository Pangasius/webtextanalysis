# webtextanalysis

# Instructions to run

> you will need to install jupyter notebook for python to run the code.

Run the first cell and it will download the required pip packages.
If you are using anaconda, it is preferable to locate the packages in conda forge and install them by hand.
Also, to install torch with cuda, refer to the website https://pytorch.org/get-started/locally/
And select the versions put in the code.
# URL to download the database

Normally, the database should download itself, however, you may want to download it by hand :
https://www.manythings.org/anki/

# URL to download GloVe

As put in the code, simply run "python3 glove_run.py" (from this folder) once you have downloaded the official git :
https://github.com/stanfordnlp/GloVe

If a bug arrises when running the command, change the permissions of demo_custom.sh to 777.

# Credits

The database and dataloader (in most part) have been done by d2l.
https://d2l.ai/chapter_recurrent-modern/machine-translation-and-dataset.html

# Rest of the code by Lize Pirenne