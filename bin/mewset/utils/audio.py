import subprocess
import os
import time
from utils.style import print_header, print_footer, styled_input, print_error, print_success, Colors
def get_sinks():
    try:
        os.system("clear")
        start_sinks = False
        result = subprocess.run(['wpctl', 'status'], capture_output=True, text=True)
        
        sinks = []

        for line in result.stdout.split('\n'):
            line = line.strip()

            if line.startswith('├─ Sources'):
                break
            
            elif line == '│':
                continue
            
            elif line.startswith('├─ Sinks'):
                start_sinks = True
                continue
            
            elif start_sinks:
                line = line.replace('│', '')
                line = line.split('[')[0].strip()
                line = ' '.join(line.split())

                sinks.append(line)
            
        return sinks
    except Exception as e:
        print_error(f'Error getting sinks: {e}')
        return []


def audio_set():
    try:
        sinks = get_sinks()

        print_header('AUDIO')
        for sink in sinks:
            print(f"{Colors.CYAN}{sink}{Colors.RESET}")
        print_footer()

        setdef = styled_input('Enter the default (enter number or "exit" to back): ')

        if setdef == 'exit':
            return

        subprocess.run(['wpctl', 'set-default', setdef])
        print_success(f"{setdef} was set as the default.")
    except Exception as e:
        print_error(f'An error occurred: {e}')
        input('Press Enter to continue...')
    
    time.sleep(2)

if __name__ == '__main__':
    audio_set()