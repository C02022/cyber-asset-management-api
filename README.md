# Cyber Asset Management API

This API manages a database of cyber assets, such as networking equipment, servers, personal computers, etc.

## Prerequisites

Before running the API, ensure you have the following installed:

- Python 3.x
- Flask
- Flask-Restful
- SQLite3

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/C02022/cyber-asset-management-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd cyber-asset-management-api
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the API server and intialize the SQLite database:

   ```bash
   python server.py
   ```

2. The API will be accessible at `http://localhost:5000`.

## Endpoints

### GET /assets

- Returns a list of all cyber assets in the database.

  Example:
  ```
  GET /assets
  ```

### POST /assets

- Adds a new cyber asset to the database.

  **Request Body (JSON):**

  ```json
  {
      "NAME": "Asset Name",
      "TYPE": "Asset Type",
      "SERIAL_NUMBER": "ABC123",
      "OPERATING_SYSTEM": "Windows"
  }
  ```

### GET /assets/{id}

- Returns details of a specific cyber asset by ID.

  Example:
  ```
  GET /assets/1
  ```

### DELETE /assets/{id}

- Deletes a specific asset by ID.

  Example:
  ```
  DELETE /assets/1
  ```

## Testing

You can test the API using tools like Postman or by making HTTP requests from your code. Here are some sample requests:

1. Create a new asset:

   ```
   POST /assets
   Request Body:
   {
       "NAME": "Asset Name",
       "TYPE": "Asset Type",
       "SERIAL_NUMBER": "ABC123",
       "OPERATING_SYSTEM": "Windows"
   }
   ```

2. Retrieve all assets:

   ```
   GET /assets
   ```

3. Delete an asset:

   ```
   DELETE /assets/1
   ```

## Contributors

- Christopher Obando 
---