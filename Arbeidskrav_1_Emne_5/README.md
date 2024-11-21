<h1>Arbeidskrav 1 - Emne 5 - Algoritmiske Metoder 2024</h1>
<a href="https://github.com/mortenlunde">Morten Lunde (link to GitHub)</a>
<p>License: MIT (See attached file)</p>
<hr>
<p>Classes:</p>
<ul>
    <li>Contact.py</li>
    <li>Phonebook.py</li>
    <li>main.py</li>
</ul>
<p>Extra files:</p>
<ul>
    <li>README.md</li>
    <li>People.jsonl (to populate phonebook)</li>
    <li>LICENSE.md</li>
</ul>
<hr>
<h4>Description:</h4>
<p>I have chosen to "challenge" myself a little with going back
to code the program in Python. It's just a simple console-
program, where I have added PrettyTable to get a slighty better
print in console. Nothing advanced really, I have made the 
functions asked for where one can sort contacts in any way
wanted. We can display single contact, or all of them and finally
we can search within contacts and show everyone that fits the
criteria (searches all the properties). I have used PrettyTable
to show the whole phonebook for a cleaner look.</p>

<h4>Search Method</h4>
<p>Takes in the users input as query, iterates for each contacts 
property from phonebook, and if there are results it adds them to 
the list of results found, and uses the Display() method to show 
the results. The method converts this search input to lowercase 
to ensure that the search is case-insensitive. The functions return 
false if there are no results and gives the user a message.</p>

<h4>Sort Method</h4>
<p>Takes in the parameters of what to sort by and the sorting order. 
It checks that the sortoption is valid, and gives the user
an error and the options to choose from. If the entered order- 
parameter is not asc or desc, it will automatically sort ascending.
It filters out any None values from the contacts list before sorting.
If the sorting option is valid it will print the list of contacts
using display_all_contacts() method, using a lambda that uses the 
getattr()- function to sort by based on the chosen option.
</p>