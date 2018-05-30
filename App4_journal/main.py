import journal
# from journal import load, save
# from journal import *


def mainLoop():
    print_header()
    run_event_loop()


def print_header():
    print('------------------------')
    print('    JOURNAL APP')
    print('------------------------')


def run_event_loop():
    """
    This is the main program loop with user interaction

    :return: None
    """
    print('What do you want to do with your journal?')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)  # []  # list()

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[X]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, we don't understand '{}'.".format(cmd))

    print('Done, goodbye.')
    journal.save(journal_name, journal_data)


def list_entries(data):
    """
    This method outputs the journal entries for user

    :param data: This is the data structure with entries
    :return: None
    """
    print('Your journal entries: ')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx + 1, entry))


def add_entry(data):
    """
    This module adds new entries to the journal

    :param data: This is the data structure to which the entry is appended
    :return: None
    """
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)
    # data.append(text)


# print("__file__ " + __file__)
# print("__name__ " + __name__)

# For running external files use __name__ to skip a call such as mainLoop() below.
# The variable __name__ (dundername) reflects which file is running; If we run this file (main.py), dundername
# is '__main__' so # mainLoop() runs. However, if we run another file e.g. program2.py, dundername will be
# 'program2' so mainLoop() will not run and program2 can run normally.
if __name__ == '__main__': # This is called "dundername"; from __name__ (underundername)
    mainLoop()

# mainLoop()
