import pandas as pd

class PEP:
    def __init__(self):
        path = "data/pep.csv"
        self.data = self.read_data(path)

    def read_data(self, path):
        """
        Reads csv file data and outputs as pandas dataframe

        Input: (str) path to datafile
        output: (DataFrame) containing entire PEP dataset
        """
        return pd.read_csv(path, sep = ",", header='infer', low_memory=False)


    def check_name(self, names = list):
        """
        Checks for matching names in PEP registry
        input (list): List of strings containing names
        output(dataframe): Dataframe containing matching entries
        """
        #Searchable pattern used by Pandas to search for all names simultaneously
        pattern = '|'.join(names)

        #search for matches in PEP in names and aliases (not case sensitive)
        matching_name = self.data[self.data[['name', 'aliases']].apply(lambda row: row.astype(str).str.contains(pattern, case=False).any(),
                                axis=1)]
        #return database matches
        return matching_name


def main():
    reader = PEP()
    #reader = PEP('data/pep_small.csv')
    reader.check_name(['Arnulf Nilsen', 'Arvid Karstein Jordet',
                        'Thomas Svankil', 'Aleksander Fjeldseth Ringnes',
                        'Knut Arild Hareide'])
    #reader.check_name('KnutArildHareide')

if __name__ == "__main__":
    main()
