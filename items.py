pkg_dnf = {
    'grafana': {
        'needs': ['action:dnf_makecache'],
    },
}

svc_systemd = {
    'grafana-server': {
        'needs': ['pkg_dnf:grafana'],
    },
}

files = {
    '/etc/grafana/grafana.ini': {
        'owner': 'grafana',
        'content_type': 'mako',
        'mode': '0444',
        'triggers': ['svc_systemd:grafana-server:restart'],
    },
}
