# Complexity Analysis

As programmers, we often find ourselves asking the same two questions over and over again:

- How much **time** does this algorithm need to finish?

- How much **space** does this algorithm need for its computation?

## Big-O Notation

Big-O Notation gives an upper bound of the complexity in the **worst** case _(always in the worst case)_, helping to quantify performance as the input size becomes **arbitrarily large**.

n - The size of the input

Complexities ordered in from smallest to largest:

- Constant Time: **O(1)**
- Logarithmic Time: **O(log(n))**
- Linear Time: **O(n)**
- Linearithmic Time: **O(nlog(n))**
- Quadric Time: **O(n²)**
- Cubic Time: **O(n³)**
- Exponential Time: **O(b^n)**, b > 1
- Factorial Time: **O(n!)**

## Big-O Porperties

O(n + c) = **O(n)**
O(cn) = **O(n)**, c > 0

Let f be a function that describes the running time of particular algorithm for an input of size n:

f(n) = 7log(n)³ + 15n² + 2n³ + 8
0(f(n)) = **O(n³)**

## Big-O Examples

---

The following run in constant time: **O(1)**

Por que nenhum do códigos asseguir depende de n

```
a := 1
b := 2
c := a + 5*b
```

```
i := 0
while i < 11 do
  i = i + 1
```

---

The following run in linear time: **O(n)**

```
i := 0
while i < n do
  i = i + 1

  f(n) = n
O(f(n)) = O(n)
```

```
i := 0
while i < n do
  i = i + 3

  f(n) = n/3
O(f(n)) = O(n)
```

---

Both of the following run in quadratic time.
The first may be obvious since n work done n times is n\*n = **O(n²)**, but what about the second one?

```
for(i := 0; i < n; i = i + 1)
  for(j := 0; j < n; j = j + 1)

  f(n) = n*n = n²
  O(f(n)) = O(n²)
```

For a moment just focus on the second loop.
Since _i_ goes from [0,n] the amount of looping done is directly determined by what _i_ is.
Remaker that if **_i=0_**, we do _n_ work, if _i=1_, we do _n-1_ work, if _i=1_, we do _n-2_ work, etc..

So the question the becomes what is:
_n + (n-1) + (n-2) + (n-3) + ... + 3 + 2 + 1_?
Remarkably this turns out to be _n(n+1)/2_, so O(n(n+1)/2) = O(n²/2 + n/2) = O(n²)

```
for(i := 0; i < n; i = i + 1)
  for(j := i; j < n; j = j + 1)
           ^ replaced 0 with i
```

---

**Binary Search**

Suppose we have a sorted array and we want to find the index of particular value in the array, if it exists. What is the time complexity of the following algorithm?

```
low := 0
high := n-1
while low <= high Do
  mid := low + (high - low) // 2
  if array[mid] == value: return mid
  else if array[mid] < value: low = mid + 1
  else if array[mid] > hi = mid - 1

return -1
```

Ans: O(log2(n)) = **O(log(n))**

---

Quadric Time

```
i := 0
while i < n do
  j := 0
  while j < 3*n do
    j := j + 1

  j = 0
  while j < 2*n do
    j = j + 1

  i = i + 1
```

f(n) = n \* (3n + 2n) = 5n²
O(f(n)) = **O(n²)**

---

```
i := 0
while i < 3 * n do
  j := 10
  while j < 50 do
    j := j + 1

  j = 0
  while j < n*n*n do
    j = j + 2

  i = i + 1
```

f(n) = 3n \* (40 + n³/2) = 3n/40 + 3n^4/2
O(f(n)) = **O(n^4)**

---

Classic examples of Big-O:

- Finding all subsets of set - **O(2^n)**
- Finding all permutations of a tring = **O(n!)**
- Sorting using mergesorte - **O(nlog(n))**
- Inverting over all the cells in a matrix of size n by m - **O(nm)**
