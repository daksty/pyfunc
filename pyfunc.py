from faker import Faker
import re
import pyshorteners
import datetime
import os
import requests
from tqdm import tqdm
import shutil
import random
import time
import socket
import subprocess
import platform
import zipfile
import zlib
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import string


# ANSI escape codes for text coloring
red = "\033[91m"
blue = "\033[94m"
yellow = "\033[93m"
green = "\033[92m"
reset = "\033[0m"
font= '\033[1m'

letters = {
    'P': ['  ##### ',
          '  #    #',
          '  #    #',
          '  ##### ',
          '  #     ',
          '  #     '],

    'Y': ['  #   # ',
          '   # #  ',
          '    #   ',
          '    #   ',
          '    #   ',
          '    #   '],

    'F': ['  ##### ',
          '  #     ',
          '  #     ',
          '  ##### ',
          '  #     ',
          '  #     '],

    'U': ['  #   # ',
          '  #   # ',
          '  #   # ',
          '  #   # ',
          '  #   # ',
          '   ###  '],

    'N': ['  #   # ',
          '  ##  # ',
          '  # # # ',
          '  #  ## ',
          '  #   # ',
          '  #   # '],

    'C': ['   #### ',
          '  #     ',
          '  #     ',
          '  #     ',
          '  #     ',
          '   #### ']
}


def PYFUNC(text):
    for row in range(6):
        for char in text:
            if char in letters:
                letter_row = letters[char][row]
                big_letter = ''
                for ch in letter_row:
                    if ch == '#':
                        big_letter += random.choice(string.ascii_letters)
                    else:
                        big_letter += ' '
                print(big_letter, end='  ')
        print()        

