
для запуска БД:
```
mongod --dbpath /полный/путь/к/вашему/каталогу/backend/admin/data/db
```


для запуска админкм из директории /admin:
```
uvicorn app_admin.main:app
```
