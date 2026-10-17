"""Maintenance scenario arithmetic. Author: Feras Elghandour."""
from decimal import Decimal

def annual_net_benefit(incidents, incident_cost, avoided_fraction,
                       interventions, intervention_cost, annual_platform_cost):
    values=[Decimal(str(v)) for v in [incidents,incident_cost,avoided_fraction,
                                     interventions,intervention_cost,annual_platform_cost]]
    if any(not v.is_finite() or v < 0 for v in values) or values[2] > 1:
        raise ValueError('Use finite nonnegative assumptions and fraction <= 1')
    count, loss, share, actions, service, platform = values
    avoided_loss = count * loss * share
    return {'avoided_loss': avoided_loss, 'intervention_cost': actions * service,
            'net_benefit': avoided_loss - actions * service - platform}

def break_even_avoided_fraction(incidents, incident_cost, interventions,
                               intervention_cost, annual_platform_cost):
    result = annual_net_benefit(incidents, incident_cost, 0, interventions,
                                intervention_cost, annual_platform_cost)
    loss = Decimal(str(incidents)) * Decimal(str(incident_cost))
    if loss == 0:
        raise ValueError('Baseline incident loss must be positive')
    return -result['net_benefit'] / loss
