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

From the mathematical point of view we will consider the problem of n bodies as that of n non-zero, punctual masses, subject to Newton's law of universal attraction. From the physical point of view this is an idealised model.

## Resources
We provide a list of links from different websites and the information we get from each one.
- [Windows2Universe](https://www.windows2universe.org/our_solar_system/moons_table.html&lang=sp) from this website we got all the names of the moons we are going to use and the distance between them and the planet.
- [SISV-LunasdeUrano](https://sisv.idideadigital.com/urano/lunas-dats.htm) from this website we got the data referring to the mass of each one of the moons.
- [The n-body problem](https://core.ac.uk/download/pdf/39029007.pdf) from this pdf we were able to learn more about the problem of n bodies.

## Methodology
For this project, we use the model of N-body, It works by calculating the path of motion of a body, based on its speed, position, and mass.

The first thing that we need, is have all the parameters of each body, in this case:
- Uranus: mass and position (the position is 0,0,0 because of is the framework)
- Mass, velocity and position of:
  - Cordelia
  - Cressida
  - Cupid
  - Puck
  - Mab

When we have all the data, the next step is to calculate the new position for each body (except for the framework that is static), for this, the program will be able to select one body, calculate the distance to all the other object, calculate the resultant force, and get the new position of the body based on its initial position and the resultant force, save the new position, and do it for all the bodies when the program already has all the new positions, these become into the new "starting positions", the resultant force become into the new force of the body, and the whole process is repeated, until the required simulation time is reached.

## Implementation

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

## Tests

## Results

## Conclusions

## Bibliography
