# API Endpoints

### Note:

1. 🟢 - No authentication
2. 🚫 - Needs JWT bearer token

### Endpoints:

- `🟢 GET /`

  **Description:** Returns a HTML document that displays all the publically available urls along with their shortened tags in a tabular form.

---

- `🟢 GET /404`

  **Description:** Returns a HTML document that displays "404- Page not found" error.

---

- `🟢 GET /json`

  **Description:** Returns a list of all publically available urls along with their shotened tags in JSON format. This endpoint is an alternative to the `GET /` endpoint if the user wants the url data in JSON format.

---

- `🟢 GET /{short_tag}`

  **Description:** Redirects the user to the target url if the short tag is added to the database otherwise redirects user to the `GET /404` endpoint.

---

- `🟢 POST /auth`
  **Request Body:**
  ```JSON
  {
     "username": "string",
     "password": "string"
  }
  ```
  **Description:** This endpoint authenticates the user by matching the provided credentials with the credentials exported as environment variables. Returns a JWT bearer token if the user is authenticated, which is valid for 5 mins, otherwise returns an error message.

---

- `🚫 GET /stats`

  **Description:** This endpoint returns all the urls present in the database along with all detials like short tag, target url, visit count, and public visibility.

---

- `🚫 POST /url`

  **Request Body:**

  ```JSON
  {
     "short_tag": "string",
     "target_url": "string",
     "public": "bool",
     "visit_count": "integer"
  }
  ```

  **Description:** This endpoint adds a new url to the database. The short tag must be unique.

---

- `🚫 GET /url/{url_id}`

  **Description:** This endpoint gets the data of the specific url from the database with the given url id.

---

- `🚫 PUT /url/{url_id}`

  **Request Body:**

  ```JSON
  {
     "short_tag": "string",
     "target_url": "string",
     "public": "bool",
     "visit_count": "integer"
  }
  ```

  **Description:** This endpoint is used to modify the data in the database of the specific url with the given id. The visit count is not modified if its value is passed as 0.

---

- `🚫 DELETE /url/{url_id}`

  **Description:** This endpoint is used to delete the url present in the database with the given url id.
