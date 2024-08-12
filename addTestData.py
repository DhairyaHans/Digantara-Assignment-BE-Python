from Model.job import Job
from Model.jobs_list import JobsList
from jobs_utility import JobsUtility

def create_dummy_data():
    dummyData = [
        {
            "jobName": "Monday Alarm",
            "jobDescription": "Alarm scheduled for every monday",
            "repeat": True,
            "scheduledTime": "2024-08-12 00:00:00",  
            "repeatAfter": 7,
            "runTime": 0,
            "isCompleted": False
        },
        {
            "jobName": "Daily Alarm",
            "jobDescription": "Alarm scheduled Daily at 11 AM",
            "repeat": True,
            "scheduledTime": "2024-08-12 11:00:00",  
            "repeatAfter": 1,
            "runTime": 0,
            "isCompleted": False
        },
        {
            "jobName": "Today's Alarm",
            "jobDescription": "Alarm scheduled for Today at 6PM",
            "repeat": True,
            "scheduledTime": "2024-08-11 18:00:00",  
            "repeatAfter": 2,
            "runTime": 0,
            "isCompleted": False
        }
    ]

    db = JobsList()

    jobsUtility = JobsUtility(db)

    for data in dummyData:
        job = Job(jobName=data["jobName"],
                jobDescription=data["jobDescription"],
                repeat=data["repeat"],
                scheduledTime=data["scheduledTime"],
                repeatAfter=data["repeatAfter"],
                runTime=data["runTime"],
                isCompleted=data["isCompleted"],
                )

        jobsUtility.add_job(job)
        
    jobsUtility.show_all_data()
    jobsUtility.execute_Jobs()
    jobsUtility.show_all_data()




