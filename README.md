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
