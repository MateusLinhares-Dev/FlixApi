from django.core.management.base import BaseCommand
import subprocess
import sys

class Command(BaseCommand):
    help = 'Instala as dependências listadas no arquivo requirements.txt'

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo com as dependências',
        )

    def handle(self, *args, **options):
        file_name = options['file_name']

        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', file_name])
        #print do django command que foi heradado do BaseCommand
        self.stdout.write(self.style.SUCCESS(f'Sucesso ao instalar as dependências do {file_name}'))


