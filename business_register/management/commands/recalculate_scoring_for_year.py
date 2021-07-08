from django.core.management.base import BaseCommand
from business_register.models.declaration_models import Declaration


class Command(BaseCommand):
    help = '---'

    def add_arguments(self, parser):
        parser.add_argument('year', type=int, nargs=1)

    def handle(self, *args, **options):
        year = options['year'][0]
        qs = Declaration.objects.filter(year=year)
        count = qs.count()
        i = 0
        for declaration in qs:
            i += 1
            self.stdout.write(f'\r Process {i} of {count}', ending='')
            declaration.recalculate_scoring()

        self.stdout.write()
        self.stdout.write('>>> Done!')