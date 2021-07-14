# shrty

A high-performance url shortener and manager app for personal usage built with the FastAPI framework.

The user must be authenticated and should use the JWT authentication bearer token for the CRUD operations.

The app uses PostgreSQL database connected via SQLAlchemy module in Python.

### Tech Stack:

Python, FastAPI, PostgreSQL, SQLAlchemy and PyJWT.

---
## Getting Started

1. Fork the repository and then clone the repository locally. Type the following command/s in the terminal.

   ```
   git clone https://github.com/<YOUR USERNAME>/shrty-api.git
   ```

2. Navigate to the app directory. Type the following command/s in the terminal.

   ```
   cd shrty-api
   ```

3. Create a new virtual environment and install the required Python modules. Type the following command/s in the terminal.
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
4. Create a ".env" file containing following environment variables.
   ```
   SECRET_KEY="<SECRET KEY FOR THE APPLICATION> (it is used for generating and verifying the JWT bearer tokens)"
   DATABASE_URL="<POSTGRESQL DATABASE URL> (make sure that the url starts with "postgresql://" and not "postgres://")"
   USER_NAME="<USER NAME FOR AUTHENTICATION PURPOSE>"
   PASSWORD="<PASSWORD FOR AUTHENTICATION PURPOSE>"
   ```
5. Create a new Python file named as "run.py" and paste the following code in it.

   ```Python
   import uvicorn
   from dotenv import load_dotenv

   if __name__ == "__main__":
       load_dotenv(".env")
       uvicorn.run("shrty:app", reload=True)

   ```

6. Run the Python file. Type the following command/s in the terminal.

   ```
   python run.py
   ```

---
## API Endpoints

### Note:
1. 🟢 - No authentication
2. 🚫 - Needs JWT bearer token 

### Endpoints:
- ```🟢 GET /``` 

   __Description:__ Returns a HTML document that displays all the publically available urls along with their shortened tags in a tabular form.
   
---

- ```🟢 GET /404```

   __Description:__ Returns a HTML document that displays "404- Page not found" error.
   
---

- ```🟢 GET /json```

   __Description:__ Returns a list of all publically available urls along with their shotened tags in JSON format. This endpoint is an alternative to the ```GET /``` endpoint if the user wants the url data in JSON format.
   
---
   
- ```🟢 GET /{short_tag}```

   __Description:__ Redirects the user to the target url if the short tag is added to the database otherwise redirects user to the ```GET /404``` endpoint.
   
---

- ```🟢 POST /auth```
   
   __Request Body:__
   ```JSON
   {
      "username": "string",
      "password": "string"
   }
   ```
   
   __Description:__ This endpoint authenticates the user by matching the provided credentials with the credentials exported as environment variables. Returns a JWT bearer token if the user is authenticated, which is valid for 5 mins, otherwise returns an error message.
   
---

- ```🚫 GET /stats```

   __Description:__ This endpoint returns all the urls present in the database along with all detials like short tag, target url, visit count, and public visibility.
   
---
   
- ```🚫 POST /url```

   __Request Body:__
   ```JSON
   {
      "short_tag": "string",
      "target_url": "string",
      "public": "bool",
      "visit_count": "integer"
   }
   ```
   
   __Description:__ This endpoint adds a new url to the database. The short tag must be unique.
   
---

- ```🚫 GET /url/{url_id}```

   __Description:__ This endpoint gets the data of the specific url from the database with the given url id.
   
   
---

- ```🚫 PUT /url/{url_id}```

   __Request Body:__
   ```JSON
   {
      "short_tag": "string",
      "target_url": "string",
      "public": "bool",
      "visit_count": "integer"
   }
   ```
   
   __Description:__ This endpoint is used to modify the data in the database of the specific url with the given id. The visit count is not modified if its value is passed as 0.

---

- ```🚫 DELETE /url/{url_id}```

   __Description:__ This endpoint is used to delete the url present in the database with the given url id.
