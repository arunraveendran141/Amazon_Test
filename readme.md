
# Amazon Device Search Automation (Selenium + Pytest)

This project automates the process of searching for mobile devices on [Amazon India](https://www.amazon.in) using Selenium WebDriver. It supports CLI-driven test execution via Pytest with device parameterization, parallel runs, and HTML reporting.




## Features

- 🔍 Searches user-specified devices on Amazon.in
- 🧪 Pytest-based automation framework
- 🧩 Command-line parameterization for flexible test execution
- ⚡ Parallel execution using `pytest-xdist`
- 📊 Rich HTML reports using `pytest-html`


## Create and Activate Virtual Environment

```
python3 -m venv .venv

# Activate (Linux/macOS)
source .venv/bin/activate
```
## Install Python Dependencies

```
pip install -r requirements.txt
```
## How to Run the Tests

### Single Device Test (with live console output)
```
pytest amazon_test.py --devices "iPhone 15" -v -s
```

### Multiple Device Test in Parallel (with HTML Report)
```
pytest amazon_test.py --devices "iPhone 15, Samsung Galaxy A55" -v --capture=tee-sys -n 2 --html=report.html
