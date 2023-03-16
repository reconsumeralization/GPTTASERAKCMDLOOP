import logging
import subprocess

# Set up logging
logging.basicConfig(filename='gpt3_cmd.log', level=logging.INFO)

def log_error(error: str) -> None:
    logging.error(error)

def log_warning(warning: str) -> None:
    logging.warning(warning)

def log_info(info: str) -> None:
    logging.info(info)

def execute_command(command: str) -> Tuple[str, bool]:
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        output = stdout.decode('utf-8')
        return (output, True)
    except subprocess.CalledProcessError as e:
        error_message = f'Error executing command "{command}": {e}'
        log_error(error_message)
        return (error_message, False)
