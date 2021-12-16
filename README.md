# ML Salary Prediction Web App
Build A Machine Learning Web App From Scratch

## Table of contents
* [About](#about)
* [The website](#the-website)
* [Data analysis](#data-analysis)
* [Startup the project](#startup-the-project)
* [Install](#install)

## About
In this project, we build a Machine Learning web application from scratch in Python with Streamlit. We use real world data to build a machine learning model.

## The website
Check out our website:
<p align="center"><img src="https://github.com/nekoemperor/salaryprediction-ml-app/blob/master/salaryprediction/images/salaryprediction.gif" width="768"  />

## Data analysis
* Datasets and sources:
  - [Stack Overflow Annual Developer Survey](https://insights.stackoverflow.com/survey), from 2021 (With nearly 80,000 responses fielded from over 180 countries and dependent territories, our Annual Developer Survey examines all aspects of the developer experience from career satisfaction and job search to education and opinions on open source software.). [Link](https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2021.zip)
  - Extract the zip.file and put it in salaryprediction/data

* Type of analysis: machine learning using SciKit-Learn, DecisionTreeRegressor (to be optimized, we still have significant error)

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for salaryprediction in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/salaryprediction`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "salaryprediction"
git remote add origin git@github.com:{group}/salaryprediction.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
salaryprediction-run
```

# Install

Go to `https://github.com/{group}/salaryprediction` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/salaryprediction.git
cd salaryprediction
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
salaryprediction-run
```
