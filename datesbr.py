from datetime import datetime, timedelta


class Datas:
    def __init__(self):
        self.register_moment = datetime.today()

    def __str__(self):
        return self.format_date()

    def register_month(self):
        months_of_year = ["Janeiro", "Fevereiro", "Março",
                          "Abril", "Maio", "Junho",
                          "Julho", "Agosto", "Setembro"
                                             "Outubro", "Novembro", "Dezembro"
                          ]
        register_month = self.register_moment.month - 1

        return months_of_year[register_month]

    def day_of_week(self):
        day_of_week_list = ["Segunda", "Terça", "Quarta", "quinta", "Sexta", "Sábado", "Domingo"]
        day_of_week = self.register_moment.weekday()
        return day_of_week_list[day_of_week]

    def format_date(self):
        formated_date = self.register_moment.strftime("%d/%m/%Y %H:%M")
        return formated_date

    def time_registered(self):
        time_registered = (datetime.today() + timedelta(days=30)) - self.register_moment
        return time_registered
