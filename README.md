# Finance + Technology News

[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.1-brightgreen.svg)](https://djangoproject.com)

## Public Site
The live public site can be viewed [here](http://alexrpreston.pythonanywhere.com/newsapp/).

## Getting an API Key

To pull all the data you will need an API key.

You can register one application at [newsapi.org/register](https://newsapi.org/register).


## Running Locally

First, clone the repository to your local machine:

```
git clone https://github.com/alexrpreston/News-Aggregator.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Replace line 30 in views.py with your API key:
```bash
KEY = os.getenv('NEWS_API_KEY') -> KEY = "Your Key"
```

Apply the migrations:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The site will be available at **http://127.0.0.1:8000/newsapp/**.

## Crawlers

You can run the crawlers manually to collect the top stories using the following command:

```bash
python manage.py scrapeWebsitesTask
```

### Cron Jobs

You can set up cron jobs to execute the crawlers periodically. Here is what my crontab looks like:

```
59 * * * * /home/alexrpreston/.virtualenvs/alexrpreston.pythonanywhere.com/bin/python
 /home/alexrpreston/alexrpreston.pythonanywhere.com/manage.py scrapeWebsitesTask
```
