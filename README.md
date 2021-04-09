# WebScraping

Web scraping is the practice of gathering data through a program interacting with the API.

With web crawlers, you must be extremely conscientious of how much bandwidth you are using and make every effort to determine
whether there's a way to make the target server's load easier.

## VirtualEnv (Python2)

**How to install**
If you are using Python3 replace `virtualenv` with `venv`: `python -m venv envname`.
Created an environment by running `virtualenv scrapingEnv`, then activate it.

Install dependencies:
```
python3 -m pip install -r requirements.txt
```

Output dependencies:
```
python3 -m pip freeze > requirements.txt
```

**How to activate**

```sh
$ cd scrapingEnv/
$ source bin/activate
```

Check by typing `which python3`. Leaving by typing `deactivate`.