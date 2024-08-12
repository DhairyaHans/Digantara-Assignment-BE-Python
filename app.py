from flask import Flask, render_template, url_for, redirect, request
from jobs_utility import JobsUtility
from Model.jobs_list import JobsList
from Model.job import Job
from datetime import datetime
from main import db, jobsUtility
import pytz

ist_tz = pytz.timezone("Asia/Kolkata")

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/jobs", methods=['GET'])
def all_jobs():
    jobs = jobsUtility.show_all_data()
    return render_template("all_jobs.html", jobs=jobs)

@app.route("/jobs/<jobId>/<jobType>", methods=['GET'])
def specific_job(jobId, jobType):
    jobDetails = jobsUtility.show_one_job(jobId=jobId, jobType=jobType)
    print(jobDetails)
    return render_template("show_job.html", job=jobDetails, jobType=jobType)

@app.route("/add_job", methods=['GET', 'POST'])
def add_job():
    if request.method == 'POST':
        # Retrieve data from the form
        print("REPEAT", request.form.get('RepeatJob'))
        job_obj = {
            "jobName" : request.form.get('jobName'),
            "jobDescription" : request.form.get('jobDescription'),
            "repeat" : True if request.form.get('RepeatJob')=='yes' else False,
            "scheduledTime" : f"{request.form.get('date')} {request.form.get('time')}" ,
            "runTime": 0,
            "isCompleted": False
        }
        
        print("ADD", job_obj)
        job_obj["repeatAfter"] = int(request.form.get("repeatAfter")) if job_obj["repeat"] else 0

        job = Job(jobName=job_obj["jobName"],
                  jobDescription=job_obj["jobDescription"],
                  repeat=job_obj["repeat"],
                  scheduledTime=job_obj["scheduledTime"],
                  repeatAfter=job_obj["repeatAfter"],
                  runTime=job_obj["runTime"],
                  isCompleted=job_obj["isCompleted"]
                )
        
        print(job_obj)
        print(job)
        
        jobsUtility.add_job(job)
        # Redirect or render a response
        return redirect(url_for('hello_world'))
    else:
        today_date = datetime.now(tz=ist_tz).strftime('%Y-%m-%d %H:%M:%S')
        return render_template("add_job.html", today_date=today_date)
    
@app.route("/execute", methods=["GET"])
def execute_task():
    jobsUtility.execute_Jobs()
    jobsUtility.show_all_data()
    return redirect(url_for('hello_world'))

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
        "repeat": False,
        "scheduledTime": "2024-08-11 18:00:00",  
        "repeatAfter": 0,
        "runTime": 0,
        "isCompleted": False
    }
]

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

if __name__ == "__main__":
    app.run()
        