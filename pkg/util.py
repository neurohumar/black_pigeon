#!/bin/python3

import os

class Color:
    # Define basic color codes as class variables
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    
    # Colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Background colors
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"
    





def discover_all_files(directory):

    absolute_files_path = []

    for root,_,files in os.walk(directory):
        for file in files:
            abs_path = os.path.abspath(os.path.join(root,file))
            absolute_files_path.append(abs_path)
    return absolute_files_path

def show_banner():
    print(f"""{Color.YELLOW}
 ____  _            _         ____  _                        
 | __ )| | __ _  ___| | __    |  _ \(_) __ _  ___  ___  _ __  
 |  _ \| |/ _` |/ __| |/ /____| |_) | |/ _` |/ _ \/ _ \| '_ \ 
 | |_) | | (_| | (__|   <_____|  __/| | (_| |  __/ (_) | | | |
 |____/|_|\__,_|\___|_|\_\    |_|   |_|\__, |\___|\___/|_| |_|
                                       |___/                  
   {Color.BOLD}Author : {Color.CYAN}Neurohumar Group
    {Color.YELLOW}visit {Color.UNDERLINE}{Color.CYAN}https://github.com/neurohumar/black_pigeon.git
{Color.RESET}
""")

def select_files_by_index(files):

	for i,file in enumerate(files):
		print(f"{i} . {file}")
    
    promt = input(f"{Color.BLUE}Enter file index(s) : ")
    if promt in ["*","all"]:
        return files

	indexes =list(map(int ,promt.split()))
	return [files[i] for i in indexes]
