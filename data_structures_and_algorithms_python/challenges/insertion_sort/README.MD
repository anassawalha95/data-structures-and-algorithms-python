# Insertion Sort

## Challenge

* Create insertion sort algorithm.

## Approach & Efficiency

 **The Big O for this Algorithm**

 * For performance: O(N^2) 
 * For space : O(1)

## Solution

![photo](/assets/insertion-sort.jpg)

## Trace
> Sample Array: [ 20 , 18 , 12 , 8 , 5 , -2 ]
```
list
0   1   2   3   4   5
18  20  12  8   5   -2
```
> i = 1
> j = 0
> temp = 18
```
list #after while loop
0   1   2   3   4   5
20  20  12  8   5   -2
```
> j = -1
```
0   1   2   3   4   5
18  20  12  8   5   -2
```
___
> i = 2
> j = 1
> temp = 12
```
list
0   1   2   3   4   5
18  20  20  8   5   -2
```
> j = 0
```
list
0   1   2   3   4   5
18  18  20  8   5   -2
```
> j = -1
```
list
0   1   2   3   4   5
12  18  20  8   5   -2
```
___
> i = 3
> j = 2
> temp = 8
```
list
0   1   2   3   4   5
12  18  20  20  5   -2
```
> j = 1
```
list
0   1   2   3   4   5
12  18  18  20  5   -2
```
> j = 0
```
list
0   1   2   3   4   5
12  12  18  20  5   -2
```
> j = -1
```
list
0   1   2   3   4   5
8   12  18  20  5   -2
```
---
> i =   4
> j = 3
> temp = 5
```
list
0   1   2   3   4   5
8   12  18  20  20  -2
```
> j = 2
```
list
0   1   2   3   4   5
8   12  18  18  20  
```
> j = 1
```
list
0   1   2   3   4   5
8   12  12  18  20  -2
```
> j = 0
```
list
0   1   2   3   4   5
8   8   12  18  20  -2
```
> j = -1
```
list
0   1   2   3   4   5
5   8   12  18  20  -2
```
---
> i =   5
> j = 4
> temp = -2
```
list
0   1   2   3   4   5
5   8   12  18  20  20
```
> j = 3
```
list
0   1   2   3   4   5
5   8   12  18  18
```
> j = 2
```
list
0   1   2   3   4   5
5   8   12  12  18  20
```
> j = 1
```
list
0   1   2   3   4   5
5   8   8   12  18  20
```
> j = 0
```
list 
0   1   2   3   4   5
5   5   8   12  18  20
```
> j = -1
## final result
```
list
0   1   2   3   4   5
-2  5   8   12  18  20
```
---
## note 
- when the j become (-1) it will brake out from the foor loop