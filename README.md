# PasswordStrengthEvaluator

A strong password is an essential part of online security. It helps protect your accounts, personal information, and data from unauthorized access. A strong password is long, complex, and unique, making it difficult for someone else to guess or crack. It should not be based on personal information, such as your name or birthdate, and should be changed regularly to maintain its strength. Using strong passwords can help prevent identity theft, financial fraud, and other cyber crimes. It is important to use strong passwords for all of your online accounts, including email, social media, banking, and shopping accounts. By following best practices for creating and managing strong passwords, you can help keep yourself and your sensitive information safe online.

## how this system works:

<ul>
<li> The user enters their password into a form on the web GUI.</li>
<li> The password is sent to the server, which is running a Python script using the Flask framework.</li>
<li>The script begins by checking the length of the password. If it is less than 8 characters, it is considered weak. If it is between 8 and 12 characters, it is considered medium strength. If it is 12 characters or more, it is considered strong.</li>
<li>In addition to checking the length, the script also checks for the presence of certain characters, such as uppercase letters, lowercase letters, numbers, and special characters.The more of these character types the password contains, the stronger it is considered.</li>
<li>Once the password has been evaluated, the script returns the result to the web GUI, which displays a message indicating whether the password is strong, medium, or weak.</li>
</ul>

## Project demo

[PasswordStrengthEvaluator](https://leontech254.github.io/PasswordStrengthEvaluator/)

## To Note:

### flask sever running on:

<pre>
<code>
app.run(debug=True, port=5002)
</code>
</pre>

### axios endpoint

<pre>
<code>
# running on server
axios.post("https://api.leonteqsecurity.com/password-checker", password)

#running locally
axios.post("http://127.0.0.1:5002/password-checker", password)
</code>
</pre>
