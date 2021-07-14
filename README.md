# shrty
A high-performance url shortener and manager app for personal usage built with the FastAPI framework. 

The user must be authenticated and should use the JWT authentication bearer token for the CRUD operations. 

The app uses PostgreSQL database connected via SQLAlchemy module in Python. 


### Tech Stack:
Python, FastAPI, PostgreSQL, SQLAlchemy and PyJWT.


## Getting Started

1. Fork the repository and then clone the repository locally. Type the following command/s in the terminal. \
    ```
    https://github.com/<YOUR USERNAME>/shrty-api.git
    ```

2. Navigate to the app directory. Type the following command/s in the terminal. \
    ```
    cd shrty-api
    ```

3. Create a new virtual environment and install the required Python modules. Type the following command/s in the terminal. \
    ```
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
    
4. Before running the app locally, don't forget to export the following environment variables.
    ``` 
    SECRET_KEY: "<SECRET KEY FOR THE APPLICATION>" (it is used for generating and verifying the JWT bearer tokens)
    DATABASE_URL: "<POSTGRESQL DATABASE URL>" (make sure that the url starts with "postgresql://" and not "postgres://")
    USER_NAME: "<USER NAME FOR AUTHENTICATION PURPOSE>"
    PASSWORD: "<PASSWORD FOR AUTHENTICATION PURPOSE>"
    ```
    
5. Run the app using the Uvicorn server.
    ```
    uvicorn shrty:app --reload
    ```
