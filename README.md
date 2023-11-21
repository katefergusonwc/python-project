# Help Desk Ticketing System Prototype

This is a simple prototype of a Help Desk ticketing system implemented in Python.

## Overview

The Help Desk ticketing system allows staff members of an organization to submit tickets for assistance. The system can handle internal tickets, and it provides functionalities to submit, respond to, and track the status of tickets.

## Features

- **Submitting Tickets:**

  - Tickets can be submitted by providing Staff ID, Ticket creator name, Contact email, and a description of the issue.
  - The system automatically assigns a ticket number.

- **Responding to Tickets:**

  - If the ticket description contains "Password Change," a new password is generated following a specific rule.

- **Ticket Statistics:**

  - The system keeps track of the number of created, resolved, and open tickets.
  - Statistics can be displayed to the console.

- **Closing and Reopening Tickets:**

  - Tickets can be resolved, closed, and reopened based on IT department responses.

- **Displaying Ticket Information:**
  - Ticket information, including ticket number, creator name, staff ID, email address, description, response, and status, can be displayed.

## Technical Requirements

- The code uses a `Ticket` class with methods to submit, respond to, resolve, and reopen tickets.
- Ticket statistics are tracked using class variables.
- The main script (`help_desk_ticketing.py`) demonstrates the usage of the system.

## Usage

1. **Install Python:**
   [Python Downloads](https://www.python.org/downloads/)

2. **Install Visual Studio Code:**
   [Visual Studio Code](https://code.visualstudio.com/)

3. **Open the project in VS Code:**

   - Open VS Code and navigate to the folder containing `help_desk_ticketing.py`.

4. **Install the Python extension:**

   - Install the Python extension provided by Microsoft from the Extensions view (`View` -> `Extensions` or use the shortcut `Ctrl+Shift+X`).

5. **Run the script:**

   - Open the integrated terminal in VS Code (`View` -> `Terminal` or use the shortcut `Ctrl+``).
   - Navigate to the directory where `help_desk_ticketing.py` is located.
   - Run the script using the command:
     ```bash
     python help_desk_ticketing.py
     ```
     or
     ```bash
     python3 help_desk_ticketing.py
     ```

6. **Review Output:**
   - The script will execute, and you should see the output in the terminal.

## Example Output

```plaintext
[Output Example]
...

```
