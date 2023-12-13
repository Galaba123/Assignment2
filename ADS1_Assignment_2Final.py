# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 16:08:59 2023

@author: Naga Praveen G
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_process_clean(filename, indicator_name):
    """ Read, process, and clean the data from the world bank data for selected indicators, countries and years. """

    world_bank_data = pd.read_csv(filename, skiprows=3)

    Countries = ['Australia', 'Canada', 'China',
                 'Germany', 'India', 'Switzerland']

    data = world_bank_data[(world_bank_data['Indicator Name'] == indicator_name)
                           & (world_bank_data['Country Name'].isin(Countries))]
    df = data.drop(['Country Code', 'Indicator Name', 'Indicator Code',
                    '1960', '1961', '1962', '1963', '1964', '1965', '1966',
                    '1967', '1968', '1969', '1970', '1971', '1972', '1973',
                    '1974', '1975', '1976', '1977', '1978', '1979', '1980',
                    '1981', '1982', '1983', '1984', '1985', '1986', '1987',
                    '1988', '1989', '1990', '2015', '2016', '2017', '2018',
                    '2019', '2020', '2021', '2022', 'Unnamed: 67'],
                   axis=1).reset_index(drop=True)
    df_t = df.transpose()
    df_t.columns = df_t.iloc[0]
    df_t = df_t.iloc[1:]
    df_t.index = pd.to_numeric(df_t.index)
    df_t['Years'] = df_t.index
    return df, df_t


def slice_data(df):
    """ To extract required indicators, countries and years for statistical analysis of data """

    df = df[['Country Name', '2014']]
    return df


def merge_seven(ind1, ind2, ind3, ind4, ind5, ind6, ind7):
    """ To merge the all different dataset of different indicators data having the one or more common columns data  """

    merge1 = pd.merge(ind1, ind2, on='Country Name', how='outer')
    merge2 = pd.merge(merge1, ind3, on='Country Name', how='outer')
    merge3 = pd.merge(merge2, ind4, on='Country Name', how='outer')
    merge4 = pd.merge(merge3, ind5, on='Country Name', how='outer')
    merge5 = pd.merge(merge4, ind6, on='Country Name', how='outer')
    merge6 = pd.merge(merge5, ind7, on='Country Name', how='outer')
    merge6 = merge6.reset_index(drop=True)
    return merge6


def create_barplot(df, x_value, y_value, head_title, x_label, y_label, colors, figsize=(10, 6)):
    """ Creating a bar plot for required data and column values"""
    # Create a heatmap with annotations
    sns.set_style('whitegrid')
    #Plotting values of bar plot like xaxis yaxis title and best plot
    df.plot(x=x_value, y=y_value, kind='bar', title=head_title, color=colors,
            width=0.65, figsize=figsize, xlabel=x_label, ylabel=y_label)
    plt.legend(loc='best', bbox_to_anchor=(1, 0.4))
    plt.savefig('barplot.png')
    plt.show()


def create_lineplot(df, y_label, title):
    """ Consructing a line plot of different countries over the 2two decade years from the world bank data"""
    # Create a heatmap with annotations
    sns.set_style("whitegrid")
    #Plotting values of bar plot like xaxis yaxis title and best plot
    df.plot(x='Years', y=['Australia', 'Canada', 'China', 'Germany',
            'India', 'Switzerland'], xlabel='Years', ylabel=y_label, marker='.')
    plt.title(title)
    plt.xticks(range(1990, 2015, 2))
    plt.legend(loc='best', bbox_to_anchor=(1, 0.4))
    plt.savefig('lineplot.png')
    plt.show()


def skew_kurt_plot(melted_df):
    """ To create a Statistical analysis propwerties like skewness and kurtosis plots """

    # Melt the dataset to have years as a variable

    melted_df = pd.melt(
        green, id_vars=['Country Name'], var_name='Years', value_name='Value')

    # Plotting the skewness and kurtosis

    plt.figure(figsize=(24, 6))
    plt.subplot(1, 2, 1)
    sns.boxplot(x='Years', y='Value', data=melted_df, hue='Country Name')
    plt.title('Skewness Plot')

    plt.subplot(1, 2, 2)
    sns.boxplot(x='Years', y='Value', data=melted_df, hue='Country Name')
    plt.title('Kurtosis Plot')

    plt.tight_layout()
    plt.grid()
    plt.show()


Indicators = ["Arable land (% of land area)",
              "Agriculture, forestry, and fishing, value added (% of GDP)",
              "Electric power consumption (kWh per capita)",
              "Energy use (kg of oil equivalent per capita)",
              "Forest area (% of land area)",
              "Total greenhouse gas emissions (kt of CO2 equivalent)",
              "Urban population growth (annual %)"]


AffGDP, AffGDP_t = read_process_clean(
    'API_19_DS2_en_csv_v2_6183479.csv',
    "Agriculture, forestry, and fishing, value added (% of GDP)")
ele, ele_t = read_process_clean(
    'API_19_DS2_en_csv_v2_6183479.csv',
    'Electric power consumption (kWh per capita)')
arable, arable_t = read_process_clean(
    'API_19_DS2_en_csv_v2_6183479.csv', 'Arable land (% of land area)')
