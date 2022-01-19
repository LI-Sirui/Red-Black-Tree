# Unit test
from RedblackTree import *


def test_insert(tree):
    """Test insert-, write, count and healthy function for RedblackTree."""
    assert not tree.write()
    assert tree.count() == 0

    tree.insert(50)
    assert tree.write() == [50]
    # assert tree.count() == 1
    tree.healthy()

    tree.insert(77)
    assert tree.write() == [50, 77]
    # assert tree.count() == 2
    tree.healthy()

    tree.insert(55)
    assert tree.write() == [50, 55, 77]
    #assert tree.count() == 3
    tree.healthy()

    tree.insert(29)
    assert tree.write() == [29, 50, 55, 77]
    # assert tree.count() == 4
    tree.healthy()

    tree.insert(10)
    assert tree.write() == [10, 29, 50, 55, 77]
    # assert tree.count() == 5
    tree.healthy()

    tree.insert(30)
    assert tree.write() == [10, 29, 30, 50, 55, 77]
    # assert tree.count() == 6
    tree.healthy()

    tree.insert(66)
    assert tree.write() == [10, 29, 30, 50, 55, 66, 77]
    # assert tree.count() == 7
    tree.healthy()

    tree.insert(18)
    assert tree.write() == [10, 18, 29, 30, 50, 55, 66, 77]
    # assert tree.count() == 8
    tree.healthy()

    tree.insert(80)
    assert tree.write() == [10, 18, 29, 30, 50, 55, 66, 77, 80]
    tree.healthy()

    tree.insert(51)
    assert tree.write() == [10, 18, 29, 30, 50, 51, 55, 66, 77, 80]
    tree.healthy()

    tree.insert(90)
    assert tree.write() == [10, 18, 29, 30, 50, 51, 55, 66, 77, 80, 90]
    tree.healthy()


def test_delete(tree):
    """Test deletData function for RedblackTree."""
    tree.deletData(80)
    assert tree.write() == [5, 8, 15, 17, 18, 25, 40]
    assert tree.count() == 7
    tree.healthy()

    tree.deletData(25)
    assert tree.write() == [5, 8, 15, 17, 18, 40]
    assert tree.count() == 6
    tree.healthy()

    tree.deletData(17)
    assert tree.write() == [5, 8, 15, 18, 40]
    assert tree.count() == 5
    tree.healthy()


def test_find(tree):
    """Test find function for RedblackTree."""
    assert tree.find(5)
    assert not tree.find(17)


def main():
    tree = RbTree()
    test_insert(tree)
    # test_delete(tree)
    # test_find(tree)

if __name__ == '__main__':
    main()
