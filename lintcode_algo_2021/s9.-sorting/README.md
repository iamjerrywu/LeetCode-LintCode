# S9. Sorting

## External Sorting 

While dealing with massive data and under limited storage space \(cache, memory... etc\) condition, external sorting can help process data with following two steps:

* Divide big doc into several small doc
  * For 1T doc, can be divided into 1024 1G doc in order to meet memory limitation \(1G, for example\)
* Using k-way merge to merge all these small doc into one single doc
  * Using Heap \(or priority queue\) to fulfill, or `Min Heap`  \(can always pop out the minimum element\), and put it into big doc. f



