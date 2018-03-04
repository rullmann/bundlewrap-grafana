# grafana

This bundle will install [Grafana](https://grafana.com/) as part of a monitoring stack.

It's recommended to setup some kind of datasource and monitoring first. E.g. telegraf and influxdb.

## Requirements

* Bundles:
  * [dnf](https://github.com/rullmann/bundlewrap-dnf)
  * [postgresql](https://github.com/rullmann/bundlewrap-postgresql)

## Setup notes

By default Grafana will store all data inside an sqlite3 database. As this may be sufficient for testing it's recommended to setup a postgresql database.

## Integrations

* Bundles:
  * [influxdb](https://github.com/rullmann/bundlewrap-influxdb)

## Metadata

    'metadata': {
        'grafana': {
            'instance_name': node.name, # optional, defaults to node.name
            'http_port': '3000', # optional
            'domain': node.name, # optional, defaults to node.name'
            'router_logging': 'false', # optional
            'database_type': 'sqlite3' # optional

        },
    }

### PostgreSQL

When using PostgreSQL metadata can be set like this:

    'metadata': {
        'grafana': {
            'database_type': 'postgres',
            'database_password': 'somesecretpassword',
        },
    }
