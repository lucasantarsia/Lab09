from database.DAO import DAO
from model.model import Model
from datetime import datetime

def tstModel():
    mymodel = Model()

    airports = DAO.getAllAirports()

    flights = DAO.getAllFlights()


if __name__ == '__main__':
    tstModel()
