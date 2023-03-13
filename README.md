# OAuth server

A simple services that handles OAuth flow for limited input devices.

It involves the following steps:
- App calls the POST https://{server}/initialize endpoint with the OAuth data, this returns a short unique code.
- The url with the code in presented in the app interface: e.g. 'Visit https://{server}/ABCD'.
- End user visits the url on a device of choice and does all that is required for the OAuth flow.
- Finally a callback is made to https://{server}/callback with the OAuth code, this returns a short code.
- End user enters the short code in the app on the limited input device.
- The app calls https://{server}/code/EFGH to retrieve the OAuth code.

## urls
POST /initialize
GET /{code}
GET /callback/
GET /code/{code}
