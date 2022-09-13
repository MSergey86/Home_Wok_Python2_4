#
# ## Задача 1 #####################################################
#
# class FlatIterator:
#     def __init__(self, list):
#         self.base_list = list
#
#     def __iter__(self):
#         self.base_list_cursor = 0
#         self.nested_list_cursor = 0
#         return self
#
#     def __next__(self):
#         self.nested_list_cursor += 1
#         if self.base_list_cursor > len(self.base_list):
#             raise StopIteration
#         if self.nested_list_cursor > len(self.base_list[self.base_list_cursor]):
#             self.base_list_cursor += 1
#             self.nested_list_cursor = 1
#         if self.base_list_cursor == len(self.base_list):
#             raise StopIteration
#         return self.base_list[self.base_list_cursor][self.nested_list_cursor-1]
#
# if __name__ == '__main__':
#     nested_list = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None],
#     ]
#     for item in FlatIterator(nested_list):
#         print(item)

##  Задача 2 ############################

def flat_generator(list):
    list_cursor = 0
    nested_list_cursor = 0
    while list_cursor < len(list):
      if nested_list_cursor == len(list[list_cursor]):
          list_cursor += 1
          nested_list_cursor = 0
      if list_cursor != len(list):
        yield list[list_cursor][nested_list_cursor]
      nested_list_cursor += 1

if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None],
    ]
    print([item for item in flat_generator(nested_list)])