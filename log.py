# Python log posting script

# Importing modules
from bs4 import BeautifulSoup
from datetime import datetime
import subprocess
import os
import sys
import platform

now = datetime.now()
current_date = now.strftime(" | %B %d, %Y %I:%M:%S %p")

def log():
    # Automatically set the working directory to the script's location
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(script_dir)

    with open('log.html', 'r', encoding='utf-8') as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')

        print("What is the title of the post?")
        title = input("").title()

        # Log Post Title
        log_title = soup.new_tag('h2', attrs={'id': 'log-post-title'})
        log_title.string = title + current_date

        print("Type out the post")
        content = input("")

        # Log Post Content
        log_content = soup.new_tag('p', attrs={'id': 'log-post'})
        log_content.string = content

        print("Do you want to submit the post? (Y/N)")
        submit = input("").upper()
        if "Y" in submit:
            print("Submitted")
        elif "N" in submit:
            exit()
        else:
            print("Do you want to restart the post? (Y/N)")
            answer_restart = input("").upper()
            if "Y" in answer_restart:
                log()
            else:
                exit()

        # Formats the blog-post-title before the blog-post-content
        soup.html.body.h2.insert_before(log_content)
        soup.html.body.p.insert_before(log_title)

        # Write back to log.html
        with open("log.html", "w", encoding='utf-8') as file:
            file.write(str(soup.prettify()))

        # Determine the correct command for Neocities push
        if platform.system() == "Windows":
            neocities_command = ['neocities.bat', 'push', '-e', 'log.py', '.']
        else:
            neocities_command = ['neocities', 'push', '-e', 'log.py', '.']

        # Push changes using Neocities
        try:
            subprocess.run(neocities_command, check=True)
        except FileNotFoundError:
            print("Error: Neocities command not found. Ensure the Neocities gem is installed and available in PATH.")
        except subprocess.CalledProcessError as e:
            print(f"Error while running Neocities command: {e}")

log()
