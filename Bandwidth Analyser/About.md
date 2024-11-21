# Real-Time Bandwidth Monitor in Python

## Overview

The **Real-Time Bandwidth Monitor** is a Python application that monitors and displays your system's network bandwidth utilization in real-time. It uses the `psutil` library to fetch network statistics and `matplotlib` to dynamically plot the data.

The tool provides a visual representation of data received and sent over the network, making it useful for analyzing network performance or diagnosing potential issues.

---

## Features

- **Real-Time Updates:** Refreshes every second to display current bandwidth usage.
- **Dynamic Plotting:** Uses `matplotlib` to graph MB received and sent over time.
- **Data Retention:** Maintains the last 600 data points for a smooth display of recent activity.

---

## Prerequisites

Before running the application, ensure you have the following installed:

1. **Python 3.7 or above**
2. Required Python libraries:
   - `psutil`
   - `matplotlib`

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/real-time-bandwidth-monitor.git
   cd real-time-bandwidth-monitor
   ```

2. Install the dependencies:
   ```bash
   pip install psutil matplotlib
   ```

---

## Usage

1. Run the script:
   ```bash
   python bandwidth.py
   ```

2. A real-time graph will appear showing:
   - **MB Received:** Data received over the network.
   - **MB Sent:** Data sent over the network.

3. Close the graph window to stop monitoring.

---

## Code Explanation

- **Data Collection:**  
  Uses `psutil.net_io_counters()` to retrieve the bytes received and sent on the network interface. It calculates differences between successive calls to derive bandwidth.

- **Dynamic Graph Updates:**  
  `matplotlib.animation.FuncAnimation` updates the graph every second with the new data.

- **Data Smoothing:**  
  Retains only the last 600 data points for plotting to ensure the graph is clear and manageable.

---

## Example Output

The application plots two lines on the graph:
- **Blue Line:** Represents the MB of data received.
- **Orange Line:** Represents the MB of data sent.

---

## Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

---


## Author

[Prince Kumar Singh](https://github.com/Prince11038) 
Feel free to reach out for questions or feedback!
