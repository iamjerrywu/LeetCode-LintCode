# Count Email Groups 1632 \(E\)

## Problem

Give you an array of n email addresses.  
Find the number of email groups and each group should have more than one email address\(the address can be duplicated\). If two strings have the same value after being transformed, they are in the same group.

The rules of transforming are as follows:

1. Ignore all the characters '.' before the character '@'.
2. Ignore the substring which starts with the first '+'\(included\) and ends with the character '@'\(exclude\).

a email group have at least two same email address\(after transforming\)Example

**Example1**

```text
Input: emails = ["abc.bc+c+d@jiuzhang.com", "abcbc+d@jiuzhang.com", "abc.bc.cd@jiuzhang.com"]
Output: 1
Explanation: 
"abc.bc+c+d@jiuzhang.com" transforms to "abcbc@jiuzhang.com"
"abcbc+d@jiuzhang.com" transforms to "abcbc@jiuzhang.com"
"abc.bc.cd@jiuzhang.com" transforms to "abcbccd@jiuzhang.com"
We can see that the first address and the second address are in the same group, and there is no address can transform to the same address as the third one. Therefore, there is only one group which meets the requrements.
```

**Example2**

```text
Input: emails = ["abc.b+c+d@jiuzhang.com", "abcbc+d@jiuzhang.com", "abc.bc.cd@jiuzhang.com"]
Output: 0
Explanation: 
There is no group meet the conditions.
```

## Solution

Simply process the email string \(required splitting based on '@'\)

* Need to used set\(\) to avoid same raw input
* Need to use dict to record each groups member counts after processing the raw data 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param emails: Original email
    @return: Return the count of groups which has more than one email address in it.
    """
    def countGroups(self, emails):
        # Write your code here
        ref, appeared = {}, set()
        
        for email in emails:
            if email in appeared:
                continue
            appeared.add(email)
            email_lists = email.split('@')
            processed_email = ''
            for i in range(len(email_lists)):
                # text before '@'
                for c in email_lists[0]:
                    if c == '+':
                        break
                    if c!='.':
                        processed_email+=c
                # text after '@'
                for c in email_lists[1]:
                    processed_email+=c
            ref[processed_email] = ref.get(processed_email, 0) + 1
            
        cnt = 0
        for val in ref.values():
            if val > 1:
                cnt+=1
        return cnt        

```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n \* l\)**
  * n: total mail's amount
  * l: max length of the mail
* **Space Complexity: O\(n\)**
  * Might need the max length n of hashmap or set

