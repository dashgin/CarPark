# REST API for Car Parking

## Tools and Libraries

- Python 3.9.9
- Django 4.0
- Django REST Framework 3.13.0
- SQLite 3

## Endpoints
Driver:
+ GET /drivers/driver/ - output the list of drivers
+ GET /drivers/driver/?created_at__gte=10-11-2021 - output the list of drivers created after 10-11-2021
+ GET /drivers/driver/?created_at__lte=16-11-2021 - output the list of drivers created before 16-11-2021

+ GET /drivers/driver/<driver_id>/ - get information on a specific driver
+ POST /drivers/driver/ - create a new driver
+ UPDATE /drivers/driver/<driver_id>/ - driver editing
+ DELETE /drivers/driver/<driver_id>/ - remove the driver

Vehicle:
+ GET /vehicles/vehicle/ - output of the list of cars
+ GET /vehicles/vehicle/?with_drivers=yes - output the list of cars with drivers
+ GET /vehicles/vehicle/?with_drivers=no - output the list of cars without drivers

+ GET /vehicles/vehicle/<vehicle_id>/ - get information on a specific machine
+ POST /vehicles/vehicle/ - create a new machine
+ UPDATE /vehicles/vehicle/<vehicle_id>/ - edit the machine
+ POST /vehicles/set_driver/<vehicle_id>/ - put the driver in the car / get the driver out of the car
+ DELETE /vehicles/vehicle/<vehicle_id>/ - delete the machine

For running local and deployment: [SETUP.md](SETUP.md)