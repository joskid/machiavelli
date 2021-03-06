from django.conf import settings

def banners(request):
	context = {}
	try:
		conf = settings.BANNERS
	except AttributeError:
		return context
	else:
		for k, v in conf.items():
			if not v['banner'] is None and v['banner'] != "":
				context.update({'%s_banner' % k: v['banner']})
			if not v['url'] is None:
				context.update({'%s_url' % k: v['url']})
	return context
			
