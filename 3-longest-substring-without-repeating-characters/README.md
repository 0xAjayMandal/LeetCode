<h2><a href="https://leetcode.com/problems/longest-substring-without-repeating-characters">Longest Substring Without Repeating Characters</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given a string <code>s</code>, find the length of the <strong>longest</strong> <span data-keyword="substring-nonempty"><strong>substring</strong></span> without repeating characters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcabcbb&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;abc&quot;, with the length of 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bbbbb&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> The answer is &quot;b&quot;, with the length of 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;pwwkew&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;wke&quot;, with the length of 3.
Notice that the answer must be a substring, &quot;pwke&quot; is a subsequence and not a substring.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists of English letters, digits, symbols and spaces.</li>
</ul>

## Solution Explanation

In this code, the `left` and `right` variables are used to track the boundaries of the current substring being considered.

The `left` variable represents the left boundary of the current substring, and initially it is set to 0. We will use this variable to move the left boundary to the right, whenever we encounter a repeat character.

The `right` variable represents the right boundary of the current substring, and it iterates through each character in the given string `s`. We will use this variable to extend the right boundary of the substring as long as we encounter new characters.

The algorithm uses a sliding window approach to find the longest substring without repeating characters. The set `charSet` is used to store the unique characters encountered so far in the current substring.

Here's a breakdown of the logic inside the for loop:

1. Iterate through each character in `s`, using the variable `right` as the index.
2. Check if the character at `s[right]` is already present in the `charSet` set.
3. If it is present, it means we have encountered a repeated character. In this case, we need to shrink the current substring from the left side to exclude the repeated character.
    - We remove the character at `s[left]` from the `charSet` set.
    - Increment the `left` variable to move the left boundary of the substring.
4. Add the current character `s[right]` to the `charSet` set to indicate that it has been encountered in the current substring.
5. Update the `res` variable to keep track of the maximum length of the substring seen so far.
    - It is calculated as the maximum of the current `res` value and the length of the current substring `(right - left + 1)`.

After the loop, the `res` variable will contain the length of the longest substring without repeating characters. We return this value as the result.
