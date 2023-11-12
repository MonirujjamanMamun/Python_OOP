from abc import ABC, abstractmethod
from datetime import datetime


class User:
    def __init__(self, name, email, nid) -> None:
        self.__id = 0
        self.__nid = nid
        self.name = name
        self.email = email
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError


class Rider(User):
    def __init__(self, name, id, email, nid, wallet, current_location) -> None:
        super().__init__(name, id, email, nid, wallet)
        self.current_location = current_location

    def display_profile(self):
        print(f'The name of rider {self.name} and email id is {self.email}')

    def request_ride(self, location, destination, wallet):
        self.loaction = location
        self.destination = destination
        self.wallet = wallet

    def load_cash(self, amount):
        if 0 < amount:
            self.wallet += amount


class Driver(User):
    def __init__(self, name, email, nid, current_location, wallet) -> None:
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = wallet

    def ride(self, ride):
        self.ride = ride


class Ride:
    def __init__(self, start_location, end_location, driver, estimated_fare) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = driver
        self.start_time = datetime.now()
        self.end_time = datetime.now()
        self.estimate_fare = estimated_fare

    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self):
        pass

    def end_ride(self, ride, amount):
        self.ride = ride
        self.amount = amount
