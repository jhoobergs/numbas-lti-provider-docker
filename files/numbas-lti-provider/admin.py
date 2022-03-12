from django.contrib import admin

from .models import Resource, Exam, LTIConsumer, ConsumerTimePeriod, LTIContext, ReportProcess, AccessToken, AccessChange, UsernameAccessChange, EmailAccessChange, LTIUserData, LTILaunch, Attempt, AttemptLaunch, AttemptQuestionScore, RemarkPart, DiscountPart, ScormElement, RemarkedScormElement, ScormElementDiff, EditorLink, EditorLinkProject, StressTest, StressTestNote, FileReport
# Register your models here.

admin.site.register(Resource)
admin.site.register(Exam)
admin.site.register(LTIConsumer)

admin.site.register(ConsumerTimePeriod)
admin.site.register(LTIContext)
admin.site.register(ReportProcess)
admin.site.register(AccessToken)
admin.site.register(AccessChange)
admin.site.register(UsernameAccessChange)
admin.site.register(EmailAccessChange)
admin.site.register(LTIUserData)
admin.site.register(LTILaunch)
admin.site.register(Attempt)
admin.site.register(AttemptLaunch)
admin.site.register(AttemptQuestionScore)
admin.site.register(RemarkPart)
admin.site.register(DiscountPart)
admin.site.register(ScormElement)
admin.site.register(RemarkedScormElement)
admin.site.register(ScormElementDiff)
admin.site.register(EditorLink)
admin.site.register(EditorLinkProject)
admin.site.register(StressTest)
admin.site.register(StressTestNote)
admin.site.register(FileReport)
