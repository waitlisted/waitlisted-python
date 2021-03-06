# waitlisted
Waitlisted API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0.0
- Package version: 2.0.0
- Build date: 2017-02-12T22:31:55.664-06:00
- Build package: class io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/waitlisted/waitlisted-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/waitlisted/waitlisted-python.git`)

Then import the package:
```python
import waitlisted 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import waitlisted
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import time
import waitlisted
from waitlisted.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
waitlisted.configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# waitlisted.configuration.api_key_prefix['X-API-Key'] = 'Bearer'
# create an instance of the API class
api_instance = waitlisted.ReservationApi
body = waitlisted.ReservationRequest() # ReservationRequest | Reservation Data

try:
    api_response = api_instance.activate_reservation(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ReservationApi->activate_reservation: %s\n" % e

```

## Documentation for API Endpoints

All URIs are relative to *https://www.waitlisted.co/api/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ReservationApi* | [**activate_reservation**](docs/ReservationApi.md#activate_reservation) | **POST** /reservations/activate | 
*ReservationApi* | [**create_reservation**](docs/ReservationApi.md#create_reservation) | **POST** /reservations | 
*ReservationApi* | [**delete_reservation**](docs/ReservationApi.md#delete_reservation) | **DELETE** /reservations | 
*ReservationApi* | [**get_reservation**](docs/ReservationApi.md#get_reservation) | **GET** /reservations | 
*SiteApi* | [**get_site**](docs/SiteApi.md#get_site) | **GET** /site | 


## Documentation For Models

 - [ErrorResponse](docs/ErrorResponse.md)
 - [FormResponse](docs/FormResponse.md)
 - [Reservation](docs/Reservation.md)
 - [ReservationRequest](docs/ReservationRequest.md)
 - [ReservationsResponse](docs/ReservationsResponse.md)
 - [SiteResponse](docs/SiteResponse.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: X-API-Key
- **Location**: HTTP header


## Author



