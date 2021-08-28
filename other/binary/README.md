# Binary

## Decimal to Binary 

Similar to binary search

```python
n = 23
bi_str = ''
cal_one = 0
while n:
    if n%2 == 1:
        cal_one +=1
    bi_str = str(n%2) + bi_str
    n//=2

print(bi_str)
print(cal_one)
```

```text
10111
4
```

