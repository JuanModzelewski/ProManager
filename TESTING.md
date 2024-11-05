[&lt; Back to README file](/README.md)

# TESTING

## CONTENT

- [Python Validation](#python-validation)
    - [Projects App CI Linter](#projects-app)
    - [Epics App CI Linter](#epics-app)
    - [Tasks App CI Linter](#tasks-app)
    - [Teams App CI Linter](#teams-app)
- [HTML Validation](#html-validation)
- [CSS Validation](#css-validation)
- [JS Validation](#js-validation)

## Validation Testing

### Python Validation
I used the Code Institute Python Linter to ensure sure the source code throughout was PEP8 compliant. The only errors were found in: 

Below are the results for each apps model.py, views.py, urls.py and forms.py

#### Projects App
![Projects Model](/documentation/testing/ci-linter/project-model-py.jpg)

![Projects View](/documentation/testing/ci-linter/project-views-py.jpg)

![Projects Urls](/documentation/testing/ci-linter/project-urls-py.jpg)

![Projects Forms](/documentation/testing/ci-linter/project-forms-py.jpg)

#### Epics App
![Epics Model](/documentation/testing/ci-linter/epics-model-py.jpg)

![Epics View](/documentation/testing/ci-linter/epics-views-py.jpg)

![Epics Urls](/documentation/testing/ci-linter/epics-urls-py.jpg)

![Epics Forms](/documentation/testing/ci-linter/epics-forms-py.jpg)

#### Tasks App
![Tasks Model](/documentation/testing/ci-linter/tasks-model-py.jpg)

![Tasks View](/documentation/testing/ci-linter/tasks-views-py.jpg)

![Tasks Urls](/documentation/testing/ci-linter/tasks-url-py.jpg)

![Tasks Forms](/documentation/testing/ci-linter/tasks-forms-py.jpg)

#### Teams App
![Teams Model](/documentation/testing/ci-linter/teams-model-py.jpg)

![Teams View](/documentation/testing/ci-linter/teams-views-py.jpg)

![Teams Urls](/documentation/testing/ci-linter/teams-url-py.jpg)

![Teams Forms](/documentation/testing/ci-linter/teams-forms-py.jpg)

### HTML Validation

![HTML Validation](/documentation/testing/index-html-report-w3.jpg)

Only the home.html page passed validation; all other pages with Django template language generated errors in addition to the HTMX request used in GET queries. The code continued to function despite all of the suggested error.

### CSS Validation
No errors were found when passing it through the validator.
![W3C CSS Validation Image](/documentation/testing/css-w3c-report.jpg)

### JS Validation
The warnings produced had no effect on the functionality 
![JSHint Validation Image](/documentation/testing/jshint-report.jpg)



## Manual Testing (BDD)

- Be aware! On some of the evidence below, when using the modal, the screen capture doesn't show the modal elements showing.


## User Journey Testing

1. Home Page 

| Action | Expected Behavior | Result |
| :---         |     :---:      |          ---: |
| 1. Selecting Get Starting CTA on Hero Image | The sign up for appear providing information needed to sign up  | Pass |
| 2. Existing Username Sign up | Usernames need to be unique and validation provides feedback  | Pass |
| 3. Password Validation | Passwords need to match and adhere to form validation on password strength   |   Pass    |
| 4. CTA Changes on authentication  |   If authenticated the Get Started CTA changes to go tho Projects  | Pass |


## Lighthouse Dev Tools
I evaluated my website's usability and performance using the Lighthouse Dev Tools.

### Lighthouse results (Desktop)
![Home Page Desktop](/documentation/testing/lighthouse/homepage-lighthouse-desktop.jpg)

![Projects Page Desktop](/documentation/testing/lighthouse/projects-page-lighthouse-desktop.jpg)

![Project Overview Desktop](/documentation/testing/lighthouse/project-overview-lighthouse-desktop.jpg)

![Timeline View Desktop](/documentation/testing/lighthouse/timeline-lighthouse-desktop.jpg)

![Board View Desktop](/documentation/testing/lighthouse/board-lighthouse-desktop.jpg)

![Task Manager View Desktop](/documentation/testing/lighthouse/task-manager-lighthouse-desktop.jpg)

![Teams View Desktop](/documentation/testing/lighthouse/teams-lighthouse-desktop.jpg)

### Lighthouse results (Mobile)
![Home Page Mobile](/documentation/testing/lighthouse/homepage-lighthouse-mobile.jpg)

![Projects Page Mobile](/documentation/testing/lighthouse/projects-page-lighthouse-mobile.jpg)

![Project Overview Mobile](/documentation/testing/lighthouse/project-overview-lighthouse-mobile.jpg)

![Timeline View Mobile](/documentation/testing/lighthouse/timeline-lighthouse-mobile.jpg)

![Board View Mobile](/documentation/testing/lighthouse/board-lighthouse-mobile.jpg)

![Task Manager View Mobile](/documentation/testing/lighthouse/task-manager-lighthouse-mobile.jpg)

![Teams View Mobile](/documentation/testing/lighthouse/teams-lighthouse-mobile.jpg)
