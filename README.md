[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)
![GitHub commit activity](https://img.shields.io/github/commit-activity/y/ikostan/Build_Backend_REST_API_with_Python_and_Django)
[![Build Status](https://travis-ci.org/ikostan/Build_Backend_REST_API_with_Python_and_Django.svg?branch=master)](https://travis-ci.org/ikostan/Build_Backend_REST_API_with_Python_and_Django)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c8581d51c457467a9e5d106e5acebd94)](https://www.codacy.com/manual/ikostan/Build_Backend_REST_API_with_Python_and_Django?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ikostan/Build_Backend_REST_API_with_Python_and_Django&amp;utm_campaign=Badge_Grade)

# [Backend EST API with Python & Django](https://www.udemy.com/course/django-python-advanced)

<div align="center"> 
<img width="9%" height="9%" src="https://github.com/ikostan/Build_Backend_REST_API_with_Python_and_Django/blob/master/img/python-icon-18.jpg" hspace="20">
<img width="9%" height="9%" src="https://github.com/ikostan/Build_Backend_REST_API_with_Python_and_Django/blob/master/img/django-icon-0.jpg" hspace="20">
<img width="9%" height="9%" src="https://github.com/ikostan/Build_Backend_REST_API_with_Python_and_Django/blob/master/img/docker-icon-14.jpg" hspace="20">
<img width="10%" height="10%" src="https://github.com/ikostan/Build_Backend_REST_API_with_Python_and_Django/blob/master/img/travis-ci.png" hspace="20">
<img width="9%" height="9%" src="https://github.com/ikostan/Build_Backend_REST_API_with_Python_and_Django/blob/master/img/rest-api-icon-8.jpg" hspace="20">
<img width="9%" height="9%" src="https://github.com/ikostan/Build_Backend_REST_API_with_Python_and_Django/blob/master/img/iconfinder_api-code-window_532742.png" hspace="20">
<!--<img width="9%" height="9%" src="https://github.com/ikostan/Build_Backend_REST_API_with_Python_and_Django/blob/master/img/build-devops-automation-recycle_code-refresh_settings-preferences-512.png" hspace="20">-->
</div>

### Create an advanced REST API with Python, Django REST Framework and Docker using Test Driven Development (TDD)

### Table of Contents

1. <a href="#about">About</a>

2. <a href="#main_objectives">Main Objectives</a>

3. <a href="#topics">Tech Topics Covered</a>

4. <a href="https://github.com/ikostan/Build_Backend_REST_API_with_Python_and_Django/tree/master/img">Icons Library</a>

5. <a href="#resources">Official Web Resources</a>

6. <a href="#moreresources">Additional Resources</a>

7. <a href="#tech_issues">Tech Issues and Problem Solving</a>

8. <a href="https://github.com/ikostan/Build_Backend_REST_API_with_Python_and_Django/tree/master/app">Django App:</a>

   - <a href="https://github.com/ikostan/Build_Backend_REST_API_with_Python_and_Django/tree/master/app/app">Django App Configuration Files</a>
   - <a href="https://github.com/ikostan/Build_Backend_REST_API_with_Python_and_Django/tree/master/app/core">Core app</a>

### About
<a id="about"></a>

The advanced course on how to Build a Backend REST API using Python, Django (2.0), Django REST Framework (3.9), Docker, Travis CI, Postgres and Test Driven Development!

The original course content was created by [Mark Winterbottom](https://linkedin.com/in/markwinterbottom/).

### The main goal is to built a fully functioning REST API that can handle
<a id="main_objectives"></a>

- User authentication
- Creating objects
- Filtering and sorting objects
- Uploading and viewing images

### Additional topics covered
<a id="topics"></a>

- Setup a project with Docker and Docker-Compose
- Configure Travis-CI to automatically run linting and unit tests
- Write unit tests using the Django Test Framework
- Apply best practice principles including Test Driven Development  
- Handle uploading media files with Django
- Customize the Django admin
- Configure a Postgres database

### Official Web Resources
<a id="resources"></a>

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com)
- [Travis-CI](https://travis-ci.org/)
- [PostgreSQL](https://www.postgresql.org)
- [GitHub](https://github.com/)

### Additional Resources
<a id="moreresources"></a>

- [GitHub Desktop](https://desktop.github.com/)
- [PyCharm](https://www.jetbrains.com/pycharm/)

### Tech Issues and Problem Solving
<a id="tech_issues"></a>

<details>
  <summary><b>First-Time Git Setup</b></summary>
  
  The first thing you should do when you install Git is to set your user name and email address. This is important because every Git commit uses this information, and it’s immutably baked into the commits you start creating:

  ```bash
    git config --global user.name "John Doe"
    git config --global user.email johndoe@example.com
  ```
  
  [Source](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
  
</details>

<details>
  <summary><b>Changing the project interpreter in the PyCharm project settings</b></summary>

1. In the **Settings/Preferences dialog** (Ctrl+Alt+S), select **Project <project name> | Project Interpreter**.
2. Expand the list of the available interpreters and click the **Show All** link.
3. Select the target interpreter. When PyCharm stops supporting any of the outdated Python versions, the corresponding project interpreter is marked as unsupported.
4. The Python interpreter name specified in the **Name** field, becomes visible in the list of available interpreters. Click **OK** to apply the changes.

For more info please [check here](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)
</details>

<details>
  <summary><b>PyCharm - Choosing Your Testing Framework</b></summary>
 
1. Open the Settings/Preferences dialog, and under the node Tools, click the page **Python Integrated Tools**.
2. On this page, click the **Default Test Runner** field.
3. Choose the desired test runner:

<div align="center"> 
<img width="60%" height="60%" src="https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/blob/master/testing_selenium_capabilities/img/py_choosing_test_runner.png" hspace="20">
</div>

For more info please see [Enable Pytest for you project](https://www.jetbrains.com/help/pycharm/pytest.html)
</details>

<details>
  <summary><b>Setting up Python3 virtual environment on Windows machine</b></summary>

1. open CMD<br/>
2. navigate to project directory, for example:<br/> 
```bash
cd C:\Users\superadmin\Desktop\Python\CodinGame
```
3. run following command:<br/> 
```bash 
pip install virtualenv
```
4. run following command:<br/> 
```bash 
virtualenv venv --python=python
```
</details>

<details>
  <summary><b>Manjaro: Install Python3 pip, virtualenv</b></summary>

<br/>
All python3 packages are prefixed python-, whereas python2 packages are prefixed python2-.

   1. The package is called python-pip. First check if it's already installed: `pacman -Qs python-pip`
    
   2. If there is no output after running the above command, that means that the package is not installed. In order to install it, run: `sudo pacman -Syu python-pip`
    
   3. In order to install `virtualenv` run: `pip install virtualenv`
    
   4. You also need to run `sudo /usr/bin/easy_install virtualenv` which puts it in `/usr/local/bin/`.

[Source](https://stackoverflow.com/questions/31133050/virtualenv-command-not-found)

</details>

<details>
  <summary><b>Setting up Python3 virtual environment on Linx (Ubuntu) machine</b></summary>

### How to install virtualenv

1. Install **pip** first
```bash
    sudo apt-get install python3-pip
```

2. Then install **virtualenv** using pip3
```bash
    sudo pip3 install virtualenv
```

3. Now create a virtual environment
```bash
    virtualenv venv
```
>you can use any name insted of **venv**

4. You can also use a Python interpreter of your choice:

```bash
    virtualenv -p /usr/bin/python2.7 venv
```

5. Active your virtual environment:

```bash
    source venv/bin/activate
```

6. Using fish shell:

```bash
    source venv/bin/activate.fish
```

7. To deactivate:

```bash
    deactivate
```

8. Create virtualenv using Python3:

```bash
    virtualenv -p python3 myenv
```

9. Instead of using virtualenv you can use this command in Python3:

```bash
    python3 -m venv myenv
```

[Source](https://gist.github.com/frfahim/73c0fad6350332cef7a653bcd762f08d)
</details>

<details>
  <summary><b>Activate Virtual Environment</b></summary>

In a newly created virtualenv there will be a bin/activate shell script. For Windows systems, activation scripts are provided for CMD.exe and Powershell.

1. Open Terminal
2. Run: \path\to\env\Scripts\activate 
  
[Source](https://pypi.org/project/virtualenv/1.8.2/)
</details>

<details>
  <summary><b>Auto generate requirements.txt</b></summary>

Any application typically has a set of dependencies that are required for that application to work. The requirements file is a way to specify and install specific set of package dependencies at once.<br/>
Use pip’s freeze command to generate a requirements.txt file for your project:
```bash
pip freeze > requirements.txt
```

If you save this in requirements.txt, you can follow this guide: [PyCharm - Manage dependencies using requirements.txt](https://www.jetbrains.com/help/pycharm/managing-dependencies.html), or you can:<br/>
   
```bash
pip install -r requirements.txt
```   
[Source](https://www.idiotinside.com/2015/05/10/python-auto-generate-requirements-txt/)
</details>

<details>
<summary><b>Install Python 3 virtualenv on Ubuntu</b></summary>

Step by step:

```bash
# Step 1: Update your repositories
sudo apt-get update

# Step 2: Install pip for Python 3
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
sudo apt install python3-pip

# Step 3: Use pip to install virtualenv
sudo pip3 install virtualenv 

# Step 4: Launch your Python 3 virtual environment, here the name of my virtual environment will be `venv`
virtualenv -p python3 venv

# Step 5: Activate your new Python 3 environment. There are two ways to do this
. venv/bin/activate # or source env3/bin/activate which does exactly the same thing

# you can make sure you are now working with Python 3
python -- version

# this command will show you what is going on: the python executable you are using is now located inside your virtualenv repository
which python 

# Step 6: code your stuff

# Step 7: done? leave the virtual environment
deactivate
```

[Source](https://naysan.ca/2019/08/05/install-python-3-virtualenv-on-ubuntu/)

</details>

<details>
  <summary><b>Install Docker Engine on Ubuntu</b></summary>
  
1. Older versions of Docker were called `docker`, `docker.io`, or `docker-engine`. If these are installed, uninstall them:
  ```bash
  sudo apt-get remove docker docker-engine docker.io containerd runc
  ```

2. Update the `apt` package index and install packages to allow `apt` to use a repository over HTTPS:
  ```bash
  sudo apt-get update

  sudo apt-get install \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg-agent \
        software-properties-common
  ```

3. Add Docker’s official GPG key:
  ```bash
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

  # Verify that you now have the key with the fingerprint
  sudo apt-key fingerprint 0EBFCD88
  ```

4. Use the following command to set up the `stable` repository:
  ```bash
  sudo add-apt-repository \
  "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
  (lsb_release -cs) \
  stable"
  ```

5. Update the `apt` package index, and install the latest version of Docker Engine and container:
  ```bash
  sudo apt-get update
  sudo apt-get install docker-ce docker-ce-cli containerd.io
  ```

6. Verify that Docker Engine is installed correctly by running the `hello-world` image:
  ```bash
  sudo docker run hello-world
  ```
  This command downloads a test image and runs it in a container. When the container runs, it prints an informational message and exits.
  
[Source](https://docs.docker.com/engine/install/ubuntu/)
  
</details>

<details>
  <summary><b>Install Docker Compose on Linux systems</b></summary>
    
 Step-by-step instructions are included below:
  
 1. Run this command to download the current stable release of Docker Compose:
  ```bash
  sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  ```
  
 2. Apply executable permissions to the binary:
  ```bash
  sudo chmod +x /usr/local/bin/docker-compose
  ```

 3. Test the installation:
  ```bash
  docker-compose --version
  ```
  
[Source](https://docs.docker.com/compose/install/)
</details>

<details>
  <summary><b>error: RPC failed; curl 56 Recv failure: Connection was reset</b></summary>

1. Open Git Bash
2. Run: "git config --global http.postBuffer 157286400" 
  
[Source](https://stackoverflow.com/questions/36940425/gitlab-push-failed-error)
</details>

<details>
  <summary><b>How to fix in case .gitignore is ignored by Git</b></summary>

Even if you haven't tracked the files so far, Git seems to be able to "know" about them even after you add them to .gitignore<br/> 

**NOTE:**

- First commit your current changes, or you will lose them.
- Then run the following commands from the top folder of your Git repository:

```bash 
git rm -r --cached .
git add .
git commit -m "fixed untracked files"
```
</details>

<details>
  <summary><b>How to generate Allure report with history trends (Windows OS)</b></summary>

<br/>Step by step:

1. Run tests from pytest using following arguments: -v --alluredir=allure-results
2. Copy '.\allure-report\history\' folder into '.\allure-results\history\'
3. Run: allure generate .\allure-results\ -o .\allure-report\ --clean
4. Following output should appear: Report successfully generated to .\allure-report
5. Run: allure open .\allure-report\

[Source](https://github.com/allure-framework/allure2/issues/813)
</details>

<details>
  <summary><b>Sphinx Documentation Set Up</b></summary>

<br/>Step by step:

1. Create docs directory

2. Open cmd > Go to docs directory

3. cmd > Run: sphinx-quickstart. **Note:** run with default answers
    
4. Go to docs/conf.py

5. Uncomment following lines:
```python
    import os
    import sys
    sys.path.insert(0, os.path.abspath('.'))
```
6. Update extensions list as following:
```python
extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc']
```
7. Update template as following:
```python
html_theme = 'sphinx_rtd_theme'
```
8. Update sys.path.insert as following:
```python
sys.path.insert(0, os.path.abspath('..'))
```
9. Go to docs/index.rst > add modules, see example below:
```bash

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
```
10. Open cmd > run: 
```python
sphinx-apidoc -o . ..
```
11. cmd > Run: make html
12. Install html template:
```python
pip install sphinx_rtd_theme
```

[Video Tutorial](https://www.youtube.com/watch?v=b4iFyrLQQh4)
[Sphinx Documentation](https://www.sphinx-doc.org/en/master/usage/quickstart.html)
[More Info](https://stackoverflow.com/questions/13516404/sphinx-error-unknown-directive-type-automodule-or-autoclass)
</details>

<details>
  <summary><b>Auto-Generated Python Documentation with Sphinx</b></summary>

<br/>Step by step:

1. Open CMD
2. Go to docs directory
3. Run: make clean
4. Run: make html

[Source](https://www.youtube.com/watch?v=b4iFyrLQQh4)
</details>
