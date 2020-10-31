from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="preetham",email="varanasipreetham999@gmail.com",
                          is_staff=True,is_superuser=True,phone='9441355920',
                          gender='Male')
        user.set_password("Preetham@123")
        user.save()

    dependencies = [

        ]
    operations = [
            migrations.RunPython(seed_data),
        ]