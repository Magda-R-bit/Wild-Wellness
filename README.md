# **Wild Wellness**

[Project live link](https://wild-wellness-c99e47528d25.herokuapp.com/)


![Screenshot of Main Page](https://res.cloudinary.com/drrjh78y3/image/upload/v1741048761/responsiveness_tez65j.png)

 **Wild Wellness**  is a platform designed to help people reconnect with nature through wellness retreats, outdoor adventures, and cozy cabin stays. Whether you're looking to relax, meditate, or go on an adventurous journey surrounded by wildlife, Wild Wellness offers a variety of activities to recharge and rejuvenate the mind, body, and spirit.

 This website is designed for nature enthusiasts, wellness seekers, and anyone in need of a peaceful getaway. It's perfect for those who want to escape from the stresses of modern life, and their routine, and experience the healing powers of nature.


## Contents

* [UI/UX](#uiux) 
* [Features](#features)
* [Design](#design)
* [Technologies](#technologies)
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

- User authentication with Django Allauth (signup, login, logout).
- Responsive UI with Bootstrap 5.
- Booking system with availability validation.
- Review system with modals for easy editing.
- **CRUD** Functionality:
  - Bookings – Users can create, view, update, and delete their bookings.
  - Cabins – Admins can manage available cabins.
  - Reviews – Users can add, edit, and delete their feedback. Admin can approve or delete review.


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

#### **404 Error Page**

![404 Error](https://res.cloudinary.com/drrjh78y3/image/upload/v1741839451/404Error_tkm4fl.png)


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

* Testing for layout and functionality completed on the below browser:
  - Chrome ✅
  - Edge ✅
  - FireFox ✅
  - DuckDuckGo ✅

* For more manual tests please refer to [Manual Testing](TESTING.md)


### Automated Tests

* Automated test created for booking app to test app functionality. All tests ok, no errors found.

![Model Test](https://res.cloudinary.com/drrjh78y3/image/upload/v1741820711/ModelTest_fihgkt.png)
![Form Test](https://res.cloudinary.com/drrjh78y3/image/upload/v1741821543/FormTest_gklfmh.png)
![Form Test 2](https://res.cloudinary.com/drrjh78y3/image/upload/v1741820957/FormTest2_v7cg1q.png)
![Views Test](https://res.cloudinary.com/drrjh78y3/image/upload/v1741821066/ViewsTest_u916c1.png)
![View Test 2](https://res.cloudinary.com/drrjh78y3/image/upload/v1741821210/ViewTest2_rhucdc.png)
![View Test 3](https://res.cloudinary.com/drrjh78y3/image/upload/v1741821308/ViewTest3_gzzbdl.png)


* Tests Results

![Tests Results](https://res.cloudinary.com/drrjh78y3/image/upload/v1741821789/TestResults_hszfua.png)

### Validation

- [HTML Validator](https://validator.w3.org/)

base.html

![Base HTML](https://res.cloudinary.com/drrjh78y3/image/upload/v1741830441/BaseHTML_ggmjc4.png)

index.html

![Home Page](https://res.cloudinary.com/drrjh78y3/image/upload/v1741830468/ValidatorHomePage_ec7w3x.png)

header.html

![Navbar HTML](https://res.cloudinary.com/drrjh78y3/image/upload/v1741831238/ValidatorNavbar_zxpvvz.png)

footer.html

![Footer  HTML](https://res.cloudinary.com/drrjh78y3/image/upload/v1741832239/ValidatorFooter_yvbc68.png)

404.html

![Error Page](https://res.cloudinary.com/drrjh78y3/image/upload/v1741830461/ValidatorError_exstc8.png)


- [CSS Validator](https://validator.w3.org/#validate_by_input)

![Base CSS](https://res.cloudinary.com/drrjh78y3/image/upload/v1741830448/CSSValidator_yjwggh.png)

#### Python 

To maintain clean, readable, and PEP8 compliant code throughout the project:
   - [Black](https://pypi.org/project/black/) was used as an automatic code formatter. Since the project contains multiple Python files, Black ensured consistency and adherence to PEP8 standards across all files.
   - [Flake8](https://flake8.pycqa.org/en/latest/) was used as a Python linter to check for potencial errors and enforce coding standards.

Special attention was given to views.py files for cabins and booking apps to ensure high quality code, so double checked these files with 
[CI Python Linter](https://pep8ci.herokuapp.com/)

![Cabins Views](https://res.cloudinary.com/drrjh78y3/image/upload/v1741823131/CabinsViews_v70gsf.png)

![Booking Views](https://res.cloudinary.com/drrjh78y3/image/upload/v1741823143/BookingsViews_popmrq.png)


#### Lighthouse Testing

Mobile

![Lighthouse Mobile](https://res.cloudinary.com/drrjh78y3/image/upload/v1741825581/LighthouseMobile_k49rln.png)

Desktop

![Lighthouse Desktop](https://res.cloudinary.com/drrjh78y3/image/upload/v1741825297/LightHouse_qngxmz.png)


## Bugs

### Fixed Bugs

1. Modal for Updating Reviews did not work

   * Issue: The update review modal was not functioning properly, preventing users from editing their reviews.
   * Fix: Fixed the form submission method inside the modal and ensured the correct review ID was passed to update the right review.

2. Booking Form overlapping validation did not work

   * Issue: The form was incorrectly flagging valid booking updates as overlapping. When a user tried to adjust their booking (e.g., shorten the stay), the system incorrectly rejected the update.
   * Fix: Adjusted the overlapping booking validation logic in forms.py to exclude the current booking instance when checking for conflicts.

3. Booking List View Test failed

   * Issue: The test cases for booking views were failing due to image handling by ResizedImageField and Cloudinary
   * Fix: Adjusted the test setup to exclude image validation when testing views. This ensured that tests didn't attempt to access Cloudinary stored images.

4. Static Files did not load in Deployment (WhiteNoise Issue)

   * Issue: CSS and JavaScript files were not loading correctly after deployment.
   * Fix: Configured WhiteNoise in settings.py and made sure collectstatic was running properly.



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
  - Go to *Config Vars*, click *Reveal Config Vars*, and add the KEY, and the VALUE for Database, Cloudinary and Secret Key. Click *add*
  - Go to VS Code project settings and allow Heroku as a host (ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost'])
  - Navigate to the *Deploy* tab at the top
  - Click *GitHub*, then *Connect to GitHub*
  - Search for the repository you want to deploy and click *connect*
  - Select *Enable Automatic Deploys* or *Deploy Branch*

[Link to deployed project](https://wild-wellness-c99e47528d25.herokuapp.com/)

### How to clone the repository

- Go to the https://github.com/Magda-R-bit/Wild-Wellness reposotory on GitHub
- Click on the Code button located above the project files
- Select HTTPS and copy the repository link
- Open your work environment, type *git clone* and paste the copied Git URL and press Enter
- The project is now created as a local clone

### How to Fork the repository

- Log into GitHub and click on repository to download ([Wild-Wellness](https://github.com/Magda-R-bit/Wild-Wellness))
- Click the **Fork** button in the top right-hand corner
- Click **Create Fork**
- The repository is now in your chosen account and can be cloned or changed

## Credits

 - **Special Thanks**:
   - **Spencer Barriball**- For your mentorship. Your insights and advices were crucial to the success of this project
 - *ChatGPT-4* - For creating Cabins description and debugging
 -  Slack Community - For helping me solving issues with settings

### Inspiration

- [w3schools](https://www.w3schools.com/howto/howto_css_modals.asp)
- [stackoverflow](https://stackoverflow.com/)
- [I Think Therefore I Blog Walkthrough Project](https://github.com/Magda-R-bit/django-blog)
- [Dee Mc](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=1)
- [DarshanDev](https://www.youtube.com/watch?v=9NcIXkp1Tmo&list=PL_6Ho1hjJirn8WbY4xfVUAlcn51E4cSbY&index=8
)
- Antonio Melé: ["Django 5 By Example"](https://books.google.ie/books/about/Django_5_By_Example.html?id=P-AEEQAAQBAJ&redir_esc=y)

### Media

- [Leonardo AI](https://leonardo.ai/) Used for creating Cabins images
- [Unsplash](https://unsplash.com/s/photos/wild-nature) Used for images in the Home Page
- [Canva](https://www.canva.com/logos/) Used for creating Logo
- [Favicon](https://favicon.io/) Used for generating favicon
