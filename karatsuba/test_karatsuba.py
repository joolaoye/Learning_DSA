from karatsuba import karatsuba


def test_1():
    assert karatsuba("1000", "9") == 9000
    assert karatsuba("5678", "1234") == 7006652
    assert karatsuba("99999", "123") == 12299877