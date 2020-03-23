#
#
# script to download the ERA5 10m winds
#
#
#
from ecmwfapi import ECMWFDataServer

for YEAR in range(1979,2000):
    for MON in range(1,13):
        MONfil = str(MON).zfill(2) # make 1 display as 01 etc.
        server = ECMWFDataServer()
        server.retrieve({
                'class'     : "ea",
                'stream'    : "oper",
                'levtype'   : "sfc",
                'param'     : "134.128/165.128/166.128/167.128/246.228/247.228",
                'expver'    : "1",
                'dataset'   : "era5",
                'step'      : "0",
                'grid'      : "0.28/0.28",
                'time'      : "00:00:00/03:00:00/06:00:00/09:00:00/12:00:00/15:00:00/18:00:00/21:00:00",
                'date'      : str(YEAR)+"-" + MONfil + "-01/to/"+str(YEAR)+"-" + MONfil + "-31",
                'type'      : "an",
                'gaussian'  : "regular",
                'resol'     : "av",
                'area'      : "90/-45/30/40",
                'grid'      : "320",
                'format'    : "netcdf",
                'target'    : "ERA5_3hr_" + str(YEAR) + "_" + MONfil+ "_DET.nc"
})
