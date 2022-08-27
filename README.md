# bindicator
A visual alerting system to show which bin to collect, when.

## Bin Collection API
### GET /api/current_bin
Returns current bin colour in JSON
```
[
    {
        "bin_colour": "brown",
        "collection_date": "27-08-2022",
        "entry_id": 7
    }
]
```

### POST /api/add_collection_date
Allows a new bin collection date and colour to be added in the below JSON format.
```
{
    "bin_colour": "brown",
    "collection_date": "27-08-2022"
}
```

Returns upon successful request
```
{
    "status": "Collection date added successfully"
}
```

### DELETE api/delete_collection_date/<27-08-2022>
Delete any collections on a specific date passed in the URI in format dd-mm-yyyy

Returns upon successful delete
```
{
    "status": "Collection date deleted successfully"
}
```

## 
