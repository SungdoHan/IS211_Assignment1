__author__ = 'SungdoHan'


def listDivide(numbers, divide=2):
    divisible = []
    for values in numbers:
        if values % 2 == 0:
            divisible.append(values)	
    return divisible


class ListDivideException(Exception):
    pass


def testListDivide():
    try:
        print listDivide([1,2,3,4,5])
        print listDivide([2,4,6,8,10])
        print listDivide([30, 54, 63,98, 100], divide=10)
        print listDivide([])
        print listDivide([1,2,3,4,5], 1)
    except (ListDivideException):
        pass
    

if __name__ == '__main__':
	two = testListDivide()
	ttwo = listDivide([30, 54, 63,98, 100], divide=10)
