<h2><a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array">Find Minimum in Rotated Sorted Array</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Suppose an array of length <code>n</code> sorted in ascending order is <strong>rotated</strong> between <code>1</code> and <code>n</code> times. For example, the array <code>nums = [0,1,2,4,5,6,7]</code> might become:</p>

<ul>
	<li><code>[4,5,6,7,0,1,2]</code> if it was rotated <code>4</code> times.</li>
	<li><code>[0,1,2,4,5,6,7]</code> if it was rotated <code>7</code> times.</li>
</ul>

<p>Notice that <strong>rotating</strong> an array <code>[a[0], a[1], a[2], ..., a[n-1]]</code> 1 time results in the array <code>[a[n-1], a[0], a[1], a[2], ..., a[n-2]]</code>.</p>

<p>Given the sorted rotated array <code>nums</code> of <strong>unique</strong> elements, return <em>the minimum element of this array</em>.</p>

<p>You must write an algorithm that runs in&nbsp;<code>O(log n) time.</code></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,5,1,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The original array was [1,2,3,4,5] rotated 3 times.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,5,6,7,0,1,2]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [11,13,15,17]
<strong>Output:</strong> 11
<strong>Explanation:</strong> The original array was [11,13,15,17] and it was rotated 4 times. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5000</code></li>
	<li><code>-5000 &lt;= nums[i] &lt;= 5000</code></li>
	<li>All the integers of <code>nums</code> are <strong>unique</strong>.</li>
	<li><code>nums</code> is sorted and rotated between <code>1</code> and <code>n</code> times.</li>
</ul>

### Solution Approach

The code uses a modified binary search algorithm to find the minimum number in the given list. It starts by initializing two pointers, `first` and `last`, which represent the first and last indices of the list.

Inside the `while` loop, it compares the numbers at the `first` and `last` indices. If the number at `first` is smaller than the number at `last`, it means that the list is sorted in ascending order, so the minimum number is at the `first` index. In this case, the code updates the `result` variable with the minimum of the current `result` and the number at the `first` index, and then breaks out of the loop.

If the numbers at `first` and `last` indices are not in ascending order, it means that the list is rotated, and the minimum number is somewhere in the middle of the list. The code calculates the middle index using `(first + last) // 2`. It updates the `result` variable with the minimum of the current `result` and the number at the middle index.

Then, it checks if the number at the middle index is greater than or equal to the number at the `first` index. If it is, it means that the minimum number is located in the right half of the list. In this case, it updates the `first` pointer to `mid + 1` and continues searching in the right half.

If the number at the middle index is smaller than the number at the `first` index, it means that the minimum number is located in the left half of the list. In this case, it updates the `last` pointer to `mid - 1` and continues searching in the left half.

The loop continues until the `first` pointer is greater than the `last` pointer, which indicates that the search is complete. Finally, it returns the `result` variable, which contains the minimum number found in the list.

Overall, the algorithm has a time complexity of O(log n) as it divides the search space in half at each step of the binary search.
