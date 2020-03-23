# before you do this you need to do module load python/canopy-2.1.3
import cdsapi

# the 31st day of feb is the 2nd march etc (it just makes sure all the months of data are downloaded and complete)
for YEAR in range(1989,1991):
    for MONTH in range(11,13):
        m = str(MONTH).zfill(2) # make sure it is 01, 02 etc
        y = str(YEAR)
        c = cdsapi.Client()
        r = c.retrieve('reanalysis-era5-single-levels',{'variable':'surface_solar_radiation_downwards',
                                                        'product_type':'reanalysis',
                                                        'year':[y],
                                                        'month':[m],
                                                        'day':['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'],
                                                        'time':['00:00','03:00','06:00','09:00','12:00','15:00','18:00','21:00'],
                                                        'area' : [90,-45,29.8,40.3],# N/W/S/E shoudl be 30 and 40 but trying to get that last gridbox in the same as the wind and temp!
                                                        'grid'      : "0.28/0.28",
                                                        'gaussian': "regular",
                                                        'resol'     : "av",
                                                        'grid'      : "320",
                                                        'format':'netcdf'}) # same area as seasonal forecasts
        r.download('ERA5_3hr_RSDS_' +str(y) + '_' + str(m) + '_DET.nc')
