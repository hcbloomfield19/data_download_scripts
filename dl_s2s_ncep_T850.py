#!/usr/bin/env python
import numpy as np
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()


# check CF of PF down the bottom to get all the members!!

# get all of the january data
for YEAR in range(1999,2011):
    for MONTH in [11,12,1,2,3]:
        qmonth = str(MONTH).zfill(2) # in some months 9 starts are available, i am only using the first 8 for each month. 
        if MONTH == 1:
            day_list = np.linspace(1,31,31)
        if MONTH == 2:
            day_list = np.linspace(1,28,28) # no leap years
        if MONTH == 3:
            day_list = np.linspace(1,31,31)
        if MONTH == 11:
            day_list = np.linspace(1,30,30)
        if MONTH == 12:
            day_list = np.linspace(1,31,31)


        for DAY in day_list: # these are the days the fcast starts at.
            server.retrieve({
            "class": "s2",
            "dataset": "s2s",
                "date": "2011-03-01",
            "expver": "prod",
                "hdate": str(YEAR) + "-" +str(MONTH).zfill(2) + "-" + str(np.int(DAY)).zfill(2),
                "area":[65,-20,30,30],# N/W/S/E
            "number": "1/2/3",
            "levtype": "pl",
            "origin": "kwbc",
            "param": "130",
            "step": "0-24/24-48/48-72/72-96/96-120/120-144/144-168/168-192/192-216/216-240/240-264/264-288/288-312/312-336/336-360/360-384/384-408/408-432/432-456/456-480/480-504/504-528/528-552/552-576/576-600/600-624/624-648/648-672/672-696/696-720/720-744/744-768/768-792/792-816/816-840/840-864/864-888/888-912/912-936/936-960/960-984/984-1008/1008-1032/1032-1056", # 46 Day fcast
            "stream": "enfh",
            "time": "00:00:00",
            "type": "cf",
            "format": 'netcdf',
            "target": "ncep_hc_T850_cf_20110301_" + str(YEAR) + str(MONTH).zfill(2) + str(np.int(DAY)).zfill(2) + ".nc",
})
