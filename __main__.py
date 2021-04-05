import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



class starterclass:
    def __init__(self):
        self.data_path = "Copy of data.xlsx"
        self.data_frame_excel = None
        self.df_2 = None
        self.random_data = 0


        # Load that data
        self.load_dataframe()
        self.create_datastuff()
        #plot data
        self.graph_the_data(self.df_2)

    def create_datastuff(self):
        self.random_data = np.random.randint(0, 100, size = (100,2))
        #self.random_y = np.random.randint(0, 100, size = 100,2)
        self.df_2 = pd.DataFrame(self.random_data,columns=['x value','y value'])


    def load_dataframe(self):
        self.data_frame_excel = pd.read_excel(self.data_path)

    def graph_the_data(self,df):
        df.plot(kind='line', x='x value', y='y value')
        plt.show()



test1 = starterclass()