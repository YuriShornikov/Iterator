

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.flat_iterator_item = iter([])
        return self

    def __next__(self):
        if self.list_of_list is None:
            raise StopIteration
        try:
            self.list1 = next(self.flat_iterator_item)
        except StopIteration:
            self.list_of_list_pop = self.list_of_list.pop()
            self.flat_iterator_item = iter(self.list_of_list_pop)
            self.list1 = next(self.flat_iterator_item)
        # self.list1 = reversed(self.item_test)
        return self.list1

list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]


for i in FlatIterator(list_of_lists_1):
    print(i)



# iter1 = iter(list_of_lists_1)
# for i in iter1:
#     iter2 = iter(i)
#     for a in iter2:
#         print(a)



    # print(i)
    # print(next(iter1))
# def test_1():
#
#     list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
#     ]
#
#
#     # flat_iterator_item == FlatIterator(list_of_lists_1) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#     # check_item == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#
#     for flat_iterator_item, check_item in zip(
#             FlatIterator(list_of_lists_1),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#     ):
#
#             assert flat_iterator_item == check_item
#
#     assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
# #
# #
# if __name__ == '__main__':
#     test_1()


# test = []
# a = [1, 2, 3]
# # while a != []:
# #     test.append(a.pop())
# # print(list(reversed(test)))
# for i in a:
#     print(i)
#     if a != []:
#         test.append(a.pop())
# print(test)
