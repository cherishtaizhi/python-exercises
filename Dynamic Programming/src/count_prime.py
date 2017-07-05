# -*- coding: utf-8 -*-


class Solution(object):
    def countPrimes(self, n):
        if n < 2:
            return 0

        a = [i for i in range(2, n+1)]
        for i in a:
            if i * i >= a[-1]:
                break
            m = a.index(i * i)
            for j in a[m:]:
                if j % i == 0:
                    a.remove(j)
        return len(a)
