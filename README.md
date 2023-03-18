# KSP Konstellations

KSP Konstellations is a small and fast app that you can use to easily calculate data for your next constellation of satellites anywhere in the Kerbol system.

#### https://forum.kerbalspaceprogram.com/index.php?/topic/215089-ksp-konstellations/

## Usage
If you need to make a constellation of satellites cause you lost twice connection with you're probe on Eeloo or you just want to challenge your friend Elon you need to know how to proceed.<br>
You need 2 orbits, the final orbit (red) where all the satellites will circularize one by one, and the transfer orbit (blue) where the main stage is gonna drop a satellite every period (or more).

![image](https://user-images.githubusercontent.com/79790839/225386603-98a2ff86-2414-4592-895a-48718a19c13f.png)

All the required things you need to know are the number of satellites, the final orbit, and the celestial body orbited.<br>
KSP Konstellations will provide you with the following pieces of information:
- Transfer orbit periapsis
- Both orbits periods
- Drops frequency, meaning how many periods you need to wait before dropping the next satellite (usually 1)
- The required antenna to handle the connection between the satellites (only the relays ones)
- A ΔV estimation for each stage (including the main one)
- Total dropping time, meaning how long dropping all satellites will take ingame

KSP Konstellations will also provide some warnings if necessary:
- If the transfer orbit is crossing other body's orbits (SOI or body)
- If the final orbit is too close and the body will block communications
- If the final orbit is too high and no antennas can handle the distance between 2 satellites

Then you'll have to head to the body, set you're main vessel to the transfer orbit, and start dropping satellites, and burning prograde for each one until you've reached the final orbit. (circularization)

## Installation

- Head to the latest release here https://github.com/PurrfectsBoots/KSP-Konstellations/releases/latest and download the `KSP_Konstellations.zip` file
- Unzip the file
- Open the `KSP_Konstellations.exe` inside and you're ready to go

## Important disclaimer
Because the zip file contains an unknown executable file Windows will surely flag it as dangerous. If you are not sure about what you are doing you can always check the source code here: 
- https://github.com/PurrfectsBoots/KSP-Konstellations

### THANK YOU FOR USING KSP KONSTELLATIONS
