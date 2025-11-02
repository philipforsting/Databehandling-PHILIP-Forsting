import pandas as pd

cities = {
    "Kommun": ["Malmö", "Stockholm", "Uppsala", "Göteborg"],
    "Population": [347949, 975551, 233839, 583056]
}
print(f"data: \n{cities}")

#a
df_cities = pd.DataFrame(cities)
print(f"df_cities: \n{df_cities}")

#b
print(df_cities[df_cities["Kommun"] == "Göteborg"]) # Selekterar rad som innehåller "Göteborg " via maskning
print(df_cities["Kommun"] == "Göteborg") # Mask som är true för raden som innehåller "Göteborg" (0,0,0,1)

#c
df_cities_sorted = df_cities.sort_values(by="Population", ascending=False)
print(f"df_cities_sorted: \n{df_cities_sorted}")

#d
df_cities_top3 = df_cities_sorted.iloc[:3] 
print(f"df_cities_top5: \n{df_cities_top3}")

#e
df_cities_sorted["Population (%)"] = 100 * df_cities_sorted["Population"] / 10379295
print(f"df_cities_sorted \n{df_cities_sorted}")