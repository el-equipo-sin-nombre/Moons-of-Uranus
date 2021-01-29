# Moons of Uranus
## Authors
- Esperanza Monserrat Alvarez Elias esperanzaalvarez120@gmail.com
- Antonio Chacón Flores chacon.floresantonio@gmail.com
- Karina Enriquez Guillén karienriquezguillen@gmail.com
- Saúl Armas Gamiño   luasikirfl@gmail.com

## License

GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.

## Introduction

Uranus is the seventh planet in the solar system, the third largest, and the fourth most massive. The system of Uranus has a unique configuration with respect to the other planets since its axis of rotation is very inclined, almost to its plane of revolution around the Sun. Therefore, its north and south poles are located where most of the other planets have the equator.

The Newton's law of universal attraction, calculates the force of attraction between two bodies, based on their mass, distance and the Universal gravitation constant.
Its formula is the following.

<img src="https://render.githubusercontent.com/render/math?math=F = G \frac{M1M2}{r^2}">
where F are the force, G are the Universal gravitation constant, M1 and M2 are the mass of the body 1 and 2, and r^2 are the distance squared. which means the masive and closer objects have more attractive force.

From the mathematical point of view we will consider the problem of n bodies as that of n non-zero, punctual masses, subject to Newton's law of universal attraction. From the physical point of view this is an idealised model.

In this work we are going to model the orbit of some moons of Uranus to analyze their trajectory, the goal of the project is to get the system to converge and to be able to see the orbit that the moons of Uranus follow, as well as to analyze the results.

The N-body problem, which focuses on finding the trajectories of several moving bodies subject to the forces exerted on each other, is one of the classical
subject to the forces they exert on each other, is one of the classical problems of mechanics and astronomy, in our case we chose the planet of Uranus and its moons. Within the astronomical context, the force of interaction is the force of gravity and the bodies in question can be planets, stars, galaxies, etc.

This model we are working with, as we mentioned before, uses Newton's law, but to have more realistic results, it would be necessary to use Einstein's theory of relativity. In this case, the problem would be more complex, so we decided to use Newton's Law because good results were obtained.

## Objetives
- The system convergence
- Get the orbits of the moons
- Interpret the results

## Resources
We provide a list of links from different websites and the information we get from each one.
- [Windows2Universe](https://www.windows2universe.org/our_solar_system/moons_table.html&lang=sp) from this website we got all the names of the moons we are going to use and the distance between them and the planet.
- [SISV-LunasdeUrano](https://sisv.idideadigital.com/urano/lunas-dats.htm) from this website we got the data referring to the mass of each one of the moons.
- [The n-body problem](https://core.ac.uk/download/pdf/39029007.pdf) from this pdf we were able to learn more about the problem of n bodies.

## Methodology
For this project, we use the model of N-body, It works by calculating the path of motion of a body, based on its speed, position, and mass.

The first thing that we need, is have all the parameters of each body, in this case:
- Uranus: 
  - mass: 8.681 x 10^25 kg
  - the position is 0,0,0 because of is the framework.
- Mass, velocity and position of:
  - Cordelia
    - Mass: 0.044 x 10^18 kg
    - Orbital speed: 38,918.2 km/h
    - Distance to Urano: 49 750km
  - Cressida
    - Mass: 0.34 x 10^18 kg
    - Orbital Speed: 34,869.0km/h
    - Orbital Speed: 34,869.0km/h
  - Cupid
    - Mass: 0.0038 x 10^18 kg
    - Orbital speed: 31,771.2 km/h
    - Distance to Urano: 74 800 km
  - Puck
    - Mass: 2.90x10^18 kg
    - Orbital speed: 29 546,9 km/h
    - Distance to Urano: 86 010 km
  - Mab
    - Mass 0.01x10^18 kg
    - Orbital speed:27,720 km/h
    - Distance to Urano: 97 734 km

When we have all the data, the next step is to calculate the new position for each body (except for the framework that is static), for this, the program will be able to select one body, calculate the distance to all the other object, calculate the resultant force, and get the new position of the body based on its initial position and the resultant force, save the new position, and do it for all the bodies when the program already has all the new positions, these become into the new "starting positions", the resultant force become into the new force of the body, and the whole process is repeated, until the required simulation time is reached.

## Implementation
The implementation was already done by Victor de la luz, we take his code from this page:
- https://github.com/itztli/n-body/blob/master/n-body.py
## How to Install
You need to have installed ```math```, ```matplotlib```, ```mpl toolkits```, and ```python3```.
###### Dependencies
1. Python
    - ```sudo apt install -y python3-pip```
2. Math
     - ```pip3 install math```
3. Matplotlib
     - ```pip3 install mathplotlib```
4. Mpl-toolkits
     - ```pip3 install mpl_toolkits```
## How to run
Go to the folder of the project and run “python3 n-body.py”, the program will be executed, and you will get a graphic with the trajectory of the five moons.
## Tests
First, we try running the code with one moon, and we use a delta_time of 0.5s, but we use an incorrect distance of the moon, so the system collapses.
In the other experiments, we get the correct distance and the system converged, successfully.
In order to determine if the variable Delta_time was correct, for the simulation time we chose was the one that took the slowest moon to go around.
## Results
![imagen1](/results/collapse.png)

In this image, we can see that the system collapses because we don't use the correct distance. the distance that we use was 4.98e4 instead of 4.98e7, that is te correct distance, the error was because the information was written by people that use "." instead of the coma that we use normally, so we think that was 49.750 km (Forty-nine point seventy-five) when in the reality was 49,750 km (Forty-nine thousand seven hundred fifty).

![imagen2](/results/cordelia.png)

With the correct distance, the system converged.

![imagen2](/results/bien_etiquetadas.png)
![imagen2](/results/etiqueta_lado.png)

These images show the five moons.
## Conclusions
Modeling some moons of Uranus was not a difficult task to do, since the code was already done, we only adjust it to our parameters and we look for the chosen data to agree with those requested by the code.
So it was important to make unit conventions from those we researched to those required by the code, for example, change meters per hour to meters per second, distance from kilometers to meters, because the code was made to work with these units, and as we saw in the first experiment if you don't use the adequate units, the system collapse, so it's important to use the units that the code specifies.

The obtained results show that the trajectory of the moons is an ellipse and the graphic has more points in the part most far away from Urano, which we believe is explained by Newton's law, since it says, "If two massive bodies are close, the force of attraction between them will be greater ", therefore, being close, the moon moves faster around it, and it will move more slowly when it is far from Uranus.




In conclusion, modeling is a very important tool in our lifes. Models help us to visualize a system as it is or as we want it to be. They let us specify the structure or behavior of a system. Models give us a template that guides us in constructing a system.
## Bibliography
- INFORMATION ABOUT THE MOONS OF URANUS
  - Cordelia
https://solarsystem.nasa.gov/moons/uranus-moons/cordelia/by-the-numbers/
  - Cressida
https://solarsystem.nasa.gov/moons/uranus-moons/cressida/by-the-numbers/
  - Cupid
https://solarsystem.nasa.gov/moons/uranus-moons/cupid/by-the-numbers/

