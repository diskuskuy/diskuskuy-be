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

class DiscussionGuide(models.Model):
    deadline = models.DateTimeField()
    description = models.CharField(max_length=500)
    mecanism_expectation = models.CharField(max_length=500)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

class Summary(models.Model):
    content = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

class ReferenceFile(models.Model):
    title = models.CharField(max_length=100)
    url = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE,)

class InquiryPhase(models.Model):

    class InquiryState(models.TextChoices):
        PHASE1 = 1
        PHASE2 = 2
        PHASE3 = 3
        PHASE4 = 4

    discussion_guide = models.ForeignKey(DiscussionGuide, on_delete=models.CASCADE)
    state = models.CharField(
        max_length=255,
        choices=InquiryState.choices,
        default=InquiryState.PHASE1
    )