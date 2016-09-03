# python-cucm-axl-access
Simple Python script to access CUCM 9.1 AXL API

####Usage:

As it's shown on the AXL documentation from Cisco's developer site, to access the AXL API we must send a SOAP object according to the XML schema of the feature we want to use, for example in this case the AXL method:  **listLine.**



![Alt text](https://developer.cisco.com/media/axl-schema-11-0/Files/AXLSoap_p1020.png "List Line)")

This object can be found in the code as the payload variable.
Once it's send as a HTTP POST request you will get the response in XML format with the aditional information that was missing
in the original object.

E.g: 
```xml
<?xml version='1.0' encoding='utf-8'?>
<soapenv:Envelope
  xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
  <soapenv:Body>
    <ns:listLineResponse
      xmlns:ns="http://www.cisco.com/AXL/API/9.1">
      <return>
        <line uuid="{472FB464-0A35-E918-6007-264BDC119C8D}">
          <pattern>1234</pattern>
          <description>Luciano Ortega</description>
          <usage>Device</usage>
          <routePartitionName uuid="{B06D3111-977A-8F46-1BCA-8936C8377070}">P_IP_Telephony</routePartitionName>
        </line>
      </return>
    </ns:listLineResponse>
  </soapenv:Body>
</soapenv:Envelope>

```
For further references check on Cisco's developer site:

https://developer.cisco.com/site/axl/develop-and-test/documentation/latest-version/axl-soap.gsp
