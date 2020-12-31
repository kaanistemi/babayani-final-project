<h1>babayani.lab</h1>
This platform is created to turn to website to e-commerce website, educate and entertain all cocktail-lovers, home-bar owners, professional bartenders & baristas or anyone who'd like to enjoy a cocktail today. Finding the recipe with true amounts
can sometimes be frustrating and there are very few websites dedicated to cocktail recipes only. This website makes it easier for users to search and find all the cocktail recipes they wish on just one page. 
The aim of the website is to provide users a platform where they can find cocktail recipes and create, share and edit their own cocktail recipes.

<h2>UX</h2>
User's have to log in/sign up in order to start using the platform, after they will be directed to the home page where they will be able to see all the cocktails. Picture and a little insight below the name is presented to introduce the coctails. By simply clicking on the cocktails picture, users will be able to see the type of the cocktail and the recipe; as divided into two subheads like "equipments" and “ingredients". If they wish, they will be able to edit or delete these details. 

The structure and navigation of the website is pretty straight-forward. The user can easily navigate through the home page and to other pages by using the nav-bar. On the "Add cocktail" section, they will be able to share their own recipe ideas with the other users. 

The user's primary goal would be easily searching and finding the complete cocktail recipes without no frustration, compare the recipes, ingredients and materials. So, the primary goal of the UX process of this website was to eliminate pain points, complications and interruptions as the other recipe websites have, and it has been made simpler for users to see the recipes with every important detail and being able to compare between them on the same page. This website would be the best way that the users can easily decide what they'll drink, learn new cocktails and how to do it or check what they are doing right or wrong with the cocktail. 

In addition to their primary goal, sharing their new ideas would be another goal of the users. If a user has any idea about the cocktail already given, or has a whole new cocktail recipe, he/she can easily edit the details or add new cocktail if they wish to.

User Story: A bartender would like to know if he does the tequila sunrise right or wrong after having a discussion with a customer. He needs a website that accurately shows the recipe of this cocktail, and approved by many. He logs in to website from his phone, searching for tequila sunrise on the home page. He clicks on the picture and see the ingredients, shows it to his customer and proves his point. However, the customer who likes making her own cocktails, insisting on her idea about making of this cocktail. She thinks it’s a great idea and wants to share it. She logs in to website from her phone, checks the other cocktails to get an insight and compare the recipes. Then, she adds a new cocktail with her own choice of ingredients and share it on the home page. 


<h2>Features</h2>

<h4>Existing Features</h4>

- Carousel and new arrivals category added to main page.

- Users can use coupon code as long as they register/login.

- Users can make a comment under products as long as they register/login.

- Users can get free delivey if they order over 100$.

- Login page directs users main page if login is succesfull. After login users can use coupon and comment under the product.

- Register page created for user who hasn't singed up yet. After succesful resgistiration user receives verification mail.

- There are 5 list item in mobile top header which are "babayani.lab" which directs you to home page, search button, call icon that directs you to babayani office on phone, My Account provide users to login,register,log out options and to see previous orders. Bag icon allows user to collect their orders in the shopping bag and to do checkout. Admin can edit product by clicking My account and Product management.

- There are 4 list item in main navigation that shows categories of products which are "All product, Homeware, Accessories & Gifts, Special Offers". For each page brief explanation added.

- Sort by feature is added to each category page to help user to sort their products as they want.

- Stripe is embedded to the website and all payment can be seen on Stripe

- Cards display product's name, photo, information, price, categories, delivery time, rate and comments. For admin, Bottom of the card there are two button that provide user edit and delete option. Edit button opens new page
to allow admin editing product.

- Footer part gives brief information about website, social media links and conctact details.


<h4>Features Left to Implement</h4>

- Adding star rate for users

- Providing coupon if users shares the page on social media.

- Customer service chat.

<h2>Technologies Used</h2>
[HTML](https://html.com/) and [CSS](https://html.com/)
- For webite's front-end

[JavaScript](https://www.javascript.com/)
- To use a hamburger menu

[Bootstrap](https://getbootstrap.com//)
- Design and customize responsive mobile-first


[Python](https://www.python.org/)
- Python to develop back-end

[Django](https://www.djangoproject.com/)
- To create full-stack web application development and server development.

[Flask](https://flask.palletsprojects.com/en/1.1.x/)
- Flask to bulild web app


<h2>Testing</h2>
All features of website work properly and it has tested by me and my mentor few times.
- Login/Register:

    * Go to the "Login" page.
    * Try to submit the empty form and verify that, "Please fill the blank" appears warning appears.
    * Try to submit the form with correct username and wrong password and verify that, "The username and/or password you specified are not correct." warning appears and user has to fill the form again.
    * Try to type random words to e-mail part on Register page, system warn users to use valid mail adress.
    * Try to submit the form with all inputs valid on Register page, it directs you e-mail verification page and you'll receive an e-mail.
    * Try to submit the form with all inputs valid on Login page and verify that it directs user main.
    
- Secure Checkout:

    * Add product to the bag and click Secure Checkout button.

    * Try to type invalid mail adress or card number, "Your card number is invalid." warning will appear.

    * Once you type valid information, blue screen will appear then payment will be approved.

    * On Stripe all payments are recorded, it can be checked to make sure.

- CRUD:

    * Login as an admin.

    * For each prudcts there are two buttons, when click delete button card dissapear.

    * Clicking Edit button directs admin to Product Manageent Page and allows admin to change all features of product.

    * After you make the change and click Update Procut button, it directs you to choosen product detail page to show your changes again.

- All links, feautures (comments, coupon), payments are working as intended and edit products, add products, delete works without problem. Website designed responsive for every device and it is tested on inspected page and not faced with any issue.

- Begining of the project I faced with cache bug and I couldn't activate css. Eventhough my mentor and tutors has helped me out a lot to solve that bug, it hasn't been sorted yet so I have to copy the link 
on by browser and paste it to incognito to see changings on front-end.

<h2>Deployment</h2>
I've deployed my project on GitHub and Heroku.

- To deploy my project on Github i followed these steps;

    * echo "# babayani-final-project" >> README.md
    * git init
    * git add README.md
    * git commit -m "first commit"
    * git remote add origin https://github.com/kaanistemi/babayani-final-project
    * git push -u origin master
 
- To deploy on Heroku

    * heroku login
    * heroku git:clone -a babayani-finalproject
    * cd babayani-finalproject

- and to make changes for both

    * git add .
    * git commit -m "last update"
    * git push heroku/origin master


<h2>Credit</h2>

<h4>Contents</h4>

All texts provided by Babayani's owner by e-mail.


<h4>Media</h4>

All photos provided by Babayani's owner by e-mail.

<h4>Acknowledgements</h4>

- I received inspiration for this project from Code Institute Boutique Ado Project and https://www.wooden-furniture-store.co.uk/
