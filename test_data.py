import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobalerts.settings')
django.setup()

from django.contrib.auth.models import User
from job_alerts.models import JobAlert, Job

# Create a test user
user, created = User.objects.get_or_create(username='testuser', defaults={'email': 'test@example.com'})
if created:
    user.set_password('password123')
    user.save()

# Create a job alert
alert, created = JobAlert.objects.get_or_create(
    user=user,
    keyword='Python',
    location='New York',
    min_salary=50000,
    job_type='full_time',
    defaults={'is_active': True}
)

# Create some jobs
jobs_data = [
    {
        'title': 'Python Developer',
        'company': 'Tech Corp',
        'location': 'New York',
        'salary': 60000,
        'job_type': 'full_time',
        'description': 'Develop Python applications'
    },
    {
        'title': 'Senior Python Engineer',
        'company': 'Innovate Ltd',
        'location': 'New York',
        'salary': 80000,
        'job_type': 'full_time',
        'description': 'Lead Python development team'
    },
    {
        'title': 'Data Scientist',
        'company': 'Data Inc',
        'location': 'California',
        'salary': 70000,
        'job_type': 'full_time',
        'description': 'Analyze data with Python'
    }
]

for job_data in jobs_data:
    Job.objects.get_or_create(**job_data)

print("Test data created successfully")
print(f"User: {user.username}")
print(f"Alert ID: {alert.id}")
print(f"Jobs created: {len(jobs_data)}")
