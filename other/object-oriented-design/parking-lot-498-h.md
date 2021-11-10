# Parking Lot 498 (H)

## Problem

Design a parking lot.

see CC150 OO Design for details.

1. `n` levels, each level has `m` rows of spots and each row has `k` spots.So each level has `m` x `k` spots.
2. The parking lot can park motorcycles, cars and buses
3. The parking lot has motorcycle spots, compact spots, and large spots
4. Each row, motorcycle spots id is in range `[0,k/4)(0 is included, k/4 is not included)`, compact spots id is in range `[k/4,k/4*3)(k/4*3 is not included)` and large spots id is in range `[k/4*3,k)(k is not included)`.
5. A motorcycle can park in any spot
6. A car park in single compact spot or large spot
7. A bus can park in five large spots that are consecutive and within same row. it can not park in small spots

Example

**Example 1**

```
Input:level=1num_rows=1spots_per_row=11parkVehicle("Motorcycle_1")parkVehicle("Car_1")parkVehicle("Car_2")parkVehicle("Car_3")parkVehicle("Car_4")parkVehicle("Car_5")parkVehicle("Bus_1")unParkVehicle("Car_5")parkVehicle("Bus_1")Output:truetruetruetruetruetruefalsetrueExplanation: Parking Lot：Motorcycle: 0 1Car:        2 3 4 5Bus:        6 7 8 9 10When "Car_5" first got to the parking lot, there is no place for it in compact spots. The "Car_5" has to park in Bus spot 6. So "Bus_1" cannot park until "Car_5" left.
```

**Example 2**

```
Input:level=1num_rows=1spots_per_row=14parkVehicle("Motorcycle_1")parkVehicle("Motorcycle_2")parkVehicle("Motorcycle_3")parkVehicle("Car_1")parkVehicle("Car_2")parkVehicle("Car_3")parkVehicle("Motorcycle_4")parkVehicle("Car_4")parkVehicle("Car_5")parkVehicle("Car_6")parkVehicle("Car_7")parkVehicle("Bus_1")unParkVehicle("Car_1")unParkVehicle("Motorcycle_4")unParkVehicle("Car_3")unParkVehicle("Car_6")parkVehicle("Bus_1")unParkVehicle("Car_7")parkVehicle("Bus_1")Output:truetruetruetruetruetruetruetruetruetruetruefalsefalsetrue
```

## Procedure

### Clarify:

* Multi-level parking lots
* Vehicle: consider of 1. Bus 2. Car 3. Motorcycle
* No need to consider charging/handicapped parking
* Parking lots can show available spaces
* Flat fee

### Core Object

![](<../../.gitbook/assets/Screen Shot 2021-07-22 at 11.15.02 AM.png>)

### Cases

Parking Lot:

* Get available count
* Park vehicle
* Clear spot
* Calculate price

Management user cases:

* Reservation: X
* Serve: Park vehicle
* Check out: Clear spot + Calculate price

### Class

![](<../../.gitbook/assets/Screen Shot 2021-07-22 at 11.54.36 AM.png>)

#### Correctness

{% tabs %}
{% tab title="Java" %}
```java
// go through all levels'rows to get available spots count
int availableSpots = parkingLot.getAvailableCount();
System.out.print("There are" + availableSpots + " spots available.");

// park vehicle will do the following:
// - find open spots for htis vehicle
// - update available count
// - update spot availability and generate ticket
Ticket ticket = parkingLot.parkVehicle(myVehicle);
System.out.print("Remember to bring your ticket with you");

// clear spot will do the following:
// - calculate price based on start time
// - process payment
// - set the spot to empty and update available count
parkingLot.clearSpot(ticket, payment)
```
{% endtab %}

{% tab title="Python" %}

