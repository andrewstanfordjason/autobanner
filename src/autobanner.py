import os
import sys
from datetime import datetime

# insert the text within a commented section but center it
def centered(text, width, comment_thing = '//'):
    space = (width - len(comment_thing)*2 - len(text))
    left_padding = space // 2 
    right_padding = space - left_padding
    return comment_thing + ' ' * left_padding + text + ' ' * right_padding + comment_thing

def left(text, width, comment_thing = '//'):
    space = (width - len(comment_thing)*2 - len(text))
    left_padding = 1
    right_padding = space - left_padding
    return comment_thing + ' ' * left_padding + text + ' ' * right_padding + comment_thing

def autobanner(width = 80, extra_lines = []):

    banner_str = ''
    banner_str += '/'*width + '\n'

    banner_str += centered('', width)+ '\n'
    banner_str += centered("This file was generated, DO NOT EDIT.", width)+ '\n'
    banner_str += centered('', width)+ '\n'

    cwd = os.getcwd()
    cmd = ' '.join(sys.argv)

    banner_str += left('To reproduce, run:', width)+ '\n'
    banner_str += left('   python ' + str(cmd), width)+ '\n'
    banner_str += left('From:', width)+ '\n'
    banner_str += left('   ' + str(cwd) , width)+ '\n'
    banner_str += centered('', width)+ '\n'

    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    banner_str += left('Generated on: ' + date_time, width)+ '\n'
    banner_str += left('          by: ' + str(os.getlogin()), width)+ '\n'
    banner_str += left('   ', width)+ '\n'

    banner_str += '/'*width+ '\n'

    for line in extra_lines:
        banner_str += left(line, width)+ '\n'
        banner_str += left('', width)+ '\n'

    return banner_str
