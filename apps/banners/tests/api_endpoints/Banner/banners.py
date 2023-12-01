from apps.banners.models import Banner

banners = [
    Banner(title='Title 1', subtitle='Subtitle 1', picture='test_data/edu.jpg', is_active=True),
    Banner(title='Title 2', subtitle='Subtitle 2', picture='test_data/edu.jpg', is_active=True),
    Banner(title='Title 3', subtitle='Subtitle 3', picture='test_data/edu.jpg', is_active=True),
    Banner(title='Title 4', subtitle='Subtitle 4', picture='test_data/edu.jpg', is_active=True),
    Banner(title='Title 5', subtitle='Subtitle 5', picture='test_data/edu.jpg', is_active=True),
    Banner(title='Title 6', subtitle='Subtitle 6', picture='test_data/edu.jpg', is_active=False),
]


def create_banners():
    Banner.objects.bulk_create(banners)


__all__ = ['create_banners']
