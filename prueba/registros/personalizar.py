class personalizarmiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        url = request.META.get('PATH_INFO')
        if url == '/admin/login/':
         if 'anonymoususer' in str(request.user).lower():
            print("hola")
        else:
            print(request.user)


