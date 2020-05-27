This repository includes the automated tests for `https://demo.applitools.com/hackathon.html` website.
It is designed to develop a portfolio and is not meant for any challenge or hackathon.

## Packages

The project uses the following packages:
* Selenium Web Driver
* ChromeDriver / GeckoDriver
* Pytest
* Applitools Eyes SDK


## Project Structure

* The tests are organized as `conftest`, `pages`, and `tests`.  
* `conftest` file includes all the fixtures that are required for the tests' setup.
* `pages` folder contains page objects which represent each page of the website.
* `tests` folder includes two types of tests - traditional and visual. The visual tests utilize Applitools Eyes SDK.

## Author
* Vica Markosyan