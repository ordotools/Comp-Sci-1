# Python List Methods: Basic to Advanced

---

## Basic Methods

### `append(x)`
Adds a single item to the end of the list.
```python
lst = [1, 2, 3]
lst.append(4)
# [1, 2, 3, 4]
```

### `insert(i, x)`
Inserts item `x` at index `i`, shifting elements right.
```python
lst = [1, 2, 3]
lst.insert(1, 99)
# [1, 99, 2, 3]
```

### `remove(x)`
Removes the **first** occurrence of `x`. Raises `ValueError` if not found.
```python
lst = [1, 2, 3, 2]
lst.remove(2)
# [1, 3, 2]
```

### `pop(i=-1)`
Removes and returns the item at index `i` (default: last item).
```python
lst = [1, 2, 3]
lst.pop()    # returns 3 → [1, 2]
lst.pop(0)   # returns 1 → [2]
```

### `clear()`
Removes all items from the list.
```python
lst = [1, 2, 3]
lst.clear()
# []
```

### `index(x, start=0, end=len(lst))`
Returns the index of the **first** occurrence of `x`. Optional start/end bounds.
```python
lst = [10, 20, 30, 20]
lst.index(20)      # 1
lst.index(20, 2)   # 3
```

### `count(x)`
Returns the number of times `x` appears in the list.
```python
lst = [1, 2, 2, 3, 2]
lst.count(2)  # 3
```

### `reverse()`
Reverses the list **in-place**.
```python
lst = [1, 2, 3]
lst.reverse()
# [3, 2, 1]
```

### `copy()`
Returns a **shallow** copy of the list.
```python
lst = [1, 2, 3]
lst2 = lst.copy()
```

---

## Intermediate Methods

### `extend(iterable)`
Appends all items from an iterable to the list (mutates in-place).
```python
lst = [1, 2]
lst.extend([3, 4, 5])
# [1, 2, 3, 4, 5]

# Difference from append:
lst.append([3, 4])   # [1, 2, [3, 4]]
lst.extend([3, 4])   # [1, 2, 3, 4]
```

### `sort(key=None, reverse=False)`
Sorts the list **in-place** using Timsort (stable, O(n log n)).
```python
lst = [3, 1, 4, 1, 5]
lst.sort()                          # [1, 1, 3, 4, 5]
lst.sort(reverse=True)              # [5, 4, 3, 1, 1]
lst.sort(key=lambda x: -x)         # same as reverse=True
words = ["banana", "fig", "apple"]
words.sort(key=len)                 # ['fig', 'fig', 'apple', 'banana'] → by length
```

---

## Built-in Functions That Work on Lists
*(Not methods, but essential list operations)*

### `sorted(lst, key=None, reverse=False)`
Returns a **new** sorted list; original unchanged.
```python
lst = [3, 1, 2]
new = sorted(lst)        # [1, 2, 3]; lst unchanged
```

### `reversed(lst)`
Returns a reverse **iterator** (not a list). Wrap in `list()` to materialize.
```python
lst = [1, 2, 3]
list(reversed(lst))  # [3, 2, 1]
```

### `len(lst)`, `min(lst)`, `max(lst)`, `sum(lst)`
```python
lst = [3, 1, 4, 1, 5]
len(lst)   # 5
min(lst)   # 1
max(lst)   # 5
sum(lst)   # 14
```

---

## Advanced Patterns & Techniques

### List Comprehensions
Concise construction with optional filtering.
```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
flat    = [x for row in matrix for x in row]  # flatten 2D list
```

### Slicing `lst[start:stop:step]`
```python
lst = [0, 1, 2, 3, 4, 5]
lst[1:4]    # [1, 2, 3]
lst[::2]    # [0, 2, 4]
lst[::-1]   # [5, 4, 3, 2, 1]  ← reverse copy
lst[1:4] = [10, 20]  # slice assignment → [0, 10, 20, 4, 5]
```

### Unpacking
```python
first, *middle, last = [1, 2, 3, 4, 5]
# first=1, middle=[2,3,4], last=5
```

### `zip()` with lists
```python
keys = ["a", "b", "c"]
vals = [1, 2, 3]
pairs = list(zip(keys, vals))       # [('a',1), ('b',2), ('c',3)]
d = dict(zip(keys, vals))           # {'a':1, 'b':2, 'c':3}
```

### `enumerate(lst, start=0)`
```python
for i, val in enumerate(["a", "b", "c"], start=1):
    print(i, val)  # 1 a, 2 b, 3 c
```

### `map()` and `filter()`
```python
doubled  = list(map(lambda x: x * 2, lst))
filtered = list(filter(lambda x: x > 0, lst))
```

### `functools.reduce()`
Accumulates a list to a single value.
```python
from functools import reduce
product = reduce(lambda acc, x: acc * x, [1, 2, 3, 4])  # 24
```

### `itertools` — Advanced List Iteration
```python
import itertools

# Chain multiple lists
list(itertools.chain([1,2], [3,4], [5]))       # [1,2,3,4,5]

# All combinations / permutations
list(itertools.combinations([1,2,3], 2))        # [(1,2),(1,3),(2,3)]
list(itertools.permutations([1,2,3], 2))        # [(1,2),(1,3),(2,1),...]

# Group consecutive items by a key
data = [("a",1),("a",2),("b",3)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, list(group))

# Sliding window (Python 3.12+)
list(itertools.pairwise([1,2,3,4]))             # [(1,2),(2,3),(3,4)]

# Flatten one level deep
list(itertools.chain.from_iterable([[1,2],[3,4]]))  # [1,2,3,4]
```

### `bisect` — Binary Search on Sorted Lists
```python
import bisect

lst = [1, 3, 5, 7, 9]
bisect.bisect_left(lst, 5)    # 2 — leftmost insertion point
bisect.bisect_right(lst, 5)   # 3 — rightmost insertion point
bisect.insort(lst, 6)         # insert 6 in sorted order → [1,3,5,6,7,9]
```

### `heapq` — Priority Queue Operations on Lists
```python
import heapq

lst = [5, 1, 3, 2, 4]
heapq.heapify(lst)              # min-heap in-place: [1,2,3,5,4]
heapq.heappush(lst, 0)          # push new element
heapq.heappop(lst)              # pop smallest: 0
heapq.nlargest(3, lst)          # [5, 4, 3]
heapq.nsmallest(3, lst)         # [1, 2, 3]
```

### In-place Slice Assignment (Advanced Mutation)
```python
lst = [1, 2, 3, 4, 5]
lst[1:3] = []        # delete elements: [1, 4, 5]
lst[::2] = [0, 0, 0] # replace every other element
```

### `__contains__` / membership testing
```python
3 in lst          # True/False — O(n) for lists
# Use a set for O(1) lookups if checking membership repeatedly
s = set(lst)
3 in s            # O(1)
```

---

## Performance Notes

| Operation        | Average Case |
|-----------------|-------------|
| `append`        | O(1)        |
| `insert(0, x)`  | O(n)        |
| `pop()`         | O(1)        |
| `pop(0)`        | O(n)        |
| `remove(x)`     | O(n)        |
| `index(x)`      | O(n)        |
| `sort()`        | O(n log n)  |
| `x in lst`      | O(n)        |
| Slice `lst[a:b]`| O(k)        |

> For frequent insertions/deletions at the front, prefer `collections.deque` over a list.
