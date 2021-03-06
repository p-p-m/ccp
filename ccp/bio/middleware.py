from models import Request


class StoreRequest(object):
    '''
    Saves every request to db
    '''

    def process_request(self, request):
        stored_request = Request()
        for f in ('META', 'path'):
            setattr(stored_request, f.lower(), str(getattr(request, f)))
        stored_request.path = str(request.path)
        stored_request.save()
