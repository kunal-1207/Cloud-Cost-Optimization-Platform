import random

def generate_recommendations(resources):
    recommendations = []
    for r in resources:
        if r['type'] == 'EC2':
            recommendations.append({'id': r['id'], 'action': 'shutdown'})
    return recommendations
