import requests
import json
from terminaltables import AsciiTable

CAPITAL_CITIES = ['Tirana', 'Andorra la Vella', 'Vienna', 'Minsk', 'Brussels', 'Sarajevo', 'Sofia',
                  'Zagreb', 'Prague',
                  'Copenhagen', 'Tallinn', 'Helsinki', 'Paris', 'Berlin', 'Athens', 'Budapest', 'Reyjavík',
                  'Dublin',
                  'Rome', 'Pristina',
                  'Riga', 'Vaduz', 'Vilnius', 'Luxembourg', 'Skopje', 'Valletta', 'Warsaw']


class WeatherApi:
    def __init__(self):
        self.retryCounter = 0

    def getEnvVar(self, wordkey):
        try:
            self.wordkey = wordkey
            with open("envVars.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data['envVars'][wordkey]
        except FileNotFoundError:
            print('File not found :(')
            exit(1)

    def currentConditionsData(self):
        self.response = requests.get(self.getEnvVar("URL"), params={"apikey": self.getEnvVar("API_KEY")})
        if self.response.status_code != requests.codes.ok:
            print(f'Error {self.response.status_code}')
            exit(0)
        else:
            return self.response

    def dataFilteringAndPrinting(self):
        self.retryCounter = 0
        while self.retryCounter < self.getEnvVar("MAX_RETRY"):
            self.response = self.currentConditionsData()
            if type(self.response) == "string":
                break
            self.retryCounter += 1

        table_rows = [
            ['Miasto', 'Data obserwacji', 'Temperatura stopnie celcjusza']
        ]

        for row in json.loads(self.response.text):
            if row['EnglishName'] in CAPITAL_CITIES:
                table_rows.append([
                    row['EnglishName'],
                    row['LocalObservationDateTime'],
                    row['Temperature']['Metric']['Value']
                ])
        table = AsciiTable(table_rows)
        return print(table.table)


if __name__ == '__main__':
    print('Pan da 3 :(')
    App = WeatherApi()
    data = App.dataFilteringAndPrinting()
