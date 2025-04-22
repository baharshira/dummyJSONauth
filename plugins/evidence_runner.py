from evidences.user_evidence import UserEvidence
from evidences.post_evidence import PostEvidence


EVIDENCE_PLUGINS = [UserEvidence(), PostEvidence()]

def collect_all(token):
    results = {}
    for plugin in EVIDENCE_PLUGINS:
        key = plugin.__class__.__name__
        results[key] = plugin.collect(token)
    return results