# Django Billing_Details Module (Uber/Ola-style Billing System)

This project implements a configurable, admin-managed **pricing module** like the one used in services such as Uber/Ola. It calculates the final ride invoice based on **distance**, **time**, **waiting time**, and **day of the week**, with support for **differential pricing**.

---

##  Features

-  Distance-based Base Price (DBP)
-  Distance Additional Price (DAP)
-  Time Multiplier Factor (TMF)
-  Waiting Charges (WC)
-  Enable/disable pricing configs via Admin
-  Audit log for config changes
-  REST API to calculate price
-  Clean architecture and modular business logic
-  Basic test case support

---

##  Tech Stack:

- **Backend:** Django + Django REST Framework
- **Database:** SQLite (easy to switch to PostgreSQL)
- **UI:** Django Admin

---

## Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/Avi-Y94/Billing_Details-module.git
cd Billing-module


##  API Endpoint

### **POST** `/api/v1/calculate-price/`

Send a JSON body like this:

```json
{
  "distance_travelled": 6.5,
  "waiting_time_minutes": 5,
  "ride_duration_minutes": 90,
  "ride_day": "Tuesday"
}


{
  "price": 225.5,
  "applied_config_id": 2
}

# install independicies 

pip install -r requirements.txt

# create superuser
python manage.py createsuperuser
