# Online School 

This project is an Online School  platform built using Django Rest Framework (DRF), where users can browse and purchase courses. It provides various API endpoints for managing courses, categories, carts, and purchases. It also includes JWT authentication for secure user login and access, as well as detailed API documentation via Swagger.

## Features

- **Courses**: List, create, update, and delete courses.
- **Categories**: Manage course categories for better organization.
- **Cart**: Add courses to the cart and manage the cart contents.
- **Purchase**: Complete course purchases through the API.
- **JWT Authentication**: Secure login and access control using JWT (JSON Web Tokens).
- **API Documentation**: Swagger-based interactive API documentation using drf_yasg.

## Requirements

- Python 3.x
- Django 4.x
- Django Rest Framework
- djoser (for JWT authentication)
- drf_yasg (for Swagger documentation)
- PostgreSQL (or your preferred database)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/online-school.git
   cd online-school
Install the dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Apply migrations:

bash
Copy
Edit
python manage.py migrate
Create a superuser for the admin interface (optional):

bash
Copy
Edit
python manage.py createsuperuser
Run the development server:

bash
Copy
Edit
python manage.py runserver
API Endpoints
Authentication
api


POST
/api/v1/carts/
api_v1_carts_create


GET
/api/v1/carts/{id}/
api_v1_carts_read


DELETE
/api/v1/carts/{id}/
api_v1_carts_delete


GET
/api/v1/categories/
api_v1_categories_list


POST
/api/v1/categories/
api_v1_categories_create


GET
/api/v1/categories/{id}/
api_v1_categories_read


PUT
/api/v1/categories/{id}/
api_v1_categories_update


PATCH
/api/v1/categories/{id}/
api_v1_categories_partial_update


DELETE
/api/v1/categories/{id}/
api_v1_categories_delete


GET
/api/v1/course/
api_v1_course_list


POST
/api/v1/course/
api_v1_course_create


GET
/api/v1/course/{course_pk}/images/
api_v1_course_images_list


POST
/api/v1/course/{course_pk}/images/
api_v1_course_images_create


GET
/api/v1/course/{course_pk}/images/{id}/
api_v1_course_images_read


PUT
/api/v1/course/{course_pk}/images/{id}/
api_v1_course_images_update


PATCH
/api/v1/course/{course_pk}/images/{id}/
api_v1_course_images_partial_update


DELETE
/api/v1/course/{course_pk}/images/{id}/
api_v1_course_images_delete


GET
/api/v1/course/{course_pk}/reviews/
api_v1_course_reviews_list


POST
/api/v1/course/{course_pk}/reviews/
api_v1_course_reviews_create


GET
/api/v1/course/{course_pk}/reviews/{id}/
api_v1_course_reviews_read


PUT
/api/v1/course/{course_pk}/reviews/{id}/
api_v1_course_reviews_update


PATCH
/api/v1/course/{course_pk}/reviews/{id}/
api_v1_course_reviews_partial_update


DELETE
/api/v1/course/{course_pk}/reviews/{id}/
api_v1_course_reviews_delete


GET
/api/v1/course/{id}/
api_v1_course_read


PUT
/api/v1/course/{id}/
api_v1_course_update


PATCH
/api/v1/course/{id}/
api_v1_course_partial_update


DELETE
/api/v1/course/{id}/
api_v1_course_delete


GET
/api/v1/orders/
api_v1_orders_list


POST
/api/v1/orders/
api_v1_orders_create


GET
/api/v1/orders/{id}/
api_v1_orders_read


PATCH
/api/v1/orders/{id}/
api_v1_orders_partial_update


DELETE
/api/v1/orders/{id}/
api_v1_orders_delete


POST
/api/v1/orders/{id}/cancel/
api_v1_orders_cancel


PATCH
/api/v1/orders/{id}/update_status/
api_v1_orders_update_status

auth


POST
/auth/jwt/create/
auth_jwt_create_create


POST
/auth/jwt/refresh/
auth_jwt_refresh_create


POST
/auth/jwt/verify/
auth_jwt_verify_create


GET
/auth/users/
auth_users_list


POST
/auth/users/
auth_users_create


POST
/auth/users/activation/
auth_users_activation


GET
/auth/users/me/
auth_users_me_read


PUT
/auth/users/me/
auth_users_me_update


PATCH
/auth/users/me/
auth_users_me_partial_update


DELETE
/auth/users/me/
auth_users_me_delete


POST
/auth/users/resend_activation/
auth_users_resend_activation


POST
/auth/users/reset_email/
auth_users_reset_username


POST
/auth/users/reset_email_confirm/
auth_users_reset_username_confirm


POST
/auth/users/reset_password/
auth_users_reset_password


POST
/auth/users/reset_password_confirm/
auth_users_reset_password_confirm


POST
/auth/users/set_email/
auth_users_set_username


POST
/auth/users/set_password/
auth_users_set_password


GET
/auth/users/{id}/
auth_users_read


PUT
/auth/users/{id}/
auth_users_update


PATCH
/auth/users/{id}/
auth_users_partial_update


DELETE
/auth/users/{id}/

API Documentation
The API documentation is available through Swagger at:

arduino
Copy
Edit
http://127.0.0.1:8000/swagger/
This provides an interactive interface to explore and test all the available endpoints.

Testing
To run the test suite:

bash
Copy
Edit
python manage.py test
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Django Rest Framework

Djoser

drf_yasg for Swagger integration

Contact
If you have any questions or suggestions, feel free to reach out to your-email@example.com.

vbnet
Copy
Edit

This README gives a clear overview of the project, how to set it up, and provides useful links to