from calc import square

def main():
    test_square()


    # def test_square():
    #     # this might be corner case because 2+2= 4 and 2 squared 2 is also 4
    #     if square(2) != 4:
    #         print("2 squared was not 4")
    #     if square(3) != 9:
    #         print("3 squared was not 9")
    #     #assert square(2) == 4

# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("AssertionError at 2 squared not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("AssertionError at -3 squared not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("AssertionError at 0 squared not 0")
    try:
        assert square(-1) == -1
    except AssertionError:
        print("AssertionError at -1 squared not -1")


if __name__ == "__main__":
    main()