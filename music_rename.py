"""
@descriptiom: File to rename my music folders 
@author: Stavros Avramidis (@purpl3F0x)


@usage: music_rename.py [artist=, workdir=, source=]

#LICENSE: APACHE 2.0
"""

import os

try:
    from termcolor import colored
except ImportError:
    def colored(x, _):
        return x

CUR_PATH = os.getcwd()
ARTIST = None
SOURCE = None


if __name__ == "__main__":
    import sys
    import getopt

    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "ho:v",
            ["artist=", "workdir=", "source="]
        )

    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)

    for i, j in opts:
        if (i == "--workdir"):
            if (os.path.exists(j) and os.path.isdir(j)):
                CUR_PATH = j
            else:
                raise OSError("Directory Not Found"); exit(2)

        elif (i == "--artist"):
            ARTIST = j

        elif(i == "--source"):
            SOURCE = j

    if not ARTIST:
        ARTIST = os.path.basename(CUR_PATH)

    LOCAL_FOLDERS = [d for d in os.listdir(CUR_PATH) if not d.startswith(".") and os.path.isdir(d)]

    if not LOCAL_FOLDERS:
        exit(0)

    max_length = max([len(x) for x in LOCAL_FOLDERS])

    RENAMES = []
    for folder in LOCAL_FOLDERS:
        RENAMES.append(
            [folder, "{} - {} {}".format(ARTIST, folder, "" if not SOURCE else "[{}]".format(SOURCE))]
        )

        print("{}{} -->  ".format(colored(RENAMES[-1][0], 'red'),(max_length - len(folder))*" "), end="")
        print(colored(RENAMES[-1][1], 'green'))

    print("Proceed (y/N)?", end='')

    if input() not in ('y','Y'): print("Aborting ... bye ;(");exit()

    for old_name, new_name in RENAMES:
        os.rename(
            os.path.join (CUR_PATH, old_name),
            os.path.join (CUR_PATH, new_name)
        )

    print("Found and renamed %i folders\nBye :))")
