# ✨BestHack-IIoT-2024✨ 
## [*пока без-названия] Team  


<h1>Проблематика:</h1>

<h2>Постановка задачи:</h2>
<b>Создание максимального no-code упрощения настройки системы видеоаналитики под камеру на базе нескольких кадров с неё.
Ожидаемый функционал:
  
⭐️  Начальная настройка логики работы детекторов и их параметров

⭐️  Донастройка в случае изменения ракурса камеры или других внешних условий при повторном открытии интерфейса 

⭐️  Интуитивный интерфейс настройки

⭐️  Подсказки настроек на основе текущих кадров</b>

<h1>MVP решение кейса:</h1>

На данный момент было реализовано распознавание образов с помозщью открытых моделей. На вход подаётся изображение (в случае кейса - кадр с подключенной камеры).

```python
# Set custom configuration parameters for hat_model
base_model.overrides['classes'] = [0] # Only detect class 0 (hard hat)
base_model.overrides['conf'] = 0.25 # NMS confidence threshold
base_model.overrides['iou'] = 0.45 # NMS IoU threshold
```

<h1>Что дальше?</h1>

Дальше - больше! Больше интерактивности, больше функционала, больше бессонных ночей в работе над проектом.

<h2>Какие планы ?</h2>

- [ ] Реализация графического интерфейса (GUI) для упрощения работы пользователя

- [ ] Создание системы рекомендаций, 

- [ ] Тестирование работы системы с другими датчиками
