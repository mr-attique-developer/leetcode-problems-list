<h2><a href="https://leetcode.com/problems/remove-palindromic-subsequences/?envType=problem-list-v2&envId=two-pointers">1332. Remove Palindromic Subsequences</a></h2><h3>Easy</h3><hr><p>You are given a string <code>s</code> consisting <strong>only</strong> of letters <code>&#39;a&#39;</code> and <code>&#39;b&#39;</code>. In a single step you can remove one <strong>palindromic subsequence</strong> from <code>s</code>.</p>

<p>Return <em>the <strong>minimum</strong> number of steps to make the given string empty</em>.</p>

<p>A string is a <strong>subsequence</strong> of a given string if it is generated by deleting some characters of a given string without changing its order. Note that a subsequence does <strong>not</strong> necessarily need to be contiguous.</p>

<p>A string is called <strong>palindrome</strong> if is one that reads the same backward as well as forward.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ababa&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> s is already a palindrome, so its entirety can be removed in a single step.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abb&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> &quot;<u>a</u>bb&quot; -&gt; &quot;<u>bb</u>&quot; -&gt; &quot;&quot;. 
Remove palindromic subsequence &quot;a&quot; then &quot;bb&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;baabb&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> &quot;<u>baa</u>b<u>b</u>&quot; -&gt; &quot;<u>b</u>&quot; -&gt; &quot;&quot;. 
Remove palindromic subsequence &quot;baab&quot; then &quot;b&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i]</code> is either <code>&#39;a&#39;</code> or <code>&#39;b&#39;</code>.</li>
</ul>
