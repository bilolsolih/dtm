from apps.tests.models import Topic, Subject, TestCategory

test_categories = [
    TestCategory(title='Title 1', description='Description 1'),
    TestCategory(title='Title 2', description='Description 2'),
    TestCategory(title='Title 3', description='Description 3'),
]

subjects = [
    Subject(title='Title 1', is_active=True),
    Subject(title='Title 2', is_active=True),
    Subject(title='Title 3', is_active=False),
]

topics = [
    Topic(subject_id=1, title='Title 1'),
    Topic(subject_id=1, title='Title 2'),
    Topic(subject_id=2, title='Title 3'),
    Topic(subject_id=2, title='Title 4'),
    Topic(subject_id=3, title='Title 5'),
    Topic(subject_id=3, title='Title 6'),
]


def create_categories():
    TestCategory.objects.bulk_create(test_categories)
    Subject.objects.bulk_create(subjects)
    Topic.objects.bulk_create(topics)


__all__ = ['create_categories']
