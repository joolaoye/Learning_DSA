def karatsuba(string_a, string_b):
    if len(string_a) == 1 and len(string_b) == 1:
        return int(string_a) * int(string_b)


    maxlen = max(len(string_a), len(string_b))

    string_a = string_a.zfill(maxlen)
    string_b = string_b.zfill(maxlen)

    n = maxlen // 2

    if maxlen % 2:
        a,b = string_a[:n+1], string_a[n+1:]
        c,d = string_b[:n+1], string_b[n+1:]
    else:
        a, b = string_a[:n], string_a[n:]
        c, d = string_b[:n], string_b[n:]

    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    ad_bc = karatsuba(str(int(a)+int(b)), str(int(c)+int(d))) - ac - bd

    return (10 ** (2*n)) * ac + (10 ** n) * ad_bc + bd