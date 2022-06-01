from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    jobs = set()
    for job in data:
        jobs.add(job["job_type"])
    return jobs


def filter_by_job_type(jobs, job_type):
    types = []
    for type in jobs:
        if type["job_type"] == job_type:
            types.append(type)
    return types


def get_unique_industries(path):
    data = read(path)
    industries = set()
    for industry in data:
        if industry["industry"] != '':
            industries.add(industry["industry"])
    return industries


def filter_by_industry(jobs, industry):
    types = []
    for type in jobs:
        if type["industry"] == industry:
            types.append(type)
    return types


def get_max_salary(path):
    data = read(path)
    max_number = 0
    for row in data:
        if row["max_salary"].isdigit() and int(row["max_salary"]) > max_number:
            max_number = int(row["max_salary"])
    return max_number


def get_min_salary(path):
    data = read(path)
    min_number = set()
    for row in data:
        if row["min_salary"].isdigit():
            min_number.add(int(row["min_salary"]))
    return min(min_number)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError()
    elif type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError()
    elif int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError()
    elif type(salary) != int:
        raise ValueError()
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
