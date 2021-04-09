# BeautifulSoup Objects

An example of a beautifulSoup Object:

```html
html→<html><head>...</head><body>...</body></html>
— head → <head><title>A Useful Page<title></head>
    — title → <title>A Title</title>
— body → <body><h1>An Int...</h1><div>Lorem ip...</div></body>
    — h1 → <h1>An H1 tag Title</h1>
    — div → <div>Lorem Ipsum dolor...</div>
```

# Tag Objects
All `bs.h1`, `bs.html.body.h1`, ..., `bs.html.h1` have the same output.

---> `bs.tagName`

## Searching tags by attributes

`bs.findAll('span', {'class': 'green'})` - list of all tags: `<span class="green"></span>`

---> `find_all(tag, attributes, recursive, text, limit, keywords)`  
---> `find(tag, attributes, recursive, text, keywords)`

* __tag__: a single name of a tag or a list of string of tag names  
* __attributes__: matches tags that contain __any one of those attributes__  -> this works as **or**
* __recursive__: boolean, if False, only at the top-level  
* __text__: matches based on the text content of the tags  
* __limit__: only the first x items from the page  
* __keywords__: allow you to select tags that contain a particular attribute or set of attributes  
---> example of keywords `bs.find_all(class_='green', id='title')` -> this works as **and**



`.get_text()` strips all tags from the document you are working with and returns a Unicode string containing the text only.

# NavigableString Objects

We have children, siblings and descendants, parents.  
  --> `.parent(s), .children, .descendants, .next(previous)_siblings, next(previous)_sibling`  

## Regular expression

A regex can be inserted as any argument in a BeautifulSoup expression.
`bs.find_all('img', {'src': re.compile('a regular expression')}`

## Accessing Attributes

`myTag.attrs` -> returns a dictionary object

## Lambda Expressions

These functions must take a tag object as an argument and return a boolean
`bs.find_all(lambda tag: len(tag.attrs) == 2)`
Combine with regex: `lambda tag: tag.get_text() == re.compile()"`

# Comment Object

-------------------------------------------------------

You can use the BeautifulSoup select function with a single string CSS selector for each
piece of information you want to collect and put all of these selectors in a dictionary object.