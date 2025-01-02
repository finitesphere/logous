## Logous
A simple and efficient Python script that allows the user to write a log post via the terminal and upload it to Neocities.

![](https://github.com/finitesphere/logous/blob/main/logous-demo.gif)

## About
The Python script allows the user to write a log post, which includes a title, date, and the content of the post itself, all within the comfort of a command-line interface. This repository contains my Python script, HTML, and CSS files for my log website. You can replace the HTML and CSS files with your own.

## Requirements
* Python3 https://www.python.org/downloads/
* Neocities account and neocities CLI software (You can change this to upload to GitHub Pages instead of Neocities by changing the neocities command) https://neocities.org/
* Python module requirements: ```BeautifulSoup4```, ```datetime```, and ```subprocess```
* Download Ruby (Used to download neocities CLI, note that some Linux distros can install neocities CLI with their respective package manager) https://rubyinstaller.org/downloads/

## How To
1. Make sure you have python installed and added to your PATH
2. Open a terminal and install beautifulsoup4 (```datetime``` and ```subprocess``` are part of Python's standard library and are pre-installed with python)
```
pip install beutifulsoup4
```
3. Download Ruby
4. Install neocities using Ruby gem
```
gem install neocities
```
5. Neocities login
```
neocities login
```
6. Run the script
```
python log.py
```

   
