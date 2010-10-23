def authentication_context(request):
	from django.conf import settings
	return {'authenticated': request.user.is_authenticated()}
