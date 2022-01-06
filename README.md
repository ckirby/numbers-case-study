# Chaim Kirby's submission for Case Study
## Startup
Run `docker-compose build` to build the project for use or development
## USAGE
This project uses docker-compose to run. Running `docker-compose up dev` will bring up the dev server on port :8000. Using curl, Postman, or a browser the following endpoints can be exercised.
* GET `/num_to_english?number=<positive or negative integer negative sys.maxsize to sys.maxsize>`
* POST `/num_to_english {"number": "<positive or negative integer negative sys.maxsize to sys.maxsize>"`
* Both GET and POST will respond to a non-integer or missing number parameter with an error message in the "status" portion
## DEVELOPMENT
This project has 3 `docker-compose` services for use in development
* `lint` will lint the project using `black`
* `tests` will run the test suite with pytest
* `dev` will run django's development server `runserver` for endpoint testing 
