# from django.dispatch import receiver
# from django.contrib.auth.signals import user_logged_in, user_login_failed
# from users.models import UserLoginActivity
#
#
# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip
#
#
# @receiver(user_logged_in)
# def log_user_logged_in_success(sender, user, request, **kwargs):
#     try:
#         user_agent_info = request.META.get('HTTP_USER_AGENT', '<unknown>')[:255],
#         user_login_activity_log = UserLoginActivity(login_IP=get_client_ip(request),
#                                                     login_username=user.username,
#                                                     user_agent_info=user_agent_info,
#                                                     status=UserLoginActivity.SUCCESS)
#         user_login_activity_log.save()
#     except Exception as e:
#         # log the error
#         print("log_user_logged_in request: %s, error: %s" % (request, e))
#
#
# @receiver(user_login_failed)
# def log_user_logged_in_failed(sender, credentials, request, **kwargs):
#     try:
#         user_agent_info = request.META.get('HTTP_USER_AGENT', '<unknown>')[:255],
#         user_login_activity_log = UserLoginActivity(login_IP=get_client_ip(request),
#                                                     login_username=credentials['username'],
#                                                     user_agent_info=user_agent_info,
#                                                     status=UserLoginActivity.FAILED)
#         user_login_activity_log.save()
#     except Exception as e:
#         # log the error
#         print("log_user_logged_in request: %s, error: %s" % (request, e))
