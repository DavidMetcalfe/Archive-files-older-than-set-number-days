from os import path, makedirs, walk
from datetime import datetime, date, timedelta
from shutil import move
import logging

'''
Checks last used/accessed and creation date
of file(s) in directory. If older than set
threshhold, move to Archived folder.Archived

David Metcalfe, May 5 2017
'''

makedirs('Archived', exist_ok=True)

# Logging config
logging.basicConfig(level=logging.INFO)

def get_script_directory():
    # Returns the directory of the script.
    return path.dirname(path.realpath(__file__))


def get_file_modification_date(filename):
    # Returns the modification date of the inputted file.
    return datetime.fromtimestamp(path.getmtime(filename))


def days_to_compare_from_today(days):
    # Return the timedelta of today's date minus 'days'
    return date.today() - timedelta(days=days)

def compare_dates(date1, date2):
    return get_file_modification_date(date1).date() < days_to_compare_from_today(365)


scriptDir = get_script_directory()


def osWalk():
    # Walk the directory of the script, return filenames.
    for dirname, dirnames, filenames in walk(scriptDir):
        for file in filenames:
            if compare_dates(path.join(scriptDir, file), days_to_compare_from_today(365)):
                move(path.join(scriptDir, file), 'Archived')
                logging.info("Archived {0}".format(file))
        break

osWalk()
