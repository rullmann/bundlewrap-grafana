@metadata_processor
def dnf(metadata):
    if node.has_bundle('dnf'):
        metadata.setdefault('dnf', {})
        metadata['dnf'].setdefault('repositories', {})
        metadata['dnf']['repositories'].setdefault('grafana', {})
        metadata['dnf']['repositories']['grafana'].setdefault(
            'name',
            'Grafana Repository',
        )
        metadata['dnf']['repositories']['grafana'].setdefault(
            'baseurl',
            'https://packagecloud.io/grafana/stable/el/7/$basearch',
        )
        metadata['dnf']['repositories']['grafana'].setdefault(
            'gpgkey',
            'https://packagecloud.io/gpg.key https://grafanarel.s3.amazonaws.com/RPM-GPG-KEY-grafana',
        )
    return metadata, DONE
