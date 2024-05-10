import pygetwindow as gw
import psutil
import time

def end_tasks():
    while True:
        try:
            for process in psutil.process_iter(['name']):
                process_name = process.info['name'].lower()
                if any(keyword in process_name for keyword in ['roblox', 'xbox', 'game', 'races', 'launcher']):
                    process.kill()
        except Exception as e:
            print(e)
        
        title = gw.getActiveWindowTitle()
        if title:
            title = title.lower()
            if any(keyword in title for keyword in ['google','roblox', 'youtube', '1v1', 'xbox', 'war thunder', '.io', 'fortnite', 'gartic', 'store']):
                gw.getActiveWindow().close()
        time.sleep(3)

def check_processes():
    with open('processes.txt', 'r') as f:
        processes = f.read().splitlines()
    
    found_new = False
    for process in psutil.process_iter(['name']):
        if process.info['name'] not in processes:
            found_new = True
            print(process.info['name'])

    if not found_new:
        print(">>> No new processes found <<<")

def write_processes():
    with open('processes.txt', 'w') as f:
        for process in psutil.process_iter(['name']):
            f.write(process.info['name'] + '\n')
    print(">>> Processes saved <<<")

# To use these functions, uncomment the appropriate one:
# end_tasks()
# check_processes()
# write_processes()
