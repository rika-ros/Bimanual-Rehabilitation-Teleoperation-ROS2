# Bimanual Rehabilitation Teleoperation (ROS2 - Interbotix RX200)

This repository contains a ROS 2 based extension of the original bimanual assist-as-needed rehabilitation system. It replaces Novint Falcon devices with dual Interbotix RX200 robotic arms for simulating and controlling upper-limb rehab tasks, while preserving the core logic of assist-as-needed control.

> This repository contains two ROS 2 workspaces:
>
> - `interbotix_ws/` — the base workspace containing Interbotix ROS 2 packages used to simulate and move the dual RX200 robotic arms.
> - `rika_ws/` — the extended workspace that adapts the original bimanual rehabilitation control logic from ROS1 (with Novint Falcons) to ROS2, and includes the custom Gazebo world, control nodes, and assist-as-needed logic.
>
> Integration between the two workspaces is currently a work in progress, with the goal of combining RX200 motion control and bimanual shared-control logic into a unified teleoperation framework.


## Features

- Bimanual teleoperation using dual Interbotix RX200 arms
- Assist-as-needed (AAN) shared control based on game theory
- Modular ROS 2 (Humble) architecture
- Realistic simulation using Gazebo
- Migrated from ROS 1 + Falcon to ROS 2 + RX200


## Project Structure
```
BIMANUAL-REHABILITATION-TELEOPERATION-ROS2/
├── interbotix_ws/
│   ├── build/
│   ├── install/
│   ├── log/
│   └── src/
├── rika_ws/
│   └── src/
│       └── bimanual_pkg/
│           ├── bimanual_pkg/      
│           ├── launch/
│           ├── resource/
│           ├── test/
│           ├── urdf/
│           ├── worlds/
│           ├── package.xml
│           ├── setup.cfg
│           ├── setup.py
├── .gitignore
├── README.md
```

## Requirements

- Ubuntu 20.04
- ROS 2 Humble
- [Interbotix ROS 2 packages - already inside repo](https://docs.trossenrobotics.com/interbotix_xsarms_docs/ros_interface/ros2/overview.html)
- Gazebo 11+
- Python 3.8+
- Required ROS 2 packages:
  - `rclcpp`, `sensor_msgs`, `geometry_msgs`, `controller_manager`, `gazebo_ros`, etc.


## Setup Instructions

1. Clone the repository

```
git clone https://github.com/rika-ros/Bimanual-Rehabilitation-Teleoperation-ROS2.git
cd Bimanual-Rehabilitation-Teleoperation-ROS2
```

```

2. Build and source the workspaces 

```
colcon build
source /opt/ros/humble/setup.bash
source /usr/share/gazebo/setup.sh
source ~/Bimanual-Rehabilitation-Teleoperation-ROS2/rika_ws/install/setup.bash
source ~/Bimanual-Rehabilitation-Teleoperation-ROS2/interbotix_ws/install/setup.bash
```

## Running the Simulation

1. Launch the rx200

```
ros2 launch interbotix_xsarm_dual xsarm_dual.launch
```

2. Launch gazebo file

```
ros2 launch bimanual_pkg floating_box_launch.launch.py
```


## Contact

For queries:

📧 rchps.05@gmail.com/ashikachandavarkar@gmail.com

📂 GitHub: [rika-ros](https://github.com/rika-ros)