{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Java" %}
```java
float fee = parkingLot.calculateParkingFee(ticket);
parkingLot.processPayment(ticket, payment, fee);
parkingLot.clearParkingSpot(ticket);
```
{% endtab %}

{% tab title="Python" %}

{% endtab %}
{% endtabs %}

### Design Pattern - Singleton

Ensure a class has only one instance, and provide a global point of access to it

![](<../../.gitbook/assets/Screen Shot 2021-07-22 at 12.28.07 PM.png>)

![](<../../.gitbook/assets/Screen Shot 2021-07-22 at 12.57.46 PM.png>)

#### Example (will fail in concurrent situation)

{% tabs %}
{% tab title="Java" %}
```java
public class ParkingLot
{
    private static ParkingLot _instance = null;
    
    private List<Level> levels;
    
    private ParkingLot()
    {
        levels = new ArrayList<Level>();
    }
    
    // with static attribute, can call getInstance without creating instance
    // static makes the function getInstance() no longer relate to instance, but related to class ParkingLot
    public static ParkingLot getInstance()
    {
        // this will fail in multi-threading
        // instance will probably create multiple (duplicated) times during context switches
        if(_instance == null)
        {
            _instance = new ParkingLot();
        }
        return _instance;
    }
```
{% endtab %}

{% tab title="Second Tab" %}

{% endtab %}
{% endtabs %}

#### Example in parallel programming with synchronization

{% tabs %}
{% tab title="Java" %}
```java
public class ParkingLot
{
    private static ParkingLot _instance = null;
    
    private List<Level> levels;
    
    private ParkingLot()
    {
        levels = new ArrayList<Level>();
    }
    
    // with synchronized attribute, will create mutex that don't allow other thead to call the same getInstance()
    // after release the mutex, then can be retrieved
    public static synchronized|ParkingLot getInstance()
    {
        if(_instance == null)
        {
            _instance = new ParkingLot();
        }
        return _instance;
    }
```
{% endtab %}

{% tab title="Second Tab" %}

{% endtab %}
{% endtabs %}

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
VEHICLE_TYPE = {
    'UNKNOWN': 0,
    'MOTORCYCLE': 1,
    'CAR': 2,
    'BUS': 3,
}


class Vehicle:
    def __init__(self):
        self.TYPE = VEHICLE_TYPE['UNKNOWN']
        self.COST_SPOTS = 0
        self.at_level = None
        self.at_spots = None

    def get_range(self, n):
        raise NotImplementedError('This method should have implemented.')

    def unpark(self):
        if not self.at_level:
            return
        for x, y in self.at_spots:
            self.at_level.spots[x, y] = None
        self.at_level = None
        self.at_spots = None


class Motorcycle(Vehicle):
    def __init__(self):
        self.TYPE = VEHICLE_TYPE['MOTORCYCLE']
        self.COST_SPOTS = 1

    def get_range(self, n):
        return range(n)


class Car(Vehicle):
    def __init__(self):
        self.TYPE = VEHICLE_TYPE['CAR']
        self.COST_SPOTS = 1

    def get_range(self, n):
        return range(n // 4, n)


class Bus(Vehicle):
    def __init__(self):
        self.TYPE = VEHICLE_TYPE['BUS']
        self.COST_SPOTS = 5

    def get_range(self, n):
        return range(n // 4 * 3, n)


class Level:
    def __init__(self, id, m, n):
        self.id = id
        self.m = m
        self.n = n
        self.spots = {}

    def park_vehicle(self, vehicle):
        RANGE = vehicle.get_range(self.n)

        for x in range(self.m):
            found_spots = 0
            spots = []
            for y in RANGE:
                if self.spots.get((x, y)):
                    found_spots = 0
                    spots = []
                    continue

                found_spots += 1
                spots.append((x, y))

                if found_spots == vehicle.COST_SPOTS:
                    vehicle.at_level = self
                    vehicle.at_spots = spots
                    for _x, _y in spots:
                        self.spots[_x, _y] = vehicle
                    return True

        return False


class ParkingLot:
    # @param {int} k number of levels
    # @param {int} m each level has m rows of spots
    # @param {int} n each row has n spots
    def __init__(self, k, m, n):
        self.levels = [Level(i, m, n) for i in range(k)]

    # Park the vehicle in a spot (or multiple spots)
    # Return false if failed
    def park_vehicle(self, vehicle):
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False

    # unPark the vehicle
    def unpark_vehicle(self, vehicle):
        vehicle.unpark()
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
