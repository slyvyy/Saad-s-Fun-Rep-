from colorama import init, Fore, Back, Style

# Initialize Colorama
init(autoreset=True)

# Print colored text
print(Fore.RED + "sorta")
print(Back.GREEN + "cool")
print(Fore.YELLOW + Back.BLUE + "this is")
print(Style.RESET_ALL + "Back to the default colors.")
