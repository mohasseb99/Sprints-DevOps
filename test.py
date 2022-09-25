import sprints

def test_func():
    assert sprints.MyFunc([2, 5, 4, 3.2, 5.2]) == [3, 5.2], "should be [3, 5.2]"


def test_func1():
    assert sprints.MyFunc([]) == 0, "should be 0"

def test_func2():
    assert sprints.MyFunc([2, 5, 4]) == [3, "none"], "should be [3, 'none']"


if __name__ == "__main__":
    test_func()
    test_func1()
    test_func2()
    print("Everything passed")
