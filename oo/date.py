class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        print('new Python Object')

    def __str__(self):
        return f'{self.day} - {self.month} - {self.year}'


date = Date(1, 1, 2018)
print(date)
