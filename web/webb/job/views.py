from django.shortcuts import render
from datetime import datetime
import requests


def vacancies(request):
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": "Android-разработчик",
        "period": 1,
        "per_page": 10,
        "order_by": "publication_time"
    }
    response = requests.get(url, params=params).json()
    vacancies = response.get('items', [])

    # Преобразование даты публикации
    for vacancy in vacancies:
        published_at = vacancy.get('published_at')  # Получение строки даты
        if published_at:
            # Преобразование строки в объект datetime
            vacancy['published_at'] = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%S%z")

    return render(request, 'job/job_op.html', {'vacancies': vacancies})