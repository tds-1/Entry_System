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

- Registration of a new host
- Recording Visitor Check In
- Visitor Check Out

### REGISTRATION OF A NEW HOST

- ![Screenshot_2019-12-01 https entry-system herokuapp com](https://user-images.githubusercontent.com/32020192/69917908-4he e9dcf80-1491-11ea-8fcf-0f7009cbdb63.png)
- A new host can register himself here. If the host is already registered he can find himself in the visitor section.
- ![Screenshot_2019-12-01 https entry-system herokuapp com(1)](https://user-images.githubusercontent.com/32020192/69917944-edc2c700-1491-11ea-9704-44ae8202c891.png)
- All the fields are mandatory to fill.

### RECORDING VISITOR CHECK IN
- Any person who intends to attend a meeting would go the visitor section and accordingly would select a host. After selecting the host the visitor would be required to fill the necessary details. 
- ![Screenshot_2019-12-01 https entry-system herokuapp com(2)](https://user-images.githubusercontent.com/32020192/69917992-a38e1580-1492-11ea-8b7f-665d7e2e01a7.png)
- All the fields are mandatory to fill.
- After checking in the host will recieve an e-mail and a SMS containg details of the visitor.
- ![WhatsApp Image 2019-12-01 at 23 34 47(1)](https://user-images.githubusercontent.com/32020192/69918086-d389e880-1493-11ea-94c1-81b3205689b9.jpeg)

### VISITOR CHECK OUT
- Every visitor has an option of checking-out when the meeting has been completed. After the visitor has checked-out the visitor would recieve an e-mail and also a SMS regarding the details of the meeting with real time check-in and check-out information.
- ![WhatsApp Image 2019-12-01 at 23 34 47](https://user-images.githubusercontent.com/32020192/69918134-4b581300-1494-11ea-9e39-461862c838a0.jpeg)
- ![Screenshot_2019-12-01 Meeting details - innovaccercheckout gmail com - Gmail](https://user-images.githubusercontent.com/32020192/69918135-4bf0a980-1494-11ea-814c-742004ece1c6.png)



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
- ![Screenshot from 2019-12-01 23-12-18](https://user-images.githubusercontent.com/32020192/69917830-822c2a00-1490-11ea-8a4c-0ae611e9fadd.png)

- As soon as you execute these commands open [http://localhost:5000](http://localhost:5000) in your browser to see the application running.


## Future Enhancements

- AJAX can be used to check the form details in realtime.
- Authentication can be added in registration. (here since OTP can not be sent Authentication can not be added)
- A host can accept or reject the visitor, and could set a cap on maximum number of visitors.
- A host can also reschedule the meetings

## Credits

Created and Developed By: Tanmay Deep Sharma  
Contact Email: tanmaydeepsharma21@gmail.com
