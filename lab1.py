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

def reverse_rec(int_list, iter):  # must use recursion
   if int_list == None:
      raise ValueError
      # returns error if nothing given
   if iter == None:
      iter = 0
      # when someone else uses this method they wont give an iter, but need for recursive so set it to 0 on first run without them having to give an iter
   tsil_tni.insert(0, int_list[iter])  # puts int_list[iter] at tsil_tni[0] pushing the earlier int_lists back
   return reverse_rec(int_list, iter + 1) if len(int_list) > iter else tsil_tni  # returns tsil_tni when iter = len(int_list)

def bin_search(target, low, high, int_list):  # must use recursion
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
