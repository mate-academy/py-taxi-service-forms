import init_django_orm  # noqa: F401

from db.models import User


def main():
    User.objects.create(name='Dan')
    User.objects.create(name='Robert')

    return User.objects.all()


if __name__ == '__main__':
    print(main())
