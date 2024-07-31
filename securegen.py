import random
import string
import os
import json
import csv
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()

PASSWORD_FILE = 'passwords.json'
MAX_PASSWORDS = 5

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

excluded_characters = set('. , ? |  % $ ^ : < ; " \' ~ ` {# > } [  ]')     # another 

def generate_password(length, include_letters=True, include_digits=True, include_specials=True):
    characters = ''
    
    if include_letters:
        characters += string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_specials:
        characters += ''.join(c for c in string.punctuation if c not in excluded_characters or c == '-')
    
    if not characters:
        raise ValueError("No valid characters to generate password.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(password):
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'r') as file:
            passwords = json.load(file)
    else:
        passwords = []
    
    passwords.append(password)
    
    if len(passwords) > MAX_PASSWORDS:
        passwords.pop(0)
    
    with open(PASSWORD_FILE, 'w') as file:
        json.dump(passwords, file)

def get_saved_passwords():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'r') as file:
            passwords = json.load(file)
        return passwords
    return []

def estimate_time_to_crack(password):
    length = len(password)
    charset_size = len(string.ascii_letters + string.digits + string.punctuation) - len(excluded_characters) + (1 if '-' not in excluded_characters else 0)
    total_combinations = charset_size ** length
    
    attempts_per_second = 100_000_000_000_000_000_000
    """ time infinity """
    
    try:
        time_seconds = total_combinations / attempts_per_second
        return time_seconds
    except OverflowError:
        return float('inf')

def format_time(seconds):
    if seconds == float('inf'):
        return "Estimated time too large to display."
    
    days_per_year = 365.25
    years = seconds / (60 * 60 * 24 * days_per_year)
    days = years * days_per_year % 365
    hours = (seconds % (60 * 60 * 24)) // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    
    return f"{int(years)} years {int(days)} days {int(hours)} hours {int(minutes)} minutes {int(seconds)} seconds"

def print_title():
    ascii_title = r"""
   
                                                    .___                 
___________    ______ ________  _  _____________  __| _/                 
\____ \__  \  /  ___//  ___/\ \/ \/ /  _ \_  __ \/ __ |                  
|  |_> > __ \_\___ \ \___ \  \     (  <_> )  | \/ /_/ |                  
|   __(____  /____  >____  >  \/\_/ \____/|__|  \____ |                  
|__|       \/     \/     \/                          \/                  
                                                      __                 
              ____   ____   ____   ________________ _/  |_  ___________  
             / ___\_/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \ 
            / /_/  >  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/ 
            \___  / \___  >___|  /\___  >__|  (____  /__|  \____/|__|    
           /_____/      \/     \/     \/           \/                    

    t7c
    """
    title = Text(ascii_title, style="bold green")
    console.print(Panel(title, expand=False, border_style="cyan", padding=(0, 2), title_align="center"))

