def miasta_panstwa(city, country, population=''):
	"""Funkcja z miastami i państwami."""
	if population:
		return city.title() + ", " + country.title() + ' - populacja ' + \
		population
	else:
		return city.title() + ", " + country.title()
