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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


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
