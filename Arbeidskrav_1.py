# Arbeidskrav 1 _ Elham Bårdsen
# Antall KM kjørt per år
KM = 10000

# Beregning av Elbil
forsikring_elbil = 5000  # Årlig forsikringsum 
trafikkavgift_elbil = 8.38 * 365  # Årlig trafikkforsikringsavgift (kr per år (365 dager i året))
drivstoff_elbil = (0.2 * 2) * KM  # Årlig drivstoffbruk (kr per km * km per år)
bom_elbil = 0.1 * KM  # Årlig bomavgift (kr per km * km per år)

#  Totalkostnad for elbil
elbil_kostnad= forsikring_elbil + trafikkavgift_elbil + drivstoff_elbil + bom_elbil
print (f"Årlig kostnad for elbil = {elbil_kostnad} kr")


# Beregning av bensinbil
forsikring_bensinbil = 7500  # Årlig forsikringsum
trafikkavgift_bensinbil = 8.38 * 365  # Årlig trafikkforsikringsavgift (kr per år (365 dager i året))
drivstoff_bensinbil = 1 * KM  # Årlig drivstoffbruk (kr per km * km per år)
bom_bensinbil = 0.3 * KM  # Årlig bomavgift (kr per km * km per år)

# Totalkostnad for bensinbil
bensinbil_kostnad = forsikring_bensinbil + trafikkavgift_bensinbil + drivstoff_bensinbil + bom_bensinbil
print (f"Årlig kostnad for bensinbil = {bensinbil_kostnad} kr")

# Kostnadsdifferanse mellom bensinbil og elbil
kostnadsdifferanse = bensinbil_kostnad - elbil_kostnad
print (f"Årlig kostnadsdifferanse mellom bensinbil og elbil = {kostnadsdifferanse} kr")