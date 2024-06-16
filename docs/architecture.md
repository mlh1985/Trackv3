# Architecture

## Overview

The Racetrack system is built using a Raspberry Pi and the Flask web framework. The system integrates hardware sensors and actuators for race management and tracking.

## Components

1. **Raspberry Pi:**
   - Controls the hardware sensors and actuators.
   - Runs the Flask web server.

2. **Flask Application:**
   - Provides the web interface for different user roles.
   - Manages race parameters and tracks race results.

3. **SQLite Database:**
   - Stores user data, race parameters, and race results.

## Hardware Integration

- **Sensors:** Detect the finish line for each lane.
- **Actuator:** Starts the race by releasing cars from the top of the track.

## Software Integration

- **Flask Routes:** Define the web endpoints and handle user requests.
- **Hardware Module:** Interacts with the GPIO pins to control sensors and actuators.
