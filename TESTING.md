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
- [Manual Testing](#manual-testing)
- [Lighthouse Dev Tools](#lighthouse-dev-tools)
    - [Results Desktop](#lighthouse-results-desktop)
    - [Results Mobile](#lighthouse-results-mobile)

- - -

## Python Validation
I used the Code Institute Python Linter to ensure sure the source code throughout was PEP8 compliant. The only errors were found in: 

Below are the results for each apps model.py, views.py, urls.py and forms.py

### Projects App

![Projects Model](/documentation/testing/ci-linter/project-model-py.jpg)
projects/models.py

![Projects View](/documentation/testing/ci-linter/project-views-py.jpg)
projects/views.py

![Projects Urls](/documentation/testing/ci-linter/project-urls-py.jpg)
projects/urls.py

![Projects Forms](/documentation/testing/ci-linter/project-forms-py.jpg)
projects/form.py

### Epics App

![Epics Model](/documentation/testing/ci-linter/epics-model-py.jpg)
epics/models.py

![Epics View](/documentation/testing/ci-linter/epics-views-py.jpg)
epics/views.py

![Epics Urls](/documentation/testing/ci-linter/epics-urls-py.jpg)
epics/urls.py

![Epics Forms](/documentation/testing/ci-linter/epics-forms-py.jpg)
epics/form.py

### Tasks App

![Tasks Model](/documentation/testing/ci-linter/tasks-model-py.jpg)
tasks/models.py

![Tasks View](/documentation/testing/ci-linter/tasks-views-py.jpg)
tasks/views.py

![Tasks Urls](/documentation/testing/ci-linter/tasks-url-py.jpg)
tasks/urls.py

![Tasks Forms](/documentation/testing/ci-linter/tasks-forms-py.jpg)
tasks/form.py

### Teams App
![Teams Model](/documentation/testing/ci-linter/teams-model-py.jpg)
teams/models.py

![Teams View](/documentation/testing/ci-linter/teams-views-py.jpg)
teams/views.py

![Teams Urls](/documentation/testing/ci-linter/teams-url-py.jpg)
 teams/urls.py

![Teams Forms](/documentation/testing/ci-linter/teams-forms-py.jpg)
teams/form.py

- - -

## HTML Validation

![HTML Validation](/documentation/testing/index-html-report-w3.jpg)

- Only the home.html page passed validation; all other pages with Django template language generated errors in addition to the HTMX request used in GET queries. The code continued to function despite all of the suggested error.

- - -

## CSS Validation
- No errors were found when passing it through the validator.
![W3C CSS Validation Image](/documentation/testing/css-w3c-report.jpg)

- - -

## JS Validation
- The warnings produced had no effect on the functionality 
![JSHint Validation Image](/documentation/testing/jshint-report.jpg)

- - -

## Manual Testing
### User Journey Testing

1. Home Page 

| Action | Expected Behavior | Result |
| :---         |     :---:      |          ---: |
| 1. Selecting Get Starting CTA on Hero Image | The sign-up form appears with the necessary information  | Pass |
| 2. Existing Username Sign up | User names must be distinct, and validation offers comments  | Pass |
| 3. Password Validation | Passwords must match and follow the form's strength validation requirements   |   Pass    |
| 4. CTA Changes on authentication  |   The Get Started CTA switches to Projects if the user is authenticated  | Pass |
| 5. Projects Nav Item  |   When verified, the Projects Nav item appears  | Pass |
| 6. Redirect to Projects  |   The user is taken to the projects page after authenticating  | Pass |

2. Project Page

| Action | Expected Behavior | Result |
| :---         |     :---:      |          ---: |
| 1. Existing Projects Display | If any projects are available, they are shown in a list format | Pass |
| 2. First time users | A default project card instructing the user to establish a new project is shown if there are no projects  | Pass |
| 3. Create Project CTA | A modal with form elements to create a new project appears when the "create project" call to action is clicked    |   Pass    |
| 4. Form Validation  |   The description and title fields are both required  | Pass |
| 5. Alert Message  |   When the project is successfully created, a confirmation message appears and the modal is closed  | Pass |
| 6. Updated Projects View  |  The projects list shows the New Project  | Pass |
| 7. Edit Project  |   When you choose 'Edit Project', a modal with a form is displayed, rendering the project details into the form.  | Pass |
| 8. Update Project  |   After the modal has closed, a message verifying the update appears if any changes were made  | Pass |
| 9. Delete Project  |  When selecting to delete a project, a deletion confirmation modal with the project title in bold appears  | Pass |
| 10. Alert Message  |  An alert message verifying the deletion's success displays  | Pass |
| 11. Direct To Project Manager  |  By choosing the project link, the visitor is taken to the project overview  | Pass |

3. Project Overview Page

| Action | Expected Behavior | Result |
| :---         |     :---:      |          ---: |
| 1. Updated Sidebar Button | The project overview is displayed, and the sidebar's Project Overview tab is active | Pass |
| 2. Edit Button In Overview | Choosing the overview's edit button displays a modal form for updating the project details (Repeated Process in the Projects Page)  | Pass |

4. Timeline Page

| 1. Selecting Timeline in the Sidebar  |   The timeline button becomes active and the timeline view is opened when you click on the timeline in the sidebar  | Pass |
| 2. View Epics in Timeline  |   Epics will be shown as a graph with a table underneath if they are available  | Pass |
| 3. Creating a Epic  |  Selecting the "Create Epic" button opens a modal, the required form fields are displayed  | Pass |
| 4. Form Validation  |   All fields are required, if any are not complete, detailed validation errors are shown  | Pass |
| 5. Alert Message  |  When the Epic is successfully created, a confirmation message appears and the modal is closed   | Pass |
| 6. Updated Timeline  |  The newly created epic has been added to the graph and displayed in the table below the graph  | Pass |
| 7. Delete Epic  |  When selecting to delete an epic, a deletion confirmation modal with the epic title in bold appears  | Pass |
| 8. Alert Message  |  An alert message verifying the deletion's success displays  | Pass |
| 9. Updated Timeline  |  The newly created epic has been added to the graph and displayed in the table below the graph  | Pass |
| 10. Edit Epic  |  When you choose 'Edit Epic', a modal with a form is displayed, rendering the epic details into the form.   | Pass |
| 11.  Update Epic  |  After the modal has closed, a message verifying the update appears if any changes were made   | Pass |
| 12.  Update Timeline  |  The graph is updated to reflect any modifications, showing the most recent data   | Pass |

5. Board Page

| 1. Selecting Board in the Sidebar  |   The board button becomes active and the board view is opened when you click on the board in the sidebar  | Pass |
| 2. View Task in Board  |  If the project has any tasks, they will be shown as 'To Do', 'In Progress', or 'Complete'  | Pass |
| 3. Creating a Task  |  Selecting the "Create Task" button opens a modal, the required form fields are displayed  | Pass |
| 4. Form Validation  |   Title, description and status field are required, if any are not complete, detailed validation errors are shown  | Pass |
| 5. Epic Validation  |   The selection bar only displays Epics that have been assigned to the project  | Pass |
| 6. Assignee Validation  |   Only teams that are present in the project are shown in the selection bar  | Pass |
| 7. Alert Message  |  When the task is successfully created, a confirmation message appears and the modal is closed   | Pass |
| 8. Updated Board  |  The newly created task is shown in its designated status category on the board  | Pass |
| 9. View Task Details  |  When you select Task, the task details are displayed, along with edit and delete options at the task container's bottom  | Pass |
| 10. Edit Task  |  When you choose 'Edit Task', a modal with a form is displayed, rendering the tasks details into the form.   | Pass |
| 11. Update Task  |  After the modal has closed, a message verifying the update appears if any changes were made   | Pass |
| 12. Status Update  |  The task will be moved to the appropriate category if its status has changed   | Pass |
| 13. Delete Task  |  When selecting to delete a task, a deletion confirmation modal with the task title in bold appears  | Pass |
| 14. Alert Message  |  An alert message verifying the deletion's success displays  | Pass |
| 15. Updated Board  |  The recently deleted task is removed from the board the board  | Pass |



## Lighthouse Dev Tools
I evaluated my website's usability and performance using the Lighthouse Dev Tools.

### Lighthouse results (Desktop)

![Home Page Desktop](/documentation/testing/lighthouse/homepage-lighthouse-desktop.jpg)
Home Page Desktop

![Projects Page Desktop](/documentation/testing/lighthouse/projects-page-lighthouse-desktop.jpg)
Projects Page Desktop

![Project Overview Desktop](/documentation/testing/lighthouse/project-overview-lighthouse-desktop.jpg)
Project Overview Desktop

![Timeline View Desktop](/documentation/testing/lighthouse/timeline-lighthouse-desktop.jpg)
Timeline View Desktop

![Board View Desktop](/documentation/testing/lighthouse/board-lighthouse-desktop.jpg)
Board View Desktop

![Task Manager View Desktop](/documentation/testing/lighthouse/task-manager-lighthouse-desktop.jpg)
Task Manager View Desktop

![Teams View Desktop](/documentation/testing/lighthouse/teams-lighthouse-desktop.jpg)
Teams View Desktop

- - -

### Lighthouse results (Mobile)

![Home Page Mobile](/documentation/testing/lighthouse/homepage-lighthouse-mobile.jpg)
Home Page Mobile

![Projects Page Mobile](/documentation/testing/lighthouse/projects-page-lighthouse-mobile.jpg)
Projects Page Mobile

![Project Overview Mobile](/documentation/testing/lighthouse/project-overview-lighthouse-mobile.jpg)
Project Overview Mobile

![Timeline View Mobile](/documentation/testing/lighthouse/timeline-lighthouse-mobile.jpg)
Timeline View Mobile

![Board View Mobile](/documentation/testing/lighthouse/board-lighthouse-mobile.jpg)
Board View Mobile

![Task Manager View Mobile](/documentation/testing/lighthouse/task-manager-lighthouse-mobile.jpg)
Task Manager View Mobile

![Teams View Mobile](/documentation/testing/lighthouse/teams-lighthouse-mobile.jpg)
Teams View Mobile