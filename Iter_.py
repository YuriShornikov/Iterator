
class FlatIterator():
    def __init__(self, test_list):
        self.test_list = test_list

    def __iter__(self):
        self.cur_1 = 0
        self.cur_2 = 0
        return self

    def __next__(self):
        if len(self.test_list) > self.cur_1:
            if (len(self.test_list[self.cur_1]) - 1) > self.cur_2:
                self.cur_2 += 1
                return self.test_list[self.cur_1][(self.cur_2) - 1]
            if (len(self.test_list[self.cur_1]) - 1) == self.cur_2:
                self.cur_1 += 1
                a = self.cur_2
                self.cur_2 = 0
                return self.test_list[self.cur_1 - 1][a]

        else:
            raise StopIteration

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


if __name__ == '__main__':
    test_1()


