# Archive files older than the set number of days

## Description

This script archives files in the same directory as the script that have a modification date exceeding the numnber of days set in the script. 

It should be simple to change this to the creation date if desired, but I decided to archive against files I no longer modify/use vs files that have simply been around a while.

## Installation

As this script only relies on native libraries, there are no dependencies or other things to fuss with.

## Usage

1. Navigate to the script's directory. 
2. Run `python Archive_files_older_than_set_number_days.py` in Windows Command Prompt, Terminal, or whatever your system uses.
3. The logger output will detail what (if any) files have been archived.
4. Review the newly created **Archived** folder for the archived files.

## License

GNU GPL v3
