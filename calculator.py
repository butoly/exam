from pandas import DataFrame


class Calculator:
    def __init__(self):
        pass

    def get_total_cases_by_country(self, continent, df: DataFrame):
        total_cases_by_country = df[df.continent == continent].groupby("location")["new_cases"].agg("sum")
        return total_cases_by_country

    def get_avg_country(self, continent, df):
        avg_by_counties = df[df.continent == continent].groupby('location')['new_deaths'].mean()
        avg_by_continent = df[df.continent == continent].groupby('continent')['new_deaths'].mean()[0]
        var = avg_by_counties[avg_by_counties < avg_by_continent]
        return var
