import subprocess

# Function to run a command and capture its output
def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        return result.stderr.strip()

def install_python():
    print("Installing Python and pip...")
    run_command("sudo apt-get update && sudo apt-get install -y python3.7 python3-pip")

def install_mysql():
    print("Installing MySQL...")
    run_command("sudo apt-get update && sudo apt-get install -y mysql-server")

    # Secure the MySQL installation with auto-answers
    print("Securing MySQL installation...")
    input_text = "\n".join(["\n", "rootpassword", "y", "n", "y", "y", "y", "y"])
    run_command("sudo mysql_secure_installation", input_text=input_text)

# Function to set up a virtual environment
def setup_virtualenv():
    print("Setting up virtual environment...")
    run_command("sudo pip install virtualenv")
    run_command("mkdir envs")
    run_command("virtualenv ./envs/")

# Function to clone a Git repository
def clone_repository():
    print("Cloning git repository...")
    run_command("git clone 'https://github.com/Manisha-Bayya/simple-django-project.git'")

# Function to install required packages
def install_requirements():
    print("Installing requirements...")
    run_command("cd simple-django-project/")
    run_command("pip install -r requirements.txt")
    run_command("pip install django")
    run_command("pip install pymysql")
    run_command("pip install haystack")
    run_command("pip install phonenumber_field")

# Function to load sample data into MySQL
def load_sample_data():
    print("Loading sample data into MySQL...")
    print("# Open MySQL shell and execute the following commands:")
    print("mysql -u <mysql-user> -p")
    print("mysql> source ~/simple-django-project/world.sql")
    print("mysql> exit;")

# Function to edit project settings
def edit_settings():
    print("Editing project settings...")
    print("# Open the settings file and edit as follows:")
    print("# Edit Database configurations with your MySQL configurations.")
    print("# Edit email configurations.")
    print("# Save the file.")

# Function to run the Django server
def run_server():
    print("Running the server...")
    print("# Run the following commands:")
    print("python manage.py makemigrations")
    print("python manage.py migrate")
    print("python manage.py rebuild_index")
    print("python manage.py runserver 0:8001")

if __name__ == "__main__":
    install_python()
    install_mysql()
    setup_virtualenv()
    clone_repository()
    install_requirements()
    load_sample_data()
    edit_settings()
    run_server()
    print("Your server is up and running. Try opening http://localhost:8001 in your browser.")
