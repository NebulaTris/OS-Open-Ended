import psutil
import time
import matplotlib.pyplot as plt

# create empty lists to store data for plotting
cpu_data = []
mem_data = []
disk_data = []
sent_data = []
recv_data = []

# set the plot title and labels
plt.title('System Resource Monitor')
plt.xlabel('Time (s)')
plt.ylabel('Usage (%)')

# set the plot axis limits
plt.ylim(0, 100)

# start the loop to monitor system resources
while True:
    # get the system resource usage
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent
    net_io_counters = psutil.net_io_counters()
    sent_mb = net_io_counters.bytes_sent / 1024 / 1024
    recv_mb = net_io_counters.bytes_recv / 1024 / 1024
    
    # add the data to the lists for plotting
    cpu_data.append(cpu_percent)
    mem_data.append(mem_percent)
    disk_data.append(disk_percent)
    sent_data.append(sent_mb)
    recv_data.append(recv_mb)
    
    # print the system resource usage
    print(f"CPU Usage: {cpu_percent}%")
    print(f"Memory Usage: {mem_percent}%")
    print(f"Disk Usage: {disk_percent}%")
    print(f"Network Usage: Sent: {sent_mb} MB, Received: {recv_mb} MB")

    plt.clf()
    plt.subplot(2, 2, 1)
    plt.plot(cpu_data, 'r-', label='CPU Usage')
    plt.ylabel('Usage (%)')
    plt.legend(loc='upper left')

    plt.subplot(2, 2, 2)
    plt.plot(mem_data, 'b-', label='Memory Usage')
    plt.ylabel('Usage (%)')
    plt.legend(loc='upper left')

    plt.subplot(2, 2, 3)
    plt.plot(disk_data, 'g-', label='Disk Usage')
    plt.ylabel('Usage (%)')
    plt.legend(loc='upper left')

    plt.subplot(2, 2, 4)
    plt.plot(sent_data, 'm-', label='Sent MB')
    plt.plot(recv_data, 'y-', label='Received MB')
    plt.ylabel('Usage (MB)')
    plt.legend(loc='upper left')

    plt.suptitle('System Resource Monitor')
    plt.pause(1)
    plt.show(block=False)

    time.sleep(1)
