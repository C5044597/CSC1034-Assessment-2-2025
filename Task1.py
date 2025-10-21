class Job:
    def __init__(self, name, category, rate, date, hours):
        self.name = name
        self.category = category
        self.rate = rate
        self.date = date
        self.hours = hours

    def get_name(self):
        return self.name
    def get_category(self):
        return self.category
    def get_rate(self):
        return self.rate
    def get_date(self):
        return self.date
    def get_hours(self):
        return self.hours
    def __eq__(self, other):
        if not isinstance(other, Job):
            return False
        return (self.name == other.name and self.category == other.category and self.rate == other.rate and self.date == other.date and self.hours == other.hours)
    def __hash__(self):
        return hash(self.name and self.category and self.rate and self.date and self.hours)
    def __str__(self):
        return f"Name ={self.name}\nCategory ={self.category}\nRate ={self.rate}\nDate ={self.date}\nHours ={self.hours}"
    def __repr__(self):
        return self.__str__()

class JobManager:
    def __init__(self, jobs=None):
        if jobs is None:
            self.jobs = []
        else:
            self.jobs = jobs
    def get_jobs(self):
        return self.jobs
    def __str__(self):
        return (f"{len(self.jobs)} jobs")
    def __repr__(self):
        return self.__str__()
    def add_job(self, job):
        pass
    def remove_job(self, job):
        pass
    def edit_job(self, old_job, new_job):
        pass
    def search_by_category(self, category):
        pass
    def search_by_rate(self, rate):
        pass
    def search_by_name_and_date(self, name, date):
        pass
    def get_total_cost_per_name(self, names):
        pass
    def get_category_count_per_name(self):
        pass
    def load_from_file(self, file_name):
        pass
    def save_to_file(self, file_name):
        pass
