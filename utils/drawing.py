import pandas as pd
from scipy.stats import uniform
import warnings
warnings.filterwarnings("ignore")


def discrete_inverse_trans(prob_vec):
    """Function for drawing a value using inverse transform for discrete
    variables"""

    U = uniform.rvs(size=1)
    if U <= prob_vec[0]:
        return 1
    else:
        for i in range(1, len(prob_vec)):
            if sum(prob_vec[0:i]) < U and sum(prob_vec[0:i+1]) >= U:
                return i+1
    return 1


def transform_into_marginals_clean(row):
    """Creating a probability vector from the choosen row/column from contigency
    matrix"""

    marginals = []
    suma = sum(row)
    for i in range(len(row)):
        marginals.append((row[i]/suma))
    return marginals


def draw_from_marginals(df, column):
    """Draw from the distribution resulting from the column of the dataframe"""

    temp = df[column].value_counts().sort_index()
    index = discrete_inverse_trans(
        transform_into_marginals_clean(temp.tolist()))
    unique = sorted(temp.index)
    return unique[index-1]


# In order to form conditionals between different variables,
# we have to count each category of each variable.
# Because of this we have to create contigency tables

def create2dconditional(column1, column2):
    data_crosstab = pd.crosstab(column1, column2, margins=False)
    return data_crosstab


def create3dconditional(column1, column2, column3):
    data_crosstab = pd.crosstab([column1, column2], [column3], margins=False)
    return data_crosstab


def create4dconditional(column1, column2, column3, column4):
    data_crosstab = pd.crosstab([column1, column2, column3], [column4],
                                margins=False)
    return data_crosstab


def createNconditional(columns):
    data_crosstab = pd.crosstab(columns[:-1], columns[-1],
                                margins=False)
    return data_crosstab


def DFconditional(df, col, columns=None):
    if columns is None:
        columns_compare = df.columns.difference([col]).values
        data_crosstab = pd.crosstab([df[c] for c in columns_compare], df[col],
                                    margins=False)
    else:
        data_crosstab = pd.crosstab([df[c] for c in columns], df[col],
                                    margins=False)
    return data_crosstab
