import pandas as pd

def load_client_data():
    data = pd.read_csv(r".\terugkomdag\client_data.csv", sep=';')
    return data

def load_monthly_data():
    data = pd.read_csv(r".\terugkomdag\monthly_data.csv", sep=';')
    return data

def select_clients(client_data):
    return client_data[client_data["Missing_2010"] == False]["Klantnummer"]

def claculate_clients(monthly_data, selected_clients):
    data_to_use = monthly_data[monthly_data["Klantnummer"].isin(selected_clients)]
    return data_to_use.groupby(["Klantnummer"])["Betaalde rente"].sum()

client_data = load_client_data()
selected_clients = select_clients(client_data)

monthly_daat = load_monthly_data()

intreest_per_client = claculate_clients(monthly_daat, selected_clients)
print(intreest_per_client)
