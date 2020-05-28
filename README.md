This repository includes automated tests for `https://demo.applitools.com/hackathon.html` website.
It is designed to develop a portfolio and is not meant for any challenge or hackathon.

## Packages
The project uses the following packages:
* Selenium WebDriver
* ChromeDriver, GeckoDriver
* pytest
* pytest-xdist for parallel testing
* Applitools Eyes SDK


## Project Structure
* The tests are organized as `conftest`, `pages`, and `tests`.  
* `conftest` file includes fixtures to setup tests.
For the `browser` and `url` setup, I have used `pytest_addoption` so that the arguments can be passed via the terminal.
* `pages` folder contains page objects which represent each page of the website.
* `tests` folder includes two types of tests - traditional and visual. The visual tests utilize Applitools Eyes SDK.


## Setup and Running Tests
* `requirements` file includes all the necessary packages to run the project tests successfully.
* By default, the tests will be running on Chrome. 
To run them on Firefox, use the following option in the terminal:
`--browser="firefox"`.
* To run tests in parallel, use `-n` option and provide the number of threads.


## Author
Vica Markosyan