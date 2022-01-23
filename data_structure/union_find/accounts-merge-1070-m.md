# Accounts Merge 1070 (M)

## Problem

Given a list accounts, each element accounts\[i] is a list of strings, where the first element accounts\[i]\[0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in **sorted order**. The accounts themselves can be returned in any order.

The length of accounts will be in the range \[1, 1000].\
The length of accounts\[i] will be in the range \[1, 10].\
The length of accounts\[i]\[j] will be in the range \[1, 30].Example

```
Example 1:	Input:	[		["John", "johnsmith@mail.com", "john00@mail.com"],		["John", "johnnybravo@mail.com"],		["John", "johnsmith@mail.com", "john_newyork@mail.com"],		["Mary", "mary@mail.com"]	]		Output: 	[		["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],		["John", "johnnybravo@mail.com"],		["Mary", "mary@mail.com"]	]	Explanation: 	The first and third John's are the same person as they have the common email "johnsmith@mail.com".	The second John and Mary are different people as none of their email addresses are used by other accounts.	You could return these lists in any order, for example the answer		[		['Mary', 'mary@mail.com'],		['John', 'johnnybravo@mail.com'],		['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']	]	is also acceptable.
```

## Solution - Union Find

* Step1:&#x20;
  * dict: meails -> \[id]
    * 123@hello.com -> \[1,3,5]
    * 456@hello.com -> \[2,4]
    * 789@hello.com -> \[4, 9]
* Step2:
  * Union: for same mail's id, merge to one group
    * (1,3,5), (2,4,9)
* Step3:
  * merge id's emails to the root\_id
* Step4:
  * Mapping to people's names

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """
    def accountsMerge(self, accounts):
        # write your code here
        
        # step1: email -> id
        email_to_indexs = self.get_email_to_indexs(accounts)
        
        # step2: Union
        self.init(len(accounts))
        for email, indexs in email_to_indexs.items():
            root_id = indexs[0]
            # rest of index merge with root_id
            for index in indexs[1:]:
                self.union(root_id, index)
        # step3: 
        index_to_email_set = self.get_index_to_email_set(accounts)

        #step4: merge
        merged_account = []
        for user_id, email_set in index_to_email_set.items():
            merged_account.append([accounts[user_id][0], *sorted(email_set)])
        return merged_account
    
    def get_email_to_indexs(self, accounts):
        email_to_indexs = {}
        for user_index, emails in enumerate(accounts):
            for i in range(1, len(emails)):
                email_to_indexs[emails[i]] = email_to_indexs.get(emails[i], [])
                email_to_indexs[emails[i]].append(user_index)
        
        return email_to_indexs

    def get_index_to_email_set(self, accounts):
        index_to_email_set = {}
        for user_index, emails in enumerate(accounts):
            root_user_index = self.find(user_index)
            index_to_email_set[root_user_index] = index_to_email_set.get(root_user_index, set())
            for email in emails[1:]:
                index_to_email_set[root_user_index].add(email)
        return index_to_email_set
        

    def init(self, n):
        self.father = {}
        for i in range(n):
            self.father[i] = i
    
    def find(self, x):
        root = x
        while self.father[root] != root:
            root = self.father[root]
        
        # path compression
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        return root
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

****

## Solution - DFS

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(list)
        
        # construct data structure
        # O(mn)
        email_to_name = {}
        for acct in accounts:
            name = acct[0]
            email1 = acct[1]
            email_to_name[email1] = name
            for email2 in acct[2:]:
                graph[email1].append(email2)
                graph[email2].append(email1)
                email_to_name[email2] = name
        
        # DFS, let those in same component group, be grouped together
        seen = set()
        stack = []
        ans = []
        for email in email_to_name.keys():
            if email in seen:
                continue
            seen.add(email)
            stack.append(email)
            name = email_to_name[email]
            tmp = []
            
            while stack:
                cur_email = stack.pop()
                tmp.append(cur_email)
                for neighbor in graph[cur_email]:
                    if neighbor not in seen:
                        stack.append(neighbor)
                        seen.add(neighbor)
            
            tmp.sort() # O(mnlog(mn))
            tmp.insert(0, name) # O(mn)
            ans.append(tmp)
        return ans
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

* **Time Complexity: O(mnlog(mn)**
  * m: number of account
  * n: max length of single account
* **Space Complexity:**
