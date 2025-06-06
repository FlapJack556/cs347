# IoT HTL - Component-Level Functions (Python Implementation Skeletons)

import random
import time
import statistics

# Mock sensor data classes
class SensorData:
    def __init__(self, sensor_id, data, timestamp):
        self.sensor_id = sensor_id
        self.data = data
        self.timestamp = timestamp

class Sensor:
    def __init__(self, sensor_id, sensor_type):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type

    def read_data(self):
        # Simulate sensor reading with dummy values
        return SensorData(self.sensor_id, random.uniform(0, 100), time.time())

    def self_test(self):
        return random.choice([True, True, True, False])  # Mostly true

# 5.3.1 SensorModule
class SensorModule:
    def __init__(self):
        self.sensors = [
            Sensor("lidar01", "LiDAR"),
            Sensor("cam01", "Camera"),
            Sensor("radar01", "Radar")
        ]

    def collect_data(self):
        """Gathers raw sensor data from all physical sensors."""
        data = {}
        for sensor in self.sensors:
            reading = sensor.read_data()
            print(f"Collected data from {sensor.sensor_id}: {reading.data:.2f}")
            data[reading.sensor_id] = reading
        return data

    def self_test(self):
        """Performs diagnostic check on sensor hardware."""
        results = {sensor.sensor_id: sensor.self_test() for sensor in self.sensors}
        for sid, passed in results.items():
            print(f"Sensor {sid} self-test: {'PASSED' if passed else 'FAILED'}")
        return all(results.values())

# 5.3.2 SensorFusion
class SensorFusion:
    def __init__(self):
        self.sensors = []
        self.data_map = {}  # sensor_id -> list of SensorData
        self.environment_map = {}

    def validate_integrity(self):
        """Checks consistency of combined sensor data."""
        for sensor_id, readings in self.data_map.items():
            if not readings:
                print(f"Integrity check failed: No data for sensor {sensor_id}")
                return False
        print("All sensor data passed integrity check.")
        return True

    def handle_sensor_reading(self, event):
        """Triggered by new sensor reading."""
        if event.sensor_id not in self.data_map:
            self.data_map[event.sensor_id] = []
        self.data_map[event.sensor_id].append(event)
        print(f"Received reading from {event.sensor_id}: {event.data:.2f}")

    def aggregate_data(self):
        """Selects most recent data from each sensor."""
        latest_data = {}
        for sensor_id, readings in self.data_map.items():
            if readings:
                latest = max(readings, key=lambda r: r.timestamp)
                latest_data[sensor_id] = latest
                print(f"Latest reading from {sensor_id}: {latest.data:.2f} at {latest.timestamp}")
        return latest_data

    def fuse_sensor_data(self):
        """Executes fusion logic to update environment map."""
        aggregated_data = self.aggregate_data()
        values = [reading.data for reading in aggregated_data.values()]
        if not values:
            print("No data to fuse.")
            return

        fused_average = statistics.mean(values)
        print(f"Fused data average: {fused_average:.2f}")
        
        self.environment_map = {
            "fused_average": fused_average,
            "individual_readings": {sid: r.data for sid, r in aggregated_data.items()}
        }

# 5.3.3 PerceptionModule
class PerceptionModule:
    def handle_fused_data(self, event):
        pass

    def detect_objects(self):
        pass

    def detect_lanes(self):
        pass

    def classify_traffic_sign(self):
        pass

    def track_objects(self):
        pass

# 5.3.4 PlanningModule
class PlanningModule:
    def handle_perception_update(self, event):
        pass

    def handle_vehicle_state(self, event):
        pass

    def decide_behavior(self):
        pass

    def plan_trajectory(self):
        pass

    def evaluate_safety(self):
        pass

    def check_for_collision(self, trajectory):
        pass

    def detect_lane_change(self):
        pass

    def plan_route(self):
        pass

    def publish_plan(self, bus):
        pass
        
`# Supporting classes for simulation
class PIDController:
    def __init__(self, kp=1.0, ki=0.0, kd=0.0):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.previous_error = 0
        self.integral = 0

    def compute(self, target, current):
        error = target - current
        self.integral += error
        derivative = error - self.previous_error
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.previous_error = error
        return output

class VehicleState:
    def __init__(self, speed=0.0, angle=0.0):
        self.speed = speed
        self.steering_angle = angle

class TrajectoryPlanEvent:
    def __init__(self, trajectory_points):
        self.trajectory_points = trajectory_points

class EventBus:
    def publish(self, event_name, data):
        print(f"Event Published: {event_name} -> {data}")

class ReceivedMessage:
    def __init__(self, raw_data, source):
        self.raw_data = raw_data
        self.source = source`
        
# 5.3.5 ControlModule
class ControlModule:
    def handle_plan(self, event):
        pass

    def execute_trajectory(self):
        pass

    def adjust_steering_angle(self, target_angle):
        pass

    def adjust_speed(self, target_speed):
        pass

    def apply_brakes(self, force):
        pass

    def read_vehicle_sensors(self):
        pass

    def detect_override(self):
        pass

    def publish_vehicle_state(self, bus):
        pass

# 5.3.6 CommunicationModule
class CommunicationModule:
    def broadcast_message(self, message):
        pass

    def receive_message(self):
        pass

    def parse_and_dispatch(self, msg):
        pass

    def send_data_to_cloud(self, data):
        pass

# 5.3.7 SoftwareUpdateManager
class SoftwareUpdateManager:
    def check_for_updates(self):
        pass

    def download_update(self):
        pass

    def validate_update(self, file_path):
        pass

    def install_update(self, file_path):
        pass

    def rollback(self):
        pass

# 5.3.8 InterfaceManager
class InterfaceManager:
    def handle_system_event(self, event):
        pass

    def render_dashboard(self):
        pass

    def render_technician_ui(self, ui_type):
        pass

    def handle_user_input(self, event):
        pass

# 5.3.9 Abstract Sensor Class
class BaseSensor:
    def initialize(self):
        pass

    def get_status(self):
        pass

    def read_data(self):
        pass

    def run_selftest(self):
        pass

# 5.3.10 Specific Sensor Subclasses
class LiDAR(BaseSensor):
    def read_data(self):
        pass

    def initialize(self):
        pass

    def run_selftest(self):
        pass

    def publish_reading(self):
        pass

class Camera(BaseSensor):
    def read_data(self):
        pass

    def initialize(self):
        pass

    def run_selftest(self):
        pass

    def publish_reading(self):
        pass

class Radar(BaseSensor):
    def read_data(self):
        pass

    def initialize(self):
        pass

    def run_selftest(self):
        pass

    def publish_reading(self):
        pass
