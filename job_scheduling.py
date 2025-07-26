# job_scheduling.py

import pandas as pd

def johnsons_rule_2_machines(jobs):
    sorted_jobs = []
    jobs = jobs.copy()

    while not jobs.empty:
        min_index = jobs[["Machine1", "Machine2"]].min().idxmin()
        job_idx = jobs[["Machine1", "Machine2"]].idxmin().min()

        if jobs.loc[job_idx, "Machine1"] < jobs.loc[job_idx, "Machine2"]:
            sorted_jobs.insert(0, jobs.loc[job_idx])
        else:
            sorted_jobs.append(jobs.loc[job_idx])

        jobs = jobs.drop(job_idx)

    return pd.DataFrame(sorted_jobs)

if __name__ == "__main__":
    data = {
        'Job': ['A', 'B', 'C', 'D'],
        'Machine1': [3, 2, 5, 4],
        'Machine2': [4, 3, 2, 1]
    }

    jobs_df = pd.DataFrame(data)
    jobs_df.set_index('Job', inplace=True)

    print("Original Job Data:")
    print(jobs_df)

    ordered_jobs = johnsons_rule_2_machines(jobs_df)
    print("\nOptimal Job Order (2-Machine Johnson’s Rule):")
    print(ordered_jobs)
