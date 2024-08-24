## About
The Python script allows the user to write a log post, which includes a title, date, and the content of the post itself, all within the comfort of a command-line interface. This repository contains my Python script, HTML, and CSS files for my log website. You can replace the HTML and CSS files with your own.

## Requirements
* Python3 
* Neocities account and neocities CLI software (You can change this to upload to GitHub Pages instead of Neocities by changing the neocities command)
* Python module requirements: BeautifulSoup4, datetime, and subprocess
* CLI enviroment (Preferably a Linux BASH terminal)

## How To
1. Clone the repository:
```git clone https://github.com/finitesphere/log```
3. Create or open the existing HTML and CSS files, and configure them to your liking.
4. Open the Python script with your preferred text editor. If you have changed the names of the HTML, CSS, or Python files, update the script accordingly. Also, modify the current working directory line in the Python script as needed:
```subprocess.run('neocities push -e log.py .', shell=True, cwd="/home/user/log_website")```
6. Launch the program by entering python log.py into your command-line interface. If you changed the name of the Python script file, use that name instead. Note that this CLI environment must support BASH commands.
Once the program is running, you will be prompted to enter a title and content for the post.
7. Finally, you will have the option to either submit the post or cancel it.

## Help
If you encounter any errors, remember to change your current working directory to the directory containing the script, HTML, and CSS files. Other errors may occur if your HTML file does not include h2 or p tags. I created and executed this Python script on a GNU/Linux operating system, but it should work on other operating systems that support BASH commands. For any further help, questions, or comments, please leave them on the issues page of this GitHub repository.
