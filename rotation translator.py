import os
import csv

def process_file(filepath):
    north = 0
    north_east = 0
    east = 0
    south_east = 0
    south = 0
    south_west = 0
    west = 0
    north_west = 0

    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rotation = float(row['rotation'])
            if rotation >= 337.5 or rotation < 22.5:
                north += 1
            elif rotation >= 22.5 and rotation < 67.5:
                north_east += 1
            elif rotation >= 67.5 and rotation < 112.5:
                east += 1
            elif rotation >= 112.5 and rotation < 157.5:
                south_east += 1
            elif rotation >= 157.5 and rotation < 202.5:
                south += 1
            elif rotation >= 202.5 and rotation < 247.5:
                south_west += 1
            elif rotation >= 247.5 and rotation < 292.5:
                west += 1
            elif rotation >= 292.5 and rotation < 337.5:
                north_west += 1

    filename, file_extension = os.path.splitext(filepath)
    new_filepath = filename + "_eng.csv"
    with open(new_filepath, 'w', newline='') as new_file:
        fieldnames = ['direction', 'count']
        writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'direction': 'north', 'count': north})
        writer.writerow({'direction': 'north_east', 'count': north_east})
        writer.writerow({'direction': 'east', 'count': east})
        writer.writerow({'direction': 'south_east', 'count': south_east})
        writer.writerow({'direction': 'south', 'count': south})
        writer.writerow({'direction': 'south_west', 'count': south_west})
        writer.writerow({'direction': 'west', 'count': west})
        writer.writerow({'direction': 'north_west', 'count': north_west})

folder_path = "C:\\Users\\joshm\\Nextcloud2\\ah geogrpahy\\mr kemp\\graphing program\\hight-seperated"
#folder_path = "C:\\Users\\joshm\\PycharmProjects\\pythonProject\\hight-seperated"
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        process_file(file_path)
