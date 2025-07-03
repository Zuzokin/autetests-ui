# UI Autotests Project

[![Allure Report](https://img.shields.io/badge/Allure_Report-Deployed-success?style=for-the-badge&logo=allure)](https://zuzokin.github.io/autetests-ui/)

Latest test results are available in the Allure report above.

## How to View Reports
- **Online**: Click the Allure badge above
- **Locally**:
  ```bash
  # Install dependencies
  pip install -r requirements.txt
  
  # Run tests with pytest
  pytest -m regression --alluredir=allure-results --numprocesses 2
  
  # Generate and serve Allure report locally
  allure serve allure-results