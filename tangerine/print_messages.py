import time
import logging
from colorama import init, Fore, Back, Style, Cursor

def print_logo():
    """Method to print the logo of Tangerine.
    """
    logo = Fore.LIGHTRED_EX + '''
🌱  🍊  🌱  🍊  🌱  🍊  🌱  🍊  🌱  🍊 🌱  🍊 🌱  🍊  🌱  🍊  🌱  🍊  🌱  🍊

        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠛⠛⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⢀⣤⣶⣶⣶⣶⣤⡀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⡏⠙⢿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⡿⠋⠙⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⢀⣴⣶⣦⡀⠸⣿⣿⣿⣿⣿⣿⠇⢀⣴⣶⣦⣀⠙⢿⣿⣿⣿⣿
        ⣿⣿⣿⣿⠀⠀⠀⠙⢿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠹⣿⣿⡿⠋⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠏⠀⣴⣿⣿⣿⣿⣷⡀⢿⣿⣿⣿⣿⡟⢀⣾⣿⣿⣿⣿⣧⡀⠹⣿⣿⣿
        ⣿⣿⣿⣿⠀⠀⠀⠀⠈⢻⣧⠀⠀⠀⠀⠀⠀⠀⢀⣿⠋⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠏⠀⠸⣿⣿⣿⣿⣿⣿⣷⡘⣿⣿⣿⣿⢁⣾⣿⣿⣿⣿⣿⣿⠇⠀⠹⣿⣿
        ⣿⡇⠙⢿⣦⡀⠀⠀⠀⠀⣹⣷⣤⠴⠶⠶⢤⣤⣿⡁⠀⠀⠀⠀⢀⣠⡿⠛⢹⣿⣿⡏⠀⢀⣀⡈⠙⠻⢿⣿⣿⣿⣷⣹⣿⣿⣯⣾⣿⣿⣿⡿⠟⠋⢁⣀⡀⠀⢹⣿
        ⣿⡇⠀⠀⠈⠻⣦⡀⣠⡾⠋⠁⠀⣀⣤⣄⠀⠀⠙⠻⣦⡀⢀⣴⠿⠋⠀⠀⢸⣿⣿⠁⢠⣿⣿⣿⣿⣷⣶⣬⣝⣻⣿⠟⠋⠙⠻⣿⣟⣫⣥⣶⣶⣿⣿⣿⣿⡄⠈⢿
        ⣿⡇⠀⠀⠀⠀⠈⠻⣯⡀⠀⣠⡾⠋⠁⠙⢿⣦⡀⠀⢈⣿⠟⠁⠀⠀⠀⠀⢸⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⠀⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿
        ⣿⡇⠀⠀⠀⠀⠀⠀⠙⢿⣾⠋⠀⠀⠀⠀⠀⠙⢷⣴⠟⠁⠀⠀⠀⠀⠀⠀⣼⣿⣿⡀⠘⣿⣿⣿⣿⠿⠟⢛⣯⣿⣿⣦⣄⣠⣴⣿⣿⣝⡛⠿⢿⣿⣿⣿⣿⠃⢀⣿
        ⣿⣷⠀⠀⠀⠀⠀⠀⢠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣇⠀⠈⠉⢁⣠⣴⣾⣿⣿⣿⡿⣹⣿⣿⣟⢿⣿⣿⣿⣷⣦⣄⡈⠉⠁⠀⣸⣿
        ⣿⣿⣇⠀⠀⠀⠀⠀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣆⠀⢰⣿⣿⣿⣿⣿⣿⡿⢡⣿⣿⣿⣿⡈⢿⣿⣿⣿⣿⣿⣿⡆⠀⣰⣿⣿
        ⣿⣿⣿⣆⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣆⠈⠻⣿⣿⣿⣿⡿⠁⣾⣿⣿⣿⣿⣧⠈⢿⣿⣿⣿⣿⡟⠁⣰⣿⣿⣿
        ⣿⣿⣿⣿⣷⣄⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠈⠛⠿⠟⠁⢸⣿⣿⣿⣿⣿⣿⡆⠈⠻⠿⠟⠉⣠⣾⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣷⣤⣘⣧⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣃⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠈⠛⠿⠿⠿⠿⠛⠁⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣤⣤⣤⣤⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣤⣤⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    '''
    print(logo)

def print_info(port, host, debug):
    """The print message method.

    Args:
        port (int): The port of the host.
        host (str): The host IP of the router.
        debug (str): The debug level of Tangerine.
    """
    info = Fore.WHITE + f'''
                   ╔╦╗╔═╗╔╗╔╔═╗╔═╗╦═╗╦╔╗╔╔═╗  ╦ ╦╔═╗  ┬
                    ║ ╠═╣║║║║ ╦║╣ ╠╦╝║║║║║╣   ║ ║╠═╝  │
                    ╩ ╩ ╩╝╚╝╚═╝╚═╝╩╚═╩╝╚╝╚═╝  ╚═╝╩    o

                    DEBUGGING: {debug}
                    Server sprouted @ {host}:{port}
                    Press Ctrl+C to stop the server


🌱  🍊  🌱  🍊  🌱  🍊  🌱  🍊  🌱  🍊 🌱  🍊 🌱  🍊  🌱  🍊  🌱  🍊  🌱  🍊
    '''
    print(info)

def print_success(port, host, debug):
    """The print message constructor for a successful print.

    Args:
        port (int): The port of the router.
        host (str): The host IP of the router.
        debug (str): The debug level of Tangerine.
    """
    print_logo()
    time.sleep(0.3)
    print_info(port, host, debug)

def print_debug(message):
    """The print method for debug messages.

    Args:
        message (str): The body of the debug message.
    """
    print(Fore.CYAN + message + Style.RESET_ALL)
