import time
import random

def get_traffic_data():
    """
    Simulates real-time vehicle count per lane.
    Returns a dictionary with lane-wise vehicle counts.
    """
    return {
        'North': random.randint(5, 50),
        'South': random.randint(5, 50),
        'East': random.randint(5, 50),
        'West': random.randint(5, 50)
    }

def adjust_signal_timing(traffic_data):
    """
    Adjusts green light duration based on vehicle density.
    """
    max_traffic = max(traffic_data, key=traffic_data.get)
    green_time = min(60, max(15, traffic_data[max_traffic] * 1.5))
    return max_traffic, green_time

def traffic_light_control():
    """
    Runs the AI-based traffic light control system.
    """
    while True:
        traffic_data = get_traffic_data()
        max_lane, green_time = adjust_signal_timing(traffic_data)
        
        print("\nTraffic Data:", traffic_data)
        print(f"Green Light for {max_lane} lane for {green_time} seconds")
        time.sleep(green_time)  # Simulating the green signal duration
        print("Switching lights...")
        time.sleep(5)  # Red signal duration before switching

# Run the Traffic Light Control System
if __name__ == "__main__":
    traffic_light_control()
