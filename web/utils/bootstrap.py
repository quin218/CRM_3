from django import forms


class BootStrap:
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)  # 初始化父类方法
    #     for field in self.fields.values():
    #         field.widget.attrs = {'class': 'form-control'}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环ModelForm中的所有字段，给每个字段的插件设置
        for field in self.fields.values():
            # 字段中有属性，保留原来的属性，没有属性，才增加。
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label
                }


class BootStrapModelForm(BootStrap, forms.ModelForm):
    pass


class BootStrapForm(BootStrap, forms.Form):
    pass
