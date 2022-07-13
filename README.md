# django_graphql_movies

Application ("api") - a video movie guide developed in GraphQL query language + Django / Graphene library.

Aside from the Django application, this repo also includes the following:

* **schema.graphql** - the complete GraphQL schema
* **queries.graphql** - an exmaple of every query and mutation defined in the schema
* **actorQuery.sh** - a sample cURL request to communicate with the API
* **movies.json** - test data

## Setting up

Clone this repo, and in the directory follow these steps:

```bash
# Install dependencies
pipenv sync
# Install dependencies dev
pipenv sync --dev
# Activate virtual environment
pipenv shell
# Run DB migration
python manage.py migrate
# Optional: load test data
python manage.py loaddata movies.json
# Run the application
python manage.py runserver
```
If you go to http://127.0.0.1:8000/graphql/, you'll be able to interact with the API there.
