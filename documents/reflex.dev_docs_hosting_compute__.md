# Compute Usage

Reflex Cloud is billed on a per second basis so you only pay for when your app is being used by your end users. When your app is idle, you are not charged.

This allows you to deploy your app on larger sizes and multiple regions without worrying about paying for idle compute. We bill on a per second basis so you only pay for the compute you use.

By default your app stays alive for 5 minutes after no users are connected. After this time your app will be considered idle and you will not be charged. Start up times usually take less than 1 second for your apps to come back online.

## Warm vs Cold Start

- Apps below `c2m2` are considered warm starts and are usually less than 1 second.
- If your app is larger than `c2m2` it will be a cold start which takes around 15 seconds. If you want to avoid this you can reserve a machine.

[Compute Pricing Table](https://reflex.dev/docs/hosting/compute/#compute-pricing-table)

# Compute Pricing Table

<div class="rt-Box flex flex-col w-full py-6">
<div data-activation-direction="none" data-orientation="horizontal">
<div class="rt-Box flex flex-row gap-2 items-center justify-end pb-6 border-b border-slate-4">
<div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-1tcv0fg"></div>
</div>
</div>

# Machine Sizes

## Per min

- **c1m.5**
  - vCPU: 1
  - GB RAM: 0.5
  - Cost / min: $0.000767
- **c1m1**
  - vCPU: 1
  - GB RAM: 1
  - Cost / min: $0.001383
- **c1m2**
  - vCPU: 1
  - GB RAM: 2
  - Cost / min: $0.002617
- **c2m2**
  - vCPU: 2
  - GB RAM: 2
  - Cost / min: $0.002767
- **c2m4**
  - vCPU: 2
  - GB RAM: 4
  - Cost / min: $0.005200
- **c4m4**
  - vCPU: 4
  - GB RAM: 4
  - Cost / min: $0.005533
- **c4m8**
  - vCPU: 4
  - GB RAM: 8
  - Cost / min: $0.010417

## Per hour (Coming soon)

# Reserved Machines (Coming Soon)

If you expect your apps to be continuously receiving users, you may want to reserve a machine instead of having us manage your compute.

This will be a flat monthly rate for the machine.

[Learn More](https://reflex.dev/docs/hosting/compute/#monitoring-usage)

# Monitoring Usage

To monitor your projects usage, you can go to the billing tab in the Reflex Cloud UI on the project page. Here you can see the current billing and usage for your project.

[Real-life examples of compute charges on the pro tier](https://reflex.dev/docs/hosting/compute/#real-life-examples-of-compute-charges-on-the-pro-tier)

# Real Life Examples of Compute Charges on the Pro Tier

## Real Life Examples of Compute Charges on the Pro Tier

### Real Life Examples of Compute Charges on the Pro Tier

### Single Application - Single Region

Single Application - Single Region

# Single Application - Multi Region

This is an informational symbol indicating a single application that can operate in multiple regions.

# Single Growing Application - Multi Region

## Notes

The content of the accordion is hidden.

# Single Application High-Performance App - Single Region

## Description

This section describes a high-performance app deployed in a single region. Key points include:

- **Single Application**: A single application instance.
- **High Performance**: Optimized for performance and efficiency.
- **Single Region**: Deployed within one geographic region for reduced latency.

### Features

- **Scalability**: Can scale resources as needed to handle varying loads.
- **Cost Efficiency**: Reduced costs associated with multi-regional deployments.
- **Simplicity**: Easier management and monitoring compared to multi-region setups.

For more details, expand the accordion to view the full content.

# Single Fast Scaling App - Multiple Regions

##

# Multiple Apps - Multiple Regions

One thing that is important to note is that in the hypothetical example where you have `50 people` using your app `continuously for 24 hours` or if you have `1 person` using your app `continuously for 24 hours`, you `will be charged the same amount` as the charge is based on the amount of time your app up and not the number of users using your app. In `both these examples` your `app is up for 24 hours` and therefore you will be `charged for 24 hours of compute`.