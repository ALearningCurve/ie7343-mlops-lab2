# ie7343-mlops-lab2

This adapation is an extension of the starter logging code. 

Rather than log to a file (as done in the lab), we integrate Graphana
to have more advanced insignts into the logs and createa a dashboard
reporting app status! This setup is also compelling since the log data is stored in s3 analogue using minio, which is more robust than filesystem storage if swapped out for a s3 bucket.

This is a big change from the lab code which just used basic python logging!

The screenshots of the dashboard are shown below:

## Low Error Count
![Low error count dashboard](assets/low_error_count.png)

## High Error Count
![High error count dashboard](assets/high_error_count.png)

# Project Structure

```
.
├── alloy-local-config.yaml          # Alloy config (log collector and forwarder)
├── docker-compose.yaml              # Docker Compose (Python demo app, Loki, Grafana, Minio, Alloy)
├── Dockerfile                       # Docker image for the Python application
├── loki-config.yaml                 # Configuration for Loki (log service)
├── main.py                          # Python app which randomly generates fake logs
├── README.md                         
├── assets/                          # Directory containing dashboard screenshots for readme
│   ├── low_error_count.png
│   └── high_error_count.png
└── graphana_dashboards/             # Grafana dashboard as code
    ├── dashboards/
    │   └── python-app-metrics.json  # Logging dashboard as code
    └── provisioning/
        └── provider.yaml            # Provider for dashboard code to be loaded
```

# Steps to run yourself

1. clone this repo into a folder called `lab2`
  - `git clone git@github.com:ALearningCurve/ie7343-mlops-lab2.git lab2`
2. change directory into the repo `cd lab2`
3. start all services with `docker compose up --build` (make sure all containers start)
4. (optional) you can check that the ingress pipeline is working as follows
  - Loki handles log interactions, expect to see "ready" when visiting the status url for [ingres](http://localhost:3102/ready) and [query](http://localhost:3101/ready)
  - Alloy handles streaming logs from python app to loki, expect to see HEALTHY statuses when visiting [alloy](http://localhost:12345)
5. visit the [local graphana instance](http://localhost:3000)
6. click "Dashboards" button on the sidebar and then when the page redirects click "Services" and then "Logging Dashboard". You should now see the same view as where the screenshots were taken.

# References

- https://grafana.com/docs/loki/latest/get-started/quick-start/quick-start/
  - The docker-compose and system layout is largely sourced from this post

- https://stackoverflow.com/questions/63518460/grafana-import-dashboard-as-part-of-docker-compose
  - For defining the dashboard as code