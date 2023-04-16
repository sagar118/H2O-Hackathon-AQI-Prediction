from h2o_wave import ui

pollutants = '''=
## More Information of Pollutants

<hr/>

Let's gain an understanding of the meaning behind some of the features in the dataset. What are their respective ranges and what significance do they hold?

<img style="float: right;" src="https://ww2.arb.ca.gov/sites/default/files/inline-images/human_hair_0.png" width=400 height=400 align="center" />
<!-- Credit: [California Air Resources Board](https://ww2.arb.ca.gov/resources/inhalable-particulate-matter-and-health) -->

*   `PM2.5`: 
    *   Fine particulate matter (PM2.5) is an air pollutant that is a concern for people's health when levels in air are high. 
    *   PM2.5 are tiny particles in the air that reduce visibility and cause the air to appear hazy when levels are elevated.
    *   Outdoor PM2.5 levels are most likely to be elevated on days with little or no wind or air mixing.
    *   These tiny particles or droplets in the air that are two and one half microns or less in width. Like inches, meters and miles, a micron is a unit of measurement for distance. There are about 25,000 microns in an inch.
    *   Most studies indicate PM2.5 at or below 12 μg/m3 is considered healthy with little to no risk from exposure. If the level goes to or above 35 μg/m3 during a 24-hour period, the air is considered unhealthy and can cause issues for people with existing breathing issues such as asthma. Prolonged exposure to levels above 50 μg/m3 can lead to serious health issues and premature mortality.
    *   [Fine Particles (PM 2.5) Questions and Answers](https://www.indoorairhygiene.org/pm2-5-explained/#:~:text=Most%20studies%20indicate%20PM2.,breathing%20issues%20such%20as%20asthma.) - Department of Health NY
    *   [PM2.5 Explained](https://www.indoorairhygiene.org/pm2-5-explained/#:~:text=Most%20studies%20indicate%20PM2.,breathing%20issues%20such%20as%20asthma.) - Indoor Air Hygiene Institute


*   `PM10`:
    *   PM10 includes particles less than 10 µm in diameter, PM2.5 those less than 2.5 µm. *Therefore, PM2.5 comprises a portion of PM10.*
    *   PM10 and PM2.5 often derive from different emissions sources, and also have different chemical compositions. 
    *   Emissions from combustion of gasoline, oil, diesel fuel or wood produce much of the PM2.5 pollution found in outdoor air, as well as a significant proportion of PM10. 
    *   PM10 also includes dust from construction sites, landfills and agriculture, wildfires and brush/waste burning, industrial sources, wind-blown dust from open lands, pollen and fragments of bacteria.
    *   [Inhalable Particulate Matter and Health (PM2.5 and PM10)](https://ww2.arb.ca.gov/resources/inhalable-particulate-matter-and-health) - California Air Resources Board

*   `O3`:
    *   Ozone is a pale blue gas, soluble in water and non-polar solvents with specific sharp odor somewhat resembling chlorine bleach.
    *   Ozone cracking in car tires, gaskets, O-rings is caqused by attack of ozone on any polymer possessing olefinic or double bonds within its chain structure.

*   `CO`:
    *   Carbonous oxide, is a colorless, odorless and tasteless gas which is slightly lighter than air.
    *   It is highly toxic to humans and animals in higher quantities. Mainly formed by incomplete combustion of carbon containing fuels.

*   `SO2`:
    *   It is the chemical compound produced by volcanoes and in various industrial processes and are also a precursor to particulates in the atmosphere. 

*   Revised National Ambient Air Quality Standards (NAAQS) [NAAQS Notification dated 18th November, 2009] [(Refer Page 90-97)](https://cpcb.nic.in/upload/NAAQS_2019.pdf):


|S. No.|Pollutants|Time Weighted Average|Concentration in Ambient Air| |
|:---:|:---:|:---:|:---:|:---:|
| | | |Industrial,Residential, Rural and other Areas|Ecologically Sensitive Area (notified by Central Government)|
|1|Sulphur Dioxide (SO2)|Annual|50|20|
| | |24 Hours|80|80|
|2|Nitrogen Dioxide (NO2)|Annual|40|30|
| | |24 Hours|80|80|
|3|Particulate Matter (PMIO)|Annual|60|60|
| | |24 Hours|100|100|
|4|Particulate Matter (PM2.5)|Annual|40|40|
| | |24 Hours|60|60|
|5|Ozone (03), pg/m3|8 hours|100|100|
| | |1 hours|180|180|
|6|Carbon Monoxide (CO),|8 Hours|2|2|
| | |1 Hour|4|4|
'''

appendix = ui.markdown_card(
    box='app_content',
    title='',
    content=pollutants
)

'''
<div>
<div style="float: left; width: 60%;">

</div>

<div style="float: right; width: 40%;">

</div>
</div>

<div>
</div>
'''