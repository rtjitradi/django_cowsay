# django_cowsay
A simple django server that passes user input to the operating system, runs a command, retrieves the output, and sends it back to the client.


Not everything in computing has bindings for Python (as much as I would like that to be true), so it's important to learn how to work with the host system and pass details back and forth.

The goal for this project is to build a very simple django server (so simple that it's only two views, one form, and one model) that passes user input to the operating system, runs a command, retrieves the output, and sends it back to the client. We use the model to back up a copy of what people submit to the page, and have a second endpoint at /history where it lists the last ten things that were sent through the form.

Cowsay (Links to an external site.)Links to an external site. is a utility that has been around for a very long time, but is essentially just a toy. If you don't have it already, then you can install it simply by running:

OSX: `brew install cowsay`
Ubuntu / Debian: `sudo apt install cowsay`
Sample usage: `cowsay "Hello, world!"`

WINDOWS USERS ONLY:

Install cowsay by installing it through NPM: `npm install -g cowsay`. When using Python's `subprocess` module, you will most likely need to pass `shell=True` as well. This is because Windows does not look at the PATH without passing that flag.

Your Task
Write a Django server that:

has a view for the index that does two things: if there is output, render it to the browser, and always renders a fresh version of our form
has a form that just takes in a text line
has a model that we can save the text line to
on submission of the form, uses python's `subprocess (Links to an external site.)Links to an external site.` module to pass the submitted text to the cowsay utility and retrieves the output
re-renders the homepage with a fresh form and the output from cowsay (hint: the output is preformatted)
backs up a copy of the text submitted by the user
has a page at the endpoint /history that displays the 10 most recent strings submitted
Submission
Submit a link to your repo

https://github.com/<github_username>/django_cowsay
 

Rubric
MOO GET OUT MY HAY
MOO GET OUT MY HAY
Criteria	Ratings	Pts
This criterion is linked to a Learning OutcomeHas a view for the index that does two things: if there is output, render it to the browser, and always renders a fresh version of our form
2.0 pts
Full Marks
0.0 pts
No Marks
2.0 pts
This criterion is linked to a Learning OutcomeHas a form that just takes in a text line
1.0 pts
Full Marks
0.0 pts
No Marks
1.0 pts
This criterion is linked to a Learning OutcomeHas a model that we can save the text line to
1.0 pts
Full Marks
0.0 pts
No Marks
1.0 pts
This criterion is linked to a Learning OutcomeUpon submission of the form, uses python's `subprocess` module to pass the submitted text to the cowsay utility and retrieves the output
2.0 pts
Full Marks
0.0 pts
No Marks
2.0 pts
This criterion is linked to a Learning OutcomeRe-renders the homepage with a fresh form and the output from cowsay
1.0 pts
Full Marks
0.0 pts
No Marks
1.0 pts
This criterion is linked to a Learning OutcomeBacks up a copy of the text the user submitted
1.0 pts
Full Marks
0.0 pts
No Marks
1.0 pts
This criterion is linked to a Learning OutcomeHas a page at the endpoint /history that displays the 10 most recent strings submitted
1.0 pts
Full Marks
0.0 pts
No Marks
1.0 pts
This criterion is linked to a Learning OutcomeRepo contains pyproject.toml that includes all necessary dependencies to run application
1.0 pts
Full Marks
0.0 pts
No Marks
1.0 pts
Total Points: 10.0
