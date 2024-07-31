# Password Generator and Strength Estimator - @T7C

This Python script is a comprehensive tool for generating random passwords, estimating their cracking time, and managing saved passwords. It leverages the rich library to provide a professional and interactive command-line interface.

## Features

1. Generate Passwords:
    - Generate random passwords with options to include letters, digits, and special characters.
    - Customize the length of the generated password.

2. Estimate Cracking Time:
    - Estimate the time required to crack a given password using brute force methods.
    - Display the estimated time in a readable format (years, days, hours, minutes, seconds).

3. Manage Saved Passwords:
    - Save generated passwords to a JSON file.
    - Automatically delete the oldest password when the maximum limit (5 passwords) is reached.
    - View the last 5 saved passwords in a tabular format.

4. Import Passwords from File:
    - Import passwords from a CSV file and save them to the JSON file.

5. Additional Functionalities:
    - Save manually entered passwords.
    - Generate random passwords based on the structure of a sample password.
    - Display an "About" section with information about the tool.

## Installation

1. Clone the repository:
   ```bash
    git clone https://github.com/lysandraBars/secure-gen.git
    cd secure-gen
   ```

3. Install the required packages:
   ```bash
    pip install rich
   ```

## Usage

Run the script:
```bash
    python secure-gen.py
```

## Menu Options

1. Generate Password:
    - Follow the prompts to generate a password with desired characteristics.

2. Check Password Strength and Cracking Time:
    - Enter a password to estimate its cracking time.

3. View Saved Passwords:
    - View the last 5 saved passwords in a table.

4. Import Passwords from File:
    - Enter the path to a CSV file containing passwords to import.

5. Other:
    - Access additional functionalities like saving a manually entered password or generating random passwords based on a sample password.

6. Exit:
    - Exit the program.

## Other Menu Options

1. About:
    - Display information about the tool.

2. Save Password:
    - Manually enter and save a password.

3. Random Password:
    - Enter a sample password and generate random passwords with a similar structure.

4. Back:
    - Return to the main menu.

## Recent Updates

- Updated Functionality: Added feature to generate passwords based on a sample password's structure.
- Enhanced UI: Improved terminal UI with rich library for better interaction.
- Improved Error Handling: Enhanced error handling for file operations and user input.

## Code Structure

- secure-gen.py: Main script containing all functionalities.
- passwords.json: JSON file for storing saved passwords.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

For any questions or feedback, please contact:

- Email: tranminhtan4953@gmail.com
- Telegram: t.me/tanbaycu

## Hope
**I can't wait to hear back from you, I will listen to the errors and shortcomings, please give your comments. good luck**

