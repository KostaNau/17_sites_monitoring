# Sites Monitoring Utility

## Description
The script check up domain expiration date and http response code for each site from user list.


## How to use
Run the script ```python3 check_site_healty.py``` with postional argument ```path to the user's site list```

**User's site list requirements** *Each line must contain only one url.*


### Examples
```python3 check_site_healty.py path/to/site list```

**Output**
```
==========================================================
Domain: http://your-domain.ru
HTTP (Code 200): True
Expiration date (at least 30 days): True
==========================================================
Domain: http://www.somedomain.com
HTTP (Code 200): True
Expiration date (at least 30 days): True
==========================================================
Domain: http://foo.bar
HTTP (Code 200): Failed to establish a new connection: unknown url!!!
Expiration date (at least 30 days): Failed to determine expiration date. Unknown url!!!
==========================================================
```

### Requriments
Install the dependencies from requirements.txt using pip:

```pip install -r requirements.txt```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
