# SETU Account Aggregator


## Installation


[![Python Version](https://img.shields.io/badge/python-3.8.1-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-4.0.6-brightgreen.svg)](https://djangoproject.com)


* First, clone the repository to your local machine:

```bash
https://github.com/samirpatil2000/SETU_AA.git
```
* Create & Activate Virtual Environment For Windows

```bash
>> virtualenv env
>> .\env\Scripts\activate
```

* Create & Activate Virtual Environment For MacOs/Linux

```bash
>> virtualenv env
>> . env/bin/activate
```


* Install the requirements:

```bash
>> pip install -r requirements.txt
```

* Create Database Tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

* Create `.env` file for credentials and these key-value
```python
X_CLIENT_ID="dc692d3c....."
X_CLIENT_SECRET="5982f80d....."
```
* Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.

### API ENDPOINTS
1. Create consent & handshake

    ENDPOINT: `/setu/api/consent-handshake`
   ```
   curl --location 'http://127.0.0.1:8000/setu/api/consent-handshake' \
    --header 'Content-Type: application/json' \
    --data '{
        "phone_number": "9730614299"
    }'
   ```
2. Get account data

   ENDPOINT: `/setu/api/sessions/:session_id`
    ```
   curl --location 'http://127.0.0.1:8000/setu/api/sessions/6775a858-0026-4541-a564-c319bba699cd' \
    --data ''
    ```
   
### SEQUENCE DIAGRAM
![Screenshot 2023-06-07 at 7 16 20 PM](https://github.com/samirpatil2000/SETU_AA/assets/55244065/07148870-0330-4b6d-9c18-d887c0c1a317)
