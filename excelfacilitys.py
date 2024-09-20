import pandas as pd

facilities = [
    "Alkmaar De Vest", "Alkmaar Kanaal Schiereiland", "Alkmaar Karperton", "Alkmaar Kazerne",
    "Alkmaar Ringers", "Alkmaar Schelphoek", "Alkmaar Singel", "Alkmaar Stadafsluiting",
    "Amersfoort Asch van Wijk", "Amstelveen Schouwburg", "Amstelveen Stadsplein", "Amsterdam AH Sciencepark",
    "Amsterdam Argentinie", "Amsterdam De Overkant", "Amsterdam Gelderlandplein", "Amsterdam Houthaven",
    "Amsterdam Kalverstraat", "Amsterdam Molukkenstraat", "Amsterdam Osdorpplein", "Amsterdam Q-Residence",
    "Amsterdam Spaklerweg", "Amsterdam Stadionplein", "Amsterdam Stadionplein Zuid", "Assen Citadel",
    "Assen Drents Museum", "Assen Kolk", "Assen Mercurius", "Assen Neptunus", "Assen Stadhuis",
    "Assen Triade", "Breda Chasse", "Breda Concordia", "Breda De Barones", "Breda De Prins",
    "Breda Turfschip", "Bussum Brediusdam", "Bussum De Olmen", "Bussum Nieuwe Brink", "Bussum Westerpark",
    "Delft P1 Aula", "Delft P2 Sports", "Delft P3 TNw", "Delft P4 L&R", "Delft P5 Rotterdamseweg",
    "Delft P6 BK", "Delft P7 Heertjeslaan", "Delft P8 Molengraafsingel", "Delft P9 Heertjeslaan 10",
    "Den Haag Leyweg 2", "Den Haag Turfmarkt", "Den Helder Sluisdijk", "Deventer Brink", "Deventer Polstraat",
    "Deventer Stadspoort", "Deventer Stationsplein", "Eindhoven Genneper Parken", "Eindhoven Grijze Generaal",
    "Eindhoven PenR Meerhoven", "Eindhoven Terminal M (Meerhoven)", "Eindhoven Veemgebouw", "Hengelo De Beurs",
    "Hoofddorp PenR Hoofddorp", "Hoofddorp Primark", "Hoorn Jeudje", "Hoorn Schouwburg", "IJsselstein Eiteren",
    "IJsselstein Overtoom", "Katwijk Zeehos", "Leiden Garenmarkt", "Leiden Haarlemmerstraat",
    "Leiden Lammermarkt", "Leiden Morspoort", "Leiden Ringkade", "Leiden Soestdijkkade", "Leiden Universiteit",
    "Maastricht Noorderbrug", "Maastricht Sphinx", "Nijmegen Dukenburg", "Nootdorp Parade", "Oosterhout Arendshof",
    "Oosterhout Basiliek", "Pijnacker Keijzershof", "Purmerend Claxonate", "Purmerend Stadhuisgarage",
    "Roermond Kazerneplein", "Roermond Stationspark", "Rotterdam Eudokia", "Tilburg Emma passage",
    "Tilburg Jumbo Foodmarkt", "Tilburg Knegtel", "Tilburg Koningsplein", "Tilburg Pieter Vredeplein",
    "Tilburg Schouwburgplein", "Tilburg Stappegoor", "Tilburg Tivoli", "Tilburg Zwijssen", "Utrecht PenR Uithof",
    "Valkenburg Aan de kei", "Valkenburg Stadsafsluiting", "Veenendaal Arie van Hensbergen",
    "Veenendaal Gemeentehuis", "Veenendaal Tricotage", "Veldhoven De Geer", "Venray Blekersveld",
    "Venray Centrumgarage", "Venray Raadhuisplein", "Weert Beekpoort", "Weert Centrum Noord",
    "Weert Centrumgarage", "Weert Muntgarage", "Weert Stadafsluiting", "Weert Stationskwartier",]

# Convert the list into a DataFrame
df = pd.DataFrame(facilities, columns=['Facility Name'])

# Save the DataFrame to an Excel file
df.to_excel('facilities_list.xlsx', index=False)