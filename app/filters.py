from server.lib.jinja2.filters import environmentfilter

@environmentfilter
def age(birthdate):
    return int((date.today() - birthdate).days/365.2425)
