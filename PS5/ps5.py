# -*- coding: utf-8 -*-
# Problem Set 5: Experimental Analysis
# Name: 
# Collaborators (discussion):
# Time:

from audioop import mul
from cProfile import label
import pylab
import re

# cities in our weather data
CITIES = [
    'BOSTON',
    'SEATTLE',
    'SAN DIEGO',
    'PHILADELPHIA',
    'PHOENIX',
    'LAS VEGAS',
    'CHARLOTTE',
    'DALLAS',
    'BALTIMORE',
    'SAN JUAN',
    'LOS ANGELES',
    'MIAMI',
    'NEW ORLEANS',
    'ALBUQUERQUE',
    'PORTLAND',
    'SAN FRANCISCO',
    'TAMPA',
    'NEW YORK',
    'DETROIT',
    'ST LOUIS',
    'CHICAGO'
]

TRAINING_INTERVAL = range(1961, 2010)
TESTING_INTERVAL = range(2010, 2016)

"""
Begin helper code
"""
class Climate(object):
    """
    The collection of temperature records loaded from given csv file
    """
    def __init__(self, filename):
        """
        Initialize a Climate instance, which stores the temperature records
        loaded from a given csv file specified by filename.

        Args:
            filename: name of the csv file (str)
        """
        self.rawdata = {}

        f = open(filename, 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')

            date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))

            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature
            
        f.close()

    def get_yearly_temp(self, city, year):
        """
        Get the daily temperatures for the given year and city.

        Args:
            city: city name (str)
            year: the year to get the data for (int)

        Returns:
            a 1-d pylab array of daily temperatures for the specified year and
            city
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return pylab.array(temperatures)

    def get_daily_temp(self, city, month, day, year):
        """
        Get the daily temperature for the given city and time (year + date).

        Args:
            city: city name (str)
            month: the month to get the data for (int, where January = 1,
                December = 12)
            day: the day to get the data for (int, where 1st day of month = 1)
            year: the year to get the data for (int)

        Returns:
            a float of the daily temperature for the specified time (year +
            date) and city
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]

def se_over_slope(x, y, estimated, model):
    """
    For a linear regression model, calculate the ratio of the standard error of
    this fitted curve's slope to the slope. The larger the absolute value of
    this ratio is, the more likely we have the upward/downward trend in this
    fitted curve by chance.
    
    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by a linear
            regression model
        model: a pylab array storing the coefficients of a linear regression
            model

    Returns:
        a float for the ratio of standard error of slope to slope
    """
    assert len(y) == len(estimated)
    assert len(x) == len(estimated)
    EE = ((estimated - y)**2).sum()
    var_x = ((x - x.mean())**2).sum()
    SE = pylab.sqrt(EE/(len(x)-2)/var_x)
    return SE/model[0]

"""
End helper code
"""

def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        degs: a list of degrees of the fitting polynomial

    Returns:
        a list of pylab arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    coeff = []
    for deg in degs:
        coeff.append(pylab.polyfit(x,y,deg))
    return coeff


