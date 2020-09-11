

# Миграции
## При запущенных контейнерах:
```
docker-compose exec web python manage.py flush --no-input
docker-compose exec web python manage.py migrate
```

# Запуск проекта
```
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```
