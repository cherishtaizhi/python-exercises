# -*- coding: utf-8 -*-

from src import count_prime


def test_generate_primes():
    solut = count_prime.Solution()

    n = 5
    expected_result = 3
    result = solut.countPrimes(n)
    assert result == expected_result

    n = 0
    expected_result = 0
    result = solut.countPrimes(n)
    assert result == expected_result

    n = 1
    expected_result = 0
    result = solut.countPrimes(n)
    assert result == expected_result

    n = 2
    expected_result = 1
    result = solut.countPrimes(n)
    assert result == expected_result

    n = 3
    expected_result = 2
    result = solut.countPrimes(n)
    assert result == expected_result
