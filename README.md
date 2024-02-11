# hw-blog

## How to run locally

1. Clone repo, cd into it
2. run: 

```
export FLASK_APP=flaskr
flask run --debug
```

Debug flag is optional if you don't wanna change anything and see those changes in real time. 



## New Functionality: rank by word count

I added an endpoint (just added it to __init__.py file since this was an experiment) that performs a SQL query to get the longest blog posts by word count, and then made a template word-count.html that takes that json information and displays with with flask's render_template(). 

It's not very pretty, but the basic idea could then be fiddled with the sort ascending/descending as well as by other features (newest/oldest, etc)

Entries:
[[wordcount2.png]]

Ranked by word count: 
[[wordcount.png]]

If you were to then edit a post or add a post, the rankings would be adjusted. 

## New Design

I made buttons for the top header bar. 

[[css.png]]

## Acknowledgements

