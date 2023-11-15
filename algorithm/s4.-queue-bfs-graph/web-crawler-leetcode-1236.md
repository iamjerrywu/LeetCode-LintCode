# Web Crawler (LeetCode 1236)

## Problem



Given a url `startUrl` and an interface `HtmlParser`, implement a web crawler to crawl all links that are under the **same hostname** as `startUrl`.&#x20;

Return all urls obtained by your web crawler in **any** order.

Your crawler should:

* Start from the page: `startUrl`
* Call `HtmlParser.getUrls(url)` to get all urls from a webpage of given url.
* Do not crawl the same link twice.
* Explore only the links that are under the **same hostname** as `startUrl`.

![](https://assets.leetcode.com/uploads/2019/08/13/urlhostname.png)

As shown in the example url above, the hostname is `example.org`. For simplicity sake, you may assume all urls use **http protocol** without any **port** specified. For example, the urls `http://leetcode.com/problems` and `http://leetcode.com/contest` are under the same hostname, while urls `http://example.org/test` and `http://example.com/abc` are not under the same hostname.

The `HtmlParser` interface is defined as such:&#x20;

```
interface HtmlParser {
  // Return a list of all urls from a webpage of given url.
  public List<String> getUrls(String url);
}
```

Below are two examples explaining the functionality of the problem, for custom testing purposes you'll have three variables `urls`, `edges` and `startUrl`. Notice that you will only have access to `startUrl` in your code, while `urls` and `edges` are not directly accessible to you in code.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/10/23/sample\_2\_1497.png)

<pre><code>Input:
urls = [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.google.com",
  "http://news.yahoo.com/us"
]
edges = [[2,0],[2,1],[3,2],[3,1],[0,4]]
startUrl = "http://news.yahoo.com/news/topics/"
<strong>Output:
</strong> [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.yahoo.com/us"
]
</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2019/10/23/sample\_3\_1497.png)

<pre><code>Input: 
urls = [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.google.com"
]
edges = [[0,2],[2,1],[3,2],[3,1],[3,0]]
startUrl = "http://news.google.com"
<strong>Output:
</strong> ["http://news.google.com"]
<strong>Explanation: 
</strong>The startUrl links to all other pages that do not share the same hostname.
</code></pre>

&#x20;

**Constraints:**

* `1 <= urls.length <= 1000`
* `1 <= urls[i].length <= 300`
* `startUrl` is one of the `urls`.
* Hostname label must be from 1 to 63 characters long, including the dots, may contain only the ASCII letters from 'a' to 'z', digits  from '0' to '9' and the hyphen-minus character ('-').
* The hostname may not start or end with the hyphen-minus character ('-').&#x20;
* See:  [https://en.wikipedia.org/wiki/Hostname#Restrictions\_on\_valid\_hostnames](https://en.wikipedia.org/wiki/Hostname#Restrictions\_on\_valid\_hostnames)
* You may assume there're no duplicates in url library.



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
from collections import deque
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        res = []
        queue = deque([startUrl])
        hostname = self.get_hostname(startUrl)
        visited = set([startUrl])
        while queue:
            url = queue.popleft()
            hn = self.get_hostname(url)
            if hn == hostname:
                res.append(url)
                # only craw the url that has same hostname
                for nxt_url in htmlParser.getUrls(url):
                    if nxt_url not in visited:
                        visited.add(nxt_url)
                        queue.append(nxt_url)
        return res
    
    def get_hostname(self, url):
        hostname = url[7:]
        if '/' in hostname:
            idx = hostname.find('/')
            hostname = hostname[:idx]
        return hostname
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**
