sql_parts = []

for hour in range(1, 169):
    part = f"""SUM(IF(
        toStartOfHour(all_purchases.first_payment_date) = 
        addHours(toStartOfHour(deduplicated_events.first_signup_time), {hour}),
        1, 0)) AS paid_hour_{hour}"""
    sql_parts.append(part)

# Join all parts with commas and newlines
full_sql = ",\n\n".join(sql_parts)

print(full_sql)
