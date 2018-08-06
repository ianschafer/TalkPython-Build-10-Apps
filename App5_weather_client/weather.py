import requests  # package "requests" had to be installed using pip
import bs4  # bs4 is the package beautifulsoup4
import collections

# WeatherReport = collections.namedtuple('WeatherReport', 'cond, temp, scale, loc')
WeatherReport = collections.namedtuple('WeatherReport', 'cond, temp, loc')


def main():
    # t = 1, 7, 'cat', [1,2,3]
    # print(t)
    # print(t[1])
    #
    # n1, n2, s, l = t
    # print(n1, n2, s, l)
    # return

    print_the_header()

    print('Lets check the weather in George ... ')

    html = get_html_from_web()
    report = get_weather_from_html(html)

    print('The temp in {} is {} and {}'.format(
        report.loc,
        report.temp,
        report.cond
    ))

    # display for the forecast


def print_the_header():
    print('---------------------------------')
    print('           WEATHER APP')
    print('---------------------------------')
    print()


def get_html_from_web():
    url = 'https://www.wunderground.com/weather/za/george'
    response = requests.get(url)
    # print(response.status_code) ... 200 is successful, 404 is not good
    # print(response.text[0:250]) ... scrapes first 250 characters from url

    return response.text


def get_weather_from_html(html):
    # cityCss = '.region-content-header h1'
    # weatherScaleCss = '.wu-unit-temperature .wu-label'
    # weatherTempCss = '.wu-unit-temperature .wu-value'
    # weatherConditionCss = '.condition-icon'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    loc = find_city_and_state_from_location(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    # Covert temp to C°
    tempc = temp[0] +temp[1]
    numc = (float(tempc)-32)/1.8
    strnumc = "{:.2f}".format(numc)
    tempc = strnumc + '°C'

    # print('tempc ' + tempc)
    # print('numc ' + strnumc)
    # print(condition, temp, scale, loc)
    # return condition, temp, scale, loc
    # report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    report = WeatherReport(cond=condition, temp=tempc, loc=loc)
    return report


def find_city_and_state_from_location(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text

# Remember "dunder name" is there to prevent main() from running if someone else decides to
# use this file and imports it, i.e.main() will only run if the __name__ returns "__main__".
# You don't have to type it out you can get it from a Live Template by typing main whereupon pyCharm
# will give you some choices one of which is "if __name__ == '__main__':" ...
if __name__ == '__main__':
    main()
