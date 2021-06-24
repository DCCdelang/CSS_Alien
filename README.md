# CSS_Alien

This repository contains data and code used for the final project of the Complex Systems Simulation course of the UvA 2021. The program used for the simulations is the ALiEn-project: https://alien-project.org/index.html

![sim9b-large](Plots/Additional_Media/sim9b-large.png)

In this repository you will find different folders containing setups needed in order to run the simulations used for our project. Furthermore, data extracted during these simulations is found in the [Data](https://github.com/DCCdelang/CSS_Alien/tree/main/Data) folder. For the general data every 200 msec data was gathered on the time step, number of clusters, number of clusters with tokens, number of cells, number of particles, number of tokens, total internal energy and the total kinetic energy.

The [Pattern_data](https://github.com/DCCdelang/CSS_Alien/tree/main/Pattern_data) folder contains more in-depth data on simulations were for each 10 or 5 thousand iterations data was stored containing an overview on the species distributions. This information was used using an extra functionality that calculates the size of the repetitive species while also capturing them in a collection (.col) file, which in turn can be opened again in the model.

In the [Collections](https://github.com/DCCdelang/CSS_Alien/tree/main/Collections) and the [Simulations](https://github.com/DCCdelang/CSS_Alien/tree/main/Simulations) folder some configurations are found in order to run the simulations. Most data was created using the setup-OTS-02.sim simulations file with the Default parameter settings.

<img src="Plots\Additional_Media\OTS_2_Default_start.PNG" alt="OTS_2_Default_start" style="zoom:25%;" /><img src="Plots\Additional_Media\OTS_2_Default_30k.PNG" alt="OTS_2_Default_30k" style="zoom:24%;" /><img src="Plots\Additional_Media\OTS_2_Default_104k.PNG" alt="OTS_2_Default_30k" style="zoom:26%;" />

In the above three images snapshots are shown of the setup-OTS-02.sim file with default parameters. The first file is at iteration=0 followed by a snapshot of iter=30k and iter=104k. While the simulation is initialized with only 10 small replicators it is very interesting to see how, in a nutrition rich environment, it is able to fully take over the simulation space. At 30k almost all food is converted and at 104k different clusters are emerging each consisting of different mutation of the original replicator. 

For further data analysis the code can be found in the [Code](https://github.com/DCCdelang/CSS_Alien/tree/main/Code) folder and some plots in the [Plots](https://github.com/DCCdelang/CSS_Alien/tree/main/Plots) folder. This analyses was done using both the general data and the pattern data. 

Contributors:

Alicja Grudnowska

Dante de Lang

Mengli Feng

Warwick Louw

