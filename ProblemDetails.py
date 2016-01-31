'''
This class provide an API to manipulate UVA stat

'''

import csv
from datetime import datetime

__author__ = 'Azad'


class ProblemDetails(object):
    '''
     This class responsible for all user interface to get information
     about an user csv file collected from uhunt page

    '''

    def __init__(self, name=None, id=None,
                 verdict=None, language=None, rank=None,
                 runtime=None, date_of_submit=None):
        """
            Args:

                name: (str)
                id: (str)
                verdict: (str)
                language: (str)
                rank: (str)
                runtime: (str)
                date_of_submit: (str)
        """
        self.all_submission = []
        self.all_problem_ids = []
        self.name = name
        self.id = id
        self.verdict = verdict
        self.language = language
        self.rank = rank
        self.runtime = runtime
        self.date_of_submit = date_of_submit
        self.max_try = 40

    def read_csv_file(self, file_name):
        """
        Read from file name

        Args:
            file_name (str): This is the file name and it must be a csv format.
        """
        all_ids = []
        with open(file_name + ".csv", "rb") as f:
            reader = csv.reader(f, delimiter=",")
            for i, line in enumerate(reader):

                if i == 0:
                    continue

                name = ','.join([line[x] for x in range(1, len(line) - 5)])

                problem_details = ProblemDetails(
                    id=int(line[0]), name=name,
                    verdict=line[-5], language=line[-4],
                    runtime=line[-3], rank=line[-2],
                    date_of_submit=datetime.strptime(line[-1], "%Y-%m-%d %H:%M")
                )

                all_ids.append(problem_details.id)  # append all ids

                self.all_submission.append(problem_details)  # append all submissions

                self.all_submission.sort(key=lambda x: x.id)  # sort by id

            self.all_problem_ids = list(set(all_ids))  # all submitted problems id
            self.all_problem_ids.sort()  # sort by id

    def get_all_problem_ids(self):
        """
            This method returns all sorted problems id
        """
        return self.all_problem_ids

    # def show_all(self):
    #
    # print self.all_problem_ids
    #     print len(self.all_problem_ids)

    def count(self, id):
        """
            Count how many problem(s) in all submission are matched by id

            Args:
                id: (int) the problem's id

            Returns:
                count: (int)

        """
        count = 0
        for problem in self.all_submission:
            if problem.id == id:
                count += 1

        return count

    def filter_by_id(self, id):
        """
            Problem(s) list in all submission are matched by id

            Args:
                id: (int) the problem's id

            Returns:
                problem: (list) list of all problems are matched by id
        """
        return [problem for problem in self.all_submission if problem.id == id]

    def number_of_attempts_to_solve(self, id):
        """
            How many unsuccessful attempts for a specific problem id

            Args:
                id: (int) the problem's id

            Returns:
                index: (int) number of unsuccessful attempts

        """

        problems = self.filter_by_id(id)
        if not problems:
            return -1
        problems.sort(key=lambda x: x.date_of_submit)  # sort by date

        for index, problem in enumerate(problems):
            if problem.verdict == 'Accepted':
                return index
        return 500  # Not yet solved very long number too many attempts yet need

    def attempt_for_all(self):
        """
            For all problems how many times each problem is submitted to get accepted


            Returns:
                index: (int, int )  (attempt, count problems) [(0, 20) , (1, 34)]

                        so 0 attempt 20 problem solve 1 attempts 34 problems solve

        """
        attempts = range(self.max_try)  #Assume how max how many attepmts
        tries = []  # an empty array
        for attempt in range(self.max_try):
            one_try = []
            for x in self.get_all_problem_ids():

                if self.number_of_attempts_to_solve(x) == attempt:
                    one_try.append(x)

            tries.append(len(one_try))

        return zip(attempts, tries)

    def problem_by_attepmts(self, how_many):

        """
            How many problems solved by specific number of attempts

            Args:
                how_many: (int) number of tries to solve

            Returns:
                index: (list) id's of all problem solved by specific number of attempts

        """
        one_try = []
        for x in self.get_all_problem_ids():
            if self.number_of_attempts_to_solve(x) == how_many:
                one_try.append(x)

        return one_try

    def __repr__(self):

        """
            Just to show an user
        """
        return 'ProblemDetails(id=%s, name=%s, submission date=%s)' % (self.id, self.name, self.date_of_submit)


if __name__ == "__main__":
    od = ProblemDetails()

    od.read_csv_file('all')

    x = od.attempt_for_all()

    pair = [p for p in x if p[1] != 0]

    total = [b for (a, b) in pair]

    print sum(total)