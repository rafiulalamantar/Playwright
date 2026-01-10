---

# 🧪 Playwright Python Automation

A collection of automated end-to-end tests written in **Python** using **Playwright** and **ytest** to validate web application functionality.

---

## 🚀 Features

* Playwright based browser automation (Chromium, Firefox, WebKit)
* Pytest test runner for test execution
* Fixtures and shared configuration via `conftest.py`
* Multiple test files demonstrating validation scenarios
* Easily extendable for new UI tests

---

## 📁 Repository Structure

```text
Playwright/
├── .idea/                         # IDE config (optional)
├── playwright/                   # Playwright Python related files or utilities
├── FirstDemo.py                 # Sample Playwright demo script
├── Test2PyTestValidation.py     # Second Pytest style test
├── TestPyTestValidation.py      # First Pytest style test
├── conftest.py                  # Pytest fixtures and common setup
├── requirements.txt             # Python dependency list (if present)
└── README.md                   # This file
```

> You can update the structure here to match your exact folders/files.

---

## 📦 Prerequisites

Make sure you have the following installed:

* Python 3.8+
* **Playwright for Python**
* **pytest**

---

## 🛠 Setup

1. **Clone the repository**

```bash
git clone https://github.com/rafiulalamantar/Playwright.git
cd Playwright
```

2. **Create and activate a virtual environment (optional but recommended)**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

If you have a `requirements.txt`:

```bash
pip install -r requirements.txt
```

Otherwise install Playwright + pytest:

```bash
pip install playwright pytest
```

4. **Install Playwright browsers**

```bash
playwright install
```

---

## ▶️ Running Tests

To run all tests with pytest:

```bash
pytest
```

To run a specific test file:

```bash
pytest TestPyTestValidation.py
```

To see detailed output:

```bash
pytest -v
```

---

## 📌 Playwright Tips

* You can generate test code using playwright’s codegen tool:

```bash
playwright codegen <URL>
```

* Default Playwright report can be shown with:

```bash
playwright show-report
```

This helps visualize execution results in the browser.

---

## 🎯 Test Reporting

By default, pytest outputs results in text format. You can integrate more advanced reporting:

* **HTML reports** with `pytest-html`
* **JUnit XML** for CI systems
* Integrate **Allure** for richer reports

Example to install pytest-html:

```bash
pip install pytest-html
pytest --html=report.html
```

---

## 📈 CI (GitHub Actions)

You can add a workflow like `.github/workflows/playwright.yml` to run tests on push/pull requests. A typical workflow includes:

```yaml
name: Playwright Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.x"
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest playwright
          playwright install --with-deps
      - name: Run tests
        run: pytest
```

This ensures your tests run on each commit. ([playwright.dev][1])

---

## 🧩 Contributing

Feel free to open issues or create pull requests. Follow best practices:

* Add meaningful test cases
* Reuse fixtures in `conftest.py`
* Keep selectors stable and maintainable

---

## 📝 License

You can optionally add your license (e.g., MIT), if you choose.

---

## 🙌 Thanks

Thank you for using this automation suite! Questions or contributions are welcome.

---

