# bindicator
A visual alerting system to show which bin to collect, when.

## Bin Collection API
The bin collection API is a Python Flask app backed by a local SQLite database, it is designed to allow for collection
dates and bin colours to be mapped into an API that can be called the bindicator device itself if your local council
doesn't have an API for calling this information already.

There as a Dockerfile to package the app into an alpine OS image.



### GET /api/current_bin
Returns current bin colour in JSON
```
[
    {
        "bin_colour": "brown",
        "collection_date": "27-08-2022"
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
