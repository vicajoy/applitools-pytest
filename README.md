This repository includes automated tests for `https://demo.applitools.com/hackathon.html` website.
It is designed to develop a portfolio and is not meant for any challenge or hackathon.

## Packages
The project uses the following packages:
* Selenium WebDriver
* ChromeDriver 83.0.4103.97 
* GeckoDriver 0.26.0
* pytest
* pytest-xdist for parallel testing
* Applitools Eyes SDK

## Setup and Running Tests
* `requirements` file includes all the necessary packages to run the project tests successfully.
* By default, the tests will be running on Chrome. 
To run them on Firefox, use the following option in the terminal:
`--browser="firefox"`.
* To run tests in parallel, use `-n` option and provide the number of threads.

## Author
Vica Markosyan