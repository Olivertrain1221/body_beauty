#### Validator Testing
Please see below the validation for each page

*

#### Notable Bugs

Development bugs: One major bug i experienced was when i was linking the authors profile image to the post, opposed to the profile image of someone logged in. You would have thought a simple fix upon changing the models but was being presented with an error, on the live site when trying to create a use as well from then on, this was found to be due to the database crashing in some form. It was handing out the same UUID in the fault code presented to myself and my mentor. Upon a final decision to revert back, it still did not work. This then resulted in the database crashing in some form. When navigating through Heroku we found in their latest update they had released a “Reset” button on the postgres database. After a simple 10 seconds the database had reset but left the table.
There are no known bugs left in the site.