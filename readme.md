
# Django E-Commerce Platform with Microservices Architecture

## Project Overview
This project is a **Django-based e-commerce platform** designed with a **microservices architecture**. It simulates an online store where users can browse products, place orders, and manage their profiles. Each major functionality is encapsulated in its own microservice, providing modularity, scalability, and ease of maintenance. The project leverages **Python, Django, PostgreSQL, REST API, and Docker** to create a robust, production-ready system.

---

## Features
- **User Service**: Registration, authentication, and profile management.  
- **Product Service**: Product listings, category management, and inventory tracking.  
- **Order Service**: Order creation, order history, and status tracking.  
- **Payment Service**: Payment processing and transaction records.  
- **Notification Service**: Real-time notifications for order updates and status changes.  

---

## Microservices Breakdown

### 1. User Service
- **Purpose**: Manages user accounts, authentication, and profile data.  
- **Technologies**: Django, Django REST Framework, PostgreSQL.  
- **Key Endpoints**:  
  - `POST /api/users/signup` - Register a new user.  
  - `POST /api/users/login` - Authenticate a user.  
  - `GET /api/users/profile` - Get user profile details.  

### 2. Product Service
- **Purpose**: Handles product listings, categories, and inventory.  
- **Technologies**: Django, REST API, PostgreSQL.  
- **Key Endpoints**:  
  - `GET /api/products` - List all products.  
  - `GET /api/products/{id}` - Retrieve product details.  
  - `POST /api/products` - Add a new product (admin access).  

### 3. Order Service
- **Purpose**: Manages order processing and status tracking.  
- **Technologies**: Django REST API, PostgreSQL, Django Celery (for background tasks).  
- **Key Endpoints**:  
  - `POST /api/orders` - Place a new order.  
  - `GET /api/orders/{id}` - View order details.  
  - `GET /api/orders/user/{user_id}` - Retrieve user’s order history.  

### 4. Payment Service
- **Purpose**: Processes payments and manages transactions.  
- **Technologies**: Flask/FastAPI, REST API, PostgreSQL.  
- **Key Endpoints**:  
  - `POST /api/payments` - Process a payment.  
  - `GET /api/payments/{id}` - Get payment status.  

### 5. Notification Service
- **Purpose**: Sends notifications to users about order and payment status.  
- **Technologies**: Flask, Celery (for asynchronous processing), Redis (for job queues).  
- **Key Endpoints**:  
  - `POST /api/notifications/send` - Send a notification.  
  - `GET /api/notifications/{user_id}` - Get notifications for a user.  

---

## System Architecture
- **Microservices Communication**: REST APIs enable each microservice to communicate independently.  
- **Database**: Each microservice has its own PostgreSQL database, ensuring data independence.  
- **Service Discovery**: Services are configured via environment variables for URL routing.  
- **Dockerized Setup**: Docker is used to containerize each microservice for consistency and easy deployment.  
