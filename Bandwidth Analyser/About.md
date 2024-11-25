---

# Real-Time Bandwidth and Latency Monitor

A Python-based tool that provides real-time monitoring of network bandwidth usage and ping latency. This project visualizes data using animated analog gauges and a graph, offering an intuitive understanding of network activity.

---

## Features

- **Bandwidth Monitoring:**
  - Displays MB received and sent in real time.
- **Latency Monitoring:**
  - Measures ping latency to a specified server (default: Google DNS `8.8.8.8`).
- **Visual Representation:**
  - Analog gauges for bandwidth (received/sent) and ping latency.
  - Line graph showing historical data for MB received, MB sent, and latency.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/real-time-bandwidth-monitor.git
   cd real-time-bandwidth-monitor
   ```

2. **Install Dependencies**:
   - Ensure Python is installed (v3.6 or later).
   - Install required libraries:
     ```bash
     pip install matplotlib psutil
     ```

---

## Usage

1. Run the script:
   ```bash
   python bandwidth_analyzer.py
   ```
2. The tool displays:
   - Real-time analog gauges for bandwidth (received, sent) and latency.
   - A graph showing the historical trends.

---

## Visualization Layout

- **First Row**: 
  - Analog gauges:
    - **MB Received** (Blue)
    - **MB Sent** (Green)
    - **Ping Latency** (Red)
- **Second Row**:
  - Graph depicting:
    - Historical data for MB Received.
    - Historical data for MB Sent.
    - Ping Latency in milliseconds.

---

## Dependencies

- `matplotlib`: For plotting gauges and graphs.
- `psutil`: To retrieve network I/O statistics.
- `subprocess` & `platform`: For executing system-specific ping commands.

---

## File Structure

```
real-time-bandwidth-monitor/
├── bandwidth_analyzer.py    # Main script
├── README.md                # Project documentation
```

---

## Notes

- By default, the tool pings Google's DNS server (`8.8.8.8`) to measure latency. You can modify this in the `ping_latency()` function.
- The graph supports up to 600 data points before older data is discarded.

---

## Future Improvements

- Add support for selecting a custom server for latency monitoring.
- Extend compatibility for non-default network interfaces.
- Save data logs to a file for later analysis.

---

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---
