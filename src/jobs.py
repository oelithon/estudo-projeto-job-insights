from functools import lru_cache
import csv


@lru_cache
def read(path):
    data = []
    with open(path) as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for row in jobs_reader:
            data.append(row)
    return data
