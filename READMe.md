# Thinkland Backend Task

## Documentation

## API Reference

#### Get books list (only have image) with pagination 12 items per page

```http
  GET /api/books/
```

``` json
{
    "success": true,
    "error": null,
    "message": null,
    "count": 1,
    "current": 1,
    "total_pages": 1,
    "per_page": 12,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Kecha va kunduz",
            "slug": "kecha-va-kunduz",
            "authors": [
                {
                    "id": 1,
                    "name": "Rustamov Javohir",
                    "created_at": "2024-04-30T20:47:16.917409+05:00",
                    "updated_at": "2024-04-30T20:47:16.918930+05:00",
                    "is_active": true
                }
            ],
            "images": [
                {
                    "id": 1,
                    "image": "http://127.0.0.1:8000/media/books/kecha_va_kunduz1.jpg",
                    "alt": "Image1",
                    "title": "Image1",
                    "created_at": "2024-04-30T20:48:51+05:00",
                    "updated_at": "2024-04-30T20:52:30.617100+05:00",
                    "is_active": true
                },
                {
                    "id": 2,
                    "image": "http://127.0.0.1:8000/media/books/kecha_va_kunduz2.jpg",
                    "alt": "image2",
                    "title": "image2",
                    "created_at": "2024-04-30T20:51:21+05:00",
                    "updated_at": "2024-04-30T20:51:39.957184+05:00",
                    "is_active": true
                }
            ],
            "published": "2024-05-01",
            "description": "",
            "created_at": "2024-04-30T20:52:38+05:00",
            "updated_at": "2024-04-30T20:54:49.134872+05:00",
            "is_active": true
        }
    ]
}
```

#### Get book detail

```http
  GET /api/books/{slug}/
```

``` json
{
    "success": true,
    "error": null,
    "message": null,
    "result": {
        "id": 1,
        "name": "Kecha va kunduz",
        "slug": "kecha-va-kunduz",
        "authors": [
            {
                "id": 1,
                "name": "Rustamov Javohir",
                "created_at": "2024-04-30T20:47:16.917409+05:00",
                "updated_at": "2024-04-30T20:47:16.918930+05:00",
                "is_active": true
            }
        ],
        "images": [
            {
                "id": 1,
                "image": "http://127.0.0.1:8000/media/books/kecha_va_kunduz1.jpg",
                "alt": "Image1",
                "title": "Image1",
                "created_at": "2024-04-30T20:48:51+05:00",
                "updated_at": "2024-04-30T20:52:30.617100+05:00",
                "is_active": true
            },
            {
                "id": 2,
                "image": "http://127.0.0.1:8000/media/books/kecha_va_kunduz2.jpg",
                "alt": "image2",
                "title": "image2",
                "created_at": "2024-04-30T20:51:21+05:00",
                "updated_at": "2024-04-30T20:51:39.957184+05:00",
                "is_active": true
            }
        ],
        "published": "2024-05-01",
        "description": "",
        "created_at": "2024-04-30T20:52:38+05:00",
        "updated_at": "2024-04-30T20:54:49.134872+05:00",
        "is_active": true
    }
}
```



