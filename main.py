# This is a sample Python script.

class ZerosMaker:
    def __init__(self, m, n):
        self.m = m
        self.n = n

    def print_hi(self, name):
        print(f'Hi, {name}')

    def zeros(self):
        print(f'm == {self.m}, n == {self.n} \n')
        strz = str(0)*self.m
        for i in range(0, self.n):
            print(strz)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    zs_maker = ZerosMaker(5, 9)
    zs_maker.print_hi('PyCharm')
    zs_maker.zeros()