ener, ener_t = read_process_clean(
    'API_19_DS2_en_csv_v2_6183479.csv',
    'Energy use (kg of oil equivalent per capita)')
fore, fore_t = read_process_clean(
    'API_19_DS2_en_csv_v2_6183479.csv', 'Forest area (% of land area)')
green, green_t = read_process_clean(
    'API_19_DS2_en_csv_v2_6183479.csv',
    'Total greenhouse gas emissions (kt of CO2 equivalent)')
urban, urban_t = read_process_clean(
    'API_19_DS2_en_csv_v2_6183479.csv', 'Urban population growth (annual %)')


AffGDP_cor = slice_data(AffGDP).rename(
    columns={'2014': 'Agriculture, forestry, and fishing, value added (% of GDP)'})
ele_cor = slice_data(ele).rename(
    columns={'2014': 'Electric power consumption (kWh per capita)'})
arable_cor = slice_data(arable).rename(
    columns={'2014': 'Arable land (% of land area)'})
ener_cor = slice_data(ener).rename(
    columns={'2014': 'Energy use (kg of oil equivalent per capita)'})
fore_cor = slice_data(fore).rename(
    columns={'2014': 'Forest area (% of land area)'})
green_cor = slice_data(green).rename(
    columns={'2014': 'Total greenhouse gas emissions (kt of CO2 equivalent)'})
urban_cor = slice_data(urban).rename(
    columns={'2014': 'Urban population growth (annual %)'})

AffGDP_ele_arable_ener_fore_green_urban = merge_seven(
    AffGDP_cor, ele_cor, arable_cor, ener_cor, fore_cor, green_cor, urban_cor)


#Display Printout results

""" print out the all define functionsd output """

print(AffGDP_ele_arable_ener_fore_green_urban.describe())


create_barplot(ele, 'Country Name', ['1991', '1995', '1999', '2003', '2007',
                                     '2011', '2014'],
               'Electric power consumption (kWh per capita)',
               'Years', 'kWh per capita',
               ('violet', 'black', 'red', 'yellow', 'lightgreen', 'lightblue',))

create_barplot(AffGDP, 'Country Name', ['1991', '1995', '1999', '2003', '2007',
                                        '2011', '2014'],
               'Agriculture, forestry, and fishing, value added (% of GDP)',
               'Years', '% of GDP',
               ('black', 'red', 'yellow', 'lightgreen', 'lightblue', 'violet'))

create_lineplot(urban_t, 'annual %', 'Urban population growth')
create_lineplot(arable_t, '% of land area', 'Arable land')

skew_kurt_plot(green)


#For corellation data analysis selecting and reading data set

"""" For correlation plots  selecting Dataset """

df = pd.read_csv(
    "C:/Users/vamsi/Downloads/API_19_DS2_en_csv_v2_6183479.csv", skiprows=4)


def Correlation_Plot(Cor_data):
    """ create the the correlation plot for the selcted data from worlld bank """

# Selecting required years and indicatoirs to analyze correlations among different countries

    Years = ['1991', '1995', '1999', '2003', '2007', '2011', '2014']

    Cor_data = df[df["Country Name"] == Cor_data]
    Indicators = [
        "Arable land (% of land area)",
        "Agriculture, forestry, and fishing, value added (% of GDP)",
        "Electric power consumption (kWh per capita)",
        "Energy use (kg of oil equivalent per capita)",
        "Forest area (% of land area)",
        "Total greenhouse gas emissions (kt of CO2 equivalent)",
        "Urban population growth (annual %)",
        "CO2 emissions (kt)"]

    Cor_data_indicator = Cor_data.set_index("Indicator Name")
    Cor_data_t = Cor_data_indicator.loc[Indicators, Years].transpose()
    correlation = Cor_data_t.corr()

    # Create a heatmap with annotations
    sns.heatmap(correlation, annot=True, cmap='coolwarm',
                fmt=".2f", linewidths=0.5)

    # Add a title to the plot
    plt.title(
        f"Correlation Plot for {Cor_data.iloc[0]['Country Name']}- Selected Indicators")

    # Display the plot
    plt.show()


def covariance_plot(Cov_data):

    Cov_data = df[df["Country Name"] == Cov_data]
    Years = ['1991', '1995', '1999', '2003', '2007', '2011', '2014']
    Indicators = [
        "Arable land (% of land area)",
        "Agriculture, forestry, and fishing, value added (% of GDP)",
        "Forest area (% of land area)",
        "Urban population growth (annual %)"
    ]

    Cov_data_indicator = Cov_data.set_index("Indicator Name")

    Cov_data_t = Cov_data_indicator.loc[Indicators, Years].transpose()
    covariance = Cov_data_t.cov()

    # Create a heatmap with annotations
    sns.heatmap(covariance, annot=True, cmap='RdBu_r',
                fmt=".2f", linewidths=0.2)

    # Add a title to the plot
    plt.title(
        f"covariance Plot for {Cov_data.iloc[0]['Country Name']} - Selected Indicators")

    # Display the plot
    plt.show()

# Display the defined Correlation and coveriance functions output results


Correlation_Plot("Switzerland")
Correlation_Plot("Germany")

covariance_plot('India')
