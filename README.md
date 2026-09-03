# Pytest Selenium BDD Framework

A simple **Selenium automation framework using Python, Pytest, Pytest-BDD, and Page Object Model (POM)**.

This project is mainly built for **learning and practicing Selenium automation concepts**, with plans to gradually evolve it into a more production-ready framework.

## 🛠 What I've Practiced

* **Selenium WebDriver**
* **Pytest & Pytest-BDD**
* **BDD / Gherkin feature files**
* **Page Object Model (POM)**
* **XPath & CSS Selectors**
* XPath using:

  * `contains()`
  * `text()`
  * `starts-with()`
  * `@attribute`
  * **Parent / Child relationships**
  * **Ancestor / Descendant relationships**
  * `following-sibling`
  * `preceding-sibling`
  * `ancestor::`
  * `descendant::`
  * `..` for moving to parent elements
  * Indexing for selecting specific elements
* **Explicit waits** with `WebDriverWait` and Expected Conditions
* **Implicit waits** for practice
* Element interactions such as:

  * Click
  * Clear
  * Send keys
  * Visibility checks
  * Value assertions
* Reusable **Page Object methods**
* Pytest fixtures and test execution
* Basic Git / GitHub workflow

## 📁 Structure

```text
├── features/          # Gherkin feature files
├── steps/             # Step definitions
├── pages/             # Page Object classes
├── tests/             # Test execution
├── conftest.py        # Fixtures
└── requirements.txt
```

## 🚀 Run

```bash
pip install -r requirements.txt
pytest -v
```

## 🎯 What's Next?

This is a **learning project and a work in progress**. The plan is to gradually add better configuration management, logging, reporting, parallel execution, test utilities, and CI/CD integration.

The idea is to keep improving the framework as I learn more about building maintainable automation systems.
