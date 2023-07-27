<h2><a href="https://leetcode.com/problems/minimum-window-substring">Minimum Window Substring</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' /><hr><p>Given two strings <code>s</code> and <code>t</code> of lengths <code>m</code> and <code>n</code> respectively, return <em>the <strong>minimum window</strong></em> <span data-keyword="substring-nonempty"><strong><em>substring</em></strong></span><em> of </em><code>s</code><em> such that every character in </em><code>t</code><em> (<strong>including duplicates</strong>) is included in the window</em>. If there is no such substring, return <em>the empty string </em><code>&quot;&quot;</code>.</p>

<p>The testcases will be generated such that the answer is <strong>unique</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ADOBECODEBANC&quot;, t = &quot;ABC&quot;
<strong>Output:</strong> &quot;BANC&quot;
<strong>Explanation:</strong> The minimum window substring &quot;BANC&quot; includes &#39;A&#39;, &#39;B&#39;, and &#39;C&#39; from string t.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a&quot;, t = &quot;a&quot;
<strong>Output:</strong> &quot;a&quot;
<strong>Explanation:</strong> The entire string s is the minimum window.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a&quot;, t = &quot;aa&quot;
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> Both &#39;a&#39;s from t must be included in the window.
Since the largest window of s only has one &#39;a&#39;, return empty string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == s.length</code></li>
	<li><code>n == t.length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of uppercase and lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you find an algorithm that runs in <code>O(m + n)</code> time?</p>

## Solution Approach
The code is an implementation of the sliding window algorithm to solve the Minimum Window Substring problem. The goal of the problem is to find the minimum-length substring in string `s` that contains all the characters from string `t`.

Here is the step-by-step approach of the code:

1. Import the `Counter` class from the `collections` module, which will be used to count the occurrences of characters in the target string.

2. Define a class `Solution` containing the `minWindow` method that takes two parameters: the input string `s` and the target string `t`.

3. Create a counter `target_counter` using the target string `t`, which will count the occurrences of each character in `t`.

4. Initialize three variables:
   - `left` to keep track of the leftmost index of the sliding window
   - `min_window` to store the minimum window length found so far (initialized as positive infinity)
   - `min_window_start` to store the starting index of the minimum window substring

5. Initialize a counter `counter` with the length of the target string `t`, which represents the number of distinct characters still needed to match the target.

6. Iterate over the string `s` using the sliding window approach, where the `right` variable represents the rightmost index of the sliding window.

7. If the current character `s[right]` is present in the target string, decrement its count in the `target_counter`. If the count is still greater than or equal to zero, it means we have found a character that is needed for the target, so we decrement `counter` by one.

8. Check if we have found all the characters from the target string. If the `counter` becomes zero, it means the current window contains all characters from `t`. In this case, we try to minimize the window by moving the `left` pointer to the right. 

9. Inside the while loop, update the `min_window` and `min_window_start` if the current window is smaller than the previously found minimum window.

10. Move the `left` pointer to the right by one and update the `target_counter` and `counter` accordingly.

11. Finally, return the minimum window substring by extracting the substring from `s` starting from `min_window_start` with a length of `min_window`. If no minimum window is found (i.e., `min_window` is still infinity), return an empty string.

The code follows the sliding window approach to efficiently find the minimum window substring. By maintaining a sliding window and updating the minimum window as we traverse the input string, we can find the smallest window that satisfies the given condition in linear time complexity.
