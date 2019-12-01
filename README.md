# Entry Notifier

About the application, this app benefits against the hassle of arranging meetings in a company, we superced the need of human interaction by arranging all the necessities under a single API. In the application host can register himself and the visitor can check in for the meeting with his host. On registration of the visitor, the host recieves an email and sms containg the visitor information (here the sms wouldn't be sent to all the bumbers, since the twilio api which is used is on trial period). On checkout of the visitor, visitor will recieve an e-mail and sms about the meeting details.

## Pre-requisites

- Python 3.6 and pip should be preinstalled.
- An email account.
- Twilio account for SMS. 

## Technology Stack

- **Programming Languages**
    - Pyhton 3.6
    - JavaScript

- **Frameworks**
    - Flask 1.1.1

- **Database**
    - SQLite3

- **Frontend**
    - HTML 5
    - CSS 3
    - Jinja
    - JavaScript
    - jQuery 3.4.1
    - Bootstrap 4

- **APIs**
    - Flask_mail (0.9.1) for sending emails.
    - Twilio for sending SMS.

## Implementation

The application can be primarily used for the following three tasks:

- Recording Visitor Check In
- Visitor Check Out
- Registration of a new host

## Deployment and Testing

To test and run the application on your local system follow the steps:
- Clone this repository and install the modules mentioned in requirements.txt file.

```python
$ pip install -r requirements.txt
```

- Goto the application directory through the terminal and run the application as follows:

```python
$ cd app
$ sh run
```
- The run file have all the commands to run the application.
![Screenshot from 2019-12-01 23-12-18](https://user-images.githubusercontent.com/32020192/69917830-822c2a00-1490-11ea-8a4c-0ae611e9fadd.png)

- As soon as you execute these commands open [http://localhost:5000](http://localhost:5000) in your browser to see the application running.


## Future Enhancements


## Credits

Created and Developed By: Tanmay Deep Sharma  
Contact Email: tanmaydeepsharma21@gmail.com
