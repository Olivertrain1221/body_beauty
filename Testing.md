#### Validator Testing
Please see below the validation for each page

#### HTML Using Validator W3.org
* Home page 0 errors, 0 warnings
* About page 0 errors, 0 warning
* Gallery page 1 error An img element must have an alt attribute, except under certain conditions. (Condition met due to it being import from cloudinary)
* Individual Post page 1 error An img element must have an alt attribute, except under certain conditions. (Condition met due to it being import from cloudinary)
* Profile page 1 error An img element must have an alt attribute, except under certain conditions. (Condition met due to it being import from cloudinary)
* Login page 0 errors, 0 warning
* Signup page 1 error, 0 warning Element ul not allowed as child of element small in this context, except under certain conditions. (Condition met due to it being import from built in Django framework)
* Logout page 0 errors, 0 warning


#### CSS Validator
After running the CSS through my autoprefixer at [here](https://autoprefixer.github.io/) I ran the code then through a validator where I was greeted with A no error found message and 64 warnings due to the autoprefixer changes.

[CSS validation](/documentation/testing/css_validator.png)

#### Python Validator
Due to Python requiring standards across the board i had to ensure that any code I had writted was up to the PEP8 guidelines. I ran my code through a online validator on all code I had written, with the exception of 2x line to long warnings my code passed. The code that was flagged as being too long were to do with linking my Cloudinary to the project. This is a allowable error I have been informed

[PEP8](http://pep8online.com/)

#### Lighthouse Report
I ran the built in chrome lighthouse report for my live site to test and ensure that it met minimum standards. The report came back as follows:
* Performance = 93%
* Accessibility = 97%
* Best Practices = 92%
* SEO = 90% 

[LightHouse Report](/documentation/testing/lighthouse_report.png)

#### Notable Bugs

Development bugs: One major bug i experienced was when i was linking the authors profile image to the post, opposed to the profile image of someone logged in. You would have thought a simple fix upon changing the models but was being presented with an error, on the live site when trying to create a use as well from then on, this was found to be due to the database crashing in some form. It was handing out the same UUID in the fault code presented to myself and my mentor. Upon a final decision to revert back, it still did not work. This then resulted in the database crashing in some form. When navigating through Heroku we found in their latest update they had released a “Reset” button on the postgres database. After a simple 10 seconds the database had reset but left the table.
There are no known bugs left in the site.

#### Manual Testing

When starting my testing I used Diagram drawn by myself to track what required testing around the site to ensure that I did not overlook or miss anything. Planning this way I found worked the best for continuity and to ensure that my testing was carried out in as many circumstance/scenarious as possible.
When testing I tested all of the sites features that have to be driven via the user
The variables taken into account when testing were as follows.

* Logged into the site
* Logged out of the site
* Profile Image submitted
* No profile Image
* Own personal post
* Other users posts

When starting my testing I started page by page as a user that wasnt logged in. I tried to take the "new user stance" and one thing I noticed straight away is the site didnt show me whereto signup this is reflected in my later commits where I added this as a UI fix

#### Nav-Bar
The nav bar was simple to test Starting on a mobile device i checked it worked with the smaller widget. I then proceeded to test on desktop and table.
The site behaved as expected upon testing all of the possible links and the logo on the site.

[nav-bar](/documentation/testing/test-docs/nav-bar.png)


#### Footer
The footer was simple to test again just testing the links all worked and took me to the correct page.

[footer](/documentation/testing/test-docs/footer.png)


#### Login/Signup
The site shows a login feature at the top in the nav bar as a new user to the site.
When clicking this button a option to login is displayed which shows the login view.
Within this view the option below the login form calls for the user to click the "Sign Up Now"
When clicking this it shows a form for the user to fill out.
Upon completion of this form and adhering to all of the standards it requires it will redirect to the login page.
This then can be filled out with prior or the new users details. 

[login](/documentation/testing/test-docs/)


#### Individual Cards of posts - (Unregistered View and not the Author of the post)
The individual cards of peoples posts was shown in the correct way with all the detail but missing two elements, shown in below test.

[card-unregistered](/documentation/testing/test-docs/individual-post-links-unregistered.png)


#### Individual Cards of posts - (Registered View + Posted)
The individual card will appear as above but will add two basic crud buttons an "edit" , "delete" buttons are shows to the user only if they are the one who made the posts.

[card-registered](/documentation/testing/test-docs/individual-post-links-registered.png)


#### Gallery Page
The gallery page Make a post functionality was requried to be tested, they way upon which it worked was if the user was not logged in it said "You need to log in to post" appose to when you were logged in "Make a post"
This can all be seen in these two test methods each one working correctyly either A redirect to the login page or B take to the form to complete to create a post.

[not-logged-in](/documentation/testing/test-docs/make-a-post-unregistered.png)

[not-logged-in](/documentation/testing/test-docs/make-a-post-registered.png)


#### Profile 
The profile is only able to be accessed via the link on the navbar when you are logged in. Only your profile is accessible and the profile is displayed autofilled out due to autocreation on signup.
This is therefore why it is displayed in editable fields in a form.
This allowed for basic crud functionality

[profile](/documentation/testing/test-docs/profile.png)




