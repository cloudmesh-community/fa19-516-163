# Datacenter research

**Data center**: IU Bloomington  
**Organization**: Indiana University  
**Location**: Bloomington, IN, USA  
**Year Built**: 2009 [1]  


**IT Load**: `3300 kW.`  

The IU Datacenter has 2, 2200 horsepower diesel generators for backup power [1].
We can assume these provide sufficient power to keep the Datacenter systems 
running. This can give us a very rough idea of the Datacenter load.

```
2 generators * 2200 hp/generator * 0.75 kW/hp = 3300 kW. 
```


**Electricity Cost**: `$.10/kWh.`  

I estimated this value from the latest published Duke Energy rates for high load
factor consumers in Indiana [2]. 


**Yearly Cost**: `$2.89MM/yr.` 

Annualize the aggregate IT Load and the Eletricty Cost:

```
3300 kW * $0.10/kWh * 24 hr/day * 365 day/yr = $2.89MM/yr.
```


**Yearly CO2 Footprint (tons)**: `26336 ton/yr.` 

The U.S. EIA has determined that Indiana's aggregate CO2 emissions are 
1822 lbs/MWh (1.822 lbs/kWh) [3]. 

```
3300 kW * 1.822 lbs/kWh * 0.0005 ton/lb * 24 hr/day * 365 day/yr = 26336 ton/yr.
```


**Yearly CO2 Footprint (cars)**: `5726 car/yr.` 

The U.S. EPA estimates that the average passenger car emits 4.6 tons of CO2 per 
year [4].

```
26336 ton/yr / 4.6 ton/car = 5726 car/yr
```

**References**  

1. Nolan, B. (2017, Oct 23). Indiana University Data Center serves as 
university's technology hub. <https://news.iu.edu/stories/2017/10/iu/inside/23-data-center.html>
2. Duke Energy Indiana. (2018, August 22). Rate HLF -- Schedule for High Load 
Factor Service. <https://www.duke-energy.com/_/media/pdfs/for-your-home/rates/electric-in/ratehlf.pdf?la=en>
3. U.S. Energy Information Administration. (2019, January 8). Indiana State 
Electricty Profile, 2017. <https://www.eia.gov/electricity/state/indiana/>
4. U.S. Environmental Protection Agency. (2018, March). Greenhouse Gas Emissions
from a Typical Passenger Vehicle. <https://www.epa.gov/greenvehicles/greenhouse-gas-emissions-typical-passenger-vehicle>