# Getting Started

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
