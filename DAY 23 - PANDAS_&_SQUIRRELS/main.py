
import statistics
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_fur_number = len(data[data["Primary Fur Color"] == "Gray"])
red_fur_number = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_fur_number = len(data[data["Primary Fur Color"] == "Black"])

fur_frame = {
    "fur color": ["gray", "red", "black"],
    "squirrels": [gray_fur_number, red_fur_number, black_fur_number]
}

new_data = pandas.DataFrame(fur_frame)
new_data.to_csv("squirrels_in_park.csv")
print(new_data)








