from stark.service.stark import StarkConfig, Option, get_choice_text


class TeacherInfoConfig(StarkConfig):
    list_display = ['userid', 'username', 'collage']

    search_list = ['username', 'collage', 'userid']

    order_by = ['-id']
