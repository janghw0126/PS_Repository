required_customers, num_cities = map(int, input().split())
city_costs = []

for _ in range(num_cities):
    cost, customers = map(int, input().split())
    city_costs.append((cost, customers))

max_customers = required_customers + 100
min_cost_to_achieve = [float('inf')] * max_customers
min_cost_to_achieve[0] = 0

for cost, customers in city_costs:
    for target in range(customers, max_customers):
        min_cost_to_achieve[target] = min(min_cost_to_achieve[target], min_cost_to_achieve[target - customers] + cost)

print(min(min_cost_to_achieve[required_customers:]))