from calculator import add, sub, mul, div


def run_tests():
    assert add(2, 3) == 5
    assert sub(5, 2) == 3
    assert mul(3, 4) == 12
    assert div(10, 2) == 5

    # check division by zero raises the right error
    try:
        div(5, 0)
    except ValueError as e:
        assert "Cannot divide by zero" in str(e)
    else:
        raise AssertionError("div(5, 0) should raise ValueError")

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()


