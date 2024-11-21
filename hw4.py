from functools import reduce
import sys
import build_data
import county_demographics
import hw3
#part 1
def display(counties):
    for county in counties:
        print(county.county + ", " + county.state)
        print("Population:", county.population["2014 Population"])
        print("Age:\n"+"\t< 5: "+str(county.age["Percent Under 5 Years"])+"%")
        print("\t< 18: "+str(county.age["Percent Under 18 Years"])+"%")
        print("\t> 65: "+str(county.age["Percent 65 and Older"])+"%")
        print("Education\n"+"\t>= High School: "+str(county.education["High School or Higher"])+"%")
        print("\t>= Bachelor's: "+str(county.education["Bachelor's Degree or Higher"])+"%")
        print("Ethnicity Percentages:\n"+"\tAmerican Indian and Alaska Native: "+str(county.ethnicities["American Indian and Alaska Native Alone"])+"%")
        print("\tAsian Alone: "+str(county.ethnicities["Asian Alone"])+"%")
        print("\tBlack Alone: "+ str(county.ethnicities["Black Alone"]) + "%")
        print("\tHispanic or Latino: "+ str(county.ethnicities["Hispanic or Latino"]) + "%")
        print("\tNative Hawaiian and Other Pacific Islander Alone: "+ str(county.ethnicities["Native Hawaiian and Other Pacific Islander Alone"]) + "%")
        print("\tTwo or More Races: "+ str(county.ethnicities["Two or More Races"]) + "%")
        print("\tWhite Alone: "+ str(county.ethnicities["White Alone"]) + "%")
        print("\tWhite Alone, not Hispanic or Latino: "+ str(county.ethnicities["White Alone, not Hispanic or Latino"]) + "%")
        print("Income:\n"+"\tMedian Household "+str(county.income["Median Household Income"])+"%")
        print("\tPer Capita: "+str(county.income["Per Capita Income"])+"%")
        print("\tBelow Poverty Level: "+ str(county.income["Persons Below Poverty Level"]) + "%")

try:
    full_data = build_data.get_data()
    filename = sys.argv[1]
    infile = open("inputs/"+filename, 'r')
    print(str(len(full_data))+" records loaded")
    for line in infile:
        line = line.rstrip("\n")
        if ":" in line:
            command_list = line.split(":")
            if command_list[0] == "filter-lt":
                if "Education" in command_list[1]:
                    new_list = command_list[1].split(".")
                    full_data = hw3.education_less_than(full_data, new_list[1], float(command_list[2]))
                    print("Filter: " + command_list[1] + " lt " + str(
                        command_list[2] + " (" + str(len(full_data)) + " entries)"))
                elif "Ethnicities" in command_list[1]:
                    new_list = command_list[1].split(".")
                    full_data = hw3.ethnicity_less_than(full_data, new_list[1], float(command_list[2]))
                    print("Filter: " + command_list[1] + " lt" + str(
                        command_list[2] + " (" + str(len(full_data)) + " entries)"))
            elif command_list[0] == "filter-gt":
                new_list = command_list[1].split(".")
                if "Education" in command_list[1]:
                    full_data = hw3.education_greater_than(full_data, new_list[1], float(command_list[2]))
                    print("Filter: "+command_list[1]+" gt"+str(command_list[2]+" ("+str(len(full_data))+" entries)"))
                elif "Ethnicities" in command_list[1]:
                    new_list = command_list[1].split(".")
                    full_data = hw3.ethnicity_greater_than(full_data, new_list[1], float(command_list[2]))
                    print("Filter: " + command_list[1] + " gt" + str(
                        command_list[2] + " (" + str(len(full_data)) + " entries)"))
            elif command_list[0] == "filter-state":
                full_data = hw3.filter_by_state(full_data, command_list[1])
                print("Filter: state == " + command_list[1] + " (" + str(len(full_data)) + " entries)")
            elif command_list[0] == "population":
                if "Education" in command_list[1]:
                    new_list = command_list[1].split(".")
                    print("2014 "+command_list[1]+ " population: "+ str(hw3.population_by_education(full_data,new_list[1])))
                elif "Ethnicities" in command_list[1]:
                    new_list = command_list[1].split(".")
                    print("2014 "+command_list[1]+ " population: "+ str(hw3.population_by_ethnicity(full_data,new_list[1])))
                elif "Income" in command_list[1]:
                    print("2014 " + command_list[1] + " population: " + str(hw3.population_below_poverty_level(full_data)))
            elif command_list[0] == "percent":
                if "Education" in command_list[1]:
                    new_list = command_list[1].split(".")
                    print("2014 " + command_list[1] + " percentage: " + str(
                        hw3.percent_by_education(full_data, new_list[1])))
                elif "Ethnicities" in command_list[1]:
                    new_list = command_list[1].split(".")
                    print("2014 " + command_list[1] + " percentage: " +
                          str(hw3.percent_by_ethnicity(full_data, new_list[1])))
                elif "Income" in command_list[1]:
                    print("2014 " + command_list[1] + " percentage: " +str(hw3.percent_below_poverty_level(full_data)))
        elif line == "display":
            display(full_data)
        elif line == "population-total":
            print("2014 population:", hw3.population_total(full_data))
    infile.close()
except:
    print("An error occurred")
    exit(1)
