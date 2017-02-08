# waitlisted.SiteApi

All URIs are relative to *https://www.waitlisted.co/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_site**](SiteApi.md#get_site) | **GET** /site | 


# **get_site**
> SiteResponse get_site()



Get site settings and reservation count.

### Example 
```python
import time
import waitlisted
from waitlisted.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = waitlisted.SiteApi()

try: 
    api_response = api_instance.get_site()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SiteApi->get_site: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SiteResponse**](SiteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

