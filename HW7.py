import pandas as pd
df=pd.read_csv('/Users/momo/Desktop/titles.csv',header=0)
total= df[(df.year >= 1900) & (df.year <=2016)]
answer= len(total)

df1=pd.read_csv('/Users/momo/Desktop/cast.csv',header=0)
name=df1[df1.name == 'John Wayne']
len(name)

name1=df1[(df1.name =='John Wayne') & (df1.character.str.contains ('John ')) ]
len(name1)


def average_into_diagonal(x):
    '''
    return average of non-diagonal elements with values filled into the diagonal

    :param x: square two-dimensional input array
    :type x: numpy array
    :returns: numpy array

    '''
    assert isinstance(x, np.ndarray)
    assert x.ndim == 2
    assert x.shape[0] == x.shape[1]  # square arrays only
    x = np.array(x, dtype=np.float64)
    for i in range(5):
        x[i, i] = sum(x[i]) / 4
    return x


x=np.array([[0,   3, 14, 13, 12],
 [13,  0,  8,  5, 11],
 [11, 11,  0, 12, 10],
 [11, 12,  1,  0, 10],
 [13, 12, 11,  4,  0]])

average_into_diagonal(x)

