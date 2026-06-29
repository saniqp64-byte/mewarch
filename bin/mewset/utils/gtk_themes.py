import os
import configparser
import subprocess
import time
from utils.style import print_header, print_footer, styled_input, print_error, print_success, Colors
def open_themes() -> list:
    home_path = os.getenv('HOME')
    content = os.listdir(f'{home_path}/.themes')

    for i, val in enumerate(content):
        content[i] = f'{home_path}/.themes/{val}'
    

    return content

def search_index_themes(folders: list) -> dict:

    home_path = os.getenv('HOME')
    path_themes = {}


    for folder in folders:
        index_path = f'{folder}/index.theme'
        if os.path.exists(index_path):
            path_themes[index_path] = folder.split('/')[-1]
    
    return path_themes

def apply_gtk_theme(theme_name, index_paths):
    try:
        parser = configparser.ConfigParser()
        parser.optionxform = str
        for index_path, path in index_paths.items():
            parser.read(index_path)
            if parser['Desktop Entry']['Name'] == theme_name:

                subprocess.run(['gsettings', 'set', 'org.gnome.desktop.interface', 'gtk-theme', path])
                subprocess.run(['xfconf-query', '-c', 'xsettings', '-p', '/Net/ThemeName', '-s', path], stderr=subprocess.DEVNULL)
                print_success(f"gtk theme {parser['Desktop Entry']['Name']} was set as the default.")
                break
        else:
            print_error("theme not found")
    except Exception as e:
        print_error(f'Error applying theme: {e}')

def show_theme_names(index_paths):
    try:
        parser = configparser.ConfigParser()
        parser.optionxform = str

        print_header('GTK THEMES')
        for index_path, path in index_paths.items():
            parser.read(index_path)
            print(f"{Colors.CYAN}{parser['Desktop Entry']['Name']}{Colors.RESET}")
        print_footer()
    except Exception as e:
        print_error(f'Error showing themes: {e}')



def gtk():
    try:
        os.system("clear")
        index_paths = search_index_themes(open_themes())

        show_theme_names(index_paths)

        theme = styled_input('Enter theme name (or "exit" to back): ')

        if theme == 'exit':
            return
        
        apply_gtk_theme(theme, index_paths)
    except Exception as e:
        print_error(f'An error occurred: {e}')
        input('Press Enter to continue...')
    
    time.sleep(2)

    
