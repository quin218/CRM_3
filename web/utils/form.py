from django import forms
from web import models
from web.utils.bootstrap import BootStrapModelForm, BootStrapForm
from django.core.exceptions import ValidationError
from web.utils.encrypt import md5


class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(render_value=True),
        required=True
    )
    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput,
        required=True
    )

    # def clean_password(self):
    #     pwd = self.cleaned_data.get("password")
    #     return md5(pwd)


# class UploadModelForm(BootStrapModelForm):
#     class Meta:
#         model = models.Task
#         fields = ["Tid", "title", "collage", "owner", "img", "excel", "word"]
