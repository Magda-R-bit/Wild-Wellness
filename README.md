# **Wild Wellness**

[Project live link](https://wild-wellness-c99e47528d25.herokuapp.com/)


![Screenshot of Main Page](https://res.cloudinary.com/drrjh78y3/image/upload/v1741048761/responsiveness_tez65j.png)

 **Wild Wellness**  is a platform designed to help people reconnect with nature through wellness retreats, outdoor adventures, and cozy cabin stays. Whether you're looking to relax, meditate, or go on an adventurous journey surrounded by wildlife, Wild Wellness offers a variety of activities to recharge and rejuvenate the mind, body, and spirit.

 This website is designed for nature enthusiasts, wellness seekers, and anyone in need of a peaceful getaway. It's perfect for those who want to escape from the stresses of modern life, and their routine, and experience the healing powers of nature.


## Contents

* [UI/UX](#uiux) 
* [Features](#features)
* [Design](#design)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)


## UI/UX

### User Interface (UI) and Experience (UX)

 ### Agile

  Wild Wellness was built using **Agile** approach, allowing me to stay flexible and deliver features in incremental steps. I followed Agile principles to manage tasks and ensure continuous improvement throughout development.

  To keep track of tasks and progress, I used a **Kanban board** to visually organize work, monitor the flow of tasks, and ensure that each feature was delivered efficiently.

  1. Sprint Planning:

  - I planned my tasks in short sprints, typically lasting 1-2 weeks, to stay focused on specific goals. I focused first on functionality of my project. Each sprint would target the development of core features, like user authentication, checking cabin availability, booking system and view of booking list, updating and deleting booking.

  

  2. Kanban Board:

  -  I created [GitHub Project](https://github.com/users/Magda-R-bit/projects/5) to help me manage tasks by moving them trough various stages from To Do, to In Progress, and finally to Done.


  ![Screenshot of Kanban Board](https://res.cloudinary.com/drrjh78y3/image/upload/v1741787010/KanbanBoard_qbpeo7.png)
  ![Issue](https://res.cloudinary.com/drrjh78y3/image/upload/v1741787297/Issue_l7fisy.png)


### Wireframes

- [Figma](https://www.figma.com/) (Used to create Wireframes)

![Screenshot of Wireframes Home](https://res.cloudinary.com/drrjh78y3/image/upload/v1741697759/WireframeHome_tgycot.png)
![Screenshot of Wireframes Cabin](https://res.cloudinary.com/drrjh78y3/image/upload/v1741697846/WireframeCabins_hxpl8k.png)


### ERD Diagram

- [Graphviz](https://graphviz.gitlab.io/download/) (ERD Generated using django-extensions and Graphviz to visualize the relationships between the models and improve the understanding of the database structure)

![Screenshot of ERD](static/images/ReadMe/erd.png)


### Design

#### Colour:

The primary colours chosen for this website are green: rgb(17, 107, 54) and light-green: rgb(164, 224, 164), for its association with nature, health, and well being.

Green is often associated with relaxation and harmony, which aligns perfectly with the theme of wellness and self-care.

![Navbar](https://res.cloudinary.com/drrjh78y3/image/upload/v1741789254/NavbarColor_tj8zrc.png)
![Buttons](https://res.cloudinary.com/drrjh78y3/image/upload/v1741789247/ButtonColor_qc48yy.png)




## Features


### Existing Features

#### **Navigation**
- Responsive Navbar with burger dropdown manu
- Navigation options depend of user authentication

![Navbar](https://res.cloudinary.com/drrjh78y3/image/upload/v1741791308/Navbar_ghht8b.png)
![Burger](https://res.cloudinary.com/drrjh78y3/image/upload/v1741791312/Burger_qwubfk.png)

#### **Footer**

- Responsive Footer with social media links and address

![Footer Full](https://res.cloudinary.com/drrjh78y3/image/upload/v1741791738/FooterFull_bkxp20.png)
![Footer](https://res.cloudinary.com/drrjh78y3/image/upload/v1741791763/Footer_yvfwdu.png)



####  **Home Page**

##### User can start photo slider by clicking on the image

 ![Home Page](https://res.cloudinary.com/drrjh78y3/image/upload/v1741051889/HomePage_oybakv.png)

####  **Check Availability Form**



![Form](https://res.cloudinary.com/drrjh78y3/image/upload/v1741052056/Availabilities_cdhagw.png)

####  **Cabins**



![Cabins](https://res.cloudinary.com/drrjh78y3/image/upload/v1741052173/Cabins_suxwuw.png)


#### **Sunset View**


![Sunset View](https://res.cloudinary.com/drrjh78y3/image/upload/v1741052372/SunsetView_ergvv6.png)
![Sunset View](https://res.cloudinary.com/drrjh78y3/image/upload/v1741052713/SunsetFeautures_ckmynj.png)

#### **Lake View**



![Lake View](https://res.cloudinary.com/drrjh78y3/image/upload/v1741052574/LakeView_bk80lh.png)
![Lake View](https://res.cloudinary.com/drrjh78y3/image/upload/v1741052610/LakeFeautures_ftspre.png)


#### **Wild View**


![Wild View](https://res.cloudinary.com/drrjh78y3/image/upload/v1741052922/WildView_mobnhw.png)
![Wild View](https://res.cloudinary.com/drrjh78y3/image/upload/v1741052984/WildFeautures_tvejm9.png)


#### **Reviews**

##### Reviews Form

![Reviews Form](https://res.cloudinary.com/drrjh78y3/image/upload/v1741053349/ReviewForm_gbs5wh.png)

##### Reviews approved by admin

![Reviews approved](https://res.cloudinary.com/drrjh78y3/image/upload/v1741053110/Reviews_ltmqko.png)

#### Reviews pending admin's approval

![Reviews](https://res.cloudinary.com/drrjh78y3/image/upload/v1741053505/ReviewPending_khdd8u.png)

#### **Register Form**

![Register](https://res.cloudinary.com/drrjh78y3/image/upload/v1741053732/RegisterForm_afofb5.png)


#### **Log in Form**

![Log in](https://res.cloudinary.com/drrjh78y3/image/upload/v1741053899/LogIn_k0au2y.png)

#### **My Bookings**

##### Booking list with FullCalendar visability of unavailable dates marked in red

![Booking List](https://res.cloudinary.com/drrjh78y3/image/upload/v1741054068/MyBookings_noraoq.png)


#### **Update Booking**

![Booking Update Form](https://res.cloudinary.com/drrjh78y3/image/upload/v1741054282/UpdateBooking_whhkvv.png)

#### **Delete Booking**

![Delete Booking](https://res.cloudinary.com/drrjh78y3/image/upload/v1741054389/DeleteBooking_ytyttz.png)


#### **New Booking**

![Booking Form](https://res.cloudinary.com/drrjh78y3/image/upload/v1741054489/NewBooking_uku7y7.png)


#### **Log Out**

![Logout Form](https://res.cloudinary.com/drrjh78y3/image/upload/v1741054584/Logout_voo20h.png)


### Future Features:

- Create Treatments app.
- Create Meals app.



## Technologies

### Language

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Framework

- [Django](https://www.djangoproject.com/)

### Database

- [PostgreSQL](https://www.postgresql.org/)

### Frontend
- [HTML](https://en.wikipedia.org/wiki/HTML) (Used to structure the content and pages of the application. HTML templates are used to display dynamic data in the frontend)
- [CSS](https://en.wikipedia.org/wiki/HTML) (Used for styling the application)
   - [Bootstrap 5](https://getbootstrap.com/) (Used for styling, layout, and modals)

### Backend and Server Tools

- [Gunicorn](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/gunicorn/) (Python HTTP server for WSGI applications)
- [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) (Serves static files efficiently in production)


### Django Libraries

- [django-allauth](https://django-allauth.readthedocs.io/en/latest/) (User authentication)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) (Control the rendering behaviour of Django forms)
- [crispy-bootstrap5](https://pypi.org/project/crispy-bootstrap5/) (Support for crispy forms)
- [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/) (Manages media and static files)
- [django-resized](https://pypi.org/project/django-resized/) (Optimizes image resizing)
- [django-richtextfield](https://pypi.org/project/django-richtextfield/) (Provides rich text editing, used in the admin for creating cabin descriptions)
- [django-extensions](https://django-extensions.readthedocs.io/en/latest/) (Provides additional management commands, including graph_models for generating Entity Relationship Diagrams (ERD))


### Development & Code Formatting

- [Pillow](https://pypi.org/project/Pillow/) (Python Imaging Library)
- [Black](https://pypi.org/project/black/) (Python code formatter)
- [Flake8](https://flake8.pycqa.org/en/latest/) (Python linter used for python code validation)


### Deployment & Hosting

- [GitHub](https://github.com/Magda-R-bit) ( Repository hosting service used for version control)
- [Heroku](https://help.heroku.com/) (Cloud platform where project was deployed)
- [Cloudinary](https://cloudinary.com/) (Cloud storage for images)


### Development Environment

- [Visual Studio Code (VS Code)](https://code.visualstudio.com/) (Main code editor used for writing and testing this project)
- [Gitpod](https://www.gitpod.io/) (Online development environment for coding and testing)



## Testing
  
### Manual Tests and Results

* Testing completed on the below browser:
  - Chrome
  - Edge
  - FireFox
  - DuckDuckGo




### Validation

- [HTML Validator]()

![Screenshot of html test]()

- [CSS Validator]()

![Screenshot of css test]()

- Lighthouse Testing

![Lighthouse Testing]()

## Bugs



### Unfixed Bugs

* No unfixed bugs.

## Deployment

### Version Control

* The project was developed using the [Code Institute Template](https://github.com/Code-Institute-Org/p3-template), the Gitpod editor, and was pushed to GitHub in the remote repository Wild-Wellness.
* Git commands were used to push the code to the repository.

### Deployment to Heroku

* The project was deployed to Heroku with the following steps:
  - Create an account and log in to Heroku
  - Go to the dashboard, click *New*, then *Create new app*
  - Navigate to *Settings*
  - Go to *Config Vars*, click *Reveal Config Vars*, and add the KEY, and the VALUE. Click *add*
  - Go to *Buildpacks*, then click *Add buildpack*, in the following order:
    - Select *python* and click *Add Buildpack*
    - Select *nodejs* and click *Add Buildpack*
  - Navigate to the *Deploy* tab at the top
  - Click *GitHub*, then *Connect to GitHub*
  - Search for the repository you want to deploy and click *connect*
  - Select *Enable Automatic Deploys* or *Deploy Branch*

[Link to deployed project]()

### How to clone the repository

- Go to the https://github.com/Magda-R-bit/Chef_Secret_Recipes reposotory on GitHub
- Click on the Code button located above the project files
- Select HTTPS and copy the repository link
- Open your IDE, and paste the copied Git URL into the IDE terminal
- The project is now created as a local clone


## Credits

 - **Special Thanks**:
   - **Spencer Barriball**- For your mentorship. Your insights and advices were crucial to the success of this project.

### Inspiration

- [w3schools](https://www.w3schools.com/howto/howto_css_modals.asp)
- [stackoverflow](https://stackoverflow.com/)
- [I Think Therefore I Blog Walkthrough Project](https://github.com/Magda-R-bit/django-blog)
- [Dee Mc](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=1)
- Antonio Melé: "Django 5 By Example"

