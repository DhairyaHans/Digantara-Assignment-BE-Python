import uuid

class Job:
    def __init__(self, 
                 jobName: str, 
                 jobDescription: str,
                 repeat: bool,
                 scheduledTime: str,
                 lastRun: str=None,  
                 repeatAfter: int=0,
                 runTime: int=0,
                 isCompleted: bool=False):
        
        self.jobId = str(uuid.uuid4())
        self.jobName = jobName 
        self.jobDescription = jobDescription
        self.repeat = repeat
        self.scheduledTime = scheduledTime
        self.lastRun = lastRun 
        self.repeatAfter = repeatAfter 
        self.runTime = runTime
        self.isCompleted = isCompleted

    def __repr__(self) -> str:
        return f"Job {self.jobName} ({self.jobId}) is Next scheduled for {self.scheduledTime}" 

    def __str__(self) -> str:
        return f"Job {self.jobName} ({self.jobId}) is Next scheduled for {self.scheduledTime}, repeated after every {self.repeatAfter} days"
    
    def __lt__(self, other):
        return self.scheduledTime < other.scheduledTime