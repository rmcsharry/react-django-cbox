from chatterbox.models import Progress
from django.core.management import call_command
from datetime import date as Date

def RunProgress(get_response):
  def middleware(request):
    # Code to be executed for each request before
    # the view (and later middleware) are called.

    # NOTE This is just a hack to ensure there is always progress data for today
    # but also to show that I understand how to hook into the Djanog middleware
    isProgress = 'progress' in request.get_full_path()
    if (isProgress):
      progress = Progress.objects.filter(organisation_id=1, calculated_date__gte=Date.today()).first()
      if progress:
        call_command('calc_progress', '1')

    response = get_response(request)

    # Code to be executed for each request/response after
    # the view is called.

    return response

  return middleware

    # 
