# Datacenters

## Carbon Footprint

**Data center**: IU Bloomington  
**Organization**: Indiana University  
**Location**: Bloomington, IN, USA  
**Year Built**: 2009 [1]

**IT Load**: `3300 kW.`

The IU Datacenter has 2, 2200 horsepower diesel generators for backup power [1].
Lets assume these can provide sufficient power to keep the Datacenter up and
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

The U.S. EIA has determined that Indiana's aggregate CO2 emissions are 1822
lbs/MWh (1.822 lbs/kWh) [3].

```
3300 kW * 1.822 lbs/kWh * 0.0005 ton/lb * 24 hr/day * 365 day/yr = 26336 ton/yr.
```

**Yearly CO2 Footprint (cars)**: `5726 car/yr.`

The U.S. EPA estimates that the average passenger car emits 4.6 tons of CO2 per
year [4].

```
26336 ton/yr / 4.6 ton/car = 5726 car/yr
```

### References

1. Nolan, B. (2017, Oct 23). Indiana University Data Center serves as
   university's technology hub.
   <https://news.iu.edu/stories/2017/10/iu/inside/23-data-center.html>
2. Duke Energy Indiana. (2018, August 22). Rate HLF -- Schedule for High Load
   Factor Service.
   <https://www.duke-energy.com/_/media/pdfs/for-your-home/rates/electric-in/ratehlf.pdf?la=en>
3. U.S. Energy Information Administration. (2019, January 8). Indiana State
   Electricty Profile, 2017. <https://www.eia.gov/electricity/state/indiana/>
4. U.S. Environmental Protection Agency. (2018, March). Greenhouse Gas Emissions
   from a Typical Passenger Vehicle.
   <https://www.epa.gov/greenvehicles/greenhouse-gas-emissions-typical-passenger-vehicle>

## Renewable Energy: Geothermal

Geothermal energy production uses steam or hot water from beneath the earth's
surface to drive electrical turbines and generate electricity [1]. The spent
water is pumped back under the surface where it is reheated naturally. This form
of energy production is renewable because most/all of the heat energy is dervied
from the liquid upper mantle of the earth's core.

Like many other renewables, the economic viability of geothermal energy
production is highly location-dependant. Producers must drill wells in order to
access and return geothermally heated water. The shallowest wells can be drilled
where the liquid mantel rises furthest towards the surface. This phenomenon
predominantly occurs near seismic boundaries.

As of 2018 the United States leads the world in geothermal energy production,
with an installed capacity of ~3600 MW [2]. As a share of national energy
production Kenya leads with just over 50%, followed by Iceland with 30%.

### References

1. Union of Concerned Scientists. 2014.
   [How Geothermal Energy Works](https://www.ucsusa.org/clean_energy/our-energy-choices/renewable-energy/how-geothermal-energy-works.html).
2. Wikipedia. 2019.
   [Geothermal power](https://en.wikipedia.org/wiki/Geothermal_power).

## Geothermal Energy Casestudy: Iceland

Iceland is an excellent case study in the use of geothermal energy. Iceland is
located on the Mid-Atlantic Ridge, the divergence point of the North American
and Eurasian plates [1]. The island itself is a product of seismic activity. As
of 2013 geothermal sources account for nearly one-third of Iceland's electrical
energy production [2]. Geothermal heat sources have a number of other uses in
Iceland, such as heating homes and swimming pools, melting snow on roads and
sidewalks, and drying fish. 

Iceland's subarctic climate provides a natural supply of cold air that can be
used in cooling. These resources make Iceland an ideal location for datacenter
construction, with Power Usage Effectiveness (PUE) approaching 1.07 and a Total
Cost of Ownership (TCO) 40% lower than comparable datacenters in the United
States [3].

### References

1. Wikipedia. 2019.
   [Geology of Iceland](https://en.wikipedia.org/wiki/Geology_of_Iceland).
2. Orkustofnon (National Energy Authority).
   [Electricy Generation](https://nea.is/geothermal/electricity-generation/).
3. National Power Company of Iceland.
   [Data Centers in Iceland](https://www.landsvirkjun.com/productsservices/energyproducts/data-centers/data-centers-in-iceland/).
