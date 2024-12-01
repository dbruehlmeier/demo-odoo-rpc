# PoC N8N-Odoo
The goal of this Proof-of-Concept (PoC) is to test if calculated fields are consistently updated
when using N8N (with JSON-RPC) to update a contact.

**Results**
- For both methods (using the @api.depends decorator and overwriting the write() method), the
calculated fields are consistently updated
- Tested with Odoo 16 and Odoo 17

## Installation
- Install Docker Compose
- Clone this repo
- Run ``docker-compose up``

## Setup
### Odoo
- Open: http://localhost:8069
- Master Password: ``master4Odoo``
- Database Name: ``poc``
- Email: ``admin``
- Password: ``admin``
- Demo data: ``check``
- Click: Create database
- Login: ``admin/admin``

### N8N
- Open: http://localhost:5678
- Email: ``admin@poc.xyz``
- First Name: ``N8N``
- Last Name: ``Admin``
- Password: ``admin4N8N``
- Click: Next
- Click: Get Started
- Click: Skip

## Run
- Open N8N-Workflow: http://localhost:5678/workflow/PCUNpRcXPEwspT64
- Click: ``Test workflow``
- Open Odoo Contact: http://localhost:8069/web#id=22&cids=1&menu_id=98&action=128&model=res.partner&view_type=form
- Check: Both fields ``Test Depends`` and ``Test Write`` have ben updated