from django.shortcuts import render

from thread_app.models import ThreadModel


# Create your views here.


def home_page(request):

	# order by published ex: posts = Post.objects.order_by('-published')

	all_threads = ThreadModel.objects.order_by('-updated_at').all()
	context = {'all_threads': all_threads}

	return render(request, 'home_page_template/home_page.html', context)

