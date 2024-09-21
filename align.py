from os import get_terminal_size

def get_width():
    terminal_size = get_terminal_size(); terminal_size = str(terminal_size)
    terminal_size = terminal_size.split('=')[1].split(',')[0]
    return int(terminal_size)

def get_height():
    terminal_size = get_terminal_size(); terminal_size = str(terminal_size)
    terminal_size = terminal_size.split(',')[1].split('=')[1].split(')')[0]
    return int(terminal_size)

def centre_align(string):
    if get_width() % 2 == 0:
        if len(string) % 2 == 0:
            return ' ' * int((get_width() - len(string)) / 2) + string
        else:
            return ' ' * int(((get_width() - len(string)) - 1) / 2) + string
    else:
        if len(string) % 2 == 0:
            return ' ' * int(((get_width() + 1) - len(string)) / 2) + string
        else:
            return ' ' * int((((get_width() + 1) - len(string)) - 1) / 2) + string

def middle_align():
    pass