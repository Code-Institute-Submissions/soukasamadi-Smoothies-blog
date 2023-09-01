# Smoothie Website - Introduction

This is my Project 4 for Code Institute Full-stack development program.
This project is a Full Stack website built using the Django framework. Smoothies Blog website is a smoothies recipe template where users can look for a healthy smoothie to prepare. The looged in Users can also 
like/unlike a post and leave comments on a post. They can also participate on our challenges and share their experience with other users.

[Find my Live Project Here !](https://smoothies-blog-fb8590efb21e.herokuapp.com/)

<p align="center" style="width:300px; heigth:500px"><img src="./assets/readme/readme-pictures/pages-screenshots/home-page.jpeg"
        alt="home page smoothies blog "></p>

Content Table

## User Experience - UX

### User Stories

* As a website user, I can:

1. Easily navigate around the site.
2. View a list of recipes and select a recipe to read.
3. Search for a specific recipe.
4. Open a post to read the details.
5. create an account to get the members features.
6. View the number of likes on a post.
7. View comments on a post.

* As logged in website user, I can:

1. Like and unlike recipes.
2. Comment on recipes.
3. Delete or edit my previous comments.
4. update my profile informations.
5. Share my experience with smoothies.
6. Edit or delete my previously experience.
7. Logout from the website.

* As a website superuser, I can:

1. Create and publish a new recipe.
2. Create draft recipe posts that can be reviewed and finalised later.
3. Create/Delete a new user, recipes, author and categories.
4. Approve user's comments.
5. Delete user's challenge that was posted previously.
6. Change the website permissions for a user.

### Agile Methodology

All functionality and development of this project were managed using GitHub which Projects can be found
[here](https://github.com/soukasamadi/Smoothies-blog/issues)

### The Scope

#### Main Site Goals

* To provide users with a good experience when using the website.
* To provide users with a visually pleasing website that is intuitive to use and easy to navigate.
* To provide a website with a clear purpose.
* To provide role-based permissions that allows user to interact with the website.

## Design

#### Colours

![Colours Palete](./assets/readme/readme-pictures/color-palette.jpg)<br>

* I choosed this colores to make the website simple and close to smoothies colores.
  
#### Typography

* "Josefin Sans" font is used as the main font for the whole website.

#### Imagery

* All the imagery is related to the recipes and website design.
The remaining imagery will be uploaded by the author to the database.


### Wireframes

I craeted a couple of wireframe to get a close idea about how the wesbite will look like.

![wirframe 1](./assets/readme/wireframes/wireframe2.jpg)
![wirframe 2](./assets/readme/wireframes/wirframe1.jpg)
![wirframe 3](./assets/readme/wireframes/wireframe3.jpg)


## Database Diagram

![Database Diagrama](./assets/readme/Simple_Smoothies_DataBase_Diagram.png)<br>

## Features

### Home Page

![Home Page](./assets/readme/readme-pictures/pages-screenshots/home-page.jpeg)

* The hero image welcomes the user with a short message advertising what the website is about. These
are 3 carousel images with a button. When the button is pressed, it brings the user down to the highlighted recipes.<br>

* In the latest recipes, users can see a selection of 6 recipes. These recipes are
chosen by the site admin by clicking the featured box in the post database.<br>

### About Page

![About Page](./assets/readme/readme-pictures/pages-screenshots/about-page.jpeg)

* The About Page gives, users information about the website. It tells the users the main pupose ofteh website <br>

### Blog Page

![Blog Page](./assets/readme/readme-pictures/pages-screenshots/blog-page.jpeg)

* On the Blog Page, users have access to the full recipes posts available on the website and they can also get more informations about smoothies and healthy meals routine.


### Recipe Detail Page 

![Post Detail Page - Top](./assets/readme/readme-pictures/pages-screenshots/post-details-page.jpeg)

* At this page users can discover the smoothie ingredients and get more information about the recipe.
* At the bottom of this page, users can read the comments posted by other users. If the user is logged in or is a 
superuser they have access to the buttons for deleting or updating comments.

### Edit Comments Page

![Edit Comments Page](./assets/readme/readme-pictures/pages-screenshots/edit-comment-page.jpeg)

* On this page, users are allowed to edit their own post comments.

### Contact Page

![Contact Page](./assets/readme/readme-pictures/pages-screenshots/contact-page.jpeg)<br><br>

* The Contact Page allows users to get access to smoothies website contact details and they can also send email using the contac form there.

### Categories Page

![Categories Page ](./assets/readme/readme-pictures/pages-screenshots/all-recipes-page.jpeg)<br><br>

* On the Categories Page, users can see the categories available in the blog and filter the posts by category.

### Categories Results

![Categories Results Page](./assets/readme/readme-pictures/pages-screenshots/categories-posts-page.jpeg)

* On the Categories posts Page, users can access the post filtered by the chosen category.
  
### challenge Page

![Challenge Page](./assets/readme/readme-pictures/pages-screenshots/challenge-page.jpeg)

* On this page, registered users candiscover other users experince. If they had already published 
  a post they are allowed to edit or delete their own posts

### Add Challenge Page

![Add Challenge Page](./assets/readme/readme-pictures/pages-screenshots/add-challenge-page.jpeg)

* On this page, registered users can fill out the form to add or edit a post with their favourite cookbooks.

### Search Page

![Search Page](./assets/readme/readme-pictures/pages-screenshots/search-page.PNG)

* In this page,  users can search by inputting a keyword in the search tool.

### Search Results Page

![Search Results Page](./assets/readme/readme-pictures/pages-screenshots/search-results-page.jpeg)

* On the Search Results Page, users can see the recipes found by their search.  When their recipe is located, the user can go to the 
  Post Details Page by clicking on the card result.

### Signup Page

![Signup Page](./assets/readme/readme-pictures/pages-screenshots/signup-page.jpeg)

* On the Signup Page, a new user can sign up for the website by filling out and then submitting the form.

### Login Page

![Login Page](./assets/readme/readme-pictures/pages-screenshots/login-page.jpeg)

* On the Login Page, users can log in to the website by inputting the username and password.

### Logout Page

![Logout Page](./assets/readme/readme-pictures/pages-screenshots/logout-page.jpeg)

* On the Logout Page, users can confirm the logout.

### User Profile Page

![User Profile Page](./assets/readme/readme-pictures/pages-screenshots/profile-page.jpeg)

* On the Profile Page, users can update their informations.

## Messages and Interaction With Users

* Some interactive messages were added to the project to make the navigation on the website easier and to improve the
user's experience.

### Sign up

![Sign up](./assets/readme/interactive-message/signed-up.jpeg)


### Login

![Login](./assets/readme/interactive-message/signed-in.jpeg)


### Logout

![Logout](./assets/readme/interactive-message/signed-out.jpeg)

### Profile Update

![Profile Update](./assets/readme/interactive-message/update-profile.jpeg)


### Like Post

![Like Post](./assets/readme/interactive-message/like-post.jpeg)


### Unlike Post

![Unlike Post](./assets/readme/interactive-message/unlike-post.jpeg)


### Comment Post

![Comment Post](./assets/readme/interactive-message/comment-awainting-approval.jpeg)

### Delete/Edit Comment

![Delete Comment](./assets/readme/interactive-message/delete-comment.jpeg)
![Delete Comment](./assets/readme/interactive-message/deleted-comment-success.jpeg)

### Edit Comment

![Edit Comment](./assets/readme/interactive-message/update-comment.jpeg)

### Email Sent - Success

![Email Sent - Success](./assets/readme/interactive-message/contact-success-email-sent.PNG)

### Email Sent - Failed

![Email Sent - Failed](./assets/readme/interactive-message/contact-something-went-wrong.PNG)

You can find all the interactive message [here](https://github.com/soukasamadi/Smoothies-blog/tree/main/assets/readme/interactive-message).


## Admin Panel/Superuser
![Admin Panel](./assets/readme/readme-pictures/pages-screenshots/admin-panel.jpeg)

* On the Admin Panel, as an admin/superuser I have full access to CRUD functionality so I can view, create, edit and
delete the following ones:

1. Recipes
2. Comments
3. Author
4. Categories
5. Profiles
6. challenges
   
* As superuser I can also approve comments, challenge#s posts and change the status and give other permissions to the users.<br>




  

