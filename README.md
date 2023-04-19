# OS-Open-Ended

# System Resource Monitor (Python) and Process Viewer (Bash)
This repository contains two scripts: a System Resource Monitor written in Python and a Process Viewer written in Bash.

## System Resource Monitor
The System Resource Monitor is a Python script that identifies the current available and utilized resources of the system, such as CPU, memory, I/O, and bandwidth. The program is capable of logging historical system resources and showing resource utilization graph using the matplotlib library. The script runs continuously in the terminal until the user interrupts the program. The generated graph can be saved as an image file.

## Usage
To run the System Resource Monitor, simply execute the system_resource_monitor.py script in a terminal.

```
python3 system_resource_monitor.py
```

The script will start monitoring the system resources and will continuously print the resource usage information in the terminal. To stop the program, press Ctrl + C. The script will then generate a graph of the resource usage data.

## Process Viewer
The Process Viewer is a Bash script that shows all running processes on a Linux system at the time it boots up. The script uses the ps command to display the process information, and the output is sorted by the process ID. The script can be executed in the terminal or added to the system startup to automatically display the running processes on boot.

## Usage
To run the Process Viewer, simply execute the process_viewer.sh script in a terminal.

```
./process_viewer.sh
```

The script will display the running processes in the terminal, sorted by the process ID. The output includes the process ID, user, CPU usage, memory usage, and command name.
