import os
import sys

sys.path.append('..')

from web.get_bays_info import get_section_names_one_division 

def main():

	print(" => Test: get_section_counts_one_division")
	section_names = get_section_names_one_division(2017, "Fall", "Boys", 4, 2)
	print(len(section_names), section_names)

if __name__ == '__main__':
    main()
