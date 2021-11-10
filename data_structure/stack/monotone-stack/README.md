# Monotonic Stack

## What's Monotonic Stack?

O(n) algorithm, use to solve problem like finding the nearest element in the list that's is bigger or smaller than current element.

## Template:

```python
for i in range(n):
    while stack and condition of monotone stack is True:
        record current ans
        stack.pop()
    stack.push(i) # record the index instead of value
```

## Applicable Scenario

![](<../../../.gitbook/assets/Screen Shot 2021-06-17 at 10.07.27 AM.png>)
