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

#### 
#### Notable Bugs

Development bugs: One major bug i experienced was when i was linking the authors profile image to the post, opposed to the profile image of someone logged in. You would have thought a simple fix upon changing the models but was being presented with an error, on the live site when trying to create a use as well from then on, this was found to be due to the database crashing in some form. It was handing out the same UUID in the fault code presented to myself and my mentor. Upon a final decision to revert back, it still did not work. This then resulted in the database crashing in some form. When navigating through Heroku we found in their latest update they had released a “Reset” button on the postgres database. After a simple 10 seconds the database had reset but left the table.
There are no known bugs left in the site.