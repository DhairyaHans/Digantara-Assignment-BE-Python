import uuid

class ExecutedJob:
    def __init__(self,
                 jobId: str,
                 jobName: str,
                 jobDescription: str,
                 scheduledTime: str,
                 executedTime: str):
        
        self.executionId = uuid.uuid4()
        self.jobId = jobId
        self.jobName = jobName
        self.jobDescription = jobDescription
        self.scheduledTime = scheduledTime
        self.executedTime = executedTime

    def __repr__(self) -> str:
        return f"Job {self.jobName} ({self.executionId}) is executed on {self.executedTime}" 

    def __str__(self) -> str:
        return f"Job {self.jobName} is executed on {self.executedTime} with execution Id -> {self.executionId}"
    
        