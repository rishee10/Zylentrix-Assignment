# Zylentrix-Assignment

# User Management API

This is a RESTful API for managing users. It provides endpoints for creating, reading, updating, and deleting users.

## Getting Started

To get started with this project, follow these steps:

``` python -m venv venv ```

``` venv\Scripts\activate ```

```pip install django djangorestframework```

## Running the API

To run the API, navigate to the project directory and run the following command:

```python manage.py makemigrations```

```python manage.py migrate```

```python manage.py runserver```

## API Endpoints
The API provides the following endpoints:

POST /users/: Create a new user

GET /users/all/: Retrieve all users

GET /users/<int:pk>/: Retrieve a single user

PUT /users/<int:pk>/update/: Update a user

DELETE /users/<int:pk>/delete/: Delete a user

## Testing with Postman

### 1. Open Postman

- Install [Postman](https://www.postman.com/) if you haven't already.
  
- Open the application and set up a new request.

### 2. Create a New User (POST)
- Select **POST** request.
  
- Enter the URL: `http://127.0.0.1:8000/users/`
  
- Go to the **Body** tab and choose **raw**.
  
- Set the type to **JSON** and enter:
  
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
  }
  ```
  
- Click **Send** and check the response.

### 3. Retrieve All Users (GET)

- Select **GET** request.
  
- Enter the URL: `http://127.0.0.1:8000/users/all/`
  
- Click **Send** to see the list of users.

### 4. Retrieve a Single User (GET)

- Select **GET** request.
  
- Enter the URL: `http://127.0.0.1:8000/users/{id}/` (replace `{id}` with an actual user ID).
  
- Click **Send** to get user details.

### 5. Update a User (PUT)

- Select **PUT** request.
  
- Enter the URL: `http://127.0.0.1:8000/users/{id}/update/`.
  
- Go to **Body** > **raw**, set type to **JSON**, and enter:
  
  ```json
  {
    "name": "John Updated",
    "email": "johnupdated@example.com",
    "age": 35
  }
  ```
  
- Click **Send** to update the user.

### 6. Delete a User (DELETE)

- Select **DELETE** request.
  
- Enter the URL: `http://127.0.0.1:8000/users/{id}/delete/`.
  
- Click **Send** to delete the user.


