from django.shortcuts import render, redirect, HttpResponse
from io import BytesIO
from web import models
from web.utils.form import LoginForm
from web.utils.code import check_code
from rbac.service.init_permission import init_permission


def login(request):
    """ 登录 """
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('image_code', "")
        if code.upper() != user_input_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, 'login.html', {'form': form})

        user_object = models.UserInfo.objects.filter(**form.cleaned_data).first()
        if not user_object:
            form.add_error("password", "用户名或密码错误")
            form.add_error("username", "用户名或密码错误")
            return render(request, 'login.html', {'form': form})

        # 用户名和密码正确
        # 网站生成随机字符串; 写到用户浏览器的cookie中；在写入到session中；
        request.session["info"] = {'id': user_object.id, 'name': user_object.username}
        # session可以保存7天
        request.session.set_expiry(60 * 60 * 24 * 7)
        request.session['image_code'] = ''
        init_permission(user_object, request)
        return redirect("/stark/web/userinfo/list/")

    return render(request, 'login.html', {'form': form})

    # user = request.POST.get('user')
    # pwd = request.POST.get('pwd')
    # user_obj = models.UserInfo.objects.filter(username=user, password=pwd).first()
    # if not user_obj:
    #     return render(request, 'login.html', {'msg': '用户名或密码错误'})
    # # 用户名和密码正确
    # # 网站生成随机字符串; 写到用户浏览器的cookie中；在写入到session中；
    # request.session["info"] = {'id': user_obj.id, 'name': user_obj.username}
    # init_permission(user_obj, request)
    # # session可以保存7天
    # request.session.set_expiry(60 * 60 * 24 * 7)
    # request.session['image_code'] = ''
    # return redirect("/stark/web/userinfo/list")


def logout(request):
    request.session.clear()
    return redirect('/login/')


def image_code(request):
    # 调用pillow函数，生成图片
    img, code_string = check_code()
    request.session['image_code'] = code_string
    request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())
