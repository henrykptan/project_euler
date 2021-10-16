"""
A common security method used for online banking is to ask the user for three random characters from a passcode.
For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters;
the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order,
analyse the file so as to determine the shortest possible secret passcode of unknown length.

Notes:
    Info from each entry: for each set of 3 numbers, they all must appear in the order stated within the full passcode

    Can the same number appear more than once in the passcode?
        Looking at the entries there are no repeated numbers...

    319
    152
    295

    password must be made up of the set of all chars eg (1, 2, 3, 5, 9)

    Relationships:

    3 -> [1, 9], 1 -> [9]
    1 -> [5, 2], 5 -> [2]
    2 -> [9, 5], 9 -> [5]

    1 -> [2, 5, 9]
    2 -> [5, 9]
    3 -> [1, 9]
    5 -> [2]
    9 -> [5]
    --------------------------------------------------------------------------------------------

    For the given file the mappings look like:
    {
    '1': {'2', '9', '0', '6', '8'},
    '2': {'9', '0', '8'},
    '3': {'1', '2', '9', '0', '6', '8'},
    '6': {'9', '0', '2', '8'},
    '7': {'1', '2', '9', '0', '3', '6', '8'},
    '8': {'9', '0'},
    '9': {'0'}
    }

    Implications:
    7 not mapped to by anything -> first digit
    0 has no mappings -> last digit
    No mapping loops ie no occurrence of a -> b -> a
    -> no duplicate digits in the password
    -> shortest password is 8 digits long, only made up of (0, 1, 2, 3, 6, 7, 8, 9)

    eg 7 * * * * * * 0 where * in (1, 2, 3, 6, 8, 9)

    Plan:
    Given mappings, breadth first search starting from 7, until all digits present
    - once found that is (one of) the shortest solutions
    (Would not work for multiple disconnected graphs?)
    (Not convinced on this for other scenarios)
    (can kinda just work backwards from the mappings to get the code)
"""

import logging
import os
import pprint
from queue import Queue
from typing import List, Set

logging.basicConfig(encoding='utf-8', level=logging.INFO)


def _get_number_mappings(keylog_entries: List[str]) -> dict[str, set[str]]:
    mappings = {}
    for entry in keylog_entries:
        if entry[0] in mappings:
            mappings[entry[0]].update([entry[1], entry[2]])
        else:
            mappings[entry[0]] = {entry[1], entry[2]}
        if entry[1] in mappings:
            mappings[entry[1]].update([entry[2]])
        else:
            mappings[entry[1]] = {entry[2]}
    return mappings


def _bfs_until_all_digits_encountered(start_digit: str,
                                      mappings: dict[str, set[str]],
                                      possible_digits: Set[str]) -> tuple[int, List[str]]:
    # queue contains entries of the current digit and the running path
    # starting at start_digit where path so far is just start_digit
    queue = Queue()
    queue.put((start_digit, [start_digit]))
    while queue:
        current_digit, running_path = queue.get()
        neighbour_digits = mappings.get(current_digit, {})
        for neighbour in neighbour_digits:
            new_path = running_path + [neighbour]
            if not possible_digits - set(new_path):
                return len(new_path), new_path
            queue.put((neighbour, new_path))


if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, '../../resources/p079_keylog.txt')) as keylog:
        lines = keylog.readlines()

        bucket_1 = set(map(lambda line: line[0], lines))
        bucket_2 = set(map(lambda line: line[1], lines))
        bucket_3 = set(map(lambda line: line[2], lines))

        logging.info(f'Bucket 1: {bucket_1}')
        logging.info(f'Bucket 2: {bucket_2}')
        logging.info(f'Bucket 3: {bucket_3}')

        number_mappings = _get_number_mappings(lines)

        logging.info(f'Number mappings: {pprint.pformat(number_mappings)}')

        solution_length, solution = _bfs_until_all_digits_encountered('7',
                                                                      number_mappings,
                                                                      set.union(bucket_1, bucket_2, bucket_3))
        logging.info(f'Solution: {solution}')
