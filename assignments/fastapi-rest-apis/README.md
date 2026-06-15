# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using FastAPI to handle requests, return JSON responses, and practice routing, query parameters, and request body handling.

## 📝 Tasks

### 🛠️ Create API Endpoints

#### Description
Create routes for retrieving and returning data using FastAPI.

#### Requirements
Completed program should:

- Define a FastAPI app instance.
- Add a root endpoint that returns a welcome message.
- Add a route to retrieve an item by ID.
- Return JSON responses for each endpoint.

### 🛠️ Query Parameters and Request Body

#### Description
Handle query parameters for filtering and accept request body data to create resources.

#### Requirements
Completed program should:

- Use query parameters in at least one endpoint.
- Define a Pydantic model for request body validation.
- Accept a JSON body for creating or updating an item.
- Return the submitted data in the response.

### 🛠️ Validation and Error Handling

#### Description
Add input validation and useful error messages for bad requests.

#### Requirements
Completed program should:

- Validate request data with Pydantic.
- Return a clear error message for invalid inputs.
- Use correct HTTP status codes for responses.
- Keep the API behavior simple and consistent.
