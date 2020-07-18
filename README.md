# most-common_chars

## Solution 1
Uses a counter datastructure to count the most common chars of the input.

Timespace complexity analysis:
* Runtime `O(n log n)`, where `n` is the number of chars in the input string
The worst case requires atmost `O(n log n)` because `Counter.most_common` sorts the most common element in descending order and this requires `TimSort` or `HeapSort` algo depending on the implemtation where both are `O(n log n)`.
* Space O(n), where n is the number of chars in the input string

## Solution 2
This solution has the same timespace complexity, except the implementation details. Here only standard datastructes like `dict`, `tuple`, `list` are used and built-in sorting
