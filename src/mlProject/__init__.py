# --------------------------------------------
# Import required modules
# --------------------------------------------
import os      # For creating directories and handling file paths
import sys     # For accessing system-level output streams
import logging # For creating and managing log messages

# --------------------------------------------
# Define the logging format string
# --------------------------------------------
# This defines how each log message will appear:
# - %(asctime)s → Timestamp of log
# - %(levelname)s → Log level (INFO, ERROR, etc.)
# - %(module)s → Name of the module where log is called
# - %(message)s → Actual log message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s"

# --------------------------------------------
# Define log directory and log file path
# --------------------------------------------
log_dir = "logs"  # Folder to store all logs
log_filepath = os.path.join(log_dir, "running_logs.log")  # Full path to log file

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# --------------------------------------------
# Configure the logging system
# --------------------------------------------
# This setup ensures logs are saved both in a file and shown in the terminal
logging.basicConfig(
    level=logging.INFO,         # Minimum level of logs to capture (INFO and above)
    format=logging_str,         # Format to display each log line
    handlers=[
        logging.FileHandler(log_filepath),  # Write logs to the file
        logging.StreamHandler(sys.stdout)   # Display logs in terminal output
    ]
)

# --------------------------------------------
# Create a named logger instance
# --------------------------------------------
# This allows you to use 'logger' to log messages throughout the project
logger = logging.getLogger("mlProjectLogger")


