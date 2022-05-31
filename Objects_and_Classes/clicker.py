class CountingClicker:
    def __init__(self, count=0):
        self._count = count

    def click(self, num_times=1):
        self._count += num_times

    def read_count(self):
        return self._count

    def reset(self):
        self._count = 0

    def __repr__(self):
        return 'CountingClicker(count={count})'.format(count=self.count)


class NoResetClicker(CountingClicker):
    def reset(self):
        pass


clicker = CountingClicker()
assert clicker.read_count() == 0

clicker.click()
clicker.click()
clicker.click()
clicker.click()
assert clicker.read_count() == 4

clicker.reset()
assert clicker.read_count() == 0


noreset = NoResetClicker()
assert noreset.read_count() == 0
noreset.click()
noreset.click()
noreset.click()
noreset.click()
noreset.click()
assert noreset.read_count() == 5
noreset.reset()
assert noreset.read_count() == 5
