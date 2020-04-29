# linkedin-extractor
Python script using Selenium to parse member's info from a LinkedIn group you administrate.
## Usage
1. You need to have the Selenium library installed :
```
pip install selenium
```
2. By default, this project uses Safari as a browser. You can use any other browser by editing the `driver = webdriver.Safari()` line and using a chosen driver. More info [here](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/).
3. Then, edit `credentials.py` and add your username and password to the variables `user` and `pwd`. Add the id of your group (you can find it in the group's url) to `group`, the number of the first and last pages you want to parse to `first` and `last`.
4. Run `linkedin-extractor.py` and profit ! All you data will be added to `output.csv`.
