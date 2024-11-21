# Real-Time Bandwidth Monitor in Python

import time
import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Lists to store timestamps and bandwidth data
timestamps = []
mb_rec = []
mb_sent = []

# Get initial network I/O counters
last_rec = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent

def update_data(i):
    global last_rec, last_sent
    # Get current network I/O counters
    bytes_rec = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent
    
    # Calculate the difference from the last counters and convert to MB
    new_rec = (bytes_rec - last_rec) / 1024 / 1024
    new_sent = (bytes_sent - last_sent) / 1024 / 1024
    
    # Append new data to the lists
    timestamps.append(time.time())
    mb_rec.append(new_rec)
    mb_sent.append(new_sent)
    
    # Keep only the last 600 data points
    if len(timestamps) > 600:
        timestamps.pop(0)
        mb_rec.pop(0)
        mb_sent.pop(0)
        
    # Clear the plot and plot new data
    ax.clear()
    ax.plot(timestamps, mb_rec, label='MB Received')
    ax.plot(timestamps, mb_sent, label='MB Sent')
    
    # Add legend to the plot
    ax.legend()
    
    # Label X and Y axes
    ax.set_xlabel('Time')
    ax.set_ylabel('MB')
    
    # Update last counters
    last_rec = bytes_rec
    last_sent = bytes_sent

# Initialize the plot
fig, ax = plt.subplots()
plt.title("Real-Time Bandwidth Utilization")

# Set up the animation
ani = FuncAnimation(fig, update_data, interval=1000)

# Display the plot
plt.show()

print("use Command 'python bandwidth.py'")