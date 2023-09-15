import csv
import difflib
import dict
import DP as dp


def read_csv_to_dict(file_path):
    dictionary = {}

    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            word = row[0]
            counts = []
            for count_str in row[1:]:
                try:
                    count = int(count_str)
                    counts.append(count)
                except ValueError:
                    # Because Alabama is annoying
                    if count_str == '0':
                        counts.append(0)
            dictionary[word] = counts

    return dictionary


file_path_districts = 'districts.txt'
file_path_eligible_voters = 'eligible_voters.txt'
voting_results_dict = read_csv_to_dict(file_path_districts)
eligible_voters_dict = read_csv_to_dict(file_path_eligible_voters)



word = input('Enter the name of the state you would like to investigate for evidence of gerrymandering: ')

district_results = dict.translate(word, voting_results_dict)
eligible_voters = dict.translate(word, eligible_voters_dict)
print(eligible_voters, district_results)






# Time to manipulate the data
districts = len(district_results[0])//3 #int

width = 500
height = (districts + 2)*25+20
panel = dp.DrawingPanel(width=width, height=height, background="white")
line1 = dp.DrawingPanel.draw_line(panel, 0, 40, width, 40, color="black")

# State_Name = dp.DrawingPanel.draw_string(panel, district_results[1], 0, 0, color="black", font="")
State_Name = dp.DrawingPanel.draw_string(panel,
                                         "The state of {} has {} eligible voters.".format(district_results[1],
                                            eligible_voters[0]), 100, 0, color="black", font="")


Total_Wasted_Dem = []
Total_Wasted_GOP = []
for vote in range(districts):
    
    Dem_Vote = district_results[0][(vote*3)+1]
    GOP_Vote = district_results[0][(vote*3)+2]
    if Dem_Vote < GOP_Vote:
        Wasted_Dem = Dem_Vote
        Wasted_GOP = Dem_Vote + ((GOP_Vote-Dem_Vote) - ((GOP_Vote + Dem_Vote)/2) + 1)
        Total_Wasted_Dem.append(Wasted_Dem)
        # Difference = Dem_Vote/GOP_Vote # smaller over bigger
    elif GOP_Vote < Dem_Vote:
        Wasted_GOP = GOP_Vote
        Wasted_Dem = GOP_Vote + ((Dem_Vote-GOP_Vote) - ((GOP_Vote + Dem_Vote)/2) + 1)
        Total_Wasted_GOP.append(Wasted_GOP)
        # Difference = GOP_Vote/Dem_Vote # smaller over bigger
    
    Dem_line_width = Dem_Vote / (Dem_Vote+GOP_Vote) * 500
    bar = dp.DrawingPanel.draw_rect(panel, 0, (vote+1)*25+20, width, 20, color="red", fill='red')
    bar = dp.DrawingPanel.draw_rect(panel, 0, (vote+1)*25+20, Dem_line_width, 20, color="blue", fill='blue')
line2 = dp.DrawingPanel.draw_line(panel, width/2, 40, width/2, height, color="black")


Total_Wasted_Dem = sum(Total_Wasted_Dem)
Total_Wasted_GOP = sum(Total_Wasted_GOP)

if Total_Wasted_Dem < Total_Wasted_GOP:     
    Difference = Total_Wasted_Dem/Total_Wasted_GOP
elif Total_Wasted_GOP < Total_Wasted_Dem:
    Difference = Total_Wasted_GOP/Total_Wasted_Dem

District = Dem_Vote, GOP_Vote, "District '{}".format(vote+1) # Politicians don't count from zero
# print(District)

if Difference >= 0.7:
    # print("Gerry my Mander!")
    State_Name = dp.DrawingPanel.draw_string(panel, "The 7% test shows evidence of gerrymandering!", 100, 20, color="black", font="")
elif Difference < 0.7:
    print("The 7% test does not show evidence of gerrymandering")
    State_Name = dp.DrawingPanel.draw_string(panel,"The 7% test does not show evidence of gerrymandering",
                                             100, 20, color="black", font="")

print("The state of {} has {} eligible_voters.".format(district_results[1], eligible_voters))




