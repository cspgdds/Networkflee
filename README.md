# Networkflee
This project is an inspiration of the Hackday at the Collaborations Workshop 2018 organised by SSI and work is in progress.

## Overview
FLEE is an agent-based simulation toolkit which is purpose-built for simulating the movement of individuals across geographical locations. Flee is currently used primarily for modelling the movements of refugees. It uses data from the [Armed Conflict Location & Event Data Project](http://data2.unhcr.org/en/situations) (ACLED) to model the migration of refugees within a conflict zone and data from the [United Nations High Commission for Refugees](http://data2.unhcr.org/en/situations) (UNHCR) to identify locations of camps. 

After obtaining conflict locations and neighbouring camps, prediction of refugee movements requires network maps. As we have several locations, identifying connection routes, distances, constructing and visualising these links becomes time consuming. Hence, manually constructed network maps are proven to be inefficient at this moment. 

Automated network map construction - Networkflee - allows to detect route connections and distances between locations, as well as constuct visual representation. It requires a dataset (e.g. locations.csv) with location names and GPS coordinates in csv format, which is also used for simulation purposes at the later stage. 

## Network map construction
To construct automated network map, we use locations.csv file in the following format 

**locations.csv**
<table>
  <tr>
    <td>name</td>
    <td>region</td>
    <td>country</td>
    <td>lat</td>
    <td>long</td>
    <td>location_type</td>
    <td>conflict_date</td>
    <td>population/capacity</td>
  </tr>
  <tr>
    <td>A</td>
    <td>AA</td>
    <td>ABC</td>
    <td>xxx</td>
    <td>xxx</td>
    <td>conflict_zone</td>
    <td>yyyy/mm/dd</td>
    <td>xxx</td>
  </tr>
  <tr>
    <td>B</td>
    <td>BB</td>
    <td>ABC</td>
    <td>xxx</td>
    <td>xxx</td>
    <td>conflict_zone</td>
    <td>yyyy/mm/dd</td>
    <td>xxx</td>
  </tr>
  <tr>
    <td>Z</td>
    <td>ZZ</td>
    <td>ZZZ</td>
    <td>xxx</td>
    <td>xxx</td>
    <td>camp</td>
    <td>-</td>
    <td>xxx</td>
  </tr>
  <tr>
    <td>N</td>
    <td>NN</td>
    <td>ABC</td>
    <td>xxx</td>
    <td>xxx</td>
    <td>town</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td>…</td>
    <td>…</td>
    <td>…</td>
    <td>…</td>
    <td>…</td>
    <td>…</td>
    <td>…</td>
    <td>…</td>
  </tr>
</table>

and use pyroutelib3 package to identify distances between cities.

### Todo
- [x] API route-to-route
- [x] Single conflict_zone -> camp route
- [x] Array of routes all conflict_zones -> camps
- [x] Merge partial routes 
- [x] Identify nodes 
Output: 
- [x] Array of final routes and nodes (names OSM)
      ([route11, route12, …, route1n1], [route21, route22, …, route2n2], …, routeK1, routeK2, …, routeKnn])
- [x] Take all routex1, routex2, …, routexnx lat-lon
- [ ] Find names by OSM query


## Network map visualisation
Automated network map visualisation uses cartopy package (built on matplotlib) which allows a representation of the conflict scenario on a map. The map is in a bounding box to show the region around a conflict, the geographical features are such as coastlines and political boarders are drawn on the map. The country at the centre of the conflict zone is rendered in light gray and the surrounding countries are rendered in a yellow-green. Conflict zones are shown as red markers, camps as green markeres, forwarding camps as lawn green markers and towns as yellow markers - information on these is given in a legend. The routes are shown as blue lines between these markers with a distance printed on the mid-point of the line. This code allows all the vital elements of the network can be rendered there is not yet way to define the network digitally. Once a way to digitally encode the network is creatred it will be possible to use this to render a meaningful map.

At the end of the visualization code is some commented out source code that starts to render exploded regions that are a zoom of a small area of the map.

## Simulation of refugee movements
Acquired data from ACLED and UNHCR, publicly available sources, provide an input for running an agent-based simulation. It uses FLEE code for predicting refugee movements and produces output numbers of the population for cities and camps over the simulation period. An introductory paper on simulating refugee movements is written by [Groen (2016)](http://www.sciencedirect.com/science/article/pii/S1877050916308766) with a description of parameters, assumptions and application to crisis situation of Mali. FLEE simulation model has also been applied to Burundi, Central African Republic and South Sudan, which is written by [Suleimenova et al. (2017)](https://goo.gl/t16LA1) published in Scientific Reports. In addition to publication, Flee simulation code is released under a BSD 3-clause license. The GitHub repository with the latest source can be found at http://www.github.com/djgroen/flee-release. 


## Testing
