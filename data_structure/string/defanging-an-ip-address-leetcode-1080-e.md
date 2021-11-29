# Defanging an IP Address (LeetCode 1080) (E)

## Problem

Given a valid (IPv4) IP `address`, return a defanged version of that IP address.

A _defanged IP address_ replaces every period `"."` with `"[.]"`.

**Example 1:**

```
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
```

**Example 2:**

```
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
```

**Constraints:**

* The given `address` is a valid IPv4 address.

## Solution

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def defangIPaddr(self, address: str) -> str:
        address_list = address.split('.')
        return '[.]'.join(address_list)
        
        '''
        address_list = address.split('.')
        ans = ''
        for i in range(len(address_list) - 1):
            ans+=address_list[i] + '[.]'
        ans+=address_list[-1]
        return ans
        '''
```
{% endtab %}

{% tab title="Java" %}
```java
class Solution {
    public String defangIPaddr(String address) {
        String address_arr[] = address.split("\\.");
        
        
        String ans = "";
        for (int i = 0; i < address_arr.length - 1; i++) {
            ans+=address_arr[i] + "[.]";
        }
        ans+=address_arr[address_arr.length - 1];
        
        return ans;
    }
}
```
{% endtab %}

{% tab title="C++" %}
```
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**
