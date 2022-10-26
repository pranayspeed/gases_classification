import pandas as pd



def get_data(data_file_path = "input_data.xlsx"):
    df_gases = pd.read_excel(data_file_path)

    #select_cols = ['Time', 
    select_cols = ['CH01', 'CH02',
        'CH03', 'CH04', 'CH05', 'CH06', 'CH07', 'CH08', 'CH09', 'CH10', 'CH11',
        'CH12', 'CH13', 'CH14', 'CH15', 'CH16', 'CH17', 'CH18', 'CH19', 'CH20',
        'CH21', 'CH22', 'CH23', 'CH24', 'CH25', 'CH26', 'CH27', 'CH28', 'CH29',
        'CH30', 'CH31', 'CH32']

    #print(df_gases[select_cols]) 
    return df_gases[select_cols]      