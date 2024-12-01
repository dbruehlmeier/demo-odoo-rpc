# PoC N8N-Odoo
In this Proof-of-Concept, the goal is to test if calculated fields are consistently updated
when using N8N (with JSON-RPC) to update a contact.

## Installation
- Install Docker Compose
- Clone this repo
- Run ``docker-compose up``

## Setup
### Odoo
- Open: http://localhost:8069
- Master Password: ``knvz-cxfd-wcwj-3z2z``
- Database Name: ``poc``
- Email: ``admin``
- Password: ``admin``
- Demo data ``check``
- Create database
- Login: ``admin/admin``

### N8N
- Open: http://localhost:5678
- Email: ``admin@poc.xyz``
- First Name: ``N8N``
- Last Name: ``Admin``
- Password: ``admin4N8N``
- Click: Get Started
- Click: Skip

- Credentials: Create Credential
- Select: ``Odoo API``
- Site URL: ``http://odoo:8069``
- Username: ``admin``
- Password or API Key: ``admin``
- Database Name: ``poc``
- Click: Save

- Workflows: Create Workflow
- Add: Trigger Manually
- Add: Odoo - Update a Contact
- Contact ID: ``22``
- Update Fields: Name = ``Test N8N``
- Save the workflow

## Run
- In N8N: Click ``Test workflow``
- Open Odoo: http://localhost:8069/web#id=22&cids=1&menu_id=98&action=128&model=res.partner&view_type=form
- Check: Both fields ``Test Depends`` and ``Test Write`` have ben updated