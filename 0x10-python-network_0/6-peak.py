#!/usr/bin/python3
"""Task 6"""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
   if type(list_of_integers) != list:
       return
   if len(list_of_integers) == 0:
       return None
   list_of_integers.sort(reverse=True)
   return list_of_integers[0]
