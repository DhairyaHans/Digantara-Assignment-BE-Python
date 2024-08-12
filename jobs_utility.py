from Model.job import Job
from Model.jobs_list import JobsList
from Model.completedJob import CompletedJob
from Model.executedJob import ExecutedJob
from datetime import datetime, timedelta
import constants
import heapq


class JobsUtility:
    def __init__(self, jobsList: JobsList):
        self.jobsList = jobsList

    def add_job(self, new_job: Job):
        try:
            heapq.heappush(self.jobsList.jobsQueue, new_job)
            print(f"Job {new_job.jobName}, is scheduled for {new_job.scheduledTime}")
        except Exception as exp:
            print("Error occured while Adding Job")
            raise exp

    def show_all_jobs(self):
        print(self.jobsList.jobsQueue)
        tempQueue = self.jobsList.jobsQueue.copy()
        currently_active_jobs = []
        while tempQueue:
            job = heapq.heappop(tempQueue)
            if not job.isCompleted:
                currently_active_jobs.append(job.__dict__)

        print(currently_active_jobs)
        return currently_active_jobs
    
    def show_one_job(self, jobId, jobType):
        print(jobId)
        if jobType == constants.CURRENT:
            for job in self.jobsList.jobsQueue:
                print(job, job.jobId, type(job.jobId))
                if job.jobId == jobId:
                    print(job.__dict__)
                    return job.__dict__
            else:
                print("No Job Found with the provided Job Id")
                return "No Job Found"
        elif jobType == constants.EXECUTED:
            for job in self.jobsList.executedJobs:
                print(job, job.executionId, type(job.executionId))
                if job.executionId == jobId:
                    print(job.__dict__)
                    return job.__dict__
            else:
                print("No Job Found with the provided Job Id")
                return "No Job Found"
        elif jobType == constants.COMPLETED:
            for job in self.jobsList.completedJobs:
                print(job, job.jobId, type(job.jobId))
                if job.jobId == jobId:
                    print(job.__dict__)
                    return job.__dict__
            else:
                print("No Job Found with the provided Job Id")
                return "No Job Found"
        else:
            print("No Job Found with the provided Job Id")
            return "No Job Found"

    def execute_Jobs(self, markComplete=False):
        print("EXECUTING THE JOBS")
        curTime = datetime.now().__format__(constants.DATE_FORMAT)
        print(curTime)
        tempQueue = self.jobsList.jobsQueue
        _add_jobs = []
        while tempQueue and tempQueue[0].scheduledTime <= curTime:
            job = heapq.heappop(tempQueue)
            job.lastRun = curTime
            self._add_job_in_executed_list(job=job, curTime=curTime)
            if job.repeat and not markComplete:
                string_scheduledTime = datetime.strptime(job.scheduledTime, constants.DATE_FORMAT)
                next_schedule_date = string_scheduledTime + timedelta(days=job.repeatAfter)
                next_schedule_date = next_schedule_date.strftime(constants.DATE_FORMAT)
                job.scheduledTime = next_schedule_date
                job.runTime += 1
                _add_jobs.append(job)
            else:
                job.runTime += 1
                job.isCompleted = True
                job.repeat = False
                self._add_job_in_completed_list(job=job, curTime=curTime)
            
        while _add_jobs:
            job = _add_jobs.pop(0)
            heapq.heappush(tempQueue, job)
        

    def _add_job_in_completed_list(self, job, curTime):
        # Add Entry to the completed Jobs Section
        completed_obj = CompletedJob(
            jobId = job.jobId,
            jobName = job.jobName,
            jobDescription = job.jobDescription,
            repeat = job.repeat,
            scheduledTime = job.scheduledTime,
            lastRun = job.lastRun,
            repeatAfter = job.repeatAfter,
            runTime = job.runTime,
            isCompleted = job.isCompleted,
            jobCompletedTime = curTime
        )
        
        self.jobsList.completedJobs.append(completed_obj)

    def _add_job_in_executed_list(self, job, curTime):
        # Add Entry to the completed Jobs Section
        executedJob = ExecutedJob(
            jobId = job.jobId,
            jobName = job.jobName,
            jobDescription = job.jobDescription,
            scheduledTime = job.scheduledTime,
            executedTime = curTime
        )
        self.jobsList.executedJobs.append(executedJob)

    def show_all_data(self):
        current_jobs = []
        print("Current Jobs ->")
        for data in self.jobsList.jobsQueue:
            print(data)
            current_jobs.append(data.__dict__)

        executed_jobs = []
        print("Executed Jobs ->")
        for data in self.jobsList.executedJobs:
            print(data)
            executed_jobs.append(data.__dict__)
        
        completed_jobs = []
        print("Completed Jobs ->")
        for data in self.jobsList.completedJobs:
            print(data)
            completed_jobs.append(data.__dict__)

        return [current_jobs, executed_jobs, completed_jobs]
            
