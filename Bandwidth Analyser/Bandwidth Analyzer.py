import time
import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle, Wedge
import subprocess
import platform

# Lists to store timestamps and data
timestamps = []
mb_rec = []
mb_sent = []
latencies = []

# Get initial network I/O counters and start time
last_rec = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
start_time = time.time()

# Function to calculate ping latency
def ping_latency():
    try:
        host = "8.8.8.8"  # Google DNS for latency check
        param = "-n" if platform.system().lower() == "windows" else "-c"
        command = ["ping", param, "1", host]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Parse the output to get latency
        for line in result.stdout.splitlines():
            if "time=" in line:
                time_ms = line.split("time=")[1].split()[0].replace("ms", "")
                return float(time_ms)
    except Exception:
        return None  # Return None if ping fails

# Function to draw an analog gauge
def draw_gauge(ax, value, max_value, label, color):
    ax.clear()
    ax.add_patch(Wedge((0, 0), 1, 0, 180, width=0.3, color="lightgray"))
    ax.add_patch(Wedge((0, 0), 1, 0, min(180, value / max_value * 180), width=0.3, color=color))
    ax.add_patch(Circle((0, 0), 0.7, color="white"))
    ax.text(0, -0.1, f"{value:.2f}", ha="center", va="center", fontsize=10, color=color)
    ax.text(0, -0.4, label, ha="center", va="center", fontsize=8)
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-0.2, 1.2)
    ax.axis("off")

# Update data for real-time visualization
def update_data(i):
    global last_rec, last_sent
    net_io = psutil.net_io_counters()
    bytes_rec = net_io.bytes_recv
    bytes_sent = net_io.bytes_sent
    
    new_rec = (bytes_rec - last_rec) / 1024 / 1024
    new_sent = (bytes_sent - last_sent) / 1024 / 1024
    
    elapsed_time = time.time() - start_time
    timestamps.append(elapsed_time)
    mb_rec.append(new_rec)
    mb_sent.append(new_sent)

    latency = ping_latency()
    if latency is not None:
        latencies.append(latency)
    else:
        latencies.append(float('nan'))
    
    if len(timestamps) > 600:
        timestamps.pop(0)
        mb_rec.pop(0)
        mb_sent.pop(0)
        latencies.pop(0)
        
    ax_graph.clear()
    ax_graph.plot(timestamps, mb_rec, label='MB Received', color='blue')
    ax_graph.plot(timestamps, mb_sent, label='MB Sent', color='green')
    ax_graph.plot(timestamps, latencies, label='Ping Latency (ms)', color='red')
    ax_graph.legend(loc="upper left")
    ax_graph.set_xlabel('Elapsed Time (s)')
    ax_graph.set_ylabel('MB / Latency (ms)')
    ax_graph.set_ylim(0, 10)  # Fixed Y-axis range
    ax_graph.grid(True)
    
    draw_gauge(ax_gauge1, new_rec, 5, "MB Received", "blue")
    draw_gauge(ax_gauge2, new_sent, 5, "MB Sent", "green")
    draw_gauge(ax_gauge3, latency if latency else 0, 500, "Latency (ms)", "red")
    
    last_rec = bytes_rec
    last_sent = bytes_sent

# Adjust the layout for gauges and graph
fig = plt.figure(figsize=(10, 8))

# Create subplots: 1 row for gauges, 1 row for graph
ax_gauge1 = plt.subplot2grid((3, 3), (0, 0))
ax_gauge2 = plt.subplot2grid((3, 3), (0, 1))
ax_gauge3 = plt.subplot2grid((3, 3), (0, 2))
ax_graph = plt.subplot2grid((3, 3), (1, 0), colspan=3, rowspan=2)

plt.subplots_adjust(hspace=0.5, wspace=0.3)
plt.suptitle("Real-Time Bandwidth and Latency Monitor")

# Set up the animation
ani = FuncAnimation(fig, update_data, interval=1000)

# Display the plot
plt.show()

print("Use Command 'python bandwidth.py'")
