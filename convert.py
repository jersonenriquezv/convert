from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import Image
import os
import time

class Watcher:
    DIRECTORY_TO_WATCH = r"C:\Users\jerso\Documents\WebProgramming\Converter"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except Exception as e:
            self.observer.stop()
            print(e)

        self.observer.join()

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            if event.src_path.endswith('.webp'):
                print(f"Received created event - {event.src_path}.")
                convert_to_jpg(event.src_path)

def convert_to_jpg(webp_image_path):
    output_folder = r"C:\Users\jerso\Documents\WebProgramming\ConvertedJPGs"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    file_name_noext = os.path.splitext(os.path.basename(webp_image_path))[0]
    jpg_image_path = os.path.join(output_folder, file_name_noext + '.jpg')

    image = Image.open(webp_image_path)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    image.save(jpg_image_path, 'JPEG')
    print(f"Converted {webp_image_path} to {jpg_image_path}")

if __name__ == '__main__':
    w = Watcher()
    w.run()
