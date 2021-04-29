---
description: 10 (3E/5M/2H)
---

# Hash

## Introduction

What's the pre-condition for fulfilling O\(1\) Insert/Find/Delete in Hash?

Ans: Key is O\(1\), to strictly speaking, hash operation require O\(size of key\) but not O\(1\)

* I.e: for integer, O\(size of INT\) = O\(8\) = O\(1\)

### How to solve collision:

1. Open Hashing: using linked list 
2. Closed Hashing: the key is occupied, find other available keys that are closed to it

### What if efficiency is low for the Hash Table?

Do Rehashing, expand the hash table

### HashSet vs HashMap

* HashSet: `value`= None, only use `key`
* HashMap: Use both `value` and `key`

