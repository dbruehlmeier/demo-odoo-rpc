# PoC N8N-Odoo
The goal of this Proof-of-Concept (PoC) is to test if calculated fields are consistently updated
when using N8N (with JSON-RPC) to update a contact.

## Installation
- Install Docker Compose
- Clone this repo
- Install the [Ansible Odoo Scripts](https://ansible.build/scripts.html#odoo-scripts) ``curl -L https://raw.githubusercontent.com/mint-system/ansible-build/main/roles/odoo_scripts/files/install | bash``

## Scenario 1: Direct installation
In this scenario, the module is installed directly when launching Odoo, by
adding ``--init demo_rpc_write`` to the launch command in Docker Compose.
- Run ``docker-compose -f docker-compose_with-installation.yml up``

**Results**
- For both methods (using the @api.depends decorator and overwriting the write() method), the
calculated fields are consistently updated
- Tested with Odoo 16 and Odoo 17

## Scenario 2: Installation with Ansible
In this scenario, the module is installed after launching Odoo, by
launching ``docker-odoo-init`` with the running container.
- Run ``docker-compose -f docker-compose_without-installation.yml up``
- Run ``docker-odoo-init -c "demo-odoo-rpc_odoo_1" -d "poc" -i "demo_rpc_write"``

**Results**
- For both methods (using the @api.depends decorator and overwriting the write() method), the
calculated fields are consistently updated **if the container is restarted**.
- Without a restart, Odoo seems to fall into an undefined state, which caused different problems
after each test run.
- Tested with Odoo 16

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