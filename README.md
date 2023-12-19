# Reverse Polish Notation Calculator

Provides an arithmetic calculator using this type of notation via a web API based on FASTAPI with two routes:

- one that returns the result in JSON (POST, /calculate, body: {expression:string})
- one that export in a csv file all the calculations made (GET, /export)

## .env file

In both production and dev environment, you  will need to create a `.env` file at the root of this project. You can create one copying `.env.dist` file and filling it with your data.

## Development

- Set up env file
- Simply use `docker compose up` for the stack with dev dependencies (black and flake8 for the backend).

## Production

- Set up env file
use `docker compose up -f docker-compose.prod.yml`

