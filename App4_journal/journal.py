"""
This is the journal data structure module.
"""
import os


def load(name):
    """
    This method creates and loads a new journal.

    :param name: This base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """
    # Create new data structure; in this case empty List created by []
    data = []   # Also could have used ... data = list()
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    """
    This method saves the journal data

    :param name: This is the journal filename
    :param journal_data: This is the data list name
    :return: does not return anything
    """
    filename = get_full_pathname(name)
    print("..... saving to: {}".format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_pathname(name):
    """
    This methos gets the full pathname

    :param name: Name of journal data file
    :return: The full journal file path name
    """
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    """
    This module adds the journal entry or log to the journal data file

    :param text: Journal entry text
    :param journal_data: This is the data list name
    :return: Does not return anything
    """
    journal_data.append(text)
