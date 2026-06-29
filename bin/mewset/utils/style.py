class Colors:
    ACCENT = "\033[38;2;247;118;142m"  # #f7768e
    BLUE = "\033[38;2;122;162;247m"    # #7aa2f7
    GREEN = "\033[38;2;158;206;106m"   # #9ece6a
    YELLOW = "\033[38;2;224;175;104m"  # #e0af68
    MAGENTA = "\033[38;2;187;154;247m" # #bb9af7
    CYAN = "\033[38;2;125;207;255m"    # #7dcfff
    TEXT = "\033[38;2;192;202;245m"    # #c0caf5
    GRAY = "\033[38;2;86;95;137m"     # #565f89
    BOLD = "\033[1m"
    RESET = "\033[0m"

def print_header(title):
    width = 40
    print(f"{Colors.ACCENT}┏{"━" * (width-2)}┓{Colors.RESET}")
    print(f"{Colors.ACCENT}┃{Colors.BOLD}{title.center(width-2)}{Colors.ACCENT}┃{Colors.RESET}")
    print(f"{Colors.ACCENT}┗{"━" * (width-2)}┛{Colors.RESET}")

def print_footer():
    width = 40
    print(f"{Colors.ACCENT}{"━" * width}{Colors.RESET}")

def styled_input(prompt):
    return input(f"{Colors.CYAN}{prompt}{Colors.RESET}")

def print_error(msg):
    print(f"{Colors.ACCENT}Error: {Colors.TEXT}{msg}{Colors.RESET}")

def print_success(msg):
    print(f"{Colors.GREEN}✔ {Colors.TEXT}{msg}{Colors.RESET}")
