
# This used to download files: "ERA5_3hr_TZ850_1980_01.nc" but they were actually six-hourly data with a 9pm thrown in...which was no use! so i've deleted them and now this script does midnight only data like is available in the hindcasts.

import cdsapi
# module load python/canopy-2.1.3 to get the cdsapi
c = cdsapi.Client()

for yr in range(1980,2019):
    for mnth in ['04','05','06','07','08','09','10']: #'01','02','03','10','11','12'
         r = c.retrieve(
            'reanalysis-era5-pressure-levels',
             {'variable':['geopotential','temperature','u_component_of_wind'],
                'pressure_level':'850',
                'product_type':'reanalysis',
                'year':str(yr),
                'month':mnth,
                'day':[
                    '01','02','03',
                    '04','05','06',
                    '07','08','09',
                    '10','11','12',
                    '13','14','15',
                    '16','17','18',
                    '19','20','21',
                    '22','23','24',
                    '25','26','27',
                    '28','29','30',
                    '31'
                    ],
                'time':[
                    '00:00',
                    ],
                'area':"80/-90/20/30", # N/W/S/E
                'format':'netcdf'
             })
        
         r.download('ERA5_midnight_TZu850_' +str(yr) + '_' + str(mnth) + '.nc')
