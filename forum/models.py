from django.db import models

class Week(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Thread(models.Model):
    title = models.CharField(max_length=500, default="")
    week = models.ForeignKey(Week, related_name="threads", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    @property
    def week_name(self):
        return self.week.name

class DiscussionGuide(models.Model):
    deadline = models.DateTimeField()
    description = models.TextField()
    mechanism_expectation = models.TextField()
    thread = models.OneToOneField(Thread, on_delete=models.CASCADE, related_name="discussion_guide")

    class InquiryState(models.TextChoices):
        PHASE1 = 1
        PHASE2 = 2
        PHASE3 = 3
        PHASE4 = 4
        PHASE5 = 5

    state = models.CharField(
        max_length=255,
        choices=InquiryState.choices,
        default=InquiryState.PHASE1
    )

    @property
    def week_name(self):
        return self.thread.week.name
    
    @property
    def thread_title(self):
        return self.thread.title

class Summary(models.Model):
    content = models.TextField()
    thread = models.OneToOneField(Thread, on_delete=models.CASCADE, related_name="summary")

class ReferenceFile(models.Model):
    title = models.CharField(max_length=100)
    url = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="reference_file")
