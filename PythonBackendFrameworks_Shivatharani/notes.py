# 1.  Browser sends the request --> web server receives it --> request reaches the django --> url routing --> view handles the logic --> response is created --> response sent to the browser.

# 2. Middleware in Django is placed between the web server and the view component. Overall they process the request and response globally.
# The two built-in middleware are Session Middleware Class and Authentication Middleware Class.
# The session middleware enables session handling and attaches session data to request and it is placed before the authentication middleware.
# The authentication middleware populates user request and requires sessions and it is placed after the session middleware.

#3. WSGI - Web Server Gateway Interface is designed for synchronous applications and is best suited for traditional request–response web applications.
# ASGI - Asynchronous Server Gateway Interface supports asynchronous applications and efficiently handles long-lived connections such as WebSockets, along with non-HTTP protocols.
# Django mainly uses WSGI which is best suitable for traditional request-response web applications.

#4. Model - View - Controller
# Model - which represents the database logic and manages the data, it updates the view when data changes.
# View - It is used as a user Interface where we represent the data to the user.
# Controller - It acts as an intermediary between the model and the view and handles the business logic.

# Model - View - Template
# Model - It manages the structure and logic of the data
# View - It differes from MVC , it is used to receive user input nd processing it and it maps to the controller in the MVC.
# Template - It maps to the view in the MVC, where we used to represent the data in the form of HTML or UI elements.
# Django uses MVT model.
