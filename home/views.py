from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.core.urlresolvers import reverse
from .models import LostItems, FoundItems


class Login:
    def __init__(self, username):
        username = username

    def display(self, text):
        print('text %s' % text)
        return HttpResponse('Display from new class')


a = Login('temp_user')


# Create your views here.
def index(request):
    latest_lost_items = LostItems.objects.order_by('-date')[:5]
    latest_found_items = FoundItems.objects.order_by('-date')[:5]
    # output = ', '.join([i.item_name for i in latest_lost_items])
    # return HttpResponse(output)
    template = loader.get_template('home/index.html')
    context = {
        'latest_lost_items': latest_lost_items,
        'latest_found_items': latest_found_items,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'home/index.html', context)

# If your file isn't a django template but a plain html file, this is the easiest way:
# from django.shortcuts import render_to_response
#
# def index (request):
#     return render_to_response('app/index.html')


def login(request):

    # return HttpResponse("Login to the website!")
    return render_to_response('home/login.html')

# def login_user(request):
#     # return HttpResponseRedirect(reverse('home:inbox'))
#     return HttpResponse("login posted!")

def register(request):
    return HttpResponse('Register user functionality should be added here!')


def about(request):
    return render_to_response('home/about.html')


def contact(request):
    return render_to_response('home/contact.html')
    # try:
    #         item = LostItems.objects.get(pk=user_id)
    #     except LostItems.DoesNotExist:
    #         raise Http404('Item does not exist')
    #
    #     return render(request, 'home/detail.html', {'item': item})
    #


def detail(request, user_id):
    lost_item = get_object_or_404(LostItems, pk=user_id)
    return render(request, 'home/detail.html', {'item': lost_item})


def add_lost_item(request):
    """
    Add an item to the Lost items category
    :param request:
    :return:
    """
    return HttpResponse('Add an item to Lost category')


def add_found_item(request):
    return HttpResponse('Add an item to FOUND category')
