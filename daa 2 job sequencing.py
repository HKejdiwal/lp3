def job_sequencing(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)

    n = len(jobs)
    result = [None] * n
    total_profit = 0

    for job in jobs:
        for j in range(min(n, job[1])-1, -1, -1):
            if result[j] is None:
                result[j] = job[0]
                total_profit += job[2]
                break

    print("Selected Jobs:", result)
    print("Maximum Profit:", total_profit)


n = int(input("Enter number of jobs: "))
jobs = []

for i in range(n):
    job = input("Enter job ID: ")
    deadline = int(input("Enter deadline: "))
    profit = int(input("Enter profit: "))
    jobs.append((job, deadline, profit))

job_sequencing(jobs)