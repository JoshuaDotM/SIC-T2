def farmer_sales():
    land_total = 80
    segments = 5
    segment_acres = land_total // segments

    tomato_acres_1 = 0.3 * segment_acres
    tomato_acres_2 = 0.7 * segment_acres
    tomato_yield_1 = 10
    tomato_yield_2 = 12
    tomato_price_per_ton = 7000
    tomato_revenue = (tomato_acres_1 * tomato_yield_1 + tomato_acres_2 * tomato_yield_2) * tomato_price_per_ton


    potato_yield = 10
    potato_price_per_ton = 20000
    potato_revenue = segment_acres * potato_yield * potato_price_per_ton


    cabbage_yield = 14
    cabbage_price_per_ton = 24000
    cabbage_revenue = segment_acres * cabbage_yield * cabbage_price_per_ton

    sunflower_yield = 0.7
    sunflower_price_per_ton = 200000
    sunflower_revenue = segment_acres * sunflower_yield * sunflower_price_per_ton

    sugarcane_yield = 45
    sugarcane_price_per_ton = 4000
    sugarcane_revenue = segment_acres * sugarcane_yield * sugarcane_price_per_ton

    total_sales = tomato_revenue + potato_revenue + cabbage_revenue + sunflower_revenue + sugarcane_revenue
    chemical_free_sales = tomato_revenue + potato_revenue + cabbage_revenue + sunflower_revenue

    print(f"Total Sales from 80 acres: ₹{total_sales:,.2f}")
    print(f"Sales from Chemical-Free Farming (after 11 months): ₹{chemical_free_sales:,.2f}")

farmer_sales()

'''
footnotes-Since making the sugarcane field chemical free takes 4 months from the month 8, at 11 months it would still not be completely chemical free. 
Therefore we should noy add them to the chemical free yield at 11 months.
'''