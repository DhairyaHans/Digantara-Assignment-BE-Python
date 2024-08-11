import uuid

class CompletedJob:
    def __init__(self, 
                 jobId: str,
                 jobName: str, 
                 jobDescription: str,
                 repeat: bool,
                 scheduledTime: str,
                 lastRun: str,  
                 repeatAfter: int,
                 runTime: int,
                 isCompleted: bool,
                 jobCompletedTime: str):
        
        self.jobId = jobId
        self.jobName = jobName 
        self.jobDescription = jobDescription
        self.repeat = repeat
        self.scheduledTime = scheduledTime
        self.lastRun = lastRun 
        self.repeatAfter = repeatAfter 
        self.runTime = runTime
        self.isCompleted = isCompleted
        self.JobCompletedTime = jobCompletedTime

    def __repr__(self) -> str:
        return f"Job {self.jobName} ({self.jobId}) is scheduled for {self.scheduledTime} is completed on {self.JobCompletedTime}" 

    def __str__(self) -> str:
        return f"Job {self.jobName} is scheduled for {self.scheduledTime} is completed on {self.JobCompletedTime}, which repeated after every {self.repeatAfter} days"
    