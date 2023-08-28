# Django Project Setup (Linux HW DevOps01)
This repository contains a Django project setup script that automates the process of setting up 
a development environment for a Django web application.

# Prerequisites
Before you begin, make sure you have the following prerequisites installed on your system:

* Python 3.7
* MySQL Server
* Git
* Virtualenv (installed globally)
* Pip (Python package manager)

# Getting Started

Follow these steps to set up your development environment:
1) Clone this repository to your local machine using the following command:
   git clone https://github.com/YourUsername/YourRepository.git

2) Change into the repository directory:
   cd YourRepository

3) Run the setup script:
   python linux.py

This script will guide you through the setup process, including installing Python and
MySQL, creating a virtual environment, cloning the project repository, and installing the required
packages, loading sample data into MySQL, editing project settings, and running the Django server.

4) After running the setup script, your development environment should be ready.
You can access the Django application by opening http://localhost:8001 in your web browser.


## Important notes:

* The setup script assumes that you have sudo privileges for package installation and other system-level tasks.
* Make sure to edit the project settings file as instructed in the setup process to provide the appropriate configurations for the database and email settings.
* This setup is intended for this homework only. For production deployments, additional security measures and configurations are necessary.
