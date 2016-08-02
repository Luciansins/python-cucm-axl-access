#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Python approach to access the AXL API on the CUCM
import base64
import requests
#To disable the warning "InsecureRequestWarning: Unverified HTTPS request is being made"
#in requests using urllib3,  it's needed to import the specific instance of the module
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#authentication and CUCM AXL API address
authentication = base64.b64encode('user:password')
cucmAxlUrl = 'https://192.168.0.1/axl/'

#Dictionary containing headers for the request
headers = {
  'SoapAction':'CUCM:DB ver=9.1',
  'Authorization': 'Basic ' +authentication, 
  'Content-Type': 'text/xml; charset=utf-8'
}

#define a function to make the request
def xml_request():
  request = requests.post(cucmAxlUrl, headers=headers, verify=False, data=payload)
  response = request.text
  return response

#xml payload that will be sent to the CUCM AXL API
payload = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:axl="http://www.cisco.com/AXL/API/9.1">
   <soapenv:Header/>
   <soapenv:Body>
      <axl:listLine>
        <searchCriteria>
          <pattern>1234</pattern>
        </searchCriteria>
        <returnedTags>
          <pattern/>
          <description/>
          <usage/>
          <routePartitionName/>
        </returnedTags>
    </axl:listLine>
   </soapenv:Body>
</soapenv:Envelope>"""

#print the response
print xml_request()