def display_menu():
    print_title()
    
    while True:
        console.print("\n[bold yellow]MENU[/bold yellow]")
        console.print("[bold green][1][/bold green] Generate password")
        console.print("[bold green][2][/bold green] Check password strength and cracking time")
        console.print("[bold green][3][/bold green] View saved passwords")
        console.print("[bold green][4][/bold green] Import passwords from file")
        console.print("[bold green][5][/bold green] Other")
        console.print("[bold red][6][/bold red] Exit")
        console.print("=" * 50, style="green bold")
        
        choice = Prompt.ask("[bold magenta]Choose an option [/bold magenta]", choices=['1', '2', '3', '4', '5', '6'])
        
        if choice == '1':
            length = get_password_length()
            include_letters = Prompt.ask("[bold magenta]Include letters? [/bold magenta]", choices=['y', 'n']) == 'y'
            include_digits = Prompt.ask("[bold magenta]Include digits? [/bold magenta]", choices=['y', 'n']) == 'y'
            include_specials = Prompt.ask("[bold magenta]Include special characters? [/bold magenta]", choices=['y', 'n']) == 'y'
            
            password = generate_password(length, include_letters, include_digits, include_specials)
            console.print(f"Generated password: [bold green]{password}")
            save_password(password)
        
        elif choice == '2':
            password = Prompt.ask("[bold magenta]Enter password to check[/bold magenta]")
            time_seconds = estimate_time_to_crack(password)
            formatted_time = format_time(time_seconds)
            console.print(f"Estimated time to crack password: [bold green]{formatted_time}[/bold green]")
        
        elif choice == '3':
            passwords = get_saved_passwords()
            if passwords:
                table = Table(title="Saved Passwords (Last 5 passwords)", border_style="cyan", padding=(0, 2))
                table.add_column("No.", style="bold", justify="center")
                table.add_column("Password", style="bold green")
                for i, pwd in enumerate(passwords, 1):
                    table.add_row(f"[{i}]", pwd)
                console.print(table)
            else:
                console.print("No passwords saved yet.", style="red")
        
        elif choice == '4':
            file_path = Prompt.ask("[bold magenta]Enter the CSV file path containing passwords[/bold magenta]")
            try:
                with open(file_path, 'r') as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        if row:
                            password = row[0]
                            save_password(password)
                            console.print(f"Imported password from file: [bold green]{password}[/bold green]")
            except Exception as e:
                console.print(f"Error importing from file: {e}", style="red")
        
        elif choice == '5':
            display_other_menu()
        
        elif choice == '6':
            console.print("Exiting program.", style="yellow")
            break
        
        else:
            console.print("Invalid choice. Please try again.", style="red")

def display_other_menu():
    while True:
        console.print("\n[bold yellow]OTHER MENU[/bold yellow]")
        console.print("[bold green][1][/bold green] About")
        console.print("[bold green][2][/bold green] Save password")
        console.print("[bold green][3][/bold green] Random password")
        console.print("[bold green][4][/bold green] Back")
        console.print("=" * 50, style="green bold")
        
        choice = Prompt.ask("[bold magenta]Choose an option [/bold magenta]", choices=['1', '2', '3', '4'])
        
        if choice == '1':
            display_about()
        
        elif choice == '2':
            save_password_prompt()
        
        elif choice == '3':
            random_password()
        
        elif choice == '4':
            break
        
        else:
            console.print("Invalid choice. Please try again.", style="red")

def display_about():
    console.print("\n[bold yellow]About[/bold yellow]")
    console.print("©T7C. Random password generator and estimation of cracking time. Multiple extended and security functions available.️")

def save_password_prompt():
    password = Prompt.ask("[bold magenta]Enter the password you want to save[/bold magenta]")
    save_password(password)
    console.print(f"Saved password: [bold green]{password}[/bold green]")

def analyze_password_structure(password):
    structure = []
    for char in password:
        if char.isalpha():
            structure.append('L')
        elif char.isdigit():
            structure.append('D')
        elif char in string.punctuation:
            structure.append('S')
        else:
            structure.append('O')
    return structure

def generate_password_from_structure(length, structure):
    characters = {
        'L': string.ascii_letters,
        'D': string.digits,
        'S': ''.join(c for c in string.punctuation if c not in excluded_characters or c == '-'),
        'O': string.ascii_letters + string.digits + string.punctuation
    }
    
    password = ''.join(random.choice(characters[char_type]) for char_type in structure)
    return password

def random_password():
    sample_password = Prompt.ask("[bold magenta]Enter a sample password to generate random passwords[/bold magenta]")
    
    structure = analyze_password_structure(sample_password)
    length = len(structure)
    
    console.print(f"Sample password: [bold green]{sample_password}")
    console.print("Generating random passwords with similar structure...")
    
    num_passwords = int(Prompt.ask("[bold magenta]Number of random passwords to generate[/bold magenta]", default="5"))
    
    for i in range(num_passwords):
        password = generate_password_from_structure(length, structure)
        console.print(f"Random password {i+1}: [bold green]{password}")

def get_password_length():
    while True:
        try:
            length = int(Prompt.ask("[bold magenta]Enter password length[/bold magenta]", default="12"))
            if length < 1:
                raise ValueError
            return length
        except ValueError:
            console.print("Invalid password length. Please enter a positive integer.", style="red")

if __name__ == "__main__":
    display_menu()


