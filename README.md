# HCL Auth Automation - QA Automation Framework (Flask + Selenium + Pytest)

## 📌 Project Overview
This project is a **QA Automation Case Study** built for automating the **Authentication Module** of a web application.
It includes:
- Login Page
- Forgot Password Feature
- Error Message Validations
  
---


The project is implemented using:
- **Flask** (to build the demo authentication web application)
- **Selenium WebDriver** (for browser automation)
- **Pytest** (for test execution and test structuring)
- **Data-driven testing (CSV)**
- **HTML Reports + Logs**

---

## 🎯 Problem Statement (HCL Case Study 2)
HCLTech develops enterprise web applications that require rigorous testing before deployment.  
As a QA Automation Engineer, automate the testing of a web application’s authentication module.

---

## ✅ Features Implemented
### 🔹 Application Features
✔ Login page  
✔ Forgot password page  
✔ Validations and error messages  

### 🔹 Automation Features
✔ Automated login (valid + invalid credentials)  
✔ Automated forgot password workflow  
✔ Error message validation using assertions  
✔ Pytest test structure with fixtures and markers  
✔ Data-driven testing using CSV files  
✔ Execution logging (`execution.log`)  
✔ HTML test report generation (`html-report.html`)  
✔ Explicit waits to handle dynamic loading  

---

## ⚙️ Technologies Used
- Python 3.x
- Flask
- Selenium WebDriver
- Pytest
- webdriver-manager
- pytest-html
- CSV (data-driven testing)

---

🔑 Test Credentials  
✅ Valid Users  
admin@example.com / Admin@123  
user@example.com / User@123  

❌ Invalid Users  
Wrong email  
Wrong password  
Empty fields  

---


🧪 Run Automation Tests  
Run all tests  
python -m pytest -v  

Run Smoke tests only  
python -m pytest -m smoke -v  

Run Regression tests  
python -m pytest -m regression -v  

---


📊 Reports & Logs  
✅ HTML Report  
After execution, report is generated here:  
automation/reports/html-report.html  

✅ Execution Logs  
Logs are saved here:  
automation/logs/execution.log  

✅ Screenshots  
Screenshots are saved when tests fail:  
automation/screenshots/failed_tests/  

---

✅ Case Study Requirements Mapping  
Tasks Covered  
Automated login functionality (valid + invalid credentials)  
Validated error messages for incorrect login attempts  
Automated Forgot Password workflow  
Used Pytest to structure test cases  
Implemented reusable utilities + fixtures  
Generated execution logs + HTML report  
Handled waits and synchronization issues  

---

Constraints Covered  
✔ Data-driven tests using CSV  
✔ Synchronization handled using waits  
✔ Standard QA automation practices (POM + fixtures + logs + reports)  

---

🏁 Final Output  
✔ Total Test Cases Executed: 7  
✔ Result: All Passed Successfully  
✔ HTML Report Generated  
✔ Logs Generated  

---

<img width="1917" height="950" alt="Screenshot 2026-01-21 152123" src="https://github.com/user-attachments/assets/2daf0d5b-c7f1-4447-855e-954b2ad46031" />
<img width="1919" height="959" alt="Screenshot 2026-01-21 152139" src="https://github.com/user-attachments/assets/a3a628fc-9c8f-4c3f-9d5f-6e5b2b908d8d" />

