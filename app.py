import requests
from bs4 import BeautifulSoup
import re
import datetime


def display_title():
    print("---------------------------------")
    print("     Youtube Playlist Length     ")
    print("---------------------------------")


def get_playlist():
    playlist_url = input("Enter URL of playlist: ")
    playlist_url = playlist_url
    playlist_request = requests.get(playlist_url)
    return playlist_request


def parse_length(request):
    soup = BeautifulSoup(request.content, 'html.parser')
    results = soup.find_all('div', {"class": "timestamp"})
    times = []
    for result in results:
        times.append(result.find_all(text=True))
    return times


def process_times(times_list):
    single_times = []
    minutes = []
    seconds = []

    for time in times_list:
        single_times.append(time[0])

    for time in single_times:
        found = re.search('([0-9]+):([0-9]{2})', time)
        if found:
            minutes.append(int(found.group(1)))
            seconds.append(int(found.group(2)))

    total_seconds = sum(minutes) * 60 + sum(seconds)

    return total_seconds


def calculate_length(total_seconds):
    result = str(datetime.timedelta(seconds=total_seconds))

    print("Length of Playlist (H:M:S): {}".format(result))


def main():

    display_title()
    while True:
        cont = int(input("Enter 1 to continue and 0 to exit: "))
        if cont is 0:
            break
        playlist_request = get_playlist()
        times_list = parse_length(playlist_request)
        num_seconds = process_times(times_list)
        calculate_length(num_seconds)


if __name__ == "__main__":
    main()
