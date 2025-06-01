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

## 🚀 API Testing with Postman

To thoroughly test the `/identify` endpoint of the **Identity Reconciliation** service, I have created a comprehensive Postman collection covering all key scenarios described in the project requirements.

### 🔗 Postman Collection Link

[Open the Postman Collection](https://www.postman.com/rajat-testing-api/workspace/bitespeed-public/collection/11409748-b0f4177c-734b-4c49-9f2e-76f5d7295dc5?action=share&creator=11409748)

---

### 📋 What’s Included?

- **New Primary Contact Creation:**  
  Validate the creation of a brand new primary contact when no existing records match.

- **Secondary Contact Linking:**  
  Check cases where a new contact with overlapping email or phone number is linked as secondary.

- **Primary Contact Merging:**  
  Simulate merging two previously primary contacts when a shared identifier (email or phone) is detected.

- **Input Variations:**  
  Test the endpoint with different combinations:  
  - Email only  
  - Phone number only  
  - Both email and phone number  

- **Edge Cases & Validation:**  
  Handle null or missing fields gracefully.

---

### ⚙️ How to Use the Collection

1. **Open the link** above to view the collection in Postman.  
2. Click **Fork** or **Import** to add it to your workspace.  
3. Review each request, which includes predefined JSON payloads for all test cases.  
4. Run requests individually or use the **Collection Runner** for batch testing.  
5. Inspect responses to verify the returned contact consolidation matches expectations.

---

### 📢 Why Use This?

Using this Postman collection allows for quick, repeatable testing to ensure your Identity Reconciliation endpoint behaves correctly and reliably before deployment or integration. It’s also a great tool for demoing your API to stakeholders or teammates.

---

*If you want, I can also share the exported Postman collection file (`.json`) to include directly in the repo!*

Thanks for Visiting ! 
