import os
import shutil
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#place your file paths below
source_dir=''
image_dir=''
vid_dir=''
music_dir=''

def makeUnique(path):
    filename,extension=os.path.splitext(path)
    counter=1
    if os.path.exists(path):
        path=filename+"("+str(counter)+")"+extension
        counter+=1

    return path


def move(dest, entry, name):
    file_exists=os.path.exists(dest+"/"+name)
    if file_exists:
        unique_name=makeUnique(name)
        os.rename(entry,unique_name)
    shutil.move(entry,dest)

class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                dest = source_dir
                if name.endswith('.jpg') or name.endswith('.jpeg') or name.endswith('.png'):
                    dest = image_dir
                    move(dest,entry,name)
                elif name.endswith('.mp4') or name.endswith('.mov'):
                    dest = vid_dir
                    move(dest,entry,name)
                elif name.endswith('.mp3'):
                    dest=music_dir
                    move(dest,entry,name)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()