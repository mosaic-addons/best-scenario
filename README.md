# Berlin Sumo Traffic (BeST) Scenario

https://user-images.githubusercontent.com/2386865/186914163-1225cb32-7a1f-4bdd-8550-2be9ce9a96dd.mp4

## 24 Hours of Traffic in Berlin for SUMO and Eclipse MOSAIC

This simulation scenario provides **motorized private transport** traffic for over **24 hours for the whole city of Berlin**. 
With over **2,25 million trips** within an area of 800 km², this is **the largest microscopic traffic simulation scenario** we are currently aware of.

The scenario was made for [Eclipse MOSAIC](https://github.com/eclipse/mosaic) and thus requires it to run. 
It is, however, also possible to run it with [Eclipse SUMO](https://github.com/eclipse/sumo) only.
If you plan to test your own mobility solutions encoperating V2X technology or message exchange via LTE/5G, then Eclipse MOSAIC is your way to go. 
Here you can combine the traffic with communcation and application simulation, thus creating a holistic system solution on a large-scale.

The scenario is based on the [MATSim Open Berlin Scenario](https://github.com/matsim-scenarios/matsim-berlin) [^1]. 
We extracted traffic demand from this scenario and re-calibrated all routes to achieve a user equilibrium.
More details on our creation process can be found in the provided reference and in the background section and the bottom of this file.

[^1]: D. Ziemke, I. Kaddoura, K. Nagel; [The MATSim Open Berlin Scenario: A multimodal agent-based transport simulation scenario based on synthetic demand modeling and Open Data](https://doi.org/10.1016/j.procs.2019.04.120); Procedia Computer Science, Volume 151, 2019, 870-877

## Characteristics

Some basic characteristics describing the scenario:

|Characterstic|Number|
|-----------------|--------|
| Number of nodes | 27 404 |
| Number of edges	| 69 234 |
| Number of junctions controlled by traffic signals | 2 249 |
| Number of trips | 2 248 952 |
| Average duration of each trip | 805 sec |
| Average distance of each trip | 7,9 km |
| Overall mean speed compared to speed limits | 0.71 |
| Total number of teleports | 2 786 |
| Simulation duration on 3,4 GHz CPU (no GUI) | 7 hours |

We furthermore compared the simulated counts on some certain streets against real data from [Digitale Plattform Berlin](https://api.viz.berlin.de/daten/verkehrsdetektion):

![Vehicle counts on A100 East direction](docs/img/counts-a100-east.svg)
![Vehicle counts on A100 Altmoabit East direction](docs/img/counts-altmoabit-east.svg)
![Vehicle counts on A100 Siemensdamm East direction](docs/img/counts-siemensdamm-east.svg)
![Vehicle counts on Treskowallee South direction](docs/img/counts-treskowallee-south.svg)

## License and Attribution

All files belonging to this scenario definition are licensed under <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"> <img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a>.

The usage of this scenario has to be attributed by either providing a link to this repository, or by citing this reference:

> K. Schrab, R. Protzmann, and I. Radusch, "*A Large-Scale Traffic Scenario of Berlin for Evaluating Smart Mobility Applications*" in Proceedings of 6th Conference on Sustainable Urban Mobility, 2022.

## Installation and Usage

1. Install **Eclipse MOSAIC 22.0** [^2], e.g., by following [this manual](https://www.eclipse.org/mosaic/docs/getting_started)
2. Install **Eclipse SUMO 1.11.0** [^2], e.g., from https://sumo.dlr.de/docs/Downloads.php
3. Clone this repository to an arbitrary folder.
   ```sh
   git clone https://github.com/mosaic-addons/best-scenario.git
   ```
4. To download the SUMO files for the scenario (~420 MB), execute the `download_best_scenario.py`[^3] script in `/path/to/repository/scenario/sumo` using [Python 3](https://www.python.org/downloads).
   ```sh
   cd /path/to/repository/scenario/sumo
   py download_best_scenario.py
   ```
5. Go to the installation directory of **Eclipse MOSAIC** and type:
   ```sh
   mosaic.bat -c /path/to/repository/scenario/scenario_config.json -w 120 # Windows
   ./mosaic.sh -c /path/to/repository/scenario/scenario_config.json -w 120 # Linux
   ```
6. Be aware that completing this scenario requires several hours to complete. You can, however, reduce the simulation duration in the `scenario_config.json`.

[^2]: We calibrated and tested the BeST scenario using the mentioned versions of SUMO and MOSAIC. The scenario may still work with newer versions, but we cannot guarantee that the same results will be created.
[^3]: The download executed by this script will be counted for statistical purposes on www.dcaiti.tu-berlin.de. To disable recording the download, you can set the field `record` in the `download_best_scenario.py` to `False`. Details about tracking on that site can be found at https://www.dcaiti.tu-berlin.de/contact/imprint

In order to see a visualization of the traffic, simply edit the file `etc/runtime.json` in the Eclipse MOSAIC main directory.
Replace `SumoAmbassador` with `SumoGuiAmbassador` and save the file. 
Then execute the scenario.
Please note that using the visualization in `sumo-gui` slows down the simulation significantly due to its immense size.

```
...
  {
    "id": "sumo",
    "classname": "org.eclipse.mosaic.fed.sumo.ambassador.SumoGuiAmbassador",
    "configuration": "sumo_config.json",
    ...
  }
...
```

---
The scenario can also be used with SUMO only. Once you installed the scenario, you can execute it with SUMO directly:

```sh
sumo -c /path/to/repository/scenario/sumo/best-scenario.sumocfg
```

## The MOSAIC scenario

This scenario is compatible with Eclipse MOSAIC. It is prepared to extends the traffic simulation in SUMO with communication and application simulation. 
You can easily enable and disable simulators in the bottom section of the `scenario_config.json`. Currently, only `sumo` and `application` is activated.

```json
"federates": {
    "application": true,
    "cell": false,
    "sumo": true,
    "sns": false
}
```

In the `mapping/mapping_config.json` you will find that 1% of all vehicles are equipped with a [`HelloWorldApp`](https://github.com/eclipse/mosaic/blob/main/app/tutorials/example-applications/src/main/java/org/eclipse/mosaic/app/tutorial/eventprocessing/sampling/HelloWorldApp.java), which simply prints out the type of the vehicle in every simulation step. 
You can map our other [Example Applications](https://www.eclipse.org/mosaic/tutorials/additional_examples/), or [develop your own applications](https://www.eclipse.org/mosaic/docs/develop_applications/) and map them onto a proportion of all vehicles.

```json
{
  "prototypes":[
    {
      "name":"DefaultVehicle",
      "weight": 0.01,
      "applications":[ "org.eclipse.mosaic.app.tutorial.eventprocessing.sampling.HelloWorldApp" ]
    }
  ]
}
```

Furthermore, if you want to add communication between vehicles/their applications to the scenario, you can either activate `sns` for adhoc-communication, or `cell` for cell-based communication. Configuration files for both simulators, where you can configure delay times, paket loss, and other communication properties, can be found in `sns/sns_config.json` and `cell/network.json` files. To enable communication in applications, you furthermore need to activate the communication module accordingly in your application, and use it to send V2X messages. For more details on that, follow our [tutorials](https://www.eclipse.org/mosaic/tutorials).

Following an example for an application, which sends a Cooperative Awareness Message (CAM) via adhoc communication to its neighboring vehicles:
```java
public class V2xApp
   extends AbstractApplication<VehicleOperatingSystem>
   implements CommunicationApplication, VehicleApplication {

   public void onStartup() {
     getAdhocModule().enable();
   }

   public void onVehicleUpdated() {
     getAdhocModule().sendCam();
   }

   public void onMessageReceived(ReceivedV2xMessage msg) {
     if (msg.getMessage() instanceof Cam) {
       String senderId = msg.getMessage().getRouting().getSource().getSourceName();
       GeoPoint otherPos = ((Cam)msg.getMessage()).getPosition();
       // todo
     }
   }
}
```

## Background

Find out more about the creation process of the scenario by reading our publication once it has been published in the Conference Proceeedings of [CSUM 2022](https://csum.civ.uth.gr).
