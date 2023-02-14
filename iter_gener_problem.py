
test_list = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
        ]
class Test_for():
    def __init__(self, test_list):
        self.test_list = test_list

    def __iter__(self):
        for i in range(len(self.test_list)+1):
            for j in range(i+1):
                yield self.test_list[i][j]


t = Test_for(test_list)
it = iter(t)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