def pongi():
	print(red +"-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
	print("")
	PYFUNC('PYFUNC')
	print("")
	print(green+"Creator:", yellow +"@daksty")
	print(green + "Github:", yellow + "https://www.github.com/daksty" + reset)
	print(green + "Discord:", yellow + "ravenishandsome#4807")
	print(red+ "")
	print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
	print(reset)
	
def get_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []
        
        # Find links in <a> tags
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.startswith('http'):
                links.append(href)

        # Find links in <button> tags
        for button in soup.find_all('button'):
            onclick = button.get('onclick')
            if onclick and 'location.href=' in onclick:
                start_index = onclick.index("'") + 1
                end_index = onclick.index("'", start_index)
                button_link = onclick[start_index:end_index]
                if button_link.startswith('http'):
                    links.append(button_link)

        return links

    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return []
print("")
pongi()
print("")
name = input(green + "Name: "+ reset)
os.system('clear')
def website_link():
    while True:
        website = input("Enter a website URL: ")
        if website.lower() == 'exit':
            main()

        if not website.startswith('http'):
            website = 'https://www.' + website

        links = get_links(website)
        print("Available links:")
        for link in links:
            print(link)
        print()


def zip_finder(zip_file_path):
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            print("Shortcut:")
            print("1 - /storage/emulated/0/download/passwords.txt")
            print("2 - /users/user/downloads/passwords.txt")
            passwords_file_path = input("Passwords.txt path: ")
            if passwords_file_path == "1":
                passwords_file_path = "/storage/emulated/0/download/passwords.txt"
            if passwords_file_path == "2":
                passwords_file_path = "/users/user/downloads/passwords.txt"
                if not os.path.exists(passwords_file_path):
                    print("Passwords file not found.")
                    print("If you don't have it, download it from github.com/daksty/pyfunc")
                    return False
            try:
                with open(passwords_file_path, 'r') as password_file:
                    passwords = password_file.read().splitlines()
            except FileNotFoundError:
                print("Passwords file not found.")
                print("If you don't have it, download it from github.com/daksty/pyfunc")
                return False

            for pw in passwords:
                pw = pw.strip()
                zip_ref.setpassword(pw.encode('utf-8'))
                try:
                    zip_ref.extractall()
                    print("Extraction complete. Password found:", pw)
                    return True
                except (zipfile.BadZipFile, RuntimeError, zlib.error) as e:
                    print("Invalid ZIP file or incorrect password:", pw)
                    print("Error:", str(e))
                    continue

            print("No valid password found.")
            return False

    except FileNotFoundError:
        print("Zip file not found:", zip_file_path)
        return False
    except zipfile.LargeZipFile:
        print("ZIP file is too large to handle.")
        return False
    except Exception as e:
        print("An error occurred:", str(e))
        return False

def zip_file_pc():
    while True:
        zip_file_path = input("Zip path: ")
        if zip_file_path.lower() == 'exit':
            break
        success = zip_finder(zip_file_path)
        if success:
            main()

def get_device_temperature():
    system = platform.system()

    if system == "Windows":
        try:
            import wmi
            w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
            temperature_info = w.Sensor()
            for sensor in temperature_info:
                if sensor.SensorType == '   Temperature':
                    return sensor.Value

        except ImportError:
            pass

    elif system == "Linux" or system == "Android":
        try:
            result = subprocess.run(['cat', '/sys/class/thermal/thermal_zone0/temp'], capture_output=True, text=True)
            temperature = int(result.stdout) / 1000  # Divide by 1000 to convert to degrees Celsius

            return temperature

        except (FileNotFoundError, subprocess.CalledProcessError, ValueError):
            pass

    return None

def temperature():
    temperature = get_device_temperature()

    if temperature is not None:
        print(yellow)
        print(f"      Device Temperature: {temperature}°C")
        print(reset)
    else:
        print("Unable to retrieve device temperature information.")


def print_file_content():
    while True:
        file_path = input("Enter the file path: ")
        if file_path == "exit":
        	main()

        if not os.path.isfile(file_path):
            print("Invalid file path. Please try again.")
            print("Try to put (/) first")
            print("Ex:  /storage/emulated/0/folder")
            continue

        try:
            with open(file_path, 'r') as file:
                content = file.read()
                print("File content:")
                print(content)
                main()

        except IOError:
            print("Error reading the file. Please try again.")


def website_ip():
    while True:
        print(reset)
        print(blue + " |---Website-ip"+ red+"@" + name, reset)
        print(blue +" |")
        website = input(" --Target-website----} " + green)
        if website == "exit":
        	print("")
        	main()

        try:
            ip_address = socket.gethostbyname(website)
            print(yellow)
            print(f"    The IP address of {website} is: {ip_address}"+ reset)
        except socket.gaierror:
            print("")
            print(red+ "      Invalid website or unable to resolve IP address." + reset)


def new_file():
    while True:
        print("[1] Folder (ex: .apk, .mp4)")
        print("[2] Directory file")
        choice = input("Choose: ")
        if choice == '1':
            is_file = True
            break
        elif choice == '2':
            is_file = False
            break
        elif choice.lower() == "exit":
        	main()
        else:
            print("Invalid choice. Please enter '1' or '2'.")

    while True:
        path = input("Enter the path where the {} should be created: ".format("file" if is_file else "directory"))

        # Check if the specified path exists
        if os.path.exists(path):
            break
        else:
            print("Path does not exist. Please enter a valid path.")

    # Create the file or directory
    try:
        if is_file:
            file_name = input("Enter the file name: ")
            file_path = os.path.join(path, file_name)
            with open(file_path, 'w') as file:
                print("File created successfully:", file_path)
        else:
            dir_name = input("Enter the directory name: ")
            dir_path = os.path.join(path, dir_name)
            os.mkdir(dir_path)
            print("Directory created successfully:", dir_path)
    except Exception as e:
        print("An error occurred:", str(e))


def rename_file():
    while True:
        print('Type "exit" to exit')
        print("")
        path = input("File path: ")
        
        if path.lower() == 'exit':
            main()
        
        while not os.path.exists(path):
            print("Path not found. Try again.")
            time.sleep(1)
            print("Try to type /storage/emulated/0/folder")
            print("")
            path = input("File path: ")
            
            if path.lower() == 'exit':
                main()
        
        name = input("Enter a new name: ")
        new_path = os.path.join(os.path.dirname(path), name)
        
        while os.path.exists(new_path):
            choice = input("A file or directory with that name already exists. Do you want to overwrite it? (y/n): ")
            if choice.lower() == 'y':
                if os.path.isdir(new_path):
                    os.removedirs(new_path)
                else:
                    os.remove(new_path)
                break
            elif choice.lower() == 'n':
                name = input("Enter a different name: ")
                new_path = os.path.join(os.path.dirname(path), name)
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")
        
        os.rename(path, new_path)
        print("Path renamed successfully.")

def generate_fake_identity():
    fake = Faker()

    # Generate fake user data
    name = fake.name()
    email = fake.email()
    address = fake.address()
    phone_number = fake.phone_number()
    image_url = fake.image_url()

    # Print the generated data
    print(yellow)
    print("     Fake identity generated:")
    print("")
    print(yellow+"     Name:", blue +name+reset)
    print(yellow+"     Email:", blue+email+reset)
    print(yellow+"     Address:", blue+address+reset)
    print(yellow+"     Phone Number:",blue+ phone_number+reset)
    print(yellow+"     Image URL:",blue+ image_url+reset)
    print(reset)
    main()


def get_location(ip_address):
    url = f"https://ipapi.co/{ip_address}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        print("Location Information:")
        for key, value in data.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("An error occurred while performing the IP lookup.")

def iplookup():
    while True:
        ip_address = input("Target ip: ")
        
        if ip_address.lower() == 'exit':
            main()
        
        if not ip_address.replace('.', '').isdigit():
            print("Invalid IP address. Please enter a valid IP address.")
            continue
        
        get_location(ip_address)


def shorten_link(url):
    shortener = pyshorteners.Shortener()
    return shortener.tinyurl.short(url)

def is_valid_url(url):
    regex = re.compile(
        r"^(?:http|ftp)s?://"  # http:// or https://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
        r"localhost|"  # localhost...
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|"  # ...or IPv4
        r"\[?[A-F0-9]*:[A-F0-9:]+\]?)|"  # ...or IPv6
        r"(?:[^\s:/?#]+://)?"  # protocol-less
        r"[^\s?#]+"  # domain or path
        r"(?:\?[^\s#]*)?"  # query string
        r"(?:#[^\s]*)?$"  # fragment
        , re.IGNORECASE)
    return re.match(regex, url) is not None

def link_shorter():
    while True:
        print("Type 'exit' to exit")
        original_link = input("Enter the link: ")
        
        if original_link.lower() == "exit":
            main()

        if not original_link:
            print("Please provide a link.")
            continue

        if not is_valid_url(original_link):
            print("Invalid link. Please enter a valid URL.")
            continue

        if not original_link.startswith("http"):
            original_link = "https://" + original_link

        shortened_link = shorten_link(original_link)

        print("Shortened link:", shortened_link)
        print()

def get_time():
    current_time = datetime.datetime.now()
    formatted_date = current_time.strftime("%B %d, %Y")
    formatted_time = current_time.strftime("%H:%M:%S")
    print(yellow)
    print("      Date:", formatted_date)
    print("      Time:", formatted_time)
    print(reset)


def copy_file():
    while True:
        source_path = input("File path to copy: ")
        if source_path.lower() == "exit":
            main()
        if os.path.isfile(source_path):
            break
        else:
            print("Invalid source file path. Please try again.")

    while True:
        destination_dir = input("New destination of copied file(path): ")

        if os.path.isdir(destination_dir):
            break
        else:
            print("Invalid destination directory path. Please try again.")

    while True:
        new_file_name = input("New name for copied file: ")

        if "." in new_file_name:
            print("Please provide the new file name without the file extension.")
        else:
            break

    source_filename = os.path.basename(source_path)
    source_extension = os.path.splitext(source_filename)[1]
    destination_path = os.path.join(destination_dir, new_file_name + source_extension)

    shutil.copy(source_path, destination_path)

    print(f"File copied and renamed to '{destination_path}'.")


def delete_file():
    while True:
        print("Ex: /users/user/downloads")
        print("It will delete the downloads file")
        path = input("file path: ")
        if path.lower() == "exit":
            main()
        elif path.lower() == "clear":
            os.system('clear')

        if os.path.exists(path):
            if os.path.isdir(path):
                file_count = sum(len(files) for _, _, files in os.walk(path))
                progress_bar = tqdm(total=file_count, unit='file')

                for root, dirs, files in os.walk(path, topdown=False):
                    for file in files:
                        file_path = os.path.join(root, file)
                        os.remove(file_path)
                        progress_bar.update(1)

                shutil.rmtree(path)
                progress_bar.close()

                print(f"All files and directories in '{path}' have been deleted.")
            else:
                os.remove(path)
                print(f"File '{path}' has been deleted.")
            
            break
        else:
            print("File or directory not found. Please try again.")


def calculator():
    global a
    print("")
    print(blue +"     Basic calculator.",reset)
    print(green+"         Ex: 1+1", reset)
    print("")
    while True:
        print(blue+" |--Calculator" +red + "@"+name,reset)
        print(blue+" |")
        expression = input(blue + " ----} "+ green)

        if expression.lower() == 'exit':
            print("")
            main()
        if expression.lower() == 'clear':
            os.system('clear')

        expression = re.sub(r'[×x]', '*', expression)
        expression = re.sub(r'÷', '/', expression)

        try:
            print(yellow)
            result = eval(expression)
            print("   Result:", result,reset)
        except Exception as e:
            print(red+"     Invalid expression. Please try again." + reset)
            print(green+ "     Example: 1+1 or 1÷1" + reset)

        print()

def help():
	print(reset)
	print(red +"              |--------------|")
	print("   ", red+ "          |", green + "COMMAND LIST", red + "|")
	print("              |--------------|", reset)
	print("")
	print(blue +"       GLOBAL TOOLS")
	print("")
	print(green + "     EXIT", yellow + "          exit to any tools", reset)
	print(green+"     CLEAR", yellow + "         clear terminals")
	print(reset)
	print(blue + "       BASIC TOOLS")
	print(reset)
	print(green +"     HELP", yellow + "          show available commands.", reset)
	print(green + "     TIME", yellow + "          show current date and time.", reset)
	print(green +"     TEMPERATURE", yellow + "   check your device temperature.", reset)
	print(green +"     CALCULATOR", yellow + "    basic calculator.", reset)
	print(green+ "     GFI", yellow +"           generate fake identity.")
	print("")
	print(blue +"       WEBSITE TOOLS", reset)
	print("")
	print(green + "     WEBSITE-IP", yellow + "    check ip address of target website.", reset)
	print(green+"     LINK-SHORTER", yellow + "  make your link shorter.", reset)
	print(green + "     WEBSITE-LINK", yellow + "  direct link finder on target website.", reset)
	print("")
	print(blue+"       ADVANCED TOOLS")
	print(reset)
	print(green+"     IPLOOKUP", yellow+"      show location of an target ip address.", reset)
	print("")
	print(blue + "       FILE TOOLS",reset)
	print("")
	print(green + "     ZFPC", yellow+ "          zip file password cracker/bruteforce.",reset)
	print(green +"     NEW-FILE", yellow+ "      make new file directory/folder.")
	print(green + "     DELETE-FILE", yellow +"   delete your files. ",reset)
	print(green+"     COPY-FILE", yellow+"     copy your file directory/folder.",reset)
	print(green+"     RENAME-FILE", yellow+"   rename your file directory/folder.",reset)
	print(green+"     READ-FILE", yellow+ "     read your file content if readable")
	print(reset)

def main():
    global green
    global blue
    global red
    while True:
        import time
        global name
        print(font + blue +" |---" + "Pyfunc"+ reset + red+ "@"+name+reset+blue)
        print(" |")
        a = input(blue + " ----} "+ green)
        if a.lower() == "calculator":
            calculator()
        elif a.lower() == "clear":
            os.system('clear')
        elif a.lower() == "delete file" or a.lower() == "delete-file":
            delete_file()
        elif a.lower() == "copy file" or a.lower() == "copy-file":
            copy_file()
        elif a.lower() == "gfi":
            generate_fake_identity()
        elif a.lower() == "iplookup":
            iplookup()
        elif a.lower() == "link-shorter" or a.lower() == "link shorter":
            link_shorter()
        elif a.lower() == "time":
            get_time()
        elif a.lower() == "help":
            help()
        elif a.lower() == "exit":
            print("Exiting...")
            break
        elif a.lower() == "hi":
        	print("Hello!")
        elif a.lower() == "rename-file" or a.lower() == "rename file":
        	rename_file()
        elif a.lower() == "new-file" or a.lower() == "new file":
        	new_file()
        elif a.lower() == "read-file" or a.lower() == "read file":
        	print_file_content()
        elif a.lower() == "website-ip" or a.lower() == "website ip":
        	website_ip()
        elif a.lower() == "temperature":
        	temperature()
        elif a.lower() == "zfpc":
        	zip_file_pc()
        elif a.lower() == "website-link" or a.lower()== "website link":
        	website_link()
        elif a.lower() == "exit":
        	print("Bye!")
        	break
        else:
            print(red)
            print("   Invalid command. Type 'help' to see available command")
            print(reset)
            

main()
