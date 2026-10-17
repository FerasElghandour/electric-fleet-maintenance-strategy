# Electric fleet reliability: pilot and decision criteria

Author: Feras Elghandour

## Define the action before selecting a model

Choose a component and a feasible service action. Specify what counts as a failure event, when it became observable, the required alert lead time, and how a technician confirms it. Begin with a narrow operating envelope rather than claiming coverage across every vehicle component and climate.

## Build an event-based dataset

Join timestamped telemetry to maintenance records without using information created after an alert would have been issued. Audit clock offsets, sampling gaps, replaced sensors, truck identity, maintenance censoring, and work-order quality. Use operating state, load, ambient conditions, and vehicle configuration as context. Minimize precise location data when coarser operating features suffice.

Split by vehicle and time. Keep repeated windows from a single breakdown together. Thousands of correlated sensor rows around one failure are still one event; they cannot substitute for independent failures. Preserve a final untouched period and evaluate geographic and vehicle-family shifts.

## Compare against useful baselines

Compare scheduled maintenance and existing engineering thresholds with an operating-state baseline, an anomaly detector, and a classifier only when enough labeled events exist. Evaluate detection per failure event, precision per actionable alert, alerts per vehicle-week, lead time, missed failures, and unnecessary interventions. Report counts and uncertainty, especially when failures are rare. Avoid claiming accuracy from a heavily imbalanced row-level dataset.

## Operate in shadow mode first

Log recommendations without changing maintenance schedules. Technicians review evidence and record dispositions. Monitor missing sensors, drift, alert volume, and performance by route, season, vehicle type, and duty cycle. Escalate out-of-distribution conditions rather than assigning unsupported confidence.

Then run a controlled operational pilot where appropriate, using matched or randomized fleet groups and predeclared metrics. Distinguish prevented incidents from coincidental changes in utilization, vehicle age, season, and maintenance policy. Track downtime, maintenance spend, technician workload, and service capacity together.

## Economics and go/no-go

`economics.py` subtracts all modeled planned interventions and platform costs from avoided incident losses. A missed failure, a false alert, and an unnecessary part replacement carry different costs. Evaluate sensitivity across avoided-incident rate, baseline incident cost, intervention count, and fixed expense; include installation and integration costs in a complete investment case. A break-even fraction above 100% indicates that the modeled plan cannot pay back within those assumptions.

The 30% incident-reduction target and $800 intervention target are hypotheses. Approve wider rollout only after the pilot establishes usable lead time, an affordable alert burden, and credible net value within the tested operating envelope. No government contract, certification, or production uptime is claimed.

## Research reference

Veloso, B., Ribeiro, R. P., Gama, J., and Pereira, P. M. (2022). The MetroPT dataset for predictive maintenance. Scientific Data, 9, 764. https://doi.org/10.1038/s41597-022-01877-3

The paper motivates a sensor-maintenance dataset design; railway compressor evidence does not validate an electric-truck failure model. No MetroPT data is bundled.
