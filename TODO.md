# TODO List for Implementing GET /api/job-alerts/{alert_id}/matches/

- [x] Update settings.py to use JWT authentication instead of TokenAuthentication
- [x] Add Job model to models.py with fields: title, company, location, salary, job_type
- [x] Add JobSerializer to serializers.py
- [x] Add custom 'matches' action to JobAlertViewSet in views.py to return matching jobs
- [x] Run makemigrations and migrate for the new Job model
- [x] Test the endpoint (run server and verify)
- [x] Update JobAlert model with frequency and last_sent fields
