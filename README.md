# RideShare Database Management Script

This Python script is designed to interact with a RideShare MySQL database. It provides features for managing and rating rides for both riders and drivers.

## Key Features

- **User Authentication**: Users are authenticated based on user ID.
- **Role-based Access**: Depending on the user role (rider or driver), the script provides different functionalities.
- **Ride Management**: Riders can find drivers, and drivers can update their availability status.
- **Rating System**: Both riders and drivers can rate each other after a ride. The ratings are stored in the database and used to update a user's overall rating.
- **Real-Time Progress**: During a ride, the driver can update the ride status in real time.

## Usage

This script is designed to run in a Python environment and interact with a MySQL database. The user needs to input their ID to access the functionalities of the script based on their role (rider or driver).

For riders, the options are:
1. Find a driver
2. Rate the last driver
3. Exit

For drivers, the options are:
1. Enable DriveMode
2. Rate the last rider
3. Exit

The script will continue to run until the user chooses to exit.

## Installation

Prerequisites:
- Python 3.x
- MySQL Connector/Python

Steps:
1. Ensure Python and pip (Python package installer) are installed on your system. You can download Python from the [official website](https://www.python.org/downloads/)
2. Install MySQL Connector/Python using pip. Open your terminal and run the following command: `pip install mysql-connector-python`
3. Clone the repository or download the Python script to your local machine.
4. Update the following lines of code with your MySQL server's details: `mydb = mysql.connector.connect(host="", user="", password="", auth_plugin='', database="RideShare")`
5. Run the script using a Python interpreter.

Please note that the script assumes the existence of certain tables (Rider, Driver, and Ride) in the database. Make sure these tables exist and have the correct structure before running the script.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
None
