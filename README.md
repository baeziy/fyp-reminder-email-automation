# Project: FYP Reminder Email Automation

This Python-based project is designed to automate the process of sending daily reminder emails to members of a Final Year Project (FYP) group. The reminders include a countdown of the __days__ remaining until the FYP report submission deadline. To add a touch of motivation, each email contains a unique inspirational __quote__.

## Project Setup

### Requirements

- Python 3.6 or higher
- Python `dotenv` module: `pip install python-dotenv`
- Python `requests` module: `pip install requests`

### Installation

1. Clone the repository: `git clone https://github.com/baeziy/fyp-reminder-email-automation.git`
2. Change directory to the project folder: `cd fyp-reminder-email-automation`
3. Install the necessary packages: `pip install -r requirements.txt`

## How to Use

1. Create a `.env` file in the root directory of the project and add your email credentials:

```env
EMAIL=your_email@gmail.com
PASSWORD=your_password
```
2. Update the `names` and `emails` lists in main.py with the names and emails of your FYP group partners.

1. Execute main.py to send the emails: python main.py

## Deployment
The project is deployed on PythonAnywhere. To set it up:

* Upload the project files to PythonAnywhere.
* Create a new scheduled task to execute main.py daily.
## Technologies Used
* Python
* PythonAnywhere
## Author
Mustafa Kamal
## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgements
API Ninjas for providing the inspirational quotes API.