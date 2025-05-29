from flask import Flask, request, jsonify
from models import db, Contact
from sqlalchemy import or_
from datetime import datetime
import os

app = Flask(__name__)
# Configure the SQLite database URI and disable modification tracking
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db.init_app(app)

# Create the database tables (if not exist) when app context is active
with app.app_context():
    db.create_all()

# Define the /identify endpoint, accepts POST requests
@app.route('/identify', methods=['POST'])
def identify():
    # Parse JSON data from request body
    data = request.get_json()
    email = data.get('email')
    phone = data.get('phoneNumber')
    
    # Validate input: at least one of email or phoneNumber must be present
    if not email and not phone:
        return jsonify({"error": "Either email or phoneNumber required"}), 400

    # Query contacts where email or phoneNumber matches the input
    contacts = Contact.query.filter(
        or_(Contact.email == email, Contact.phoneNumber == phone)
    ).all()

    # If no existing contact found, create a new primary contact
    if not contacts:
        new_contact = Contact(email=email, phoneNumber=phone, linkPrecedence="primary")
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({
            "contact": {
                "primaryContactId": new_contact.id,
                "emails": [email] if email else [],
                "phoneNumbers": [phone] if phone else [],
                "secondaryContactIds": []
            }
        })

    # Collect all related contacts, including linked primary and secondary contacts
    related_contacts = set(contacts)
    for contact in contacts:
        if contact.linkedId:
            # Contact is secondary, get its primary contact and all linked contacts
            primary = Contact.query.get(contact.linkedId)
            related_contacts.update(Contact.query.filter(
                (Contact.linkedId == primary.id) | (Contact.id == primary.id)
            ).all())
        else:
            # Contact is primary, get all linked secondary contacts
            related_contacts.update(Contact.query.filter(
                (Contact.linkedId == contact.id) | (Contact.id == contact.id)
            ).all())

    # Determine the primary contact by finding the oldest created contact
    primary_contact = sorted(related_contacts, key=lambda c: c.createdAt)[0]

    # Separate secondary contacts (all except the primary)
    secondary_contacts = [c for c in related_contacts if c.id != primary_contact.id]

    # Gather existing emails and phone numbers from related contacts
    existing_emails = {c.email for c in related_contacts if c.email}
    existing_phones = {c.phoneNumber for c in related_contacts if c.phoneNumber}
    
    # Check if the incoming email or phone is new (not already linked)
    is_new_email = email and email not in existing_emails
    is_new_phone = phone and phone not in existing_phones
    
    # If new email or phone found, create a new secondary contact linked to primary
    if is_new_email or is_new_phone:
        new_secondary = Contact(
            email=email,
            phoneNumber=phone,
            linkedId=primary_contact.id,
            linkPrecedence="secondary"
        )
        db.session.add(new_secondary)
        db.session.commit()
        secondary_contacts.append(new_secondary)
    
    # Prepare the response JSON with consolidated contact info
    response = {
        "contact": {
            "primaryContactId": primary_contact.id,
            "emails": sorted({c.email for c in [primary_contact] + secondary_contacts if c.email}),
            "phoneNumbers": sorted({c.phoneNumber for c in [primary_contact] + secondary_contacts if c.phoneNumber}),
            "secondaryContactIds": [c.id for c in secondary_contacts]
        }
    }
    # Return the response with HTTP status 200 OK
    return jsonify(response), 200

# Run the app in debug mode if executed directly
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get PORT from environment or default 5000
    app.run(host="0.0.0.0", port=port)
