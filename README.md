# ProManager



Visit the deployed site: [ProManager](https://pro-manager-10b4d100221c.herokuapp.com/)

Description



## CONTENTS

* [User Experience](#user-experience-ux)

* [Design](#design)

* [Technologies Used](#technologies-used)

* [Deployment & Local Development](#deployment--local-development)

* [Testing](#testing)
  
* [Credits](#credits)


- - -

## User Experience (UX)

### User Stories

#### Initial User Goals

#### Returning User Goals

#### Frequent User Goals

- - -

## Design

### Color Scheme

### Favicon

* A favicon in the browser tab.

  ![favicon](/documentation/favicon/pro-manager-favicon-96.png)


### Typography

### Imagery

### Database ERM

![Database Diagram](/documentation/features/erd-diagram.jpg)

### Wire-frames

![Figma Design]()

### Project Author Journey

#### The Home Page

- A tidy webpage outlining ProManager's capabilities and advantages greets the user.
![Home page image](/documentation/features/promanager-homepage.jpg)

- Direct access to the projects through a straightforward login form puts the user one step closer to collaboration and organisation.
![Login](/documentation/features/promanager-signin.jpg)

- If registration is necessary, the simple form offers verification and account creation instructions.
![SignUp](/documentation/features/promanager-signup.jpg)


#### First Time User Project Creation

- The card that appears when a user visits the website for the first time will initiate their first project.
![Projects Page](/documentation/features/first-time-user-projects.jpg)

- When starting a new project, a form with easily comprehensible labels guides the user to the necessary information.
![Create Project Modal](/documentation/features/create-project-modal.jpg)

- Following the creation of a project, a success message is presented to the user along with the ability to amend or delete the project.
![Project Page after first project creation](/documentation/features/project-page.jpg)

- The edit modal is loaded and the project data is displayed for correction if the project information has to be changed.
![Edit Project](/documentation/features/edit-project-modal.jpg)

- A clear confirmation popup with the project title shown in bold appears when the delete project option is selected.
![Delete Project Confirmation](/documentation/features/delete-project-confirmation.jpg)

#### Project Overview

- A project overview is shown, along with a description of the project and the option to edit it while in this view.
![Project Overview](/documentation/features/project-overview.jpg)


#### Timeline View (Epics)

- The allocated epics are shown visually on a timeline in the graph style. A modal enabling the creation of a new epic will appear when the create epic button is selected.
Viewing epic details, editing epic information, and deleting an epic are all accessible from a table beneath the timeline. 
![Timeline View](/documentation/features/project-time-line.jpg)

- A form appears in a modal display when the "create epic" button is clicked. The form has a clear labels that list the details needed to create an epic.
![Creating An Epic](/documentation/features/create-epic-modal.jpg)

- Users can modify the epic details by using the edit epic button, which opens a modal with the epic information added.
![Editing An Epic](/documentation/features/edit-epic-modal.jpg)

- The title of the selected epic to be deleted is displayed in the delete epic modal when the delete epic button is selected.
![Deleting Epic Confirmation](/documentation/features/delete-epic-confirmation.jpg)

- The epic information and any tasks assigned to the epic are displayed when you click on the epic row or select the view icon(on available to team members).
![Viewing Epics](/documentation/features/epic-information-modal.jpg)


#### Board View (Tasks)

- All accessible tasks are listed in the board view for completion and progress. The task overview is well-represented by the board, which has unambiguous labels.
![The Board View](/documentation/features/project-board.jpg)

- The task title, the epic to which it belongs, the date of its last update, a description, and the individuals assigned to the task are all displayed using the accordion style display. Additionally, the chosen task can be edited or deleted.
![View Task Information](/documentation/features/task-accordion-open.jpg)

- When you select "create Task," a clearly labelled modal with all the necessary details to create a new task is displayed.
![Creating Tasks](/documentation/features/create-task-modal.jpg)

- When you select to edit a task, a modal window with the task's details is displayed.
![Editing Tasks](/documentation/features/edit-task-modal.jpg)

- When a task is selected for deletion, a delete confirmation popup with the task title in bold is displayed.
![Delete Task Confirmation](/documentation/features/delete-task-confirmation.jpg)


#### Task Manager


![Task Manager View](/documentation/features/project-task-manager.jpg)


![View Tasks Epics](/documentation/features/create-task-modal.jpg)


![Editing Tasks](/documentation/features/edit-task-modal.jpg)


![View Task Information](/documentation/features/task-manager-accordion-open.jpg)


![Unassigned Tasks](/documentation/features/task-manager-unassigned-tasks.jpg)


#### Teams


![Teams View](/documentation/features/project-teams.jpg)


![Create a Team](/documentation/features/create-team-modal.jpg)


![User not found Validation](/documentation/features/user-does-not-exist-validation.jpg)


![Editing Teams](/documentation/features/edit-team-modal.jpg)


![Adding Users Validation](/documentation/features/user-search-validation.jpg)


![Delete Confirmation Removing users](/documentation/features/delete-member-confirmation.jpg)


![Delete Team Confirmation](/documentation/features/delete-team-confirmation.jpg)


#### Future Implementations


### Accessibility


- - -

## Technologies Used

### Languages
- [Python](https://docs.djangoproject.com/en/5.1/releases/4.2.15/)
- [JS](https://www.javascript.com/)
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)

### Frameworks
- [Django 5.1.2](https://docs.djangoproject.com/en/5.1/releases/5.1.2/)

### Databases
- [Code Institutes Postgresql](https://www.postgresql.org/)

### 3rd Party Imports
- [Pip](https://pypi.org/project/pip/)
- [allauth](https://docs.allauth.org/en/latest/)
- [summernote](https://pypi.org/project/django-summernote/)
- [crispy forms with boostrap 5](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Gunicorn](https://gunicorn.org/)
- [whitenoise](https://whitenoise.readthedocs.io/en/stable/django.html)
- [sqlparse](https://pypi.org/project/sqlparse/) 
- [Psycopg2](https://pypi.org/project/psycopg2/)
- [oauthlib](https://oauthlib.readthedocs.io/en/latest/)
- [PyJWT](https://pyjwt.readthedocs.io/en/latest/)
- [asgiref](https://pypi.org/project/asgiref/)
- [dj-database-url](https://pypi.org/project/dj-database-url/)
- [python3-openid](https://pypi.org/project/python3-openid/)
- [requests-oauthlib](https://requests-oauthlib.readthedocs.io/en/latest/)
- [django-htmx](https://pypi.org/project/django-htmx/)
- [django-filter](https://pypi.org/project/django-filter/)

### Frameworks, Libraries & Programs Used

- [Figma](https://www.figma.com/) Used to create wire-frames.
- [Visual Studio Code](https://code.visualstudio.com/) Used as my primary IDE
- [Git](https://git-scm.com/) For version control.
- [Github](https://github.com/) To save and store the files for the website.
- [Google Fonts](https://fonts.google.com/) To import the fonts used on the website.
- [jQuery](https://jquery.com/) A JavaScript library.
- [HTMX](https://htmx.org/) To perform GET requests
- [BOOTSTRAP](https://getbootstrap.com/) for styling
- [Affinity](https://affinity.serif.com/en-gb/) To resize images and convert to webp format.
- [Am I Responsive?](http://ami.responsivedesign.is/) To show the website image on a range of devices.
- [dbdiagram.io](https://dbdiagram.io/home/) To Map out the models require to structure the database
- [PostgrSQL16 Admin](https://shields.io/) To visualize the database structure
- [Copilot](https://copilot.microsoft.com/) To create fictional use case and dat for testing

- - -

## Deployment

### Github Deployment

The website was stored using GitHub for storage of data and version control. To do this I did the following;

After each addition, change or removal of code, in the terminal within your IDE type:

- git add .
- git commit -m "meaningful commit message"
- git push

The files are now available to view within your github repository.

### Use CI Template

The CI template was cloned [CI Full Template](https://github.com/Code-Institute-Org/ci-full-template)

1. Follow the CI Full template link
2. On the right side click the button label 'Use this Template*
3. Select Create New Repository
4. Add a repository name and choose if you would like it public or private
5. Click on 'Create Repository'
6. The new repository is now created

### Github Desktop

Github desktop was used to create a local copy of this repository.

1. In the Github Desktop app select 'file'
2. Select 'clone repository'
3. Navigate to the Github tab and select the repository you created using the CI Template.
4. The repository will be loaded to your computer
    - You will be able to view any changes before you do your next commit.

### Heroku
Deployment to Heroku was completed using the following steps:

1. Update your requirements.txt file by entering entering the below into the terminal:
    - Run pip3 freeze > requirements.txt'.
    - Set debug to 'False' in the project settings
    - Commit and push the changes to Github.
2. Log in to Heroku and select New / Create new app.
    - Create an app name and select your region. 
    - Click Create App to continue.
3. Navigate to the Settings tab locate the ConfigVars section.
    - Click Reveal ConfigVars and add the following information:
    - KEY = 'DATABASE_URL', VALUE = Copy and paste the contents from the env.py file.
    - KEY = 'SECRET_KEY', VALUE = Add a confidential key/password set.
    - Click Add after entering each ConfigVar.
4. Within Settings, locate Buildpacks section.
    - Click Add Buildpack and add the following buildpacks:
    - Add Python and click Add Buildpack.
5. Go to Deploy tab and complete the deployment details.
    - Select GitHub as the Deployment Method.
    - Connect to GitHub and locate your repository and select Connect.
    - Select either to Automatic Deploy or Manual Deploy your and click Deploy Branch.
6. Once deployed, select open app to view the deployed project.

- The live link is [ProManager](https://pro-manager-10b4d100221c.herokuapp.com/)


- - -

## Testing

Please refer to [TESTING.md](TESTING.md) file for all testing carried out.

### Solved Bugs


### Known Bugs


- - -

## Credits

### Code Used


### Content


### Media


### Acknowledgments

