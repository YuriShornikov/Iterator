

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.flat_iterator_item = self.list_of_list.pop()
        self.step = 0
        return self

    def __next__(self):
        if self.step < 3:
            self.step = len(self.list_of_list) - 1
            self.step += 1
            self.flat_iterator_item
            return self.flat_iterator_item
        else:
            raise StopIteration
        # if self.list_of_list == 0:
        #     raise StopIteration
        # try:
        #     self.list1 = self.list_of_list
        # except StopIteration:
        #     self.list_of_list_pop = self.list_of_list.pop()
        #     self.flat_iterator_item = self.list_of_list_pop
        #     self.list1 = self.flat_iterator_item
        # # self.list1 = reversed(self.item_test)
        # return self.list1

list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]


for i in FlatIterator(list_of_lists_1):
    print(i)

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
