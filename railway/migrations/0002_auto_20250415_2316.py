from django.db import migrations

def update_route(apps, schema_editor):
    AddRoute = apps.get_model('railway', 'Add_route')
    AddRoute.objects.filter(route__isnull=True).update(route='Unknown Route')

class Migration(migrations.Migration):

    dependencies = [
        ('railway', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(update_route),
    ]