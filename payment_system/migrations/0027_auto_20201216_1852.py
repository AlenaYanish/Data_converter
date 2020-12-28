# Generated by Django 3.0.7 on 2020-12-16 18:52
from django.conf import settings
from django.db import migrations
from django.utils import timezone

from data_ocean.utils import generate_key


def default_projects(apps, schema):
    User = apps.get_model('users', 'DataOceanUser')
    Project = apps.get_model('payment_system', 'Project')
    # UserProject = apps.get_model('payment_system', 'UserProject')
    ProjectSubscription = apps.get_model('payment_system', 'ProjectSubscription')
    Subscription = apps.get_model('payment_system', 'Subscription')

    for user in User.objects.all():
        default_u2p = user.user_projects.filter(role='owner', is_default=True).first()

        if not default_u2p:
            new_project = Project.objects.create(
                name=settings.DEFAULT_PROJECT_NAME,
                description=settings.DEFAULT_PROJECT_DESCRIPTION,
                owner=user,
                token=generate_key(),
            )
            new_project.user_projects.create(
                user=user,
                role='owner',
                status='active',
                is_default=True,
            )

            default_subscription, created = Subscription.objects.get_or_create(
                is_default=True,
                defaults={
                    'requests_limit': 1000,
                    'name': settings.DEFAULT_SUBSCRIPTION_NAME,
                    'grace_period': 30,
                },
            )
            date_now = timezone.localdate()
            ProjectSubscription.objects.create(
                project=new_project,
                subscription=default_subscription,
                status='active',
                start_date=date_now,
                requests_left=default_subscription.requests_limit,
                duration=default_subscription.duration,
                grace_period=default_subscription.grace_period,
                expiring_date=date_now + timezone.timedelta(days=default_subscription.duration),
            )


class Migration(migrations.Migration):

    dependencies = [
        ('payment_system', '0026_auto_20201211_1951'),
    ]

    operations = [
        migrations.RunPython(
            code=default_projects,
            reverse_code=migrations.RunPython.noop,
        )
    ]
