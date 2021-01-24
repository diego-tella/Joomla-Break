# Joomla-Break
A simple brute-force for Joomla! CMS.
Tested in version 3.9.24<br>
Python 2.7.18

<h3><b>Use:</b></h3>

```python script.py -u http://127.0.0.1/joomla/administrator -w /usr/share/wordlists/rockyou.txt -l admin -t a623d221325ed6f9bd0aea00d521a7d7 ```

<h3><b>What is the token?</b></h3>
The token is a string that joomla uses to authenticate itself. It is necessary for our brute-force, so you have to catch it with Burp.

![alt text](http://keklulz.ueuo.com/uploads/token.png)
