from django.conf import settings
from django.utils.module_loading import import_string
from django.urls.resolvers import URLResolver, URLPattern
from collections import OrderedDict
from django.shortcuts import HttpResponse
import re


def check_url_exclude(url):
    """
    排除一些特定的URL

      :param url: 待检验的URL

      :return:
    """

    exclude_url = settings.PERMISSION_VALID_URL

    for regex in exclude_url:
        if re.match(regex, url):
            return True


# def recursion_urls(pre_namespace, pre_url, urlpatterns, url_ordered_dict):
#     for item in urlpatterns:
#         if isinstance(item, URLResolver):
#             if pre_namespace:
#                 if item.namespace:
#                     namespace = "%s:%s" % (pre_namespace, item.namespace,)
#                 else:
#                     namespace = pre_namespace
#             else:
#                 if item.namespace:
#                     namespace = item.namespace
#                 else:
#                     namespace = None
#             recursion_urls(namespace, pre_url + item.pattern.regex.pattern, item.url_patterns, url_ordered_dict)
#         else:
#
#             if pre_namespace:
#                 name = "%s:%s" % (pre_namespace, item.name,)
#             else:
#                 name = item.name
#             if not item.name:
#                 # raise Exception('URL路由中必须设置name属性')
#                 continue
#
#             url = pre_url + item.pattern.regex.pattern
#             url_ordered_dict[name] = {'name': name, 'url': url.replace('^', '').replace('$', '')}
def recursion_urls(pre_namespace, pre_url, urlpatterns, url_ordered_dict):
    for item in urlpatterns:
        if isinstance(item, URLPattern):
            if not item.name:
                continue
            if pre_namespace:
                name = "%s:%s" % (pre_namespace, item.name,)
            else:
                name = item.name
            url = pre_url + item.pattern.regex.pattern
            url = url.replace("^", "").replace("$", "")
            if check_url_exclude(url):
                continue
            url_ordered_dict[name] = {"name": name, "url": url}
        elif isinstance(item, URLPattern):
            if pre_namespace:
                if item.namespace:
                    namespace = "%s:%s" % (pre_namespace, item.namespace)
                else:
                    namespace = pre_namespace
            else:
                if item.namespace:
                    namespace = item.namespace
                else:
                    namespace = None
            recursion_urls(namespace, pre_url + item.pattern.regex.pattern, item.url_patterns, url_ordered_dict)


def get_all_url_dict(ignore_namespace_list=None):
    """
    获取路由中
    :return:
    """
    ignore_list = ignore_namespace_list or []
    url_ordered_dict = OrderedDict()

    md = import_string(settings.ROOT_URLCONF)
    # urlpatterns = []
    # for item in md.urlpatterns:
    #     if item.namespace in ignore_list:
    #         continue
    #     urlpatterns.append(item)

    recursion_urls(None, "/", md.urlpatterns, url_ordered_dict)
    url_list = []
    for var in url_ordered_dict:
        url_list.append(var)
    # return url_list
    return url_ordered_dict
