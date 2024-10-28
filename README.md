# Authorization System with Django and React

This repository provides a simple authentication and authorization system using Django and React. It includes functionalities for user registration, login, and access control, with Django as the backend and React as the frontend.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- User Registration
- Login with JWT Authentication
- Protected routes based on user roles

## Technologies

- **Backend**: Django, Django REST Framework
- **Frontend**: React
- **Authentication**: JSON Web Tokens (JWT)


### Prerequisites

- Python 3.8+
- Node.js and npm

### Registration

To register a new user, make a `POST` request to the `/api/register/` endpoint with the following payload:

```json
{
  "username": "newuser",
  "email": "newuser@example.com",
  "password": "your_password"
}
```
If the registration is successful, the response will include a message confirming the user creation or provide any error messages for invalid input. 

### Login

To log in, make a `POST` request to the `/api/login/` endpoint with the following payload:

```json
{
  "username": "existinguser",
  "password": "your_password"
}
```
If successful, the response will include a JSON Web Token (JWT) that can be used to access protected routes.
