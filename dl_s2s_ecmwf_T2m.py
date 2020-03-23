#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()

# get all of the Nov-Mar data from the hindcast period
for YEAR in range(1996,2017):
    for MONTH in [11,12,1,2,3]:
        qmonth = str(MONTH).zfill(2) # in some months 9 starts are available, i am only using the first 8 for each month. 
        if MONTH == 1:
            day_list = [4,7,11,14,18,21,25,28]
        if MONTH == 2:
            day_list = [1,4,8,11,15,18,22,25]#,29]
        if MONTH == 3:
            day_list = [3,7,10,14,17,21,24,28]#,31]
        if MONTH == 11:
            day_list = [3,7,10,14,17,21,24,28]
        if MONTH == 12:
            day_list = [1,5,8,12,15,19,22,26]# ,29]

        for DAY in day_list: # these are the days the fcast starts at.
            server.retrieve({
            "class": "s2",
            "dataset": "s2s",
            "date": "2016-" +str(MONTH).zfill(2) + "-" + str(DAY).zfill(2),
            "expver": "prod",
            "hdate": str(YEAR) + "-" +str(MONTH).zfill(2) + "-" + str(DAY).zfill(2),
            "area":[90,-45,29.8,40.3],# N/W/S/E
            "number": "1/2/3/4/5/6/7/8/9/10",
            "levtype": "sfc",
            "origin": "ecmf",
            "param": "167",
            "step": "0-24/24-48/48-72/72-96/96-120/120-144/144-168/168-192/192-216/216-240/240-264/264-288/288-312/312-336/336-360/360-384/384-408/408-432/432-456/456-480/480-504/504-528/528-552/552-576/576-600/600-624/624-648/648-672/672-696/696-720/720-744/744-768/768-792/792-816/816-840/840-864/864-888/888-912/912-936/936-960/960-984/984-1008/1008-1032/1032-1056/1056-1080/1080-1104", # 46 Day fcast
            "stream": "enfh",
            "time": "00:00:00",
            "type": "cf", # cf or pf 
            "format": 'netcdf',
            "target": "ecmwf_hc_T2m_cf_2016"+str(MONTH).zfill(2) + str(DAY).zfill(2) + '_' + str(YEAR) + str(MONTH).zfill(2) + str(DAY).zfill(2) + ".nc",
})
