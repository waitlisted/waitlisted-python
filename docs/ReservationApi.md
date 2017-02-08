# waitlisted.ReservationApi

All URIs are relative to *https://www.waitlisted.co/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reservation**](ReservationApi.md#create_reservation) | **POST** /reservations | 
[**delete_reservation**](ReservationApi.md#delete_reservation) | **DELETE** /reservations | 
[**get_reservation**](ReservationApi.md#get_reservation) | **GET** /reservations | 


# **create_reservation**
> ReservationsResponse create_reservation(body)



Creates a new reservation.

### Example 
```python
import time
import waitlisted
from waitlisted.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = waitlisted.ReservationApi()
body = waitlisted.Reservation() # Reservation | Reservation Data

try: 
    api_response = api_instance.create_reservation(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ReservationApi->create_reservation: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Reservation**](Reservation.md)| Reservation Data | 

### Return type

[**ReservationsResponse**](ReservationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reservation**
> delete_reservation(body)



Delete a reservation.

### Example 
```python
import time
import waitlisted
from waitlisted.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = waitlisted.ReservationApi()
body = waitlisted.ReservationRequest() # ReservationRequest | Reservation Data

try: 
    api_instance.delete_reservation(body)
except ApiException as e:
    print "Exception when calling ReservationApi->delete_reservation: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReservationRequest**](ReservationRequest.md)| Reservation Data | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reservation**
> ReservationsResponse get_reservation(email)



Get a reservation.

### Example 
```python
import time
import waitlisted
from waitlisted.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = waitlisted.ReservationApi()
email = 'email_example' # str | Email address

try: 
    api_response = api_instance.get_reservation(email)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ReservationApi->get_reservation: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email address | 

### Return type

[**ReservationsResponse**](ReservationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

