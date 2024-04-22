# Cyber Asset Management API - Part 3 - TODO

## What would you change given extra time?

1. **Pagination:** Implement pagination for the GET `/assets` endpoint to handle large volumes of data more efficiently. Unfortunately, that was the one requirement in the assessment that I wasn't able get to in time and logically would be on my list of priorities if I had more time.

2. **Unit Testing:** Develop unit tests using frameworks like pytest or the unittest library to thoroughly test each endpoint and functionality of the API. This along with data validation and authentication is something I would definitely implement given more time due to how testing is very essential to successful software and even in this assessment where the scope was relatively small, I still found myself desiring the ability to test and being caught on things that a simple test suite would've definitely caught for me.

3. **Validation:** Implement data validation and some type of authentication in the API for incoming requests to ensure that required fields are provided and that data types are correct. All API's must have some method of validating data so that definitely would be on my priority if I were to build out the API more.

4. **Error Handling:** Improve error handling by providing more informative error messages and appropriate HTTP status codes for different scenarios. I had issues implementing that in detail when implementing the requirement for error handling in part 2 of the assessment and will definitely make sure to practice more on it in future projects.

5. **Sorting and Filtering:** Add functionality to allow sorting and additional filtering options for assets, such as sorting by name or other fields in the database.

## What would you add to the API to make it more secure?

1. **Authentication:** Implement user authentication using JWT (JSON Web Tokens) or session keys to secure access to sensitive endpoints and perform operations based on user roles.

2. **Authorization:** Add role-based access control (RBAC) to restrict certain endpoints or actions based on user roles (e.g., admin, regular user). If this were to be scaled up into some type of software where users or employees would be interacting with it to observe specific data, then this would essential in allowing that scope to be granted while also reducing large risks of vulnerability.

3. **Input Sanitization:** Sanitize input data to prevent SQL injection attacks and ensure data integrity in the database. I felt that I could've taken more time during the assessment to check over my code and make sure there were no glaring openings for potential SQL or data related attacks but I think for the most part, I did a decent job at it.

4. **HTTPS:** Enforce HTTPS protocol to encrypt data transmitted between the client and server, ensuring data confidentiality and integrity. Fundamental, but important to note nonetheless.

## Would you continue using the same database?

1. **Database Migration:** Evaluate the possibility of migrating to a more scalable database solution (e.g., PostgreSQL, MySQL) if the application's data volume increases significantly. I mainly have experience working with PostgreSQL so through this assessment, I got to work with SQLite for the first time and understand the differences between the two in terms of their ability to scale with software and their use cases for said software.   

2. **ORM Integration:** Consider integrating an Object-Relational Mapping (ORM) library like SQLAlchemy to simplify database interactions and improve code maintainability. Prior to starting the assessment, I looked into how best I could implement a SQLite database with a Flask API and that specific library was a tool I saw pop up a lot in my research. Through this project, I definitely feel even more motivated to go and explore more tools and libraries similar to ones I may already be familiar with.

##  Could the project be more portable?

1. **Containerization:** Dockerize the application to create a portable and consistent development, testing, and deployment environment across different platforms. This is something that I have experience doing with other projects and assignments and for an API like this, I would definitely use it to increase its portability.

2. **Continuous Integration/Continuous Deployment (CI/CD):** Implement CI/CD pipelines using tools like GitLab CI/CD, or GitHub Actions to automate testing, build, and deployment processes for faster and more reliable software delivery.

3. **Configuration Management:** Utilize environment variables or configuration files to manage sensitive information (e.g., database credentials, API keys) securely and enable easy deployment to different environments (dev, staging, production). If I were to deploy this API in the near future, this would be something I would definitely do since there's lots of effort that needs to go into allowing simple configuration for your software on other machines/devices while also making sure its safe for those said machines/devices.
---