# Find All Possible Recipes from Given Supplies (LeetCode 2115) (M)



## Problem

****

You have information about `n` different recipes. You are given a string array `recipes` and a 2D string array `ingredients`. The `ith` recipe has the name `recipes[i]`, and you can **create** it if you have **all** the needed ingredients from `ingredients[i]`. Ingredients to a recipe may need to be created from **other** recipes, i.e., `ingredients[i]` may contain a string that is in `recipes`.

You are also given a string array `supplies` containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return _a list of all the recipes that you can create._ You may return the answer in **any order**.

Note that two recipes may contain each other in their ingredients.

&#x20;

**Example 1:**

<pre><code>Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
<strong>Output:
</strong> ["bread"]
<strong>Explanation:
</strong>We can create "bread" since we have the ingredients "yeast" and "flour".</code></pre>

**Example 2:**

<pre><code>Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
<strong>Output:
</strong> ["bread","sandwich"]
<strong>Explanation:
</strong>We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".</code></pre>

**Example 3:**

<pre><code>Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
<strong>Output:
</strong> ["bread","sandwich","burger"]
<strong>Explanation:
</strong>We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".</code></pre>

&#x20;

**Constraints:**

* `n == recipes.length == ingredients.length`
* `1 <= n <= 100`
* `1 <= ingredients[i].length, supplies.length <= 100`
* `1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10`
* `recipes[i], ingredients[i][j]`, and `supplies[k]` consist only of lowercase English letters.
* All the values of `recipes` and `supplies` combined are unique.
* Each `ingredients[i]` does not contain any duplicate values.



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
from collections import deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        rec_ing_map = dict()
        for recipe, ing_list in zip(recipes, ingredients):
            rec_ing_map[recipe] = ing_list
        in_deg = defaultdict(int)
        nxt_rec = collections.defaultdict(list)
        for recipe, ing_list in zip(recipes, ingredients):
            for ing in ing_list:
                if ing in rec_ing_map:
                    nxt_rec[ing].append(recipe)
                    in_deg[recipe]+=1
        
        queue = deque()
        # find recipe with no in_deg as starting points
        for i, recipe in enumerate(recipes):
            if recipe not in in_deg:
                queue.append(recipe)
        
        supplies = set(supplies)
        ans = []
        while queue:
            cur_rec = queue.popleft()
            if self.can_do(supplies, rec_ing_map[cur_rec]):
                ans.append(cur_rec)
                supplies.add(cur_rec)
            for nxt in nxt_rec[cur_rec]:
                in_deg[nxt]-=1
                if in_deg[nxt] == 0:
                    queue.append(nxt)
        return ans
    
    def can_do(self, supplies, ing_list):
        for ing in ing_list:
            if ing not in supplies:
                return False
        return True
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
