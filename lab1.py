tsil_tni = []  # for reverse_rec, if placed inside would set the reversed list to [] every time


def max_list_iter(int_list):  # must use iteration not recursion
   if int_list == None:
      raise ValueError
      # returns error if nothing given
   if len(int_list) == 0:
      return None
      # returns nothing if empty list given
   big_boi = int_list[0]  # holder for largest value, starts at the first value rather than 0 in case negatives
   for val in int_list:
      if val > big_boi:
         big_boi = val
      # replaces big_boi with value if bigger than previous big_boi
   return big_boi


def reverse_rec(int_list):  # must use recursion
   temp = int
   if int_list == None:
      raise ValueError
      # returns error if nothing given
   tsil_tni.append(int_list[0])  # puts int_list[iter] at tsil_tni[0] pushing the earlier int_lists back
   del int_list[0]
   return reverse_rec(int_list) if len(int_list) > 1 else tsil_tni  # returns tsil_tni when iter = len(int_list)


def bin_search(target, low, high, int_list):  # must use recursion
   """if int_list is None:
      raise ValueError
   if target < int_list[low] or target > int_list[high]:
      return None
   mid = ((high - low) // 2) + low
   if int_list[mid] == target:
      return mid
   if high - low <= 2:
      return None
   return bin_search(target, mid, high, int_list) if target > int_list[mid] else bin_search(target, low, mid, int_list)"""

   found = None  # if target isnt found returns None by default
   if int_list == None:
      raise ValueError
      # returns error if nothing given
   if len(int_list) < 1:
      return None
      # returns nothing if given empty list
   if int_list[low] == target:
      found = low
   return found if found == low or low == high else bin_search(target, low + 1, high, int_list)
   # stops when find the target to save time and stops when low = high because low goes up every time
