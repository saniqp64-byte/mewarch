from utils.gtk_themes import gtk
from utils.audio import audio_set
import sys
import os
from utils.style import print_header, print_footer, styled_input, print_error, print_success, Colors
windows = {
    'gtk': gtk,
    'audio': audio_set,
    'exit': sys.exit
}



def main():
    try:
        os.mkdir(f"{os.getenv("HOME")}/.themes")
    except FileExistsError:
        pass
    while True:
        try:
            os.system('clear')
            print_header('SETTINGS')
            print(f"{Colors.CYAN}gtk  -> set gtk themes{Colors.RESET}")
            print(f"{Colors.CYAN}audio -> set audio output{Colors.RESET}")
            print(f"{Colors.CYAN}exit  -> back{Colors.RESET}")
            print_footer()

            command = styled_input('command -> ')

            if command in windows:
                windows[command]()
                print_success('Command executed')
            else:
                print_error('Invalid command')
                input('Press Enter to continue...')
        except KeyboardInterrupt:
            sys.exit()
        except Exception as e:
            print_error(f'Error: {e}')
            input('Press Enter to continue...')


if __name__ == '__main__':
    main()



