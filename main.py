#! /bin/python3

from pkg.pigeon import Locker, Unlocker, Injector, Extractor, Authentication
from pkg.util import discover_all_files, show_banner, select_files_by_index, Color
import sys


show_banner()
print(f"""{Color.BLUE}SELECT A OPTION :

		{Color.BOLD}[1]. Hide files
		[2]. Extract files
		[3].Update Script
		[4].exit
        {Color.BOLD}
{Color.RESET}""")

option = int(input("\n>"))
print(option)

if option == 1 or option == 2:
    cover_image = input(
            f"""
            {Color.MAGENTA}COVER_IMAGE is a JPEG or PNG image where the file(s) will be obscured or extracted
            {Color.YELLOW}{Color.BOLD}
            Enter the path of the cover image :
            >{Color.RESET}"""
                        )
    if not cover_image:
        print(f"{Color.RED}{Color.BOLD}Cover Image not found!{Color.RESET}")
    if option == 1:
        dirs = input(f"""
            {Color.MAGENTA}DIRECTORY that contains all files to be obscured.
            No other files should keep in the DIRECTORY not to be hidden.
            {Color.YELLOW}{Color.BOLD}
            Enter the directory path to be hidden :
            >{Color.RESET}"""
                     )
        if not dirs:
            print(f"{Color.RED}{Color.BOLD}Directory not found!{Color.RESET}")
        all_files = discover_all_files(dirs)
        print(f"""
            {Color.MAGENTA}Select file(s) by index number separated by space to hide.
            If all files need to be hidden , enter '*'
            {Color.YELLOW}{Color.BOLD}
        """)
        files = select_files_by_index(all_files)
        password = input(f"""
            {Color.MAGENTA}PASSWORD is strong feature to save obscured file(s) from leaking to the imposter(s)
            {Color.YELLOW}{Color.BOLD}
            Enter a strong password (at least 8 characters) : 
            >{Color.RESET}""")
        if not password:
            print(f"{Color.RED}{Color.BOLD}Password not found!{Color.RESET}")
        Auth = Authentication(password=password)
        Locker("secret.zip", Auth.get_hash(), True, *files)
        Injector(cover_image, "secret.zip")
        print(f"{Color.GREEN}{Color.BOLD}File(s) successfully injected into '{cover_image}'{Color.RESET}")

    elif option == 2:
        password = input(f"""
            {Color.MAGENTA}PASSWORD is a crucial things to extract files , set during obscuration.
            {Color.YELLOW}{Color.BOLD}
            Enter the password to extract file(s) :  
            >{Color.RESET}""")
        
        if not password:
            print(f"{Color.RED}{Color.BOLD}Password not found!{Color.RESET}")
        outputpath = input(f"""
            {Color.MAGENTA}OUTPUT_PATH is a path where the extracted file(s) will be saved.
            {Color.YELLOW}{Color.BOLD}
            Enter the output path : 
            >{Color.RESET}""")
        Auth = Authentication(password=password)
        Extractor(cover_image, "secret.zip")

        u = Unlocker(
                zipfile_name="secret.zip", key=Auth.get_hash(),
                output_path=outputpath
                )

        print(f"{Color.GREEN}{Color.BOLD}File successfully extracted to '{u.output_path}'{Color.RESET}")

    elif option == 3:
        sys.exit()