def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    
    Args:
        y: 1-d pylab array with length N, representing the y-coordinates of the
            N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the R-squared error term
    """
    mean = sum(y) / len(y)
    num, den = 0, 0
    for i in range(len(y)):
        num += (y[i] - estimated[i]) ** 2
        den += (y[i] - mean) ** 2
    r_square = 1 - num/den
    return r_square

def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-squared value for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        R-square of your model evaluated on the given data points,
        and SE/slope (if degree of this model is 1 -- see se_over_slope). 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    for model in models:

        p = pylab.poly1d(model)
        r2 = r_squared(y, p(x))
        deg = len(model)-1
        pylab.figure()
        pylab.plot(x,y,'bo',label='Measured')
        pylab.plot(x,p(x),'r-',label='Fit')
        pylab.legend(loc = 'best')
        pylab.xlabel('Years')
        pylab.ylabel('°C')
        if run == 'A': # to show the difference with same scale for A
            pylab.ylim([-20,20])
        if deg == 1:
            se = se_over_slope(x, y, p(x), model)
            pylab.title('R² = ' + str(round(r2,2)) + ', ' + 
                        'Degrees = ' + str(deg) + '\n' +
                        'Standard error over slope = ' + str(round(se,2)))
        else:
            pylab.title('R² = ' + str(round(r2,2)) + ', ' + 
                        'Degrees = ' + str(deg))
        pylab.show()


def gen_cities_avg(climate, multi_cities, years):
    """
    Compute the average annual temperature over multiple cities.

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to average over (list of str)
        years: the range of years of the yearly averaged temperature (list of
            int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the average annual temperature over the given
        cities for a given year.
    """
    year_avg = []
    for year in years:
        city_avg = []
        for city in multi_cities:
            temp = climate.get_yearly_temp(city,year)
            city_avg.append(sum(temp) / len(temp))
        year_avg.append(sum(city_avg) / len(city_avg))
    return pylab.array(year_avg)

def moving_average(y, window_length):
    """
    Compute the moving average of y with specified window length.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        window_length: an integer indicating the window length for computing
            moving average

    Returns:
        an 1-d pylab array with the same length as y storing moving average of
        y-coordinates of the N sample points
    """
    ma = []
    l, r = 0, 1
    while l < r and (l >= 0 and r >=1) and (l <= len(y) - 1 and r <= len(y)):   
        window = y[l:r]
        window_avg = round(sum(window) / len(window),2)
        ma.append(window_avg)

        if r - l < window_length:
            r += 1
        else:
            l += 1
            r += 1
    return pylab.array(ma)

def rmse(y, estimated):
    """
    Calculate the root mean square error term.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:s
        a float for the root mean square error term
    """
    return (((sum((y - estimated)**2)) / len(y)) ** 0.5)




def gen_std_devs(climate, multi_cities, years):
    """
    For each year in years, compute the standard deviation over the averaged yearly
    temperatures for each city in multi_cities. 

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to use in our std dev calculation (list of str)
        years: the range of years to calculate standard deviation for (list of int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the standard deviation of the average annual 
        city temperatures for the given cities in a given year.
    """
    year_std = []
    for year in years:
        cities_temps = []
        for city in multi_cities:
            cities_temps.append(climate.get_yearly_temp(city,year))
        daily_avg_temp = pylab.array(cities_temps).mean(axis = 0)
        year_std.append(pylab.std(daily_avg_temp))
    return year_std

def evaluate_models_on_testing(x, y, models):
    """
    For each regression model, compute the RMSE for this model and plot the
    test data along with the model’s estimation.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        RMSE of your model evaluated on the given data points. 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    for model in models:

        p = pylab.poly1d(model)
        r = rmse(y, p(x))
        deg = len(model)-1
        pylab.figure()
        pylab.plot(x,y,'bo',label='Measured')
        pylab.plot(x,p(x),'r-',label='Fit')
        pylab.legend(loc = 'best')
        pylab.xlabel('Years')
        pylab.ylabel('°C')
        if deg == 1:
            se = se_over_slope(x, y, p(x), model)
            pylab.title('RMSE = ' + str(round(r,2)) + ', ' + 
                        'Degrees = ' + str(deg) + '\n' +
                        'Standard error = ' + str(round(se,2)))
        else:
            pylab.title('RMSE = ' + str(round(r,2)) + ', ' + 
                        'Degrees = ' + str(deg))
        pylab.show()

if __name__ == '__main__':
    run = 'D'
    c = Climate('PS5/data.csv')
    tr_i = pylab.array(TRAINING_INTERVAL)
    te_i = pylab.array(TESTING_INTERVAL)

    if run == 'A':
        # Part A.4.I
        nytemps = []
        for t in TRAINING_INTERVAL:
            nytemps.append(c.get_daily_temp('NEW YORK', 1, 10, t))
        model = generate_models(tr_i,nytemps,[1])
        evaluate_models_on_training(tr_i,nytemps,model)

        # # Part A.4.II
        avg_nytemps = []
        for t in TRAINING_INTERVAL:
            temp = c.get_yearly_temp('NEW YORK', t)
            avg_temp = sum(temp) / len(temp)
            avg_nytemps.append(avg_temp)
        model = generate_models(tr_i,avg_nytemps,[1])
        evaluate_models_on_training(tr_i,avg_nytemps,model)

    if run == 'B':
        # Part B
        years_avg = gen_cities_avg(c,CITIES,tr_i)
        models = generate_models(tr_i,years_avg,[1])
        evaluate_models_on_training(tr_i,years_avg, models)

    if run == 'C':
        # Part C
        years_avg = gen_cities_avg(c,CITIES,tr_i)
        ma = moving_average(years_avg, 5)
        models = generate_models(tr_i,ma,[1])
        evaluate_models_on_training(tr_i, ma, models)

    if run == 'D':
        # Part D.2.I
        years_avg = gen_cities_avg(c,CITIES,tr_i)
        ma = moving_average(years_avg, 5)
        models = generate_models(tr_i,ma,[1, 2, 20])
        evaluate_models_on_training(tr_i,ma, models)
        
        # Part D.2.II
        years_avg_test = gen_cities_avg(c,CITIES,te_i)
        ma_test = moving_average(years_avg_test, 5)
        evaluate_models_on_testing(te_i,ma_test, models) # using same models as before, but with test data

    if run == 'E':
        # Part E
        stdev = gen_std_devs(c, CITIES, tr_i)
        ma = moving_average(stdev, 5)
        models = generate_models(tr_i, ma, [1])
        evaluate_models_on_training(tr_i, ma, models)