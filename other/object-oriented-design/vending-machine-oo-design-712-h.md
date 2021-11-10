# Vending machine OO Design 712 (H)

## Problem

## Procedure

### Clarify

![](<../../.gitbook/assets/Screen Shot 2021-07-11 at 10.11.51 PM.png>)

### Core Object

![](<../../.gitbook/assets/Screen Shot 2021-07-14 at 10.42.28 AM.png>)

### Use Cases

Vending Machine

* Select item
* Insert coin
* Execute transaction
* Cancel transaction
* Refill items

### Classes

#### Use cases:&#x20;

* _Select item_: Vending machine takes an external input, shows the price of that item
* _Insert coin_: Insert a list of coins into vending machine
* _Execute transection_:&#x20;
  * Get the current selected item
  * Compare the item price and inserted coins
  * If not enough money, throw an exception
  * Else, return item that purchased
  * Refund if any
* _Cancel transection_: Return the current coins that has been inserted
* _Refill items_: Refill items on top of current stock

![](<../../.gitbook/assets/Screen Shot 2021-07-14 at 10.56.13 AM.png>)

###

### Inflexible Design&#x20;

{% tabs %}
{% tab title="Java" %}
```java
stock = new HashMap<ItemInfo, List<Item>>();
public void refillItem(List<Item> items)
{
    for (Item item: items)
    {
        ItemInfo info = item.getInfo();
        List<Item> itemsInStock = stock.get(info);
        itemsInStock.add(item);
        stock.put(info, itemsInStock);
    }
}
```
{% endtab %}

{% tab title="Second Tab" %}

{% endtab %}
{% endtabs %}

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

{% tab title="Python" %}
```python
```
{% endtab %}
{% endtabs %}

![](<../../.gitbook/assets/Screen Shot 2021-07-14 at 11.18.08 AM.png>)

### State Design Pattern

For uses cases, what if there is no item is selected, or no coins inserted....etc, Insert coin(), Execute transaction(), Cancel transaction() will all need to handle for exception. However, it's quite a redundant using if else condition like following:

{% tabs %}
{% tab title="Java" %}
```java
public void insertCoin(List<Coin> coins)
{
    if (selectedItem == null)
    {
        throw new Exception("You need to make a selection first");
    }
    else if (selectedItem != null)
    {
        currentCoins.add(coins);
    }
}
```
{% endtab %}

{% tab title="Second Tab" %}

{% endtab %}
{% endtabs %}

#### With state design

![](<../../.gitbook/assets/Screen Shot 2021-07-14 at 11.24.33 AM.png>)

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
from enum import Enum
import abc
class ItemInfo(object): # A1 -> Sprite A2 -> Coke
    def __init__(self, name, price):
        self.price = price
        self.name = name # sprite, coke, cake   

class Sprite(object): # Inheritance
    def __init__(self):
        self.info = ItemInfo("Sprite", 1.99)
        self.price = 1.99
        self.name = "Sprite"
        
class Coke(object):
    def __init__(self):
        self.name = ItemInfo("Coke", 1.50)
        self.price = 1.50
        self.name = "Coke"

class Cake(object):
    def __init__(self):
        self.name = ItemInfo("Cake", 2.99)
        self.price = 2.99
        self.name = "Cake"

class Value(Enum):
    PENNY = 1
    NICKLE = 5
    DIME = 10
    QUARTER = 25
    
    def get_value(self):
        return self.value
    
    def get_name(self):
        return self.name

class Coin(object):
    def __init__(self, value): # value --- Value(Enum)
        self.value = value.get_value()
        self.name = value.get_name()
        
