import os
import pandas as pd
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import json
from concurrent.futures import ThreadPoolExecutor

# Constants
folder_path = 'pruebas'
columns = ['file_name', 'duration(seconds)', 'call_id', 'agent_name']
valid_extension = ['.csv', '.json']

# Check if the file is valid (CSV or JSON)
def is_valid_file(file_path):
    return file_path.endswith(tuple(valid_extension))

# Class to handle new file events
class FileHandler(FileSystemEventHandler):
    def __init__(self, config, executor, dataframe):
        self.config = config
        self.executor = executor
        self.dataframe = dataframe

    # Detect new files
    def on_created(self, event):
        if not event.is_directory and is_valid_file(event.src_path):
            file_path = event.src_path
            print(f"New file detected: {file_path}")
            self.process_file(file_path)

    # Detect deleted files
    def on_deleted(self, event):
        if not event.is_directory:
            file_name = os.path.basename(event.src_path)
            print(f"File deleted: {event.src_path}")
            self.dataframe = self.dataframe[self.dataframe['file_name'] != file_name]
            self.save_dataframe()

    # Detect modified files
    def on_modified(self, event):
        if not event.is_directory and is_valid_file(event.src_path):
            print(f"File modified: {event.src_path}")
            self.process_file(event.src_path)

    # Detect moved files
    def on_moved(self, event):
        if not event.is_directory:
            print(f"File moved or renamed from {event.src_path} to {event.dest_path}")

    def process_file(self, file_path):
        try:
            print(f"Processing file: {file_path}")
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file_path.endswith('.json'):
                with open(file_path, 'r') as file:
                    data = json.load(file)
                df = pd.json_normalize(data)

            if all(col in df.columns for col in columns):
                self.dataframe = pd.concat([self.dataframe, df[columns]], ignore_index=True)
                self.save_dataframe()
            else:
                print(f"File {file_path} does not contain the required columns")
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

    # Save dataframe to pickle
    def save_dataframe(self):
        df_path = self.config['dataframe_path']
        self.dataframe.to_pickle(df_path)
        print(f"DataFrame updated and saved at {df_path}")

def load_config():
    with open('config_file.json', 'r') as file:
        return json.load(file)

def load_dataframe(df_path):
    print("Loading DataFrame...")
    if os.path.exists(df_path):
        return pd.read_pickle(df_path)
    else:
        return pd.DataFrame(columns=columns)

# Process all existing files
def process_existing_files(folder_to_watch, handler):
    print("Processing existing files...")
    with ThreadPoolExecutor(max_workers=max(handler.config['csv_jobs'], handler.config['json_jobs'])) as executor:
        for file_name in os.listdir(folder_to_watch):
            file_path = os.path.join(folder_to_watch, file_name)
            if os.path.isfile(file_path) and is_valid_file(file_name):
                executor.submit(handler.process_file, file_path)
    print("Initial file processing completed.")

# Start monitoring service
def start_monitoring():
    config = load_config()
    folder_to_watch = config['files_folder_path']
    df_path = config['dataframe_path']

    dataframe = load_dataframe(df_path)
    executor = ThreadPoolExecutor(max_workers=max(config['csv_jobs'], config['json_jobs']))

    event_handler = FileHandler(config, executor, dataframe)
    process_existing_files(folder_to_watch, event_handler)

    observer = Observer()
    observer.schedule(event_handler, folder_to_watch, recursive=False)
    observer.start()
    print(f"Monitoring folder: {folder_to_watch}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
    executor.shutdown(wait=True)

if __name__ == "__main__":
    start_monitoring()
