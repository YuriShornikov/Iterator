

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        pass

    def __iter__(self):
        self.flat_iterator_item = 0
        self.check_item = 0
        return self

    def __next__(self):

        return self.list_of_list.pop()

# list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
#     ]

# test = FlatIterator(list_of_lists_1)
# print(test)

# iter1 = iter(list_of_lists_1)
# for i in iter1:
#     iter2 = iter(i)
#     for a in iter2:
#         print(a)



    # print(i)
    # print(next(iter1))
def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

            assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#
#
if __name__ == '__main__':
    test_1()