from stark.service.stark import StarkConfig
from django.urls import reverse
from django.utils.safestring import mark_safe


class TaskInfoConfig(StarkConfig):

    # def display_follow(self, row=None, header=False):
    #     if header:
    #         return '项目进度'
    #
    #     # url = reverse("stark:crm_consultrecord_pri_changelist")
    #     return mark_safe("<a href='%s?cid=%s'>跟进记录</a>")

    list_display = [
        'Tid',
        'title',
        'collage',
        'owner',
        'file',
        # display_follow
    ]
