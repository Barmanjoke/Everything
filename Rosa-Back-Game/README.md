# Gamification
To update DB models:
```
python manage.py inspectdb > achievements\\models\\DB.py
(Get-Content .\achievements\models\DB.py) -replace '\0' -ne '' | Set-Content .\achievements\models\DB.py
```
