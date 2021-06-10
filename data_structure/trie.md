# Trie

## What's Trie?

It's a data structure that accelerates in solving graph word search problems, faster than simply using hashmap. 

For example, we add word "abc", and search ".bc", "a..", these should all give as `True` 

If using hashmap we need to store 26^3 of possibilities, and mark all the ones that can be found as `True`, while others as `False` Apparently, that's a huge space complexity we required, therefore we need to use a better approach.

 Trie is like a prefix tree, is a type of search tree, a tree **data structure** used for locating specific keys from within a set. 

## Template:

Time Complexity:

* add\(\): O\(1\)
* find\(\): O\(n\), n as the worst case that x reach the root length \(as a list\)
* merge\(\): O\(n\)
* is\_connected\(\): O\(1\)

