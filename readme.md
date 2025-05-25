## Overview

**Project Title**: Broke Budget Buddy

**Project Description**: Broke Budget Buddy is a full-stack Django web application that allows users to track personal expenses, set monthly budgets, and receive real-time visual feedback on their financial status. The app features user authentication (sign up, log in, log out), dynamic budget alerts, and a clean, responsive interface styled with custom CSS.

**Project Goals**: 

- Build a budget-tracking app using Django as the backend web framework

- Practice CRUD operations in Django with models and forms

- Implement user authentication (login, logout, registration)

- Store user-specific budget goals and filter data by logged-in user

- Use template rendering and conditional styling to enhance user experience

- Use Git and GitHub for version control and deployment

## Instructions for Build and Use

Steps to build and/or run the software:

1. Clone the repository ("https://github.com/kkafle10/BrokeBudgetBuddy.git")
2. Create and activate a virtual environment(Python in Visual Code Studio)
3. Install Django (pip install django)
4. Run database migrations(python manage.py migrations
                           python manage.py migrate)
5. Start django development server (python manage.py runserver)


## Instructions for using the software:

1. Visit the home page and sign up with a new user account.

2. After logging in, you’ll be prompted to set a monthly budget.

3. Begin adding expenses by filling out the category, amount, and notes.

4. The app dynamically displays:

                    Total spent

                    Remaining balance

                    Color-coded budget status (on track, warning, or over budget)

5. You can delete any expense entry by clicking the trash icon.

6. Logout at any time, or log back in with your existing account.

## Development Environment 

To recreate the development environment, you need the following software and/or libraries with the specified versions:

To recreate the development environment, you’ll need:

- Python 3.13.3

- Django 5.2.1

- VS Code or any Python-friendly editor

- Git for version control

## Useful Websites to Learn More

I found these websites useful in developing this software:

- [Django Documentation](https://docs.djangoproject.com/en/5.2/)
- [Django Tutorial](https://www.youtube.com/watch?v=l0QEGvAX8rU)
- [W3Schools CSS Reference](https://www.w3schools.com/cssref/)
- [MDN HTML Forms Guide](https://developer.mozilla.org/en-US/docs/Learn/Forms)
- [ChatGPT (OpenAI)](https://chat.openai.com/)
- [Stack Overflow](https://stackoverflow.com/)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Add category filters or graphs for visual spending breakdown
* [ ] Let users edit or update expenses instead of just deleting
* [ ] Add mobile responsiveness and dark mode theme
