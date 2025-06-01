# Identity Reconciliation API

This project is a Flask-based REST API designed to reconcile identity information based on emails and phone numbers. It exposes a single endpoint **`/identify`** which accepts JSON requests and returns a consolidated view of contact details, grouping primary and secondary contacts.

---

## How It Works

- The API accepts a JSON payload containing an email and/or phone number.
- It searches the database for existing contacts matching the given email or phone.
- If no contact exists, it creates a new primary contact.
- If matches exist, it collects all related contacts linked by their IDs (primary and secondary).
- It consolidates emails, phone numbers, and secondary contact IDs associated with the primary contact.
- If the incoming email or phone is new, it adds a new secondary contact linked to the primary contact.
- The response returns the **primaryContactId**, all associated emails, phone numbers, and a list of secondary contact IDs.

---

## Tech Stack

- **Python 3** — Programming language
- **Flask** — Web framework for building the API
- **Flask-SQLAlchemy** — ORM for database interaction
- **SQLite** — Lightweight database used for development and testing
- **Gunicorn** — WSGI HTTP server for production deployment
- **Render.com** — Hosting and deployment platform

---

## API Endpoint

### POST `/identify`

- **Request Content-Type:** `application/json`
- **Request Body:**  
  ```json
  {
    "email": "string (optional)",
    "phoneNumber": "string (optional)"
  }
![Primary ID Inserted](https://github.com/rajatrajat0210/Identity-Reconciliation/blob/main/PrimaryId.png?raw=true)
![Secondary ID Inserted Linked with Primary ID](https://github.com/rajatrajat0210/Identity-Reconciliation/blob/main/SecondaryId.png?raw=true)
![Error when Nothing inserted](https://github.com/rajatrajat0210/Identity-Reconciliation/blob/main/Error.png?raw=true)


## Running Locally
```bash
git clone https://github.com/rajatrajat0210/Identity-Reconciliation-.git
cd Identity-Reconciliation-
```
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
```bash
pip install -r requirements.txt
```
```bash
python app.py
```
## Render API EndPoint  - https://identity-reconciliation-t843.onrender.com/identify
If Render Service gets inactive , so just refresh the tab to make it active and use . 

📬 Postman Collection
🧪 We've prepared a full Postman collection with all the test cases for validating the /identify endpoint.

✅ Includes:

New primary contact creation

Linking new secondary contact

Merging two primaries

All valid combinations of email and phoneNumber (email only, phone only, both)

📌 How to Use:

Open the link above in Postman.

Import the collection into your workspace.

Run the test cases using the Postman runner or manually.

Thanks for Visiting ! 
