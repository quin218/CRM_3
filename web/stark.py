from web import models
from stark.service.stark import site
from web.config import collageinfo, taskinfo, userinfo

site.register(models.CollageInfo, collageinfo.CollageConfig)
site.register(models.UserInfo, userinfo.TeacherInfoConfig)
site.register(models.Task, taskinfo.TaskInfoConfig)
# site.register(models.TaskRecord, task_record.TaskRecordConfig)