class State(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def selectItem(self, selection): # string
        pass
    
    def insertCoins(self, coins):
        pass
    
    def executeTransaction(self):
        pass
    
    def cancelTransaction(self):
        pass

class Abstract_State(State):
    def __init__(self, vendingMachine):
        self.vm = vendingMachine

class No_Selection(Abstract_State):
    def __init__(self, vendingMachine):
        super().__init__(vendingMachine)
        
    def selectItem(self, selection): # string
        info = self.vm.itemIdentifiers[selection]
        self.vm.change_to_has_selection()
        self.vm.set_selected_item(selection)
        return info
    
    def insertCoins(self, coins):
        print("Please make a selection first")
    
    def executeTransaction(self):
        print("Please make a selection first")
    
    def cancelTransaction(self):
        print("Please make a selection first")
        return 0
        
class Has_Selection(Abstract_State):
    def __init__(self, vendingMachine):
        super().__init__(vendingMachine)
        
    def selectItem(self, selection): # string
        self.vm.set_selected_item(selection)
        
    def insertCoins(self, coins):
        self.vm.insert_coins(coins)
        self.vm.change_to_inserted_money()
        
    def executeTransaction(self):
        print("Please insert money first")
    
    def cancelTransaction(self):
        print("Transactions cancelled")
        self.vm.set_selected_item("null")
        self.vm.change_to_no_selection()
        return 0
    
class Inserted_Money(Abstract_State):
    def __init__(self, vendingMachine):
        super().__init__(vendingMachine)
        
    def selectItem(self, selection): # string
        print("Has incomplete transaction")
    
    def insertCoins(self, coins):
        self.vm.insert_coins(coins)
    
    def executeTransaction(self):
        inserted_value = self.vm.get_inserted_money()
        price = self.vm.currentSelection.price
        diff = abs(inserted_value - price)
        if inserted_value < price:
            print("{} more money needed to pay", price - inserted_value)
        else:
            print("Executing transaction, will return you $" + str(diff) + " and " + self.vm.currentSelection.name + " item.")
            self.vm.set_selected_item("null")
            self.vm.coins.extend(self.vm.currentCoins)
            self.vm.change_to_no_selection()
            self.vm.empty_inserted_coins()
    
    def cancelTransaction(self):
        self.vm.set_selected_item("null")
        self.vm.change_to_no_selection()
        inserted_money = self.vm.get_inserted_money()
        self.vm.empty_inserted_coins()
        return inserted_money
        
class VendingMachine(object):
    def __init__(self):
        self.coins = [] # List<Coin> 
        self.items = [] # List<Items>
        self.itemIdentifiers = {} # Map<String, ItemInfo>
        self.currentSelection = None # ItemInfo
        self.currentCoins = []
        self.stock = collections.defaultdict(list) # Map<identifier, List<Item>>
        self.No_Selection = No_Selection(self)
        self.Has_Selection = Has_Selection(self)
        self.Inserted_Money = Inserted_Money(self)
        self.state = self.No_Selection
        
    def set_itemIdentifiers(self):
        self.itemIdentifiers["A1"] = Sprite()
        self.itemIdentifiers["B1"] = Coke()
        self.itemIdentifiers["C1"] = Cake()
        self.itemIdentifiers["null"] = None
    
    def set_state(self, state):
        self.state = state
    
    def set_selected_item(self, string):
        self.currentSelection = self.itemIdentifiers[string]
    
    def insert_coins(self, coins): # List<Coins>
        self.currentCoins.extend(coins)
    
    def get_inserted_money(self):
        return sum([x.value for x in self.currentCoins])
    
    def empty_inserted_coins(self):
        self.currentCoins = []
    
    def get_current_sale_price(self):
        if not currentSelection:
            print("Please make a selection first")
            return 0
        else:
            return self.currentSelection.price
    
    def refill_items(self, id_, num):
        if id_ == "A1": # Sprite
            for _ in range(num):
                self.stock["A1"].append(Sprite())
        elif id_ == "B1": # Coke  
            for _ in range(num):
                self.stock["B1"].append(Coke())
        elif id_ == "C1": # Cake:
            for _ in range(num):
                self.stock["C1"].append(Cake())
        return
    
    def change_to_no_selection(self):
        self.state = self.No_Selection
        
    def change_to_has_selection(self):
        self.state = self.Has_Selection
    
    def change_to_inserted_money(self):
        self.state = self.Inserted_Money
    
    def selectItem(self, selection): # string
        self.state.selectItem(selection)
    
    def insertCoins(self, coins):
        self.state.insertCoins(coins)
    
    def executeTransaction(self):
        self.state.executeTransaction()
    
    def cancelTransaction(self):
        self.state.cancelTransaction()
```
{% endtab %}

{% tab title="Java" %}
```java
public class VendingMachine {
	private String currentSelectedItem;
	private int currentInsertedMoney;
	private AbstractState state;
	private NoSelectionState noSelectionState;
	private HasSelectionState hasSelectionState;
	private InsertedMoneyState insertedMoneyState;
	private Map<String, Integer> itemPrice;

	public VendingMachine() {
		currentInsertedMoney = 0;
		currentSelectedItem = null;
		noSelectionState = new NoSelectionState(this);
		hasSelectionState = new HasSelectionState(this);
		insertedMoneyState = new InsertedMoneyState(this);
		state = noSelectionState;

		itemPrice = new HashMap<>();
		itemPrice.put("Coke", 199);
		itemPrice.put("Sprite", 299);
		itemPrice.put("MountainDew", 399);
	}

	public void setSelectedItem(String item) {
		this.currentSelectedItem = item;
	}

	public String getSelectedItem() {
		return currentSelectedItem;
	}

	public void insertMoney(int amount) {
		this.currentInsertedMoney += amount;
	}

	public void emptyInsertedMoney() {
		this.currentInsertedMoney = 0;
	}

	public int getInsertedMoney() {
		return currentInsertedMoney;
	}

	public int getSalePrice() {
		if (currentSelectedItem == null) {
			System.out.println("Please make a selection before asking price");
			return 0;
		} else {
			return itemPrice.get(currentSelectedItem);
		}
	}

	public void changeToNoSelectionState() {
		state = noSelectionState;
	}

	public void changeToHasSelectionState() {
		state = hasSelectionState;
	}

	public void changeToInsertedMoneyState() {
		state = insertedMoneyState;
	}

	public void selectItem(String selection) {
		state.selectItem(selection);
	}

	public void addMoney(int value) {
		state.insertMoney(value);
	}

	public void executeTransaction() {
		state.executeTransaction();
	}

	public int cancelTransaction() {
		return state.cancelTransaction();
	}

	public String printState() {
		String res = "";

		res = "Current selection is: " + currentSelectedItem + ", current inserted money: " + currentInsertedMoney
				+ ", current state is : " + state;

		return res;
	}
}

interface State {
	public void selectItem(String selection);
	public void insertMoney(int value);
	public void executeTransaction();
	public int cancelTransaction();
	public String toString();
}

abstract class AbstractState implements State {
	protected VendingMachine vendingMachine;

	public AbstractState(VendingMachine vendingMachine) {
		this.vendingMachine = vendingMachine;
	}
}

class NoSelectionState extends AbstractState{

	public NoSelectionState(VendingMachine vendingMachine) {
		super(vendingMachine);
		// TODO Auto-generated constructor stub
	}

	@Override
	public void selectItem(String selection) {
		// TODO Auto-generated method stub
		vendingMachine.setSelectedItem(selection);
		vendingMachine.changeToHasSelectionState();
	}

	@Override
	public void insertMoney(int value) {
		// TODO Auto-generated method stub
		System.out.println("Please make a selection first");
	}

	@Override
	public void executeTransaction() {
		// TODO Auto-generated method stub
		System.out.println("Please make a selection first");
	}

	@Override
	public int cancelTransaction() {
		// TODO Auto-generated method stub
		System.out.println("Please make a selection first");
		return 0;
	}

	@Override
	public String toString(){
		return "NoSelection";
	}
}

class HasSelectionState extends AbstractState{

	public HasSelectionState(VendingMachine vendingMachine) {
		super(vendingMachine);
		// TODO Auto-generated constructor stub
	}

	@Override
	public void selectItem(String selection) {
		// TODO Auto-generated method stub
		vendingMachine.setSelectedItem(selection);
	}

	@Override
	public void insertMoney(int value) {
		// TODO Auto-generated method stub
		vendingMachine.insertMoney(value);
		vendingMachine.changeToInsertedMoneyState();
	}

	@Override
	public void executeTransaction() {
		// TODO Auto-generated method stub
		System.out.println("You need to insert money first");
	}

	@Override
	public int cancelTransaction() {
		// TODO Auto-generated method stub
		System.out.println("Transaction canceled");
		vendingMachine.setSelectedItem(null);
		vendingMachine.changeToNoSelectionState();
		return 0;
	}
	@Override
	public String toString(){
		return "HasSelection";
	}
}

class InsertedMoneyState extends AbstractState{

	public InsertedMoneyState(VendingMachine vendingMachine) {
		super(vendingMachine);
		// TODO Auto-generated constructor stub
	}

	@Override
	public void selectItem(String selection) {
		// TODO Auto-generated method stub
		System.out.println("Already has a selection, please cancel transaction to make a new selection");
	}

	@Override
	public void insertMoney(int value) {
		// TODO Auto-generated method stub
		vendingMachine.insertMoney(value);
	}

	@Override
	public void executeTransaction() {
		// TODO Auto-generated method stub
		int diff = vendingMachine.getInsertedMoney() - vendingMachine.getSalePrice();
		if(diff >= 0){
			System.out.println("Executing transaction, will return you : " + diff + " money and item: " + vendingMachine.getSelectedItem());
			vendingMachine.setSelectedItem(null);
			vendingMachine.emptyInsertedMoney();
			vendingMachine.changeToNoSelectionState();
		}
		else{
			System.out.println("Not enough money, please insert " + (-diff) + " more.");
		}
	}

	@Override
	public int cancelTransaction() {
		// TODO Auto-generated method stub
		int insertedMoney = vendingMachine.getInsertedMoney();
		vendingMachine.setSelectedItem(null);
		vendingMachine.emptyInsertedMoney();
		vendingMachine.changeToNoSelectionState();
		return insertedMoney;
	}

	@Override
	public String toString(){
		return "InsertedMoney";
	}
}
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
