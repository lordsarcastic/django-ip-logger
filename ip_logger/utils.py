def get_ip_address(request):
    presumed_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    return \
        presumed_ip.split(',')[0] \
            if presumed_ip is not None \
                else \
                    request.META.get('REMOTE_ADDR')

