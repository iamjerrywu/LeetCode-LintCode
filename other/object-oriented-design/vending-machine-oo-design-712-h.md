# Vending machine OO Design 712 \(H\)

## Problem

## Procedure

### Clarify

![](../../.gitbook/assets/screen-shot-2021-07-11-at-10.11.51-pm.png)

### Core Object

![](../../.gitbook/assets/screen-shot-2021-07-14-at-10.42.28-am.png)

### Use Cases

Vending Machine

* Select item
* Insert coin
* Execute transaction
* Cancel transaction
* Refill items

### Classes

#### Use cases: 

* _Select item_: Vending machine takes an external input, shows the price of that item
* _Insert coin_: Insert a list of coins into vending machine
* _Execute transection_: 
  * Get the current selected item
  * Compare the item price and inserted coins
  * If not enough money, throw an exception
  * Else, return item that purchased
  * Refund if any
* _Cancel transection_: Return the current coins that has been inserted
* _Refill items_: Refill items on top of current stock

![](../../.gitbook/assets/screen-shot-2021-07-14-at-10.56.13-am.png)

### Better Design on class

{% tabs %}
{% tab title="Java" %}
```java
class Stock
{
    private HashMap<ItemInfo, List<Item>> stock;
    
    public void add(Item item)
    {
        ItemInfo info = item.getInfo();
        List<Item> itemsInStock = stock.get(info);
        itemsInStock.add(item);
        stock.put(info, itemsInStock);
    }
}

stock = new Stock();

public void refillItem(List<Item> items)
{
    for(Item item:items)
    {
        stock.add(item);
    }
}
```
{% endtab %}

{% tab title="Second Tab" %}

{% endtab %}
{% endtabs %}

## Solution 

{% tabs %}
{% tab title="Python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

