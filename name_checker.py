"""
@descriptiom: Checks for properly formated music folders
@author: Stavros Avramidis (@purpl3F0x)

@usage: music_rename.py [workdir=]

@LICENSE: APACHE 2.0
"""

import os
import re

try:
    from termcolor import colored
    import colorama
    colorama.init()
except ImportError:
    def colored(x, _):
        return x

CUR_PATH = os.getcwd()

# our beloved regex, that no one understands (https://regex101.com/r/ZbeDLM/latest) might help :D
regex = r"^[^\-]+\s{1}-\s{1}[^\-]+ (?:\(\d{4}(?:-\d{4})?(?: Remaster)?\)) ?(?:\[.+\])?(?:\{.+\})?$"

#   Some Examples
#
#   Black Sabbath - Paranoid (1970-2014) [Qobuz]
#   Black Sabbath - Paranoid (1970 Remaster)
#   Black Sabbath - Heaven and Hell (2014) [TIDAL]


if __name__ == "__main__":
    import sys
    import getopt

    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["workdir="])

    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)

    for i, j in opts:
        if (i == "--workdir"):
            if (os.path.exists(j) and os.path.isdir(j)):
                CUR_PATH = j
                print("working dir", j)
            else:
                raise OSError("Directory Not Found")

    ############################################################

    # Get all sufolders
    LOCAL_FOLDERS = [d for d in os.listdir(
        CUR_PATH) if not d.startswith(".") and os.path.isdir(os.path.join(CUR_PATH, d))]

    # do some magic :)

    formatted = []
    not_formatted = []

    def total_folders(): return len(formatted) + len(not_formatted)

    for f in LOCAL_FOLDERS:
        if re.match(regex, f) and not "  " in f:
            formatted.append(f)
        else:
            not_formatted.append(f)

    print(colored('Properly Formated Folders: ({}/{})\n'.format(len(formatted),
                                                                total_folders()), 'magenta'))
    for f in formatted:
        print(colored(f, 'green'))

    print()
    for f in not_formatted:
        print(colored(f, 'red'))

    print("\n\nBye ;(")
