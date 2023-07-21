# <u> Running the tests in Docker </u>

## Prerequisites
1. Docker is running
2. '.env' contains `GAUGE_ENVI`, `GAUGE_SPEC`, `GAUGE_TABLE_ROW`

**NOTE:** *When running the test, you can change the variables in .env to run the test case that you want.*


## Steps
1.  ```docker build .``` (This will take a few minutes...)
2. You can choose either of the 2 options below:
    a. If you want to run the tests that uses mock-server, run this below:
    ```docker compose -f docker-compose.mock.yml up```
    b. If you want to run your tests in regular environment, run this below
    ```docker compose up```

<br>

# <u> Configuring the wiremock </u>

## How to configure/add mappings
The mappings are placed under *./wiremock_mappings/mappings* folder.
You can add and follow the format in the given example in *example.json*