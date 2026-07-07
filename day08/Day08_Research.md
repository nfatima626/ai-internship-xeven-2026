# Day 08 - Python Lists & List Operations Research

**Student Name:** Noor Fatima

---

# Python Lists

## Definition

A **list** is an ordered and mutable collection in Python that can store multiple values in a single variable. Lists can contain different data types such as integers, strings, floats, booleans, and even other lists.

## Characteristics

- Ordered (maintains insertion order)
- Mutable (can be modified after creation)
- Allows duplicate values
- Can store multiple data types
- Indexed (starts from 0)

## Example

```python
numbers = [10, 20, 30, 40]

mixed = ["Ali", 20, 3.5, True]
```

---

# List Methods

## append()

### Purpose

Adds an element to the end of the list.

### Syntax

```python
list.append(item)
```

### Example

```python
fruits = ["Apple", "Banana"]
fruits.append("Mango")

print(fruits)
```

**Output**

```text
['Apple', 'Banana', 'Mango']
```

---

## insert()

### Purpose

Inserts an element at a specific index.

### Syntax

```python
list.insert(index, item)
```

### Example

```python
fruits = ["Apple", "Banana"]
fruits.insert(1, "Orange")

print(fruits)
```

**Output**

```text
['Apple', 'Orange', 'Banana']
```

---

## remove()

### Purpose

Removes the first occurrence of the specified value.

### Syntax

```python
list.remove(value)
```

### Example

```python
numbers = [10, 20, 30]

numbers.remove(20)

print(numbers)
```

**Output**

```text
[10, 30]
```

---

## pop()

### Purpose

Removes and returns an element. By default, it removes the last element.

### Syntax

```python
list.pop(index)
```

### Example

```python
numbers = [10, 20, 30]

numbers.pop()

print(numbers)
```

**Output**

```text
[10, 20]
```

---

## sort()

### Purpose

Sorts the list in ascending order.

### Syntax

```python
list.sort()
```

### Example

```python
numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)
```

**Output**

```text
[10, 20, 30, 40]
```

---

## reverse()

### Purpose

Reverses the order of the list.

### Syntax

```python
list.reverse()
```

### Example

```python
numbers = [1, 2, 3]

numbers.reverse()

print(numbers)
```

**Output**

```text
[3, 2, 1]
```

---

## clear()

### Purpose

Removes all elements from the list.

### Syntax

```python
list.clear()
```

### Example

```python
numbers = [1, 2, 3]

numbers.clear()

print(numbers)
```

**Output**

```text
[]
```

---

# List Slicing

## Definition

List slicing allows us to access a portion of a list.

## Syntax

```python
list[start:end:step]
```

## Examples

### Basic Slicing

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

**Output**

```text
[20, 30, 40]
```

### Negative Indexing

```python
print(numbers[-3:])
```

**Output**

```text
[30, 40, 50]
```

### Reverse List

```python
print(numbers[::-1])
```

**Output**

```text
[50, 40, 30, 20, 10]
```

### Skip Elements

```python
print(numbers[::2])
```

**Output**

```text
[10, 30, 50]
```

---

# List Comprehensions

## Definition

List comprehension is a concise way to create new lists in Python using a single line of code.

## Syntax

```python
[expression for item in iterable]
```

## Example 1

```python
numbers = [x for x in range(10)]

print(numbers)
```

**Output**

```text
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Example 2

```python
squares = [x * x for x in range(6)]

print(squares)
```

**Output**

```text
[0, 1, 4, 9, 16, 25]
```

## Example 3

```python
even_numbers = [x for x in range(20) if x % 2 == 0]

print(even_numbers)
```

**Output**

```text
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

---

# When Should We Use Lists?

Lists are useful when:

- Data needs to remain ordered.
- Values need to be modified.
- Duplicate values are allowed.
- Index-based access is required.
- Elements are frequently added or removed.
- Different data types need to be stored together.

## Real-World Applications

- Student records
- Shopping carts
- To-do lists
- Marks management systems
- Product inventories
- Employee records

---

# Research Summary

During this research, I learned that Python lists are one of the most useful and flexible data structures. They are ordered, mutable, and can store different data types. Built-in methods such as `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`, and `clear()` make it easy to manipulate data. I also learned how list slicing provides an efficient way to access portions of a list and how list comprehensions simplify list creation with clean and readable code.