#! /bin/python3

from pkg.pigeon import Locker , Unlocker , Injector , Extractor
from pkg.util import discover_all_files , show_banner , select_files_by_index ,Color
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

#if option == 4:
	#sys.exit()
if option  < 4 and option > 0:
	container = input(f"{Color.GREEN}Enter the container image \nContainer should be a PNG or JPEG file\n>{Color.RESET}")
    

	if option == 1:
		dirs = input(f"{Color.GREEN}{Color.BOLD}Which directory you want to hide : \t\n{Color.RESET}>")
		files = discover_all_files(dirs)
		selected_files = select_files_by_index(files)
		l = Locker("secret.zip",None , True ,*selected_files)
		print (f"{Color.BLUE}Note down the encryption key . It will be needed for decrypting your files in future {Color.RESET}.{Color.BG_BLUE}\nkey {l.get_key()}\n{Color.BOLD}{Color.MAGENTA}Chack 'secret.key' file for the encrytion key in the current directory{Color.RESET}")
		with open("secret.key","w") as fk:
			fk.write(l.get_key())
		Injector(container,"secret.zip")
		print (f"{Color.YELLOW}Your contents are successfully injected to the {container}{Color.RESET}")

	elif option == 2:
		key = input(f"{Color.GREEN}Enter the decrytion key : {Color.RESET}")
		if not len(key):
			print (f"{Color.RED}Failed to decrypt???{Color.RESET}")
			sys.exit()
		outpath = input(f"{Color.GREEN}Where do you want to save the unlocked file : {Color.RESET}")
		Extractor(container,"secret.zip")
		if outpath != "":
			Unlocker("secret.zip",key,outpath)
		else:
			Unlocker("secret.zip",key,"secret/")

	elif option == 3:
		pass


