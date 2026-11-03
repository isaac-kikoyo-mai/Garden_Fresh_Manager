from django.contrib.auth.decorators import user_passes_test


def manager_required(view_func):

    decorator = user_passes_test(

        lambda u:
        u.is_authenticated and
        u.groups.filter(
            name='Manager'
        ).exists()

    )

    return decorator(view_func)
