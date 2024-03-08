# SQL---GESTION_REPARATIONS_ELECTROMENAGERS

The Python SQLite Database Management App is a simple application designed to manage repair orders for devices, using an SQLite database backend. This application allows users to perform various operations such as searching for clients, inserting repair orders, calculating total amounts for clients, displaying parts with prices above a certain threshold, and showing repair orders without parts to change.

## Features

1. **Search Client**: Allows users to search for clients by name and view their details.
2. **Insert Repair Order**: Enables users to insert new repair orders with diagnostic information and labor hours.
3. **Calculate Total Amount**: Calculates the total repair bill amount for a client based on their repair orders.
4. **Display Parts**: Displays parts with prices above a specified threshold.
5. **Show Orders**: Shows repair orders without parts to change.

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Python-SQLite-DB-Management-App.git
   cd Python-SQLite-DB-Management-App
2. **Install Dependencies**:

Ensure you have Python3 installed on your system.
Install the required Python packages by running: `pip install pillow`.

3. **Run the Application**:
   ```bash
   python3 main.py
4. **Application Interface**:

The application interface allows users to perform various database management operations using a graphical user interface (GUI).

## Database Structure

The application utilizes an SQLite database with the following tables:

- **CLIENTE**: Stores client information.
- **CATEGORIE**: Stores categories of devices.
- **APPAREIL**: Stores device information.
- **PIECE**: Stores parts information.
- **ORDREREPARATION**: Stores repair order details.
- **PIECESACHANGER**: Stores parts to change for repair orders.

## Contributors
**MEZZOUR Omar** - Creator and maintainer
