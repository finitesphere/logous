## About
The python script allows the user to write a log post which includes a title, date, and the content of the post itself, all inside the comfort of a command-line interface. This repository contains my python script, html, and css file for my log website. You can change out the html and css files with your own files.

## Requirements
* Python3 
* Neocities account and neocities CLI software (You can change this to upload to GitHub Pages instead of Neocities)
* Python module requirements: BeautifulSoup4, datetime, and subprocess
* CLI enviroment (Preferably a GNU/Linux BASH terminal)

## How To
1. Git clone the repository. ```git clone https://github.com/mvfileslashdevslashnull/log_website```
2. Create or open the existing html and css file, configure it to your liking.
3. Open the python script with your preferred text editor and change the name of the html, css, and python file if you have done so, then change the current working directory line in the python script. ```subprocess.run('neocities push -e log.py .', shell=True, cwd="/home/user/log_website")```
4. Launch the program by entering ```python log.py``` into your command-line interface, if you changed the name of the python script file then simply put the file name after python in the command. Also note this CLI enviroment must support BASH commands.
5. Once the program is executed, you be asked to enter a title and content for the post.
6. Lastly you will have the choice to submit the post or cancel it.

## Help
If you get any errors remember to change your current working directory to a directory with the script, html, and css files. Other errors can occur if you do not have any h2 or p tags in your html file. I created and executed this python script on a GNU/Linux operating system, the script should work on other operating systems that can utilize BASH commands. Any more help, questions, or comments please leave them under the issues page of this GitHub repository.
