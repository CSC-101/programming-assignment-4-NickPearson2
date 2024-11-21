import county_demographics
import data
#Part 1
'''
population_total total will take a list of county demographics and
return the total 2014 population across the set of countries in the list.
'''
def population_total(list_of_counties:list[data.CountyDemographics])->int:
    total =0
    for county in list_of_counties:
        total+=county.population["2014 Population"]
    return total
#Part 2
'''
filter_by_state will take in a list of county demographic objects and 
a two letter state abbreviation. It will return a list of county demographics
from the input list from the state.
'''
def filter_by_state(list_of_counties:list[data.CountyDemographics],state:str)->list[data.CountyDemographics]:
    list = []
    for county in list_of_counties:
        if county.state == state:
            list.append(county)
    return list
#Part 3
'''
population_by_education will take in a list of county demographics and
the education key of interest. It will return the total 2014 sub-population
across the set of counties in the input list for the specified key of interest.
'''
def population_by_education(list_of_counties:list[data.CountyDemographics],edu_key:str)->float:
    total = 0
    for county in list_of_counties:
        if edu_key in county.education:
            total += (county.population["2014 Population"]*((county.education[edu_key])/100))
    return total
'''
population_by_ethnicity will take in a list of county demographics and the ethnicity
key of interest. It will return the total 2014 sub-population across the set of 
counties in the input list for the specified key of interest.
'''
def population_by_ethnicity(list_of_counties:list[data.CountyDemographics], eth_key:str) -> float:
    total = 0
    for county in list_of_counties:
        if eth_key in county.ethnicities:
            total += (county.population["2014 Population"]*((county.ethnicities[eth_key])/100))
    return total
'''
population_below_poverty_level will take in a list of county demographics and
return the total 2014 sub-population across the set of counties in the input
list indicated by the income key 'Persons Below Poverty Level'.
'''
def population_below_poverty_level(list_of_counties:list[data.CountyDemographics])->float:
    total = 0
    for county in list_of_counties:
        total += (county.population["2014 Population"]*((county.income["Persons Below Poverty Level"])/100))
    return total
#Part 4
'''
percent_by_education will take in a list of county demographics and an
education key of interest. It will return the specified 2014 sub-population
as a percentage of the total 2014 population across the counties in the list
for the specified key of interest.
'''
def percent_by_education(list_of_counties:list[data.CountyDemographics],edu_key:str)->float:
    try:
        list_of_counties[0].education[edu_key]
    except:
        return 0
    percentage = ((population_by_education(list_of_counties,edu_key))/(population_total(list_of_counties)))*100
    return percentage
'''
percent_by_ethnicity will take in a list of county demographics and an
ethnicity key of interest. It will return the specified 2014 sub-population
as a percentage of the total 2014 population across the counties in the list
for the specified key of interest.
'''
def percent_by_ethnicity(list_of_counties:list[data.CountyDemographics],eth_key:str)->float:
    try:
        list_of_counties[0].ethnicities[eth_key]
    except:
        return 0
    percentage = ((population_by_ethnicity(list_of_counties,eth_key))/(population_total(list_of_counties)))*100
    return percentage
'''
percent_below_poverty_level will take in a list of county demographics. It will return the 
2014 sub-population indicated by the income key "Persons Below Poverty Level"
as a percentage of the total 2014 population across the counties in the list.
'''
def percent_below_poverty_level(list_of_counties:list[data.CountyDemographics])->float:
    percentage = ((population_below_poverty_level(list_of_counties))/(population_total(list_of_counties)))*100
    return percentage
#Part 5
'''
education_greater_than will take in a list of county demographics and an education key
of interest and a numeric threshold value. It will return a list of all county demographics
object for which the value for the specified key is greater than the specified threshold value.
'''
def education_greater_than(list_of_counties:list[data.CountyDemographics], edu_key:str, value:float) -> list[data.CountyDemographics]:
    new_list = []
    for county in list_of_counties:
        if edu_key in county.education:
            if county.education[edu_key] > value:
                new_list.append(county)
    return new_list
'''
education_less_than will take in a list of county demographics and an education key
of interest and a numeric threshold value. It will return a list of all county demographics
object for which the value for the specified key is less than the specified threshold value.
'''
def education_less_than(list_of_counties: list[data.CountyDemographics], edu_key: str, value: float) -> list[data.CountyDemographics]:
    new_list = []
    for county in list_of_counties:
        if edu_key in county.education:
            if county.education[edu_key] < value:
                new_list.append(county)
    return new_list
'''
ethnicity_greater_than will take in a list of county demographics and an ethnicity key
of interest and a numeric threshold value. It will return a list of all county demographics
object for which the value for the specified key is greater than the specified threshold value.
'''
def ethnicity_greater_than(list_of_counties: list[data.CountyDemographics], eth_key: str, value: float) -> list[data.CountyDemographics]:
    new_list = []
    for county in list_of_counties:
        if eth_key in county.ethnicities:
            if county.ethnicities[eth_key] > value:
                new_list.append(county)
    return new_list
'''
ethnicity_less_than will take in a list of county demographics and an ethnicity key
of interest and a numeric threshold value. It will return a list of all county demographics
object for which the value for the specified key is greater than the specified threshold value.
'''
def ethnicity_less_than(list_of_counties: list[data.CountyDemographics], eth_key: str, value: float) -> list[data.CountyDemographics]:
    new_list = []
    for county in list_of_counties:
        if eth_key in county.ethnicities:
            if county.ethnicities[eth_key] < value:
                new_list.append(county)
    return new_list
'''
below_poverty_level_greater_than will take in a list of county demographics and a numeric threshold value. 
It will return a list of all county demographics object for which the value for the 
specified key is greater than the specified threshold value.
'''
def below_poverty_level_greater_than(list_of_counties: list[data.CountyDemographics], value: float) -> list[data.CountyDemographics]:
    new_list = []
    for county in list_of_counties:
        if county.income["Persons Below Poverty Level"] > value:
            new_list.append(county)
    return new_list
'''
below_poverty_level_less_than will take in a list of county demographics and a numeric threshold value. 
It will return a list of all county demographics object for which the value for the 
specified key is greater than the specified threshold value.
'''
def below_poverty_level_less_than(list_of_counties: list[data.CountyDemographics], value: float) -> list[data.CountyDemographics]:
    new_list = []
    for county in list_of_counties:
        if county.income["Persons Below Poverty Level"] < value:
            new_list.append(county)
    return new_list