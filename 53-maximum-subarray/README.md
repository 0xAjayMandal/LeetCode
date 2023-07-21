<h2><a href="https://leetcode.com/problems/maximum-subarray">Maximum Subarray</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given an integer array <code>nums</code>, find the <span data-keyword="subarray-nonempty">subarray</span> with the largest sum, and return <em>its sum</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-2,1,-3,4,-1,2,1,-5,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The subarray [4,-1,2,1] has the largest sum 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The subarray [1] has the largest sum 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,4,-1,7,8]
<strong>Output:</strong> 23
<strong>Explanation:</strong> The subarray [5,4,-1,7,8] has the largest sum 23.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> If you have figured out the <code>O(n)</code> solution, try coding another solution using the <strong>divide and conquer</strong> approach, which is more subtle.</p>

### Solution Steps
The algorithm used in the code is known as the Kadane's algorithm. Here's a step-by-step explanation of how it works:

1. Initialize two variables: `maxSub` and `currentSum` to the value of the first element in the given list `nums`.

2. Iterate through each element `i` in the list `nums` (starting from the second element).

3. Inside the loop, check if the current sum (`currentSum`) is negative. If it is negative, reset it to 0. This is done because if the current sum is negative, it will only decrease the overall sum of any subarray it is a part of. So, we reset it to 0 to start considering a new subarray from the next element.

4. Add the current element `i` to the `currentSum`.

5. Update the `maxSub` by comparing the `maxSub` value with the `currentSum`. If the `currentSum` is greater, update `maxSub` to the `currentSum`. Otherwise, keep it as it is.

6. Repeat steps 3 to 5 for all the elements in the `nums` list.

7. Finally, return the `maxSub`, which represents the maximum subarray sum.

The algorithm works by continuously adding the elements to the `currentSum` and updating the `maxSub` whenever a higher sum is encountered. By resetting the `currentSum` to 0 when it becomes negative, the algorithm effectively handles negative numbers and finds the maximum subarray sum.
