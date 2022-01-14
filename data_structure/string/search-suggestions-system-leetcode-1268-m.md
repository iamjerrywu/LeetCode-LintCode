# Search Suggestions System (LeetCode 1268) M

## Problem

Given an array of strings `products` and a string `searchWord`. We want to design a system that suggests at most three product names from `products` after each character of `searchWord` is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return _list of lists_ of the suggested `products` after each character of `searchWord` is typed.&#x20;

**Example 1:**

```
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
```

**Example 2:**

```
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
```

**Example 3:**

```
Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
```

**Example 4:**

```
Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
```

**Constraints:**

* `1 <= products.length <= 1000`
* There are no repeated elements in `products`.
* `1 <= Σ products[i].length <= 2 * 10^4`
* All characters of `products[i]` are lower-case English letters.
* `1 <= searchWord.length <= 1000`
* All characters of `searchWord` are lower-case English letters.

## Solution - Brute Force&#x20;

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort() # O(nlogn) sorting
        
        res = []
        prefix_string = '' # O(m * n)
        for c in searchWord: #O(m)
            prefix_string+=c
            search_res = []
            for product in products: #O(n)
                if product[0:len(prefix_string)] == prefix_string :
                    search_res.append(product)
                if len(search_res) == 3:
                    break
            res.append(search_res)
        return res
        
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}

{% tab title="c++" %}
```cpp
class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        sort(products.begin(), products.end());
        
        vector<vector<string>> res;
        string prefixString = "";
        
        for (char c : searchWord) {
            prefixString+=c;
            
            vector<string> searchRes;
            
            for (string product : products) {
                if (product.substr(0, prefixString.length()) == prefixString) {
                    searchRes.push_back(product);
                }
                if (searchRes.size() == 3) break;
            }
            
            res.push_back(searchRes);
        }
        return res;
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(nlogn) + O(m\*n)**
* **Space Complexity:**

## Solution - Binary Search

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort() # O(nlogn) sorting
        
        res = []
        prefix_string = '' # O(m * logn)
        for c in searchWord: #O(m)
            prefix_string+=c
            search_res = []
            index = self.binary_search(0, len(products) - 1, products, prefix_string) #O(logn)
            # WARNING! Doing boundary and corner case check
            while index != -1 and index < len(products) and len(search_res) < 3:
                if products[index][:len(prefix_string)] == prefix_string:
                    search_res.append(products[index])
                index+=1
            res.append(search_res)
        return res
    
    def binary_search(self, start, end, products, prefix_string):
        if start >= end:
            return start
        n = len(prefix_string)
        while start + 1 < end:
            mid = (start + end)//2
            if products[mid][:n] < prefix_string:
                start = mid
            else:
                end = mid
        if products[start][:n] == prefix_string:
            return start
        if products[end][:n] == prefix_string:
            return end
        return -1
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}

{% tab title="c++" %}
```cpp
class Solution {
public:
    static int binarySearch(int start, int end, vector<string>&products, string prefixString) {
        int n = prefixString.length();
        
        while (start + 1 < end) {
            int mid = start + (end - start)/2;
            
            if (products[mid].substr(0, n) < prefixString) {
                start = mid;
            } else {
                end = mid;
            }
        }
        
        if (products[start].substr(0, n) == prefixString) {
            return start;
        }
        if (products[end].substr(0, n) == prefixString) {
            return end;
        }
        
        return -1;
    }
    
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        sort(products.begin(), products.end());
        
        vector<vector<string>> res;
        string prefixString = "";
        
        for (char c : searchWord) {
            prefixString+=c;
            vector<string> searchRes;
            int index = binarySearch(0, products.size() - 1, products, prefixString);
            while (index != -1 && index < products.size() && searchRes.size() < 3) {
                if (products[index].substr(0, prefixString.length()) == prefixString) {
                    searchRes.push_back(products[index]);
                }
                index+=1;
            }
            res.push_back(searchRes);
        }
        
        return res;
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(nlogn) + O(mlogn)**
* **Space Complexity: O(n)**
