# API examples

## Save a new order

```
curl --request POST \
  --url http://127.0.0.1:8000/order/save/ \
  --header 'Content-Type: application/json' \
  --data '{
	"client": "0cbc35ea-f702-4753-8ef7-7f8a8bc7e536",
	"items": [
			{
				"product": "6f7015a2-fe1a-427d-95ad-2b1a76a56fe7",
				"quantity": 1
			},
			{
				"product": "bdaeaaa1-c8fc-4407-bc39-450eb4afdc88",
				"quantity": 2
			}
	]
}'
```

## Get an order

```
curl --request GET \
  --url http://127.0.0.1:8000/order/detail/<uuid>
```
