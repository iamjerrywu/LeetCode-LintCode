# Prefix Sum

## 1-D Array Prefix Sum Template



{% tabs %}
{% tab title="python" %}
```python
def get_prefix_sum(self, A):
        prefix_sum = [0]
        for num in A:
            prefix_sum.append(prefix_sum[-1] + num)
        return prefix_sum
```
{% endtab %}
{% endtabs %}



## 2-D Array Prefix Sum Template



{% tabs %}
{% tab title="python" %}
```python
m = len(grid)
        n = len(grid[0])
        row_prefix_sum = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                row_prefix_sum[i][j + 1] = row_prefix_sum[i][j] + grid[i][j]
        
        col_prefix_sum = [[0] * (n) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                col_prefix_sum[i + 1][j] = col_prefix_sum[i][j] + grid[i][j]
```
{% endtab %}
{% endtabs %}

