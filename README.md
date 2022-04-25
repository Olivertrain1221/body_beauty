# Body Beauty

## Introduction
Body Beauty is a website built in Django using Python, JavaScript, CSS and HTML. It is a site that allows a user to to see and share the Tattoo artists work at that store from real time users due to it having a built in blog. Users are able to create posts for the world to see. along with there own profile!

This is My(Oliver Train) fourth project for the Code Institute Diploma in Software Development with eCommerce.

The site provides role based permissions for users to interact with a central dataset. It includes user authentication, email validation, and Full CRUD functionality for there posts and User Profiles.

![Screenshot of homepage]()

[View the live website on Heroku]()

Please note: To open any links in this document in a new browser tab, please press CTRL + Click.

## Table of Contents
* [User Experience Design (UX)](#UX)
    * [The Strategy Plane](#The-Strategy-Plane)
        * [Site Goals](#Site-Goals)
        * [Epics](#Epics)
        * [User Stories](#User-Stories)
    * [The Scope Plane](#The-Scope-Plane)
    * [The Structure Plane](#The-Structure-Plane)
        * [Opportunities](#Opportunities)
    * [The Skeleton Plane](#The-Skeleton-Plane)
        * [Wireframes](#Wireframe-mockups)
        * [Database Schema](#Database-Schema)
    * [The Surface Plane](#The-Surface-Plane)
* [Features](#features)
* [Future Enhancements](#future-enhancements)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## UX
### The Strategy Plane
*  Body Beauty is intended to be a friendly site for users to create and share their own Tattoos with others in the sociable gallery page. Users will also be able to add, delete there own posts and view all the tattoos created by tattoo artists and current artists works from the shop.

##### The Sites Ideal User
* Tattoo artists wanting to share there tattoos
* Someone looking to get inspiration over there tattoos
* Someone looking to share there own tattoos to the world

#### Site Goals

* To provide business owner more business due to advertisement via posts
* To provide users with a place to share their own Tattoos
* To provide users with a place to discover new tattoos and gain inspiration to a potential new idea

#### Epics

5 Epics were created which were then further developed into 13 User Stories. The details on each epic, along with the user stories linked to each one can be found in the project kanban board [here](https://github.com/Olivertrain1221/body_beauty/projects/1)

1. Initial Django setup [#1](https://github.com/Olivertrain1221/body_beauty/issues/3)
2. Account Creation [#2](https://github.com/Olivertrain1221/body_beauty/issues/4)
2. Account Login [#3](https://github.com/Olivertrain1221/body_beauty/issues/5)
2. User Posts [#4](https://github.com/Olivertrain1221/body_beauty/issues/6)
2. Edit/delete Users Posts [#5](https://github.com/Olivertrain1221/body_beauty/issues/7)

### User Stories

From the Epics, 13 User Stories were developed. Each story was then given also  was assigned a classification of Must-Have, Should-Have, Could-Have. Each story was also assigned its own points that could be broken further this allowed me the chance to understand how the site was developing and also allow time planning which I consistently tried to work toward.

python3 -m http.servergit pushgit pushgit commit -m "git commit -m "git commit -mg i"t push
These are the user stories that were completed within the project's first release, by Epic.

	* US#8 - As a User, I can create a login to the site so that I can move around the site and look at the images and posts from various other users.
	* US#1 - As a User, I can Navigate successfully around the site so that the User experience is rewarding.
	* US#2 - As a User, I can Post images to a user gallery of my tattoos so that they can be shared with others.
	
	* US#8 - As a User I can Create a login to the site so that I can move around the site and look at the corresponding images posted by users**
	* US#9 - As a User I can see whether I am currently logged in to the site and also create an account if not registered so that I can use the site to its full potential
	* US#10 - As a User I can view my profile and delete my profile so that I have control of my own account
	* US#11 - As a User I can Change my password so that If I forget my password I will be able to change it to continue accessing the site
	* US#12 - As a User I can Logout so that I can exit the site knowing my account is safe
	* US#13 - As a User I can use other trusted sites with a login/autofill. GMAIL, Facebook, YouTube so that Easy signup easy encouragement
	* US#14 - As a User I can View all the photos of the tattoos so that I can get influence and exposure to new tattoos
	* US#15 - As a User I can like pictures that others post so that I can then keep a record of what I liked
	* US#16 - As a User I can Search so that I can see images from most recent to oldest first.
	* US#17 - As a User I can Ensure that what I will see is suitable for the website so that I feel comfortable
	* US#18 - As a User I can view the site on my laptop and Iphone so that I can keep looking at potential tattoos

### The Scope Plane

**Features planned:**
* User Profile - Create, Read, Update and Delete (Basic CRUD functionality)
* Posts - Users can create, update and delete their own posts onto the site 
* Other Users Posts - Users can see and look at the other posts that users have shared
* Users can login to their account, change their password or their email and profile image
* Users can reset their password if they forget it.
* Users can logout of their account
* Users need to be registered and logged in to be able to post and contribute to the gallery page
* Responsive Design - the site needs to be fully responsive so the site can be checked and contributed to by users with various devices.


### The Structure Plane

The Structure Plane was modeled upon the user stories for the site. Each user story had a clear and concise objective towards the successful completion of the site you can find each of the Stories is listed above, If you would like to also read the Acceptance criteria that were written to try and ensure that the User’s Story is met and nothing is missed at what is required to meet this. I also wrote out the implementation of what was done in order for it to be successful within the project. 

The above Acceptance Criteria and Implementation process followed can be read and viewed on my Github within the [issues](https://github.com/Olivertrain1221/body_beauty/issues) tab of the project.

#### Opportunities

Arising from user stories
| Opportunities | Importance | Viability / Feasibility
| ------ | :------: | :------: |
| ** Provide users the ability to create an account ** | 5 | 5 |
| ** Provide users the ability to create a post ** | 5 | 5 |
| ** Provide users the ability to edit a post ** | 5 | 5 |
| ** Provide users the ability to view posts ** | 5 | 5 |
| ** Provide users the ability to delete their own posts ** | 5 | 5 |
| ** Provide users the ability to edit their account ** | 5 | 5 |
| ** Provide users the ability to delete their account ** | 5 | 5 |
| ** Provide users the ability to access the site on any device ** | 5 | 5 |


### The Skeleton Plane
#### Wireframe mock-ups

Home page: The home page provides the user with a clear and welcoming page to the site and allows users to understand quickly the overall purpose of the site. The welcome message is clearly visible to the user when they first arrive at the site regardless of the device they are using. ![Recipe Detail Desktop Wireframe]()

![Home Page Wireframe]()

About page: The about page sheds some history and information regarding the shop and also gives the user the chance to learn about what the shop and the overall site have to offer to users.

![About Page Wireframe]()

Users also have the ability to sign up to the site which automatically creates a profile for them. From this profile, users can change any of the information they originally supplied upon signup, also allowing them to add a profile image.

![User Profile Desktop Wireframe]()

Users that aren't registered with the site have the ability to view any posts made by other users which are displayed on the sites ‘gallery’. The posts are shown from newest to oldest so users have a constant relay of fresh posts.

![Gallery Page not Registered desktop wireframe]()

Users that are registered with the site have the extra ability to share their own posts to the site for other users to view.


Wireframes were also produced for the main major pages for the idealistic mobile view, for both mobile and tablet devices. With the intention of the site being fully responsive so that no matter the device size the user is viewing the site on, it will display accordingly.

#### Database Schema

As predicted when making a django site, certain custom models are required to be made in order for the site to work. I spent time thinking about what would be required in the models for the site to work smoothly as well as the type of relationships required between them

In order for the users of the site to be able to create Tattoo Posts and share there ideas and designs, a members model was also required for the posts and also a users for the logging in which was linked.

![Database Schema Diagram]()

### The Surface Plane

#### Design

Once I had basic page functionality and had things displaying on the pages I began to style my wireframes. A few changes happened during development that means the gallery page is also given a detail page, this shows the full user's bio on that particular post and also allows the user to be able to delete it. I ensured that the color themes were accessible to all of the users that may visit the site.

##### Typography 
Comin Neue was my chosen font for the sites page due to it being a nice clear precise font and made it easier to read for all users the colors used were a white 

##### Images
Several images that were used were on the pexels website, I used select images to fit into shop itself.

## Features
#### Home page
A welcoming homepage was built to welcome the user to the site and clearly convey the sites purpose. The call to action for the user to search for recipes is at the top of the main page, with a large, hero like welcome message appearing just below. At the bottom of the page a clear comparison showing users the benefits of signing up to the site is displayed.

![Home Page](

#### Navigation Bar
The main navigation bar appears at the top of the page, clearly displaying the main navigational links users would require.

![Logged in User Nav Bar]()


A user is given an option to login at the top of the screen and then changes to the logout depending on the current state of the user.

The Users that are not logged in are able to access the gallery still however don't have the option to post their photos and images to the site. 

![logged in user nave bar user menu open]()

The navigation bar and the user menu are fully responsive, adapting to narrower devices by appearing from the right hand side of the screen when the menu button is pressed.

![mobile user menu open]()

#### Footer
A normal common footer was used throughout the site as part of the base.html , this allowed the site to flow and also look neat.

![footer]()


#### Tattoo Posts Cards
When on the gallery page the posts are shown in a card format this allows a unison way of posts and allows the user to post any size image and for it to be scaled accordingly. 

##### Standard Gallery Post Card
![Standard Galler Post Card]()

##### Selected Individual Post
![Selected Post]()


#### User Profile
Users have the choice to add to there profile. When a User creates a login and profile is already made for them and they are given editable fields they are not supplied a profile image until they upload one. The user profile page provides the profile owner with quick access to edit and delete functionality.

![Users Profile Page]()


#### Editing a Post
From the gallery page, should they choose an image they like, they can then click the post and it will take them to the post and display more detail with a full bio, opposed to the smaller blurb given on the main gallery page.
## Future Enhancements
There are many key enhancement that as my knowledge explands i would love to introduce into this site. Some of the key enhancements I want to add are listed below. These enhancements will help to create a much more sophisticated site.
The key areas I would like to add to the site in the future are:
* The ability for users to search the sites gallery page for images they want
* The ability for users to comment on posts and share their thoughts onto the tattoos.
* The ability for users to login via social networks such as google or facebook

## Testing

### Testing Strategy
When testing my site i proceeded to use the “manual testing” procedure as I found this the easiest way to understand and ensure competent testing is carried out. The tests carried out can be seen below.


#### Testing Overview

When testing this Project I divided it into different sections this was done therefor to ensure that basic test were written and validated within what the terms of the code was written for.

[My testing overvie]()

A full detailed breakdown of the testing procedures and methodology can be found in the testing.md file [here](TESTING.md)

#### Validator Testing
All of my code was Passed validation but had 0 warnings.
*ADD WARNINGS

#### Notable Bugs

Development bugs: One major bug i experienced was when i was linking the authors profile image to the post, opposed to the profile image of someone logged in. You would have thought a simple fix upon changing the models but was being presented with an error, on the live site when trying to create a use as well from then on, this was found to be due to the database crashing in some form. It was handing out the same UUID in the fault code presented to myself and my mentor. Upon a final decision to revert back, it still did not work. This then resulted in the database crashing in some form. When navigating through Heroku we found in their latest update they had released a “Reset” button on the postgres database. After a simple 10 seconds the database had reset but left the table.
There are no known bugs left in the site.

#### Technologies Used

* Python
    * The following python modules were used on this project:
* asgiref==3.5.0
* astroid==2.9.3
* certifi==2021.10.8
* charset-normalizer==2.0.12
* cloudinary==1.29.0
* colorama==0.4.4
* dj-database-url==0.5.0
* dj3-cloudinary-storage==0.0.6
* Django==3.2
* django-crispy-forms==1.14.0
* gunicorn==20.1.0
* idna==3.3
* isort==5.10.1
* lazy-object-proxy==1.7.1
* mccabe==0.6.1
* Pillow==9.0.1
* platformdirs==2.5.1
* psycopg2==2.9.3
* pylint==2.12.2
* pytz==2021.3
* requests==2.27.1
* six==1.16.0
* sqlparse==0.4.2
* toml==0.10.2
* urllib3==1.26.8
* wrapt==1.13.3

* Django
    * Django was used as the main python framework in the development of this project
    * Django AllAuth was utilised to provide enhanced user account management functionality.
* Heroku
    * Was used as the cloud based platform to deploy the site on
* Heroku PostgreSQL
    * Heroku PostgreSQL was used as the database for this project during development and in production.
* JavaScript
    *   Various Scripts for website functionality
*  Bootstrap 5.13
    * Bootstrap was used for general layout and spacing requirements for the site.
* Font Awesome
