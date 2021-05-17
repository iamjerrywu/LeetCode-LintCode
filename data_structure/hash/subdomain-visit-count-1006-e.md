# Subdomain Visit Count 1006 \(E\)

## Problem

A website domain like "discuss.lintcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "lintcode.com", and at the lowest level, "discuss.lintcode.com". When we visit a domain like "discuss.lintcode.com", we will also visit the parent domains "lintcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count \(representing the number of visits this domain received\), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.lintcode.com".

We are given a list `cpdomains` of count-paired domains. We would like a list of count-paired domains, \(in the same format as the input, and in any order\), that explicitly counts the number of visits to each subdomain.

* The length of `cpdomains` will not exceed `100`.
* The length of each domain name will not exceed `100`.
* Each address will have either 1 or 2 "." characters.
* The input count in any count-paired domain will not exceed `10000`.
* The answer output can be returned in any order.

Example

**Example 1:**

```text
Input: 
["9001 discuss.lintcode.com"]
Output: 
["9001 discuss.lintcode.com", "9001 lintcode.com", "9001 com"]
Explanation: 
We only have one website domain: "discuss.lintcode.com". As discussed above, the subdomain "lintcode.com" and "com" will also be visited. So they will all be visited 9001 times.
```

**Example 2:**

```text
Input: 
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: 
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
Explanation: 
We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times. For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param cpdomains: a list cpdomains of count-paired domains
    @return: a list of count-paired domains
    """
    def subdomainVisits(self, cpdomains):
        # Write your code here
        record = {}
        for cpdomain in cpdomains:
            cpdomain_list = cpdomain.split(" ")
            count = int(cpdomain_list[0])
            domains = cpdomain_list[1]
            domains_list = cpdomain_list[1].split(".")
            for i in range(len(domains_list)):
                record[".".join(domains_list[i:])] = record.get(".".join(domains_list[i:]), 0) + count
        res = []
        for key, val in record.items():
            res.append(str(val) + " " + key)
        return res
                
